# Railway Deployment Guide

This guide will walk you through deploying the Story-to-Scene Generator application on Railway.

## Prerequisites

1. A Railway account (sign up at [railway.app](https://railway.app))
2. A Google Gemini API key (get one from [Google AI Studio](https://makersuite.google.com/app/apikey))
3. Your project code pushed to a Git repository (GitHub, GitLab, or Bitbucket)

## Step-by-Step Deployment

### 1. Prepare Your Repository

Make sure your code is committed and pushed to your Git repository. The following files should be in your repository:
- `Procfile` ✅ (created)
- `requirements.txt` ✅ (already exists)
- `main.py` ✅ (updated for Railway)
- `railway.json` ✅ (created)
- All source files in `src/`
- Frontend files (`index.html`, `js/`, `styles/`)

### 2. Create a New Railway Project

1. Go to [railway.app](https://railway.app) and sign in
2. Click **"New Project"**
3. Select **"Deploy from GitHub repo"** (or your Git provider)
4. Select your repository
5. Railway will automatically detect it's a Python project

### 3. Configure Environment Variables

In your Railway project dashboard:

1. Go to your project → **Variables** tab
2. Add the following environment variables:

   ```
   GOOGLE_API_KEY=your_actual_gemini_api_key_here
   ENVIRONMENT=production
   ```

   **Note:** `PORT` is automatically set by Railway - you don't need to add it.

   **Optional:** If you want to use PostgreSQL instead of SQLite:
   ```
   DATABASE_URL=postgresql://user:password@host:port/dbname
   ```

### 4. Deploy

Railway will automatically:
- Detect the Python runtime
- Install dependencies from `requirements.txt`
- Run the app using the `Procfile`
- Assign a public URL to your application

### 5. Access Your Application

Once deployed:
1. Railway will provide a public URL (e.g., `https://your-app.railway.app`)
2. Your application will be accessible at this URL
3. The API will be available at `https://your-app.railway.app/api/`
4. API documentation at `https://your-app.railway.app/docs`

## Configuration Details

### Port Configuration
- Railway automatically sets the `PORT` environment variable
- The app is configured to use this port (see `main.py`)

### Database
- By default, the app uses SQLite stored in the `database/` directory
- **Important:** SQLite files are ephemeral on Railway - data may be lost on redeploy
- For production, consider using Railway's PostgreSQL service:
  1. Add a PostgreSQL service in Railway
  2. Set `DATABASE_URL` to the PostgreSQL connection string
  3. Update `src/database.py` if needed to support PostgreSQL

### Static Files
- Frontend files (HTML, CSS, JS) are served by FastAPI
- Images are stored in `scene_images/` directory
- **Note:** Files in these directories are also ephemeral on Railway
- Consider using Railway's volume storage or external storage (S3, Cloudinary) for persistent file storage

### API Endpoints
All API endpoints are prefixed with `/api/`:
- `POST /api/auth/register` - User registration
- `POST /api/auth/login` - User login
- `POST /api/generate-scenes` - Generate story scenes
- `POST /api/generate-images/{story_id}` - Generate images
- `GET /api/history` - Get user stories
- `GET /api/story/{story_id}` - Get story details
- And more...

## Troubleshooting

### Application Won't Start
1. Check the **Deployments** tab in Railway for error logs
2. Verify all environment variables are set correctly
3. Check that `GOOGLE_API_KEY` is valid
4. Review logs: Railway dashboard → Your service → **View Logs**

### Database Issues
- If using SQLite: Database is recreated on each deploy (data is lost)
- Consider migrating to PostgreSQL for persistent storage

### API Connection Errors
- The frontend automatically uses the current domain (no localhost)
- Check browser console for specific error messages
- Verify CORS is configured correctly (already set to allow all origins)

### Image Generation Fails
- Check that `GOOGLE_API_KEY` is set and valid
- Verify API quota/limits in Google AI Studio
- Check Railway logs for specific error messages

## Custom Domain (Optional)

1. In Railway dashboard → Your project → **Settings**
2. Click **"Generate Domain"** or **"Custom Domain"**
3. Follow the instructions to configure your domain

## Monitoring

- **Logs:** View real-time logs in Railway dashboard
- **Metrics:** Check resource usage in the **Metrics** tab
- **Health Check:** The app has a health endpoint at `/api/health`

## Updates and Redeployments

Railway automatically redeploys when you push to your connected branch:
1. Push changes to your Git repository
2. Railway detects the push
3. Automatically builds and deploys the new version
4. Zero-downtime deployment (new version starts before old one stops)

## Cost Considerations

- Railway offers a free tier with usage limits
- Monitor your usage in the Railway dashboard
- Consider upgrading if you exceed free tier limits
- Google Gemini API has its own pricing (check Google AI Studio)

## Additional Resources

- [Railway Documentation](https://docs.railway.app)
- [FastAPI Documentation](https://fastapi.tiangolo.com)
- [Google Gemini API Docs](https://ai.google.dev/docs)

---

**Need Help?** Check Railway's logs and documentation, or review the error messages in your application logs.

