# Simple Deployment Guide

## Method 1: Using Commands (Recommended)

### Step 1: Open Terminal/Command Prompt
Navigate to your project folder and run these commands one by one:

```bash
git init
git add .
git commit -m "Portfolio website"
git branch -M main
```

### Step 2: Connect to GitHub
Replace YOUR_USERNAME and REPO_NAME with your actual details:

```bash
git remote add origin https://github.com/YOUR_USERNAME/REPO_NAME.git
git push -u origin main
```

### Step 3: Deploy on Vercel
1. Go to vercel.com
2. Sign in with GitHub
3. Click "New Project"
4. Select your repository
5. Click "Deploy"

## Method 2: Manual Upload (No Commands)

### Step 1: GitHub Upload
1. Create new repository on github.com
2. Click "uploading an existing file"
3. Drag all your project files
4. Click "Commit changes"

### Step 2: Vercel Deployment
Same as Method 1, Step 3

## Environment Variables

In Vercel dashboard → Settings → Environment Variables:

**Add this variable:**
- Name: `SESSION_SECRET`
- Value: `portfolio2025secret`

## Important Files to Include

Make sure these files are uploaded:
- `main.py`
- `vercel.json`
- `requirements-vercel.txt`
- `templates/` folder
- `static/` folder
- All other project files

## After Deployment

Your website will be at: `your-project-name.vercel.app`
Admin login: `your-site-url/admin/login` (admin/admin123)

Deployment takes 2-3 minutes to complete.