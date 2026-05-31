"""Main FastAPI application"""

from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

from app.config import settings
from app.database import get_db, engine
from app import models
from app.schemas import (
    UserProfileCreateSchema,
    UserProfileSchema,
    MessageSchema
)

# Create database tables
models.Base.metadata.create_all(bind=engine)

# Initialize FastAPI app
app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    description="AI-powered car buying advisor for Spanish market"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ============================================
# HEALTH CHECK
# ============================================

@app.get("/", tags=["Health"])
@app.get("/health", tags=["Health"])
async def health_check():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "app": settings.APP_NAME,
        "version": settings.APP_VERSION
    }


# ============================================
# PROFILE ENDPOINTS
# ============================================

@app.post("/api/profile", response_model=UserProfileSchema, tags=["Profile"])
async def create_profile(
    profile_data: UserProfileCreateSchema,
    db: Session = Depends(get_db)
):
    """Create or update user profile"""
    
    # Check if profile exists
    existing_profile = db.query(models.UserProfile).filter(
        models.UserProfile.user_id == profile_data.name
    ).first()
    
    if existing_profile:
        # Update existing
        existing_profile.name = profile_data.name
        existing_profile.primary_route = profile_data.driving_pattern.primary_route
        existing_profile.highway_percentage = profile_data.driving_pattern.highway_percentage
        existing_profile.yearly_km_estimate = profile_data.driving_pattern.yearly_km_estimate
        existing_profile.driving_style = profile_data.driving_pattern.driving_style
        existing_profile.condition = profile_data.vehicle_requirements.condition
        existing_profile.transmission = profile_data.vehicle_requirements.transmission
        existing_profile.eco_label_required = profile_data.vehicle_requirements.eco_label_required
        existing_profile.min_length = profile_data.vehicle_requirements.min_length
        existing_profile.target_length = profile_data.vehicle_requirements.target_length
        existing_profile.max_length = profile_data.vehicle_requirements.max_length
        existing_profile.budget_min = profile_data.budget.budget_min
        existing_profile.budget_max = profile_data.budget.budget_max
        existing_profile.currency = profile_data.budget.currency
        existing_profile.preferred_fuel_types = profile_data.vehicle_requirements.preferred_fuel_types
        existing_profile.priority_metrics = profile_data.priority_metrics
    else:
        # Create new
        existing_profile = models.UserProfile(
            user_id=profile_data.name,
            name=profile_data.name,
            primary_route=profile_data.driving_pattern.primary_route,
            highway_percentage=profile_data.driving_pattern.highway_percentage,
            yearly_km_estimate=profile_data.driving_pattern.yearly_km_estimate,
            driving_style=profile_data.driving_pattern.driving_style,
            condition=profile_data.vehicle_requirements.condition,
            transmission=profile_data.vehicle_requirements.transmission,
            eco_label_required=profile_data.vehicle_requirements.eco_label_required,
            min_length=profile_data.vehicle_requirements.min_length,
            target_length=profile_data.vehicle_requirements.target_length,
            max_length=profile_data.vehicle_requirements.max_length,
            budget_min=profile_data.budget.budget_min,
            budget_max=profile_data.budget.budget_max,
            currency=profile_data.budget.currency,
            preferred_fuel_types=profile_data.vehicle_requirements.preferred_fuel_types,
            priority_metrics=profile_data.priority_metrics
        )
        db.add(existing_profile)
    
    db.commit()
    db.refresh(existing_profile)
    return existing_profile


@app.get("/api/profile/{user_id}", response_model=UserProfileSchema, tags=["Profile"])
async def get_profile(user_id: str, db: Session = Depends(get_db)):
    """Get user profile"""
    profile = db.query(models.UserProfile).filter(
        models.UserProfile.user_id == user_id
    ).first()
    
    if not profile:
        raise HTTPException(status_code=404, detail="Profile not found")
    
    return profile


# ============================================
# PLACEHOLDER ENDPOINTS (Phase 2)
# ============================================

@app.get("/api/search", tags=["Search"])
async def search_vehicles(
    fuel_type: str = "hybrid",
    max_price: float = 40000,
    db: Session = Depends(get_db)
):
    """Search for vehicles - Coming in Phase 2"""
    return {
        "message": "Search functionality coming in Phase 2",
        "status": "not_implemented"
    }


@app.post("/api/analysis/tco", tags=["Analysis"])
async def calculate_tco(vehicle_id: int, db: Session = Depends(get_db)):
    """Calculate TCO for vehicle - Coming in Phase 2"""
    return {
        "message": "TCO calculation endpoint coming in Phase 2",
        "status": "not_implemented"
    }


@app.get("/api/recommendations", tags=["Recommendations"])
async def get_recommendations(user_id: str, db: Session = Depends(get_db)):
    """Get recommendations - Coming in Phase 2"""
    return {
        "message": "Recommendations coming in Phase 2",
        "status": "not_implemented"
    }


# ============================================
# STARTUP/SHUTDOWN EVENTS
# ============================================

@app.on_event("startup")
async def startup_event():
    """Initialize on startup"""
    print(f"🚀 {settings.APP_NAME} v{settings.APP_VERSION} started")
    print(f"📊 Database: {settings.DATABASE_URL}")
    print(f"🤖 LLM: {settings.OLLAMA_MODEL} at {settings.OLLAMA_BASE_URL}")


@app.on_event("shutdown")
async def shutdown_event():
    """Cleanup on shutdown"""
    print(f"🛑 {settings.APP_NAME} shutdown")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",
        port=8000,
        reload=settings.DEBUG
    )
