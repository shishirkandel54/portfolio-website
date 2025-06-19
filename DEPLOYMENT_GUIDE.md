# Portfolio Website Deployment Guide

## Overview
This guide will help you deploy your Flask portfolio website to various hosting platforms and set up local development.

## Prerequisites
- Python 3.11+
- PostgreSQL database
- Git repository
- Environment variables configured

## Deployment Options

### 1. Heroku (Recommended for beginners)

#### Step 1: Prepare your project
```bash
# Create requirements.txt
pip freeze > requirements.txt

# Create Procfile
echo "web: gunicorn --bind 0.0.0.0:\$PORT main:app" > Procfile

# Create runtime.txt
echo "python-3.11.9" > runtime.txt
```

#### Step 2: Deploy to Heroku
```bash
# Install Heroku CLI and login
heroku login

# Create Heroku app
heroku create your-portfolio-name

# Add PostgreSQL addon
heroku addons:create heroku-postgresql:essential-0

# Set environment variables
heroku config:set SECRET_KEY="your-secret-key-here"
heroku config:set SESSION_SECRET="your-session-secret-here"

# Deploy
git add .
git commit -m "Deploy to Heroku"
git push heroku main

# Run database migrations
heroku run python -c "from app import app, db; app.app_context().push(); db.create_all()"
```

### 2. Railway (Modern alternative)

#### Step 1: Connect your repository
1. Go to [Railway.app](https://railway.app)
2. Sign up and connect your GitHub account
3. Deploy from your repository

#### Step 2: Configure environment
```bash
# Set environment variables in Railway dashboard
SECRET_KEY=your-secret-key-here
SESSION_SECRET=your-session-secret-here
```

#### Step 3: Add PostgreSQL
1. In Railway dashboard, click "New Service"
2. Select "PostgreSQL"
3. Railway will automatically set DATABASE_URL

### 3. DigitalOcean App Platform

#### Step 1: Prepare app.yaml
```yaml
name: portfolio-website
services:
- name: web
  source_dir: /
  github:
    repo: your-username/your-repo
    branch: main
  run_command: gunicorn --bind 0.0.0.0:$PORT main:app
  environment_slug: python
  instance_count: 1
  instance_size_slug: basic-xxs
  envs:
  - key: SECRET_KEY
    value: your-secret-key-here
  - key: SESSION_SECRET
    value: your-session-secret-here
databases:
- name: portfolio-db
  engine: PG
  version: "14"
```

### 4. Vercel (For Static/Serverless)

#### Step 1: Install Vercel CLI
```bash
npm i -g vercel
```

#### Step 2: Configure vercel.json
```json
{
  "builds": [
    {
      "src": "main.py",
      "use": "@vercel/python"
    }
  ],
  "routes": [
    {
      "src": "/(.*)",
      "dest": "main.py"
    }
  ]
}
```

## Local Development Setup

### 1. Clone and Setup
```bash
# Clone your repository
git clone https://github.com/your-username/your-repo.git
cd your-repo

# Create virtual environment
python -m venv portfolio_env
source portfolio_env/bin/activate  # Linux/Mac
# or
portfolio_env\Scripts\activate     # Windows

# Install dependencies
pip install -r requirements.txt
```

### 2. Database Setup
```bash
# Install PostgreSQL locally
# Ubuntu/Debian:
sudo apt-get install postgresql postgresql-contrib

# macOS:
brew install postgresql

# Windows: Download from postgresql.org
```

### 3. Environment Configuration
Create `.env` file:
```bash
DATABASE_URL=postgresql://username:password@localhost/portfolio_db
SECRET_KEY=your-development-secret-key
SESSION_SECRET=your-development-session-secret
```

### 4. Initialize Database
```bash
# Create database
createdb portfolio_db

# Run the application (it will create tables automatically)
python main.py
```

### 5. Create Admin User
```bash
# Access Python shell
python -c "
from app import app, db
from models import Admin
app.app_context().push()
admin = Admin(username='admin', email='admin@example.com')
admin.set_password('your-admin-password')
db.session.add(admin)
db.session.commit()
print('Admin user created successfully!')
"
```

## Environment Variables Required

### Production Environment Variables
```bash
DATABASE_URL=postgresql://user:pass@host:port/dbname
SECRET_KEY=your-production-secret-key
SESSION_SECRET=your-production-session-secret
```

### Optional Configuration
```bash
MAIL_SERVER=smtp.gmail.com
MAIL_PORT=587
MAIL_USE_TLS=True
MAIL_USERNAME=your-email@gmail.com
MAIL_PASSWORD=your-app-password
```

## Domain Configuration

### 1. Custom Domain (Heroku)
```bash
# Add custom domain
heroku domains:add yourdomain.com
heroku domains:add www.yourdomain.com

# Configure DNS records
# A record: @ -> your-app-name.herokuapp.com
# CNAME record: www -> your-app-name.herokuapp.com
```

### 2. SSL Certificate
Most platforms (Heroku, Railway, Vercel) provide automatic SSL certificates.

## Performance Optimization

### 1. Static File Optimization
```python
# In production, serve static files via CDN
# Add to app.py:
from flask import send_from_directory
import os

@app.route('/static/<path:filename>')
def static_files(filename):
    return send_from_directory('static', filename)
```

### 2. Database Connection Pooling
```python
# Already configured in config.py
SQLALCHEMY_ENGINE_OPTIONS = {
    "pool_recycle": 300,
    "pool_pre_ping": True,
}
```

## Monitoring and Maintenance

### 1. Log Monitoring
```bash
# Heroku logs
heroku logs --tail

# Railway logs
Available in Railway dashboard

# DigitalOcean logs
Available in App Platform dashboard
```

### 2. Database Backups
```bash
# Heroku
heroku pg:backups:capture
heroku pg:backups:download

# Manual backup
pg_dump DATABASE_URL > backup.sql
```

## Security Checklist

- [ ] Set strong SECRET_KEY and SESSION_SECRET
- [ ] Use HTTPS in production
- [ ] Configure CSRF protection
- [ ] Set up proper database user permissions
- [ ] Enable database connection encryption
- [ ] Regular security updates
- [ ] Monitor application logs

## Troubleshooting

### Common Issues
1. **Database Connection**: Verify DATABASE_URL format
2. **Static Files**: Ensure proper static file serving
3. **Environment Variables**: Check all required variables are set
4. **Dependencies**: Verify requirements.txt is complete

### Debug Mode
Never enable debug mode in production:
```python
# main.py - ensure this is set correctly
if __name__ == '__main__':
    app.run(debug=False)  # Always False in production
```

## Cost Estimation

### Free Tiers Available
- **Heroku**: Free tier discontinued, basic plan ~$7/month
- **Railway**: $5/month for hobby plan
- **Vercel**: Free for personal projects
- **DigitalOcean**: $5/month basic plan

### Recommended Setup
For a professional portfolio: **Railway** or **DigitalOcean** for reliability and performance.

## Support
If you encounter issues:
1. Check platform-specific documentation
2. Verify environment variables
3. Check application logs
4. Test locally first
5. Contact platform support if needed

Your portfolio website is now ready for deployment!