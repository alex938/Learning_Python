#pip install python-dotenv
#DO NOT FORGET TO ADD .env TO YOUR GITIGNORE!

import os
from dotenv import load_dotenv

load_dotenv()

SECRET: str = os.getenv('SECRET_KEY')

print("SECRET = {}".format(SECRET))