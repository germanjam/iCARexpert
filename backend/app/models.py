"""SQLAlchemy ORM Models"""

from datetime import datetime
from sqlalchemy import Column, Integer, String, Float, DateTime, JSON, Boolean, ForeignKey, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class UserProfile(Base):
    """User profile with driving patterns and preferences"""
    __tablename__ = "user_profiles"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String(100), unique=True, index=True)
    name = Column(String(255))

    # Driving Pattern
    primary_route = Column(String(255))
    highway_percentage = Column(Float, default=0.95)
    yearly_km_estimate = Column(Integer, default=18000)
    driving_style = Column(String(50))

    # Vehicle Requirements
    condition = Column(String(50))
    transmission = Column(String(50))
    eco_label_required = Column(Boolean, default=True)
    min_length = Column(Float)
    target_length = Column(Float)
    max_length = Column(Float)

    # Budget
    budget_min = Column(Float)
    budget_max = Column(Float)
    currency = Column(String(3), default="EUR")

    # Preferences
    preferred_fuel_types = Column(JSON)
    priority_metrics = Column(JSON)

    # Timestamps
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    searches = relationship("Search", back_populates="profile")
    offers = relationship("Offer", back_populates="profile")


class Search(Base):
    """Search results for vehicles"""
    __tablename__ = "searches"

    id = Column(Integer, primary_key=True, index=True)
    profile_id = Column(Integer, ForeignKey("user_profiles.id"))
    fuel_types = Column(JSON)
    max_price = Column(Float)
    min_price = Column(Float)
    search_timestamp = Column(DateTime, default=datetime.utcnow)
    total_results = Column(Integer, default=0)

    profile = relationship("UserProfile", back_populates="searches")
    vehicles = relationship("Vehicle", back_populates="search")


class Vehicle(Base):
    """Vehicle data from scraping"""
    __tablename__ = "vehicles"

    id = Column(Integer, primary_key=True, index=True)
    search_id = Column(Integer, ForeignKey("searches.id"))

    # Basic Info
    brand = Column(String(100))
    model = Column(String(100))
    year = Column(Integer)
    price = Column(Float)

    # Specifications
    length = Column(Float)
    fuel_type = Column(String(50))
    transmission = Column(String(50))
    power_cv = Column(Integer)
    consumption_highway = Column(Float)
    battery_kwh = Column(Float, nullable=True)
    range_km = Column(Integer, nullable=True)

    # Additional Info
    eco_label = Column(String(50))
    km_odometer = Column(Integer, nullable=True)

    # Seller Info
    seller_name = Column(String(255))
    seller_email = Column(String(255))
    seller_phone = Column(String(20), nullable=True)
    dealer_url = Column(String(500), nullable=True)

    # Metadata
    source = Column(String(100))
    source_url = Column(String(500))
    scraped_at = Column(DateTime, default=datetime.utcnow)

    search = relationship("Search", back_populates="vehicles")
    offers = relationship("Offer", back_populates="vehicle")
    tco_data = relationship("TCOData", back_populates="vehicle", uselist=False)


class Offer(Base):
    """Seller offers and inquiries"""
    __tablename__ = "offers"

    id = Column(Integer, primary_key=True, index=True)
    profile_id = Column(Integer, ForeignKey("user_profiles.id"))
    vehicle_id = Column(Integer, ForeignKey("vehicles.id"))

    # Inquiry Status
    inquiry_sent_at = Column(DateTime, nullable=True)
    response_received_at = Column(DateTime, nullable=True)
    inquiry_status = Column(String(50))
    seller_response_text = Column(Text, nullable=True)
    final_price = Column(Float, nullable=True)

    # Negotiation
    asking_price = Column(Float)
    negotiation_status = Column(String(50))
    negotiation_margin_estimated = Column(Float, nullable=True)

    # Timestamps
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    profile = relationship("UserProfile", back_populates="offers")
    vehicle = relationship("Vehicle", back_populates="offers")
    analysis = relationship("OfferAnalysis", back_populates="offer", uselist=False)


class TCOData(Base):
    """Total Cost of Ownership calculations"""
    __tablename__ = "tco_data"

    id = Column(Integer, primary_key=True, index=True)
    vehicle_id = Column(Integer, ForeignKey("vehicles.id"), unique=True)

    # 5-Year Projection
    purchase_price = Column(Float)
    yearly_fuel_cost = Column(Float)
    yearly_maintenance_cost = Column(Float)
    yearly_insurance_cost = Column(Float)
    yearly_tax_cost = Column(Float)
    yearly_toll_cost = Column(Float, default=0)

    # Total 5-Year
    total_fuel_5y = Column(Float)
    total_maintenance_5y = Column(Float)
    total_insurance_5y = Column(Float)
    total_tax_5y = Column(Float)
    total_tolls_5y = Column(Float)

    # Depreciation
    estimated_resale_value = Column(Float)
    depreciation_percentage = Column(Float)

    # Final TCO
    total_tco_5y = Column(Float)
    daily_cost = Column(Float)
    monthly_cost = Column(Float)
    yearly_cost = Column(Float)

    calculated_at = Column(DateTime, default=datetime.utcnow)

    vehicle = relationship("Vehicle", back_populates="tco_data")


class OfferAnalysis(Base):
    """AI analysis of offers"""
    __tablename__ = "offer_analysis"

    id = Column(Integer, primary_key=True, index=True)
    offer_id = Column(Integer, ForeignKey("offers.id"), unique=True)

    # Scoring
    tco_score = Column(Float)
    reliability_score = Column(Float)
    feature_match_score = Column(Float)
    seller_rating_score = Column(Float)
    overall_score = Column(Float)

    # Analysis Text
    analysis_text = Column(Text)
    pros = Column(JSON)
    cons = Column(JSON)
    recommendation = Column(String(50))
    negotiation_strategy = Column(Text)

    # Generated by LLM
    llm_model = Column(String(100))
    analyzed_at = Column(DateTime, default=datetime.utcnow)

    offer = relationship("Offer", back_populates="analysis")
