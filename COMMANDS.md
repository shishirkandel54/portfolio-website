# Commands for GitHub and Vercel Deployment

## 1. GitHub Commands (Run in your project folder)

```bash
# Initialize git repository
git init

# Add all files
git add .

# Commit files
git commit -m "Initial portfolio website"

# Add your GitHub repository (replace with your username and repo name)
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git

# Push to GitHub
git push -u origin main
```

**Replace YOUR_USERNAME and YOUR_REPO_NAME with your actual GitHub details**

## 2. Environment Variables for Vercel

In Vercel dashboard, add these environment variables:

### Required:
- **Name**: `SESSION_SECRET`
- **Value**: `myportfolio2025secretkey` (or any random text)

### Optional (for advanced users):
- **Name**: `SECRET_KEY` 
- **Value**: `flask-secret-key-2025`

## 3. Complete Step-by-Step Process

### Step A: Create GitHub Repository
1. Go to github.com
2. Click "New repository"
3. Repository name: `my-portfolio-website`
4. Make it public
5. Don't add README (we already have one)
6. Click "Create repository"

### Step B: Upload Code to GitHub
Copy the repository URL from GitHub, then run:

```bash
git init
git add .
git commit -m "Portfolio website ready for deployment"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/my-portfolio-website.git
git push -u origin main
```

### Step C: Deploy on Vercel
1. Go to vercel.com
2. Sign in with GitHub
3. Click "New Project"
4. Select your repository
5. Keep default settings
6. Add environment variable: `SESSION_SECRET` = `myportfolio2025`
7. Click "Deploy"

## 4. Alternative: Upload Files Manually

If you prefer not to use command line:

1. **GitHub**: Use the "Upload files" button in your repository
2. **Drag and drop** all your project files
3. **Commit changes**
4. **Connect to Vercel** as described above

## 5. After Deployment

Your website will be available at:
- `https://my-portfolio-website.vercel.app` (or similar)
- Admin panel: `https://your-site.vercel.app/admin/login`
- Login: admin / admin123

## 6. Important Files to Upload

Make sure these files are in your GitHub repository:
- `main.py`
- `vercel.json`
- `requirements-vercel.txt`
- All folders: `templates/`, `static/`, etc.
- `.gitignore`

Your website will be live in 2-3 minutes after deployment!