"""
iCARexpert Setup Guide
======================

Complete installation and setup instructions for iCARexpert
"""

# Installation Steps

## 1. Prerequisites

Ensure you have:
- Python 3.10 or higher
- Git
- Ollama (for local LLM)
- Docker & Docker Compose (optional, for database)

## 2. Clone Repository

```bash
git clone https://github.com/germanjam/iCARexpert.git
cd iCARexpert
```

## 3. Create Virtual Environment

### Linux/Mac
```bash
python3 -m venv venv
source venv/bin/activate
```

### Windows
```bash
python -m venv venv
venv\Scripts\activate
```

## 4. Install Dependencies

```bash
pip install --upgrade pip
pip install -r backend/requirements.txt
```

## 5. Setup Ollama (LLM)

### Install Ollama
Visit: https://ollama.ai

Or on Linux:
```bash
curl https://ollama.ai/install.sh | sh
```

### Download Llama 2 Model
```bash
ollama pull llama2:7b-chat-q4_K_M
```

This downloads a quantized version (~5GB) suitable for local development.

### Start Ollama Service
```bash
ollama serve
```

Ollama will start on: `http://localhost:11434`

## 6. Setup Database

### Option A: Using SQLite (Recommended for Development)
No setup needed! SQLite will create automatically on first run.

### Option B: Using PostgreSQL with Docker
```bash
docker-compose up -d postgres
```

Then update `.env`:
```
DATABASE_URL=postgresql://icarexpert_user:secure_password@localhost:5432/icarexpert_db
```

## 7. Configure Environment

```bash
cp .env.example .env
```

Edit `.env` with your settings:
- Ollama configuration
- Email credentials (for Phase 3)
- Database URL

## 8. Run the Application

### Start Backend Server
```bash
cd backend
uvicorn app.main:app --reload
```

The API will be available at: `http://localhost:8000`

### Access API Documentation
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## 9. Test the Setup

### Health Check
```bash
curl http://localhost:8000/health
```

Expected response:
```json
{
  "status": "healthy",
  "app": "iCARexpert",
  "version": "0.1.0"
}
```

### Create User Profile
```bash
curl -X POST http://localhost:8000/api/profile \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Usuario",
    "driving_pattern": {
      "primary_route": "Madrid-Asturias",
      "highway_percentage": 0.95,
      "yearly_km_estimate": 18000,
      "driving_style": "steady_highway"
    },
    "vehicle_requirements": {
      "condition": "new",
      "transmission": "automatic",
      "eco_label_required": true,
      "min_length": 4.0,
      "target_length": 4.10,
      "max_length": 4.20,
      "preferred_fuel_types": ["hybrid", "electric"]
    },
    "budget": {
      "budget_min": 20000,
      "budget_max": 40000,
      "currency": "EUR"
    }
  }'
```

## Troubleshooting

### Ollama Connection Error
```
Error: Failed to connect to Ollama at http://localhost:11434
```

**Solution:**
1. Ensure Ollama is running: `ollama serve`
2. Check Ollama is accessible: `curl http://localhost:11434/api/tags`
3. Verify OLLAMA_BASE_URL in .env

### Database Connection Error
```
Error: could not connect to server
```

**Solution:**
1. If using PostgreSQL, ensure Docker is running
2. Check DATABASE_URL in .env
3. For SQLite, ensure write permissions in project directory

### Port Already in Use
```
Address already in use (:8000)
```

**Solution:**
```bash
# Use different port
uvicorn app.main:app --port 8001
```

## Docker Compose Setup (Full Stack)

### All Services Together
```bash
docker-compose up -d
```

Services:
- FastAPI Backend: `http://localhost:8000`
- PostgreSQL: `localhost:5432`
- Ollama: `http://localhost:11434`

### Stop Services
```bash
docker-compose down
```

## Development Commands

### Run Tests
```bash
pytest tests/
```

### Format Code
```bash
black backend/
```

### Check Linting
```bash
flake8 backend/
```

### Create Database Backup
```bash
# SQLite
cp icarexpert.db icarexpert.db.backup

# PostgreSQL
pg_dump -U icarexpert_user icarexpert_db > backup.sql
```

## Next Steps

1. **Phase 1 Complete:** Backend API ready
2. **Phase 2:** Implement vehicle search and scraping
3. **Phase 3:** Add email automation
4. **Phase 4:** Build React dashboard

## Support

If you encounter issues:

1. Check logs: `tail -f logs/icarexpert.log`
2. Open an issue: https://github.com/germanjam/iCARexpert/issues
3. Check documentation: `/docs/` directory

## Additional Resources

- FastAPI Docs: https://fastapi.tiangolo.com/
- Ollama Docs: https://ollama.ai/
- SQLAlchemy Docs: https://docs.sqlalchemy.org/
