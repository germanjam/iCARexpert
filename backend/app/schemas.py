"""Pydantic schemas for request/response validation"""

from datetime import datetime
from typing import List, Optional, Dict, Any
from pydantic import BaseModel, Field


class DrivingPatternSchema(BaseModel):
    """User driving pattern"""
    primary_route: str = "Madrid-Asturias"
    highway_percentage: float = Field(0.95, ge=0.0, le=1.0)
    yearly_km_estimate: int = Field(18000, ge=1000)
    driving_style: str = "steady_highway"


class VehicleRequirementsSchema(BaseModel):
    """Vehicle requirements"""
    condition: str = "new"
    transmission: str = "automatic"
    eco_label_required: bool = True
    min_length: Optional[float] = 4.0
    target_length: float = 4.10
    max_length: float = 4.20
    preferred_fuel_types: List[str] = ["hybrid", "electric"]


class BudgetSchema(BaseModel):
    """Budget configuration"""
    budget_min: float = Field(20000, ge=0)
    budget_max: float = Field(40000, ge=0)
    currency: str = "EUR"


class UserProfileCreateSchema(BaseModel):
    """Create or update user profile"""
    name: str
    driving_pattern: DrivingPatternSchema
    vehicle_requirements: VehicleRequirementsSchema
    budget: BudgetSchema
    priority_metrics: List[str] = ["efficiency", "reliability", "comfort"]


class UserProfileSchema(UserProfileCreateSchema):
    """Full user profile"""
    id: int
    user_id: str
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class VehicleSchema(BaseModel):
    """Vehicle information"""
    brand: str
    model: str
    year: int
    price: float
    length: float
    fuel_type: str
    transmission: str
    power_cv: int
    consumption_highway: float
    battery_kwh: Optional[float] = None
    range_km: Optional[int] = None
    eco_label: str
    seller_name: str
    seller_email: str
    seller_phone: Optional[str] = None
    dealer_url: Optional[str] = None
    source: str
    source_url: str


class VehicleDetailSchema(VehicleSchema):
    """Vehicle with ID and timestamps"""
    id: int
    scraped_at: datetime

    class Config:
        from_attributes = True


class TCODataSchema(BaseModel):
    """TCO calculation results"""
    vehicle_id: int
    purchase_price: float
    yearly_fuel_cost: float
    yearly_maintenance_cost: float
    yearly_insurance_cost: float
    yearly_tax_cost: float
    yearly_toll_cost: float
    
    total_fuel_5y: float
    total_maintenance_5y: float
    total_insurance_5y: float
    total_tax_5y: float
    total_tolls_5y: float
    
    estimated_resale_value: float
    depreciation_percentage: float
    
    total_tco_5y: float
    daily_cost: float
    monthly_cost: float
    yearly_cost: float
    calculated_at: datetime

    class Config:
        from_attributes = True


class OfferSchema(BaseModel):
    """Offer with metadata"""
    id: int
    profile_id: int
    vehicle_id: int
    asking_price: float
    inquiry_status: str
    negotiation_status: str
    final_price: Optional[float] = None
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class MessageSchema(BaseModel):
    """Simple message response"""
    message: str
    status: str = "success"


class ErrorSchema(BaseModel):
    """Error response"""
    error: str
    status: str = "error"
    details: Optional[Dict[str, Any]] = None
