# configs/config.py
import os

from dotenv import load_dotenv


def get_credentials():
    load_dotenv()  # Load environment variables from .env file
    credentials = {
        'email': os.getenv('EMAIL'),
        'password': os.getenv('PASSWORD'),
    }
    return credentials


class LoginConfig:
    credentials = get_credentials()  # Call the function to get credentials
    base_url = 'https://example.con/'
    email = credentials['email']
    password = credentials['password']
