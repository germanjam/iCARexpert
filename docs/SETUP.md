# iCARexpert Setup Guide

## Installation Steps

### 1. Prerequisites

Ensure you have:
- Python 3.10 or higher
- Git
- Ollama (for local LLM)
- 5GB disk space for Llama model

### 2. Clone Repository

```bash
git clone https://github.com/germanjam/iCARexpert.git
cd iCARexpert
```

### 3. Create Virtual Environment

```bash
# Linux/Mac
python3 -m venv venv
source venv/bin/activate

# Windows
python -m venv venv
venv\Scripts\activate
```

### 4. Install Dependencies

```bash
pip install --upgrade pip
pip install -r backend/requirements.txt
```

### 5. Setup Ollama (LLM)

#### Install Ollama
Visit: https://ollama.ai or on Linux:
```bash
curl https://ollama.ai/install.sh | sh
```

#### Download Llama 2 Model
```bash
ollama pull llama2:7b-chat-q4_K_M
```

This downloads a quantized version (~5GB) suitable for local development.

#### Start Ollama Service
```bash
ollama serve
```

Ollama will start on: `http://localhost:11434`

### 6. Setup Database

For development, SQLite is automatic. No additional setup needed.

### 7. Configure Environment

```bash
cp .env.example .env
# Edit .env with your settings if needed
```

### 8. Run the Application

```bash
cd backend
uvicorn app.main:app --reload
```

**API Access:**
- API: http://localhost:8000
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

### 9. Test the Setup

#### Health Check
```bash
curl http://localhost:8000/health
```

#### Create User Profile
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

### Port Already in Use
```
Address already in use (:8000)
```

**Solution:**
```bash
uvicorn app.main:app --port 8001
```

### Model Not Found
```
Error: model not found
```

**Solution:**
```bash
ollama pull llama2:7b-chat-q4_K_M
```

## Next Steps

1. Read [API Reference](API.md) - Understand endpoints
2. Review [User Profile Guide](USER_PROFILE.md) - Configure your needs
3. Check Phase 2 roadmap - Coming features

## Support

- GitHub Issues: https://github.com/germanjam/iCARexpert/issues
- Discussions: https://github.com/germanjam/iCARexpert/discussions
