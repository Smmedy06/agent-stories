# Story-to-Scene Generator

A LangChain-based AI agent that converts story prompts into visual scenes with image generation.

## Features

- **User Authentication**: Login/Signup system
- **Story Generation**: Convert text prompts into cinematic scenes
- **Image Generation**: Generate images for each scene using Replicate
- **Agent Memory**: Conversation and long-term memory
- **Analytics**: Summarization, Classification, Pattern Detection
- **Database**: SQLite database for storing stories, scenes, and metadata
- **Beautiful UI**: Modern, cinematic design

## Project Structure

```
project/
├── src/
│   ├── api.py              # FastAPI server
│   ├── scene_generator.py  # Scene generation logic
│   ├── image_generator.py  # Image generation logic
│   ├── analytics.py        # Analytics features
│   ├── memory.py           # Agent memory
│   ├── database.py         # Database operations
│   └── models.py           # Pydantic models
├── ui/
│   ├── index.html
│   ├── js/app.js
│   └── styles/
├── data/
│   └── story_templates.json
├── database/
│   ├── schema.sql
│   └── story_scenes.db
└── requirements.txt
```

## Setup

1. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

2. **Set Environment Variables**
   Create a `.env` file:
   ```
   GOOGLE_API_KEY=your_gemini_api_key
   REPLICATE_API_TOKEN=your_replicate_token
   DATABASE_URL=sqlite:///./database/story_scenes.db
   ```

3. **Initialize Database**
   ```bash
   python -c "from src.database import init_db; init_db()"
   ```

4. **Run Backend Server**
   ```bash
   uvicorn src.api:app --reload
   ```

5. **Open Frontend**
   Open `ui/index.html` in a browser, or serve it with a local server:
   ```bash
   # Using Python
   cd ui
   python -m http.server 8080
   ```

## API Endpoints

### Authentication
- `POST /api/auth/register` - Register new user
- `POST /api/auth/login` - Login user

### Stories
- `POST /api/generate-scenes` - Generate scenes from prompt
- `POST /api/generate-images/{story_id}` - Generate images for scenes
- `GET /api/history` - Get user's story history
- `GET /api/story/{story_id}` - Get story details

### Queries
- `POST /api/search` - Search stories
- `POST /api/filter` - Filter stories
- `POST /api/categorize` - Categorize story

## Usage

1. **Sign Up/Login**: Create an account or login
2. **Enter Prompt**: Type your story description
3. **Select Style**: Choose visual style (Cinematic, Anime, etc.)
4. **Generate**: Click send to generate scenes
5. **View Scenes**: Browse through generated scenes
6. **Generate Images**: Click "Generate Images" to create visuals

## Requirements Met

✅ **Data Source**: User input + story templates dataset  
✅ **3 Query Types**: Search, Filter, Categorize  
✅ **Agent Memory**: Conversation + Long-term memory  
✅ **Summarization**: Story and scene summaries  
✅ **Classification**: Genre, Style, Scene type  
✅ **Pattern Detection**: Narrative patterns, consistency  
✅ **Database**: SQLite with 7 tables  
✅ **Pydantic Models**: StoryInput, SceneOutput, StoryResponse  
✅ **UI**: Beautiful web interface  

## Technologies

- **Backend**: FastAPI, Python
- **AI**: LangChain, Google Gemini
- **Images**: Replicate (Imagen-4)
- **Database**: SQLite
- **Frontend**: HTML, CSS, JavaScript
- **Validation**: Pydantic

## License

MIT

