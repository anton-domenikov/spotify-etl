import os
import requests
from dotenv import load_dotenv
from urllib.parse import urlparse, parse_qs
import pdb

# Load environment variables from .env file
load_dotenv()

# Define the Spotify API endpoints
AUTH_URL = 'https://accounts.spotify.com/authorize'
TOKEN_URL = 'https://accounts.spotify.com/api/token'

# Read client ID and client secret from environment variables
CLIENT_ID = os.getenv('CLIENT_ID')
CLIENT_SECRET = os.getenv('CLIENT_SECRET')
REDIRECT_URI = 'http://localhost:8888/callback'  # Your redirect URI

# Define the scope (the permissions your application needs)
SCOPE = 'user-read-recently-played%20user-read-currently-playing'

# Step 1: Redirect user for authorization
auth_params = {
    'client_id': CLIENT_ID,
    'response_type': 'code',
    'redirect_uri': REDIRECT_URI,
    'scope': SCOPE
}

response = requests.get(AUTH_URL, params=auth_params)
pdb.set_trace()
redirect_url = response.url

# Step 2: Extract authorization code from redirect URL
parsed_url = urlparse(redirect_url)
query_params = parse_qs(parsed_url.query)
authorization_code = query_params['code'][0]

# Step 3: Exchange authorization code for access token
token_params = {
    'grant_type': 'authorization_code',
    'code': authorization_code,
    'redirect_uri': REDIRECT_URI,
    'client_id': CLIENT_ID,
    'client_secret': CLIENT_SECRET
}

response = requests.post(TOKEN_URL, data=token_params)
response_data = response.json()

if 'error' in response_data:
    print(f'Error: {response_data["error"]}')
else:
    access_token = response_data['access_token']
    print(f'Access Token: {access_token}')
