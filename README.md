# iCARexpert 🚗🤖

**AI-powered car buying advisor for the Spanish market**

An intelligent agent that analyzes your driving patterns, searches for vehicles matching your exact requirements, negotiates with sellers via email/chat, and recommends the best deal based on Total Cost of Ownership (TCO).

## Project Overview

### For Your Specific Case
- **Use Profile:** 95% highway (Madrid-Asturias via AP-66)
- **Requirements:** New, automatic, eco-labeled, 4.10-4.20m length
- **Goal:** Find the optimal new vehicle with minimal hassle

### What iCARexpert Does
1. **Analyzes Your Usage Pattern** - Calculates real consumption, maintenance, insurance
2. **Searches the Market** - Scrapes Spanish dealers and listings
3. **Negotiates** - Sends intelligent inquiries to sellers
4. **Calculates TCO** - Compares total cost of ownership (5-year outlook)
5. **Recommends** - Ranks vehicles using AI-powered analysis
6. **Generates Reports** - PDF with comparisons and justifications

## Tech Stack

```
Backend:      FastAPI + Python 3.10+
LLM:          Llama 2 (via Ollama) - local, privacy-focused
Database:     SQLite (dev) + PostgreSQL (production)
Scraping:     BeautifulSoup4, Selenium
Email:        SMTP integration
Frontend:     React (Phase 2)
Deployment:   Docker + Docker Compose
```

## Quick Start

### Prerequisites
- Python 3.10+
- Ollama (for local LLM)
- Git

### Installation

```bash
# Clone repository
git clone https://github.com/germanjam/iCARexpert.git
cd iCARexpert

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r backend/requirements.txt

# Setup Ollama
ollama pull llama2:7b-chat-q4_K_M
ollama serve

# In another terminal: Configure environment
cp .env.example .env

# Run backend
cd backend
uvicorn app.main:app --reload
```

**Access API:** http://localhost:8000
**API Docs:** http://localhost:8000/docs

## Features Roadmap

### ✅ Phase 1 (MVP - Current)
- [x] Backend API structure
- [x] User profile management  
- [x] TCO calculator (Madrid-Asturias optimized)
- [x] Database models (6 tables)
- [x] Llama 2 integration
- [ ] Spanish market scraper
- [ ] Email automation

### 🔄 Phase 2
- [ ] React web dashboard
- [ ] Real-time chat interface
- [ ] Email/chat with sellers
- [ ] Offer tracking

### 📋 Phase 3
- [ ] PDF reports
- [ ] Mobile app
- [ ] SMS notifications

## Key Endpoints

```bash
# Create/Update user profile
curl -X POST http://localhost:8000/api/profile \
  -H "Content-Type: application/json" \
  -d @profile.json

# Get profile
curl http://localhost:8000/api/profile/{user_id}

# Health check
curl http://localhost:8000/health
```

## Project Structure

```
iCARexpert/
├── backend/
│   ├── app/
│   │   ├── __init__.py
│   │   ├── config.py          # Configuration
│   │   ├── models.py          # SQLAlchemy models
│   │   ├── schemas.py         # Pydantic validation
│   │   ├── database.py        # DB session
│   │   ├── main.py            # FastAPI app
│   │   └── services/
│   │       ├── tco_calculator.py   # TCO calculations
│   │       └── llama_service.py    # LLM integration
│   └── requirements.txt
├── docs/
│   ├── SETUP.md               # Installation guide
│   ├── API.md                 # API reference
│   └── USER_PROFILE.md        # Profile configuration
├── .env.example
├── .gitignore
└── README.md
```

## Documentation

- **[Setup Guide](docs/SETUP.md)** - Complete installation & troubleshooting
- **[API Reference](docs/API.md)** - All endpoints documented
- **[User Profile Guide](docs/USER_PROFILE.md)** - How to configure your needs

## Your Profile (Madrid-Asturias)

```json
{
  "driving_pattern": {
    "primary_route": "Madrid-Asturias",
    "highway_percentage": 0.95,
    "yearly_km_estimate": 18000
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
}
```

## TCO Example (Kia Niro Hybrid)

- **Purchase Price:** €28,000
- **Yearly Fuel Cost:** €240
- **Yearly Maintenance:** €600
- **Yearly Insurance:** €350
- **Yearly Tolls (AP-66):** €114
- **5-Year TCO:** €15,720
- **Monthly Cost:** €261

## Development

```bash
# Run tests
pytest tests/

# Format code
black backend/

# Check linting
flake8 backend/

# With Docker
docker-compose up
```

## Troubleshooting

### Ollama Connection Error
```bash
# Make sure Ollama is running
ollama serve

# Check connection
curl http://localhost:11434/api/tags
```

### Port Already in Use
```bash
uvicorn app.main:app --port 8001
```

## Contributing

1. Fork the repository
2. Create feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open Pull Request

## License

MIT License - see LICENSE file

## Author

Created by [@germanjam](https://github.com/germanjam)

## Support

- 📖 Check [documentation](docs/)
- 🐛 Open an [Issue](https://github.com/germanjam/iCARexpert/issues)
- 💬 Start a [Discussion](https://github.com/germanjam/iCARexpert/discussions)

---

**Status:** 🚧 In Development - Phase 1

Last Updated: May 31, 2026
