"""
Main entry point - Run the FastAPI server
"""
import uvicorn
import os

if __name__ == "__main__":
    # Get port from environment variable (Railway provides this) or default to 8000
    port = int(os.environ.get("PORT", 8000))
    # Disable reload in production (Railway environment)
    reload = os.environ.get("ENVIRONMENT", "production") == "development"
    
    print("Starting Story-to-Scene Generator API Server...")
    print(f"API will be available on port {port}")
    print(f"API docs at http://localhost:{port}/docs")
    uvicorn.run("src.api:app", host="0.0.0.0", port=port, reload=reload)