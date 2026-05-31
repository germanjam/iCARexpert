"""TCO (Total Cost of Ownership) Calculator Service"""

from typing import Dict, Any


class TCOCalculator:
    """Calculate total cost of ownership for vehicles"""

    def __init__(self, yearly_km: int = 18000, years: int = 5):
        """
        Initialize TCO calculator
        
        Args:
            yearly_km: Estimated yearly kilometers
            years: Period for calculation (default 5 years)
        """
        self.yearly_km = yearly_km
        self.years = years
        self.highway_km_yearly = int(yearly_km * 0.95)
        self.urban_km_yearly = int(yearly_km * 0.05)
        
        # Spanish market constants
        self.fuel_price_per_liter = 1.50
        self.electricity_price_per_kwh = 0.25
        self.fast_charging_price_per_kwh = 0.45
        self.annual_insurance = 350
        self.annual_maintenance_hybrid = 600
        self.annual_maintenance_electric = 300
        self.annual_maintenance_diesel = 700
        self.ap66_toll_one_way = 28.50
        self.annual_ap66_trips = 4

    def calculate_fuel_cost(self, consumption_per_100km: float, fuel_type: str) -> Dict[str, float]:
        """
        Calculate fuel/electricity costs
        
        Args:
            consumption_per_100km: L/100km or kWh/100km
            fuel_type: "hybrid", "electric", "diesel", "gasoline"
        
        Returns:
            Dictionary with yearly and 5-year costs
        """
        if fuel_type == "hybrid":
            yearly_consumption = (self.yearly_km / 100) * consumption_per_100km
            yearly_cost = yearly_consumption * self.fuel_price_per_liter
            
        elif fuel_type == "electric":
            yearly_consumption = (self.yearly_km / 100) * consumption_per_100km
            home_charging = (self.urban_km_yearly / 100) * consumption_per_100km
            highway_charging = (self.highway_km_yearly / 100) * consumption_per_100km
            
            home_cost = home_charging * self.electricity_price_per_kwh
            highway_cost = highway_charging * self.fast_charging_price_per_kwh
            yearly_cost = home_cost + highway_cost
            
        else:
            yearly_consumption = (self.yearly_km / 100) * consumption_per_100km
            yearly_cost = yearly_consumption * self.fuel_price_per_liter
        
        total_5y = yearly_cost * self.years
        
        return {
            "yearly_fuel_cost": round(yearly_cost, 2),
            "total_fuel_5y": round(total_5y, 2)
        }

    def calculate_maintenance_cost(self, fuel_type: str) -> Dict[str, float]:
        """
        Calculate maintenance costs based on fuel type
        
        Args:
            fuel_type: "hybrid", "electric", "diesel", "gasoline"
        
        Returns:
            Dictionary with yearly and 5-year maintenance costs
        """
        if fuel_type == "hybrid":
            yearly_maintenance = self.annual_maintenance_hybrid
        elif fuel_type == "electric":
            yearly_maintenance = self.annual_maintenance_electric
        else:
            yearly_maintenance = self.annual_maintenance_diesel
        
        total_5y = yearly_maintenance * self.years
        
        return {
            "yearly_maintenance_cost": round(yearly_maintenance, 2),
            "total_maintenance_5y": round(total_5y, 2)
        }

    def calculate_insurance_tax(self) -> Dict[str, float]:
        """
        Calculate insurance and tax costs
        Spanish eco vehicles get tax benefits
        
        Returns:
            Dictionary with yearly and 5-year costs
        """
        yearly_insurance = self.annual_insurance
        yearly_tax = 0
        yearly_fixed = yearly_insurance + yearly_tax
        total_5y = yearly_fixed * self.years
        
        return {
            "yearly_insurance_cost": round(yearly_insurance, 2),
            "yearly_tax_cost": 0.0,
            "total_insurance_5y": round(yearly_insurance * self.years, 2),
            "total_tax_5y": 0.0
        }

    def calculate_tolls(self) -> Dict[str, float]:
        """
        Calculate AP-66 toll costs (Madrid-Asturias)
        
        Returns:
            Dictionary with yearly and 5-year toll costs
        """
        yearly_tolls = self.ap66_toll_one_way * self.annual_ap66_trips
        total_5y = yearly_tolls * self.years
        
        return {
            "yearly_toll_cost": round(yearly_tolls, 2),
            "total_tolls_5y": round(total_5y, 2)
        }

    def calculate_depreciation(self, purchase_price: float) -> Dict[str, float]:
        """
        Estimate vehicle depreciation
        Eco vehicles retain better value (50% at 5 years)
        
        Args:
            purchase_price: Vehicle purchase price in EUR
        
        Returns:
            Dictionary with resale value and depreciation %
        """
        depreciation_percentage = 0.50
        resale_value = purchase_price * depreciation_percentage
        
        return {
            "estimated_resale_value": round(resale_value, 2),
            "depreciation_percentage": depreciation_percentage
        }

    def calculate_total_tco(
        self,
        purchase_price: float,
        consumption_per_100km: float,
        fuel_type: str
    ) -> Dict[str, Any]:
        """
        Calculate complete TCO for a vehicle
        
        Args:
            purchase_price: Vehicle price in EUR
            consumption_per_100km: Fuel/electricity consumption
            fuel_type: "hybrid", "electric", "diesel", "gasoline"
        
        Returns:
            Complete TCO breakdown
        """
        fuel_data = self.calculate_fuel_cost(consumption_per_100km, fuel_type)
        maintenance_data = self.calculate_maintenance_cost(fuel_type)
        insurance_data = self.calculate_insurance_tax()
        tolls_data = self.calculate_tolls()
        depreciation_data = self.calculate_depreciation(purchase_price)
        
        # Calculate total
        total_tco = (
            purchase_price +
            fuel_data["total_fuel_5y"] +
            maintenance_data["total_maintenance_5y"] +
            insurance_data["total_insurance_5y"] +
            insurance_data["total_tax_5y"] +
            tolls_data["total_tolls_5y"] -
            depreciation_data["estimated_resale_value"]
        )
        
        daily_cost = total_tco / (365 * self.years)
        monthly_cost = daily_cost * 30
        yearly_cost = total_tco / self.years
        
        return {
            "purchase_price": round(purchase_price, 2),
            "yearly_fuel_cost": fuel_data["yearly_fuel_cost"],
            "yearly_maintenance_cost": maintenance_data["yearly_maintenance_cost"],
            "yearly_insurance_cost": insurance_data["yearly_insurance_cost"],
            "yearly_tax_cost": insurance_data["yearly_tax_cost"],
            "yearly_toll_cost": tolls_data["yearly_toll_cost"],
            
            "total_fuel_5y": fuel_data["total_fuel_5y"],
            "total_maintenance_5y": maintenance_data["total_maintenance_5y"],
            "total_insurance_5y": insurance_data["total_insurance_5y"],
            "total_tax_5y": insurance_data["total_tax_5y"],
            "total_tolls_5y": tolls_data["total_tolls_5y"],
            
            "estimated_resale_value": depreciation_data["estimated_resale_value"],
            "depreciation_percentage": depreciation_data["depreciation_percentage"],
            
            "total_tco_5y": round(total_tco, 2),
            "daily_cost": round(daily_cost, 2),
            "monthly_cost": round(monthly_cost, 2),
            "yearly_cost": round(yearly_cost, 2)
        }
