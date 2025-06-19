# Portfolio Website

A Flask-based portfolio website with admin dashboard for content management.

## Quick Start for GitHub + Vercel Deployment

1. **Upload to GitHub**: Create a new repository and upload all files
2. **Deploy on Vercel**: Connect your GitHub repo to Vercel
3. **Admin Access**: Go to `your-site.vercel.app/admin/login` (admin/admin123)

See `VERCEL_DEPLOYMENT.md` for detailed step-by-step instructions.

## Features

- Dynamic content management
- Admin dashboard
- Portfolio project showcase
- Skills management
- Career paths display
- Contact form
- Analytics tracking

## Files for Deployment

- `vercel.json` - Vercel configuration
- `requirements-vercel.txt` - Python dependencies  
- `main.py` - Application entry point
- `.gitignore` - Git ignore rules

## Admin Panel

Access your website admin at `/admin/login`:
- Username: `admin`
- Password: `admin123`
- Change password after first login

## Database

Uses SQLite database (perfect for free hosting on Vercel).
All data and tables are created automatically.