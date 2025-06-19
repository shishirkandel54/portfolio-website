import sys
import os

# Add the parent directory to Python path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import app

# Export the Flask app for Vercel
def handler(request, context):
    return app(request.environ, lambda status, headers: None)

# Alternative handler for different Vercel setups
application = app

# For direct calls
if __name__ == "__main__":
    app.run()