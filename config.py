import os

# Get the absolute path of the current files directory
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# Define the full path to the SQLite database file
DATABASE = os.path.join(BASE_DIR, "users.db")
