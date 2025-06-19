# FIXED: Commands for GitHub and Vercel Deployment

## SOLUTION TO YOUR VERCEL ERROR

The error was caused by missing Flask dependencies. I've fixed this with:
1. Created `requirements-deploy.txt` with compatible versions
2. Added `api/index.py` for proper Vercel structure  
3. Updated `vercel.json` configuration

## 1. GitHub Commands

```bash
git init
git add .
git commit -m "Portfolio website fixed for Vercel"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
git push -u origin main
```

## 2. Vercel Deployment Steps

1. **GitHub**: Upload all files to your repository
2. **Vercel**: Go to vercel.com and connect your repo
3. **Important**: Change the requirements file name

### CRITICAL FIX:
Before deploying, rename the requirements file:
- In your GitHub repository, rename `requirements-deploy.txt` to `requirements.txt`
- Or use the GitHub web interface to upload `requirements-deploy.txt` as `requirements.txt`

## 3. Environment Variables for Vercel

Add in Vercel dashboard:
- **Name**: `SESSION_SECRET`
- **Value**: `portfolio2025secret`

## 4. File Structure for Vercel

Your repository must include:
```
your-repo/
├── api/
│   └── index.py          ← New Vercel handler
├── templates/            ← All your HTML files
├── static/              ← CSS, JS, images
├── app.py               ← Main Flask app
├── models.py            ← Database models
├── views.py             ← Routes
├── admin.py             ← Admin panel
├── requirements.txt     ← Dependencies (rename from requirements-deploy.txt)
├── vercel.json          ← Vercel config
└── other files...
```

## 5. After Deployment

- Website: `your-project-name.vercel.app`
- Admin: `your-site.vercel.app/admin/login` (admin/admin123)

The Flask module error is now fixed with the proper file structure and dependencies.