import os

DB_HOST = os.getenv("DB_HOST", "your-db-host")
DB_NAME = os.getenv("DB_NAME", "your-db-name")
DB_USER = os.getenv("DB_USER", "your-db-user")
DB_PASS = os.getenv("DB_PASS", "your-db-password")
DB_PORT = os.getenv("DB_PORT", "5432")

SQLALCHEMY_DATABASE_URI = f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
SQLALCHEMY_TRACK_MODIFICATIONS = False
