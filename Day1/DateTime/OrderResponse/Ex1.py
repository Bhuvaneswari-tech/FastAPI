import os
from dotenv import load_dotenv
# Load environment variables from .env file
load_dotenv()

print("App Name:", os.getenv("APP_NAME"))
print("Version:", os.getenv("VERSION"))
print("Debug Mode:", os.getenv("DEBUG"))
print("Database URL:", os.getenv("DATABASE_URL"))
print("Secret Key:", os.getenv("SECRET_KEY"))   