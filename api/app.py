import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Import the Flask app from the main app.py file
from app import app

# Export for Vercel serverless functions
def handler(request):
    return app

# Alternative export
application = app