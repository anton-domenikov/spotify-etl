Welcome to my project repository! In this blog post, we'll explore how to build a simple ETL (Extract, Transform, Load) pipeline using Python, leveraging Spotify's API for data extraction, performing basic transformations, conducting Data Quality checks, and ultimately loading the retrieved data into a PostgreSQL database. Additionally, we'll demonstrate how to automate this process using Apache Airflow.


## STEP 1: Spotify API Setup Guide

This guide will walk you through the process of creating a Spotify Developer account, registering your application, and obtaining your API credentials to start using the Spotify Web API.

### Step 1.1: Create a Spotify Developer Account

1. Go to the [Spotify Developer Dashboard Login Page](https://developer.spotify.com/dashboard/login).
2. Log in with your existing Spotify account credentials or sign up for a new account if you don't have one.
3. Once logged in, you will be redirected to the Spotify Developer Dashboard. If not, use [Spotify Developer Dashboard](https://developer.spotify.com/dashboard).

### Step 1.2: Create a New Application

1. Click on the **Create an App** button. 
![](images/spotify-dashboard-app.png)
2. Fill in the required information for your application:
   - App name - can be anything
   - App description - can be anything
   - Redirect URI - You need to use `http://localhost:8888/callback` We pass the redirect URI during the Authorisation Flow, so they need to match exactly.
   - Which API/SDKs are you planning to use? - select Web API
     ![](images/spotify-api-create-app.png)

### Step 1.3: Obtain Your API Credentials

1. After creating your application, you will be redirected to the application dashboard.
2. Click on your App > Top right corner click on Settings.
3. Here, you will find your **Client ID** and **Client Secret**. These are your API credentials required for authenticating requests to the Spotify Web API.
![](images/spotify-api-app-secrets.png)
5. Make sure to keep your credentials secure. Do not share them publicly or expose them in your client-side code.
5. Go to [.env](.env) and put the Client ID and Client Secret there

### Step 1.4: Get your Token

1. Run [auth](auth.py)
2. Follow the instructions there. Get the Code from the new URL as the picture 
![](images/auth-code.png)
3. Make sure you get the whole string AFTER 'code=' and copy paste it into the expected input
![](images/auth-code-input.png)
4. Now the TOKEN is saved automatically in .env file and will be Valid for the next 3600 seconds / 1 hour. After that if needed run [auth](auth.py) again to get a new token.




### Additional Resources

- [Spotify Web API Documentation](https://developer.spotify.com/documentation/web-api/)
- [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/login)

Congratulations! You have successfully set up your Spotify Developer account, registered your application, and obtained your API credentials.