# db_config.py
import os
from dotenv import load_dotenv
import MySQLdb
from print_info import print_info, print_error

load_dotenv()

# Database configuration
db_config = {
    'host': os.getenv("DB_HOST"),
    'user': os.getenv("DB_USER"),
    'passwd': os.getenv("DB_PASSWORD"),
    'db': os.getenv("DB_NAME"),
}

def create_connection():
    try:
        connection = MySQLdb.connect(**db_config)
        print_info("Database Connected Successfully!")
        # Load environment variables from the .env file
        return connection
    except Exception as e:
        # Handle the exception, e.g., print an error message
        print_error("Error Database Connection established!")
        print(f"=============================================================================\n {e}\n=============================================================================")
        # Optionally, you might want to re-raise the exception to propagate it further
        raise e