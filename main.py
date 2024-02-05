import os
from dotenv import load_dotenv

load_dotenv()

user = os.getenv('USER')

print(user)