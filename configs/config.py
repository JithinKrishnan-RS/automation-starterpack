import os

from dotenv import load_dotenv


def get_credentials():
    load_dotenv()  # Load environment variables from .env file
    credentials = {
        'email': os.getenv('EMAIL'),
        'password': os.getenv('PASSWORD'),
        'inactive_email': os.getenv('INACTIVE_EMAIL'),
        'inactive_password': os.getenv('INACTIVE_PASSWORD'),
        'invalid_email': os.getenv('INVALID_EMAIL'),
        'invalid_password': os.getenv('INVALID_PASSWORD')
    }
    return credentials


class LoginConfig:
    credentials = get_credentials()  # Call the function to get credentials

    base_url = 'https://example.com/'

    email = credentials['email']
    password = credentials['password']

    inactive_email = credentials['inactive_email']
    inactive_password = credentials['inactive_password']

    invalid_email = credentials['invalid_email']
    invalid_password = credentials['invalid_password']
