from dotenv import load_dotenv
from app import app

import os

load_dotenv(override=True)

if __name__ == "__main__":
    app.run(debug=True)