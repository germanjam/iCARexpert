# iCARexpert API Reference

## Base URL
```
http://localhost:8000
```

## Endpoints

### GET /health
Health check

**Response:**
```json
{
  "status": "healthy",
  "app": "iCARexpert",
  "version": "0.1.0"
}
```

### POST /api/profile
Create or update user profile

**Request:**
```json
{
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
}
```

**Response (201):**
```json
{
  "id": 1,
  "user_id": "Usuario",
  "name": "Usuario",
  "primary_route": "Madrid-Asturias",
  "highway_percentage": 0.95,
  "yearly_km_estimate": 18000,
  "target_length": 4.10,
  "max_length": 4.20,
  "budget_min": 20000,
  "budget_max": 40000,
  "currency": "EUR",
  "created_at": "2026-05-31T12:00:00",
  "updated_at": "2026-05-31T12:00:00"
}
```

### GET /api/profile/{user_id}
Get user profile

**Parameters:**
- `user_id` (string, path): User identifier

**Response (200):**
```json
{
  "id": 1,
  "user_id": "Usuario",
  ...
}
```

**Error (404):**
```json
{"detail": "Profile not found"}
```

### GET /api/search (Phase 2)
Search for vehicles

**Parameters:**
- `fuel_type` (string): "hybrid", "electric"
- `max_price` (float): Maximum price EUR

### POST /api/analysis/tco (Phase 2)
Calculate TCO

### GET /api/recommendations (Phase 2)
Get top recommendations

## Status Codes

- 200: Success
- 201: Created
- 400: Bad Request
- 404: Not Found
- 500: Internal Server Error

## Documentation

- Interactive Docs: http://localhost:8000/docs
- Alternative Docs: http://localhost:8000/redoc
