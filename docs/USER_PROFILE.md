# User Profile Configuration Guide

## Your Profile (Madrid-Asturias)

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
    "min_length": 4.0,
    "target_length": 4.10,
    "max_length": 4.20,
    "preferred_fuel_types": ["hybrid", "electric"]
  },
  "budget": {
    "budget_min": 20000,
    "budget_max": 40000,
    "currency": "EUR"
  },
  "priority_metrics": ["efficiency", "reliability", "comfort"]
}
```

## Understanding Your Profile

### Driving Pattern

- **primary_route:** Madrid-Asturias via AP-66
- **highway_percentage:** 0.95 = 95% highway driving
- **yearly_km_estimate:** 18,000 km/year
  - 4 trips Madrid-Asturias: 1,440 km
  - Rest of year: 16,560 km
- **driving_style:** steady_highway = predictable fuel consumption

### Vehicle Requirements

- **condition:** new (factory fresh)
- **transmission:** automatic
- **eco_label_required:** true (Spanish label "0")
- **length:** 4.10-4.20m (parking maneuverability)
- **fuel_types:** hybrid and electric preferred

### Budget

- **Range:** €20,000 - €40,000
- **Includes:** All costs, delivery, extras

### Priority Metrics

1. **efficiency** - Low consumption/operating costs
2. **reliability** - Brand reputation, durability
3. **comfort** - Long journey comfort (6+ hours)

## TCO Example (Kia Niro Hybrid)

**Yearly Costs:**
- Fuel: €240 (5.2 L/100km @ 1.50€/L)
- Maintenance: €600
- Insurance: €350
- Tax: €0 (eco vehicle)
- Tolls (AP-66): €114
- **Total yearly: €1,304**

**5-Year Projection:**
- Purchase: €28,000
- Operating (5y): €6,520
- Tolls (5y): €570
- Resale value: -€14,000 (50% retention)
- **Total TCO: €21,090**
- **Monthly: €351**

## Hybrid vs Electric Analysis

### Hybrid (Recommended for your case)
✅ Unlimited autonomy (gas always available)
✅ 1 quick fuel stop per trip
✅ Lower initial cost
✅ Proven reliability
❌ Slightly higher fuel consumption

### Electric
✅ Lower operating costs
✅ Environmental benefits
✅ Quieter ride
❌ Requires 2-3 charging stops per 360km trip
❌ Charging infrastructure dependency
❌ Higher initial cost

**For Madrid-Asturias:** Hybrid is more practical.

## Customization Examples

### Different Budget
```json
{
  "budget": {
    "budget_min": 15000,
    "budget_max": 50000
  }
}
```

### Electric Only
```json
{
  "vehicle_requirements": {
    "preferred_fuel_types": ["electric"]
  }
}
```

### Different Route
```json
{
  "driving_pattern": {
    "primary_route": "Barcelona-Valencia",
    "highway_percentage": 0.85,
    "yearly_km_estimate": 25000
  }
}
```

## Recommended Vehicles for Your Profile

### Tier 1 (Best Overall)
- **Kia Niro Hybrid** - €28,000 | 4.8 L/100km
- **Hyundai Kona Hybrid** - €25,000 | 5.1 L/100km

### Tier 2 (Premium)
- **Lexus UX 250h** - €35,000 | 4.2 L/100km
- **Tesla Model 3** - €42,000 | Electric

### Tier 3 (Value)
- **MG 4 EV** - €24,000 | Electric | 4.10m length

## Next Steps

1. Create profile via API
2. Run TCO calculations
3. Search for matching vehicles (Phase 2)
4. Receive AI recommendations
5. Negotiate with sellers

## Support

For profile optimization:
- GitHub Issues
- GitHub Discussions
- Check docs/
