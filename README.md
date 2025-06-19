# Portfolio Website

A Flask-based portfolio website with admin dashboard for content management.

## Features

- Dynamic content management
- Admin dashboard
- Portfolio project showcase
- Skills management
- Career paths display
- Contact form
- Analytics tracking

## Local Development

1. Install dependencies:
```bash
pip install -r requirements-vercel.txt
```

2. Set environment variables:
```bash
export DATABASE_URL="your_database_url"
export SESSION_SECRET="your_secret_key"
```

3. Run the application:
```bash
python main.py
```

## Admin Access

- URL: `/admin/login`
- Default credentials: admin / admin123
- Change these in production!

## Deployment

### Vercel Deployment

1. Create a Vercel account
2. Connect your GitHub repository
3. Use `requirements-vercel.txt` as your requirements file
4. Set environment variables in Vercel dashboard:
   - `DATABASE_URL`: Your PostgreSQL database URL
   - `SESSION_SECRET`: A secure random string

### Other Platforms

See `DEPLOYMENT_GUIDE.md` for detailed instructions on deploying to:
- Heroku
- Railway
- DigitalOcean

## Environment Variables

- `DATABASE_URL`: PostgreSQL database connection string
- `SESSION_SECRET`: Secret key for session management
- `SECRET_KEY`: Flask secret key (optional, defaults to SESSION_SECRET)

## Database

The application uses PostgreSQL in production and SQLite for local development.
Database tables are created automatically on first run.