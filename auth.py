import os
import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Define the Spotify API endpoints
AUTH_URL = 'https://accounts.spotify.com/authorize'
TOKEN_URL = 'https://accounts.spotify.com/api/token'

# Read client ID and client secret from environment variables
CLIENT_ID = os.getenv('CLIENT_ID')
CLIENT_SECRET = os.getenv('CLIENT_SECRET')
REDIRECT_URI = 'http://localhost:8888/callback'

# Define the scope (the permissions your application needs)
SCOPE = 'user-read-recently-played%20user-read-currently-playing'

# Step 1: Redirect user for authorization
auth_url = f'{AUTH_URL}?client_id={CLIENT_ID}&response_type=code&redirect_uri={REDIRECT_URI}&scope={SCOPE}'

print(f'Please visit the following URL to authorize your application:\n{auth_url}')
authorization_code = input('Enter the authorization code from the callback URL: ')

# Step 2: Exchange authorization code for access token
token_params = {
    'grant_type': 'authorization_code',
    'code': authorization_code,
    'redirect_uri': REDIRECT_URI,
    'client_id': CLIENT_ID,
    'client_secret': CLIENT_SECRET
}

response = requests.post(TOKEN_URL, data=token_params)
response_data = response.json()

# Step 3: Update the access token in .env file if successful
if 'error' in response_data:
    print(f'Error: {response_data["error"]}')
else:
    access_token = response_data['access_token']
    print(f'Access Token: {access_token}')

    with open('.env', 'r') as f:
        lines = f.readlines()

    with open('.env', 'w') as f:
        for line in lines:
            if line.startswith('TOKEN='):
                f.write(f'TOKEN={access_token}\n')
                print('TOKEN saved in .env')
            else:
                f.write(line.strip() + '\n' if line.strip() else '\n')
