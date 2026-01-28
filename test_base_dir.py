# test_base_dir.py

from dotenv import load_dotenv
from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parents[0]  # parent of this file
print("BASE_DIR =", BASE_DIR)

BASE_DIR = Path(r"T:\WORK_FOLDER\SHOWCASE_PROJECTS\Backend_Portfolio_Projects\03_FastAPI_REST_API_Boilerplate_with_JWT_Auth_PostgreSQL_and_Docker")
load_dotenv(BASE_DIR / ".env")

print(os.getenv("database_url"))