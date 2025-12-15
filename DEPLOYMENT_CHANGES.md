# Changes Made for Railway Deployment

This document summarizes all the changes made to prepare the project for Railway deployment.

## Files Created

### 1. `Procfile`
- **Purpose:** Tells Railway how to run your application
- **Content:** `web: python main.py`
- Railway uses this to start your application

### 2. `railway.json`
- **Purpose:** Railway-specific configuration
- **Content:** Build and deploy settings
- Helps Railway understand your project structure

### 3. `env.example`
- **Purpose:** Template for environment variables
- **Content:** Required and optional environment variables with descriptions
- Use this as a reference when setting up environment variables in Railway

### 4. `RAILWAY_DEPLOYMENT.md`
- **Purpose:** Complete deployment guide
- **Content:** Step-by-step instructions for deploying on Railway
- Follow this guide to deploy your application

## Files Modified

### 1. `main.py`
**Changes:**
- Added support for `PORT` environment variable (Railway provides this)
- Added support for `ENVIRONMENT` variable to control reload behavior
- Changed default port handling to use environment variable

**Before:**
```python
uvicorn.run("src.api:app", host="0.0.0.0", port=8000, reload=True)
```

**After:**
```python
port = int(os.environ.get("PORT", 8000))
reload = os.environ.get("ENVIRONMENT", "production") == "development"
uvicorn.run("src.api:app", host="0.0.0.0", port=port, reload=reload)
```

### 2. `js/app.js`
**Changes:**
- Updated `API_BASE_URL` to use current domain instead of hardcoded localhost
- Updated error message to be more generic

**Before:**
```javascript
const API_BASE_URL = 'http://localhost:8000';
```

**After:**
```javascript
const API_BASE_URL = window.location.origin;
```

This allows the frontend to work on any domain (localhost for development, Railway URL for production).

### 3. `src/api.py`
**Changes:**
- Added static file serving for frontend files (`styles/`, `js/`)
- Added route to serve `index.html` at root path
- Added catch-all route for SPA (Single Page Application) routing

**New additions:**
- Mount `/styles` directory for CSS files
- Mount `/js` directory for JavaScript files
- Root route `/` serves `index.html`
- Catch-all route serves `index.html` for client-side routing

This allows the FastAPI server to serve both the API and the frontend, making it a complete full-stack application.

## Environment Variables Required

### Required:
- `GOOGLE_API_KEY` - Your Google Gemini API key (get from https://makersuite.google.com/app/apikey)

### Optional:
- `DATABASE_URL` - Database connection string (defaults to SQLite)
- `ENVIRONMENT` - Set to "development" for auto-reload (defaults to "production")
- `PORT` - Port number (Railway sets this automatically, don't set manually)

## Important Notes

### Database
- The app uses SQLite by default
- **Warning:** SQLite files are ephemeral on Railway - data may be lost on redeploy
- For production, consider using Railway's PostgreSQL service

### Static Files
- Images are stored in `scene_images/` directory
- **Warning:** These files are also ephemeral on Railway
- Consider using external storage (S3, Cloudinary) for production

### Deployment Process
1. Push code to Git repository
2. Connect repository to Railway
3. Set environment variables in Railway dashboard
4. Railway automatically deploys
5. Access your app at the provided Railway URL

## Testing Locally

Before deploying, test that the changes work locally:

1. Set environment variables:
   ```bash
   export GOOGLE_API_KEY=your_key_here
   export PORT=8000
   export ENVIRONMENT=development
   ```

2. Run the application:
   ```bash
   python main.py
   ```

3. Open browser to `http://localhost:8000`
4. Verify frontend loads and API calls work

## Next Steps

1. Review `RAILWAY_DEPLOYMENT.md` for complete deployment instructions
2. Push all changes to your Git repository
3. Follow the deployment guide to deploy on Railway
4. Set environment variables in Railway dashboard
5. Test your deployed application

## Troubleshooting

If you encounter issues:
1. Check Railway logs in the dashboard
2. Verify all environment variables are set
3. Ensure `GOOGLE_API_KEY` is valid
4. Check that all files are committed to Git
5. Review error messages in Railway deployment logs

