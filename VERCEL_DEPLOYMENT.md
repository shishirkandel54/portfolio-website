# Easy Vercel Deployment Guide

## Step 1: Prepare Your Files

Your website is ready for deployment! Make sure you have these files:
- `vercel.json` ✓
- `requirements-vercel.txt` ✓ 
- All your website files ✓

## Step 2: Push to GitHub

1. Go to GitHub.com and create a new repository
2. Name it something like "my-portfolio-website"
3. Upload all your files to this repository

## Step 3: Deploy on Vercel

1. Go to [vercel.com](https://vercel.com)
2. Sign up with your GitHub account
3. Click "New Project"
4. Select your GitHub repository
5. Vercel will automatically detect it's a Python project

### Important Settings:
- **Framework Preset**: Other
- **Root Directory**: ./
- **Build Command**: Leave empty
- **Output Directory**: Leave empty

## Step 4: Environment Variables (Optional)

In Vercel dashboard, go to Settings → Environment Variables and add:
- `SESSION_SECRET`: Any random text (like: mysecretkey123)

## Step 5: Deploy

Click "Deploy" and wait 2-3 minutes. Your website will be live!

## Admin Access

After deployment:
- Go to: `your-website-url.vercel.app/admin/login`
- Username: `admin`
- Password: `admin123`

**Important**: Change the admin password after first login!

## Common Issues & Solutions

### Issue: Build Failed
- Make sure `requirements-vercel.txt` exists
- Check that all files are uploaded to GitHub

### Issue: Website Not Working
- Check Vercel function logs in dashboard
- Make sure environment variables are set

### Issue: Database Errors
- The website uses SQLite (file database) which works on Vercel
- Data will reset on each deployment (normal for free hosting)

## Free Hosting Limitations

- Website sleeps after inactivity (normal)
- Database resets on deployments
- Limited storage and bandwidth

This is perfect for portfolio websites and testing!

## Need Help?

If you get stuck:
1. Check Vercel dashboard for error messages
2. Make sure all files are in your GitHub repository
3. Verify the admin login works locally first

Your portfolio website is now ready for the world! 🚀