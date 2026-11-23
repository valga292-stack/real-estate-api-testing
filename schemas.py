from pydantic import BaseModel, Field


class GeoLocation(BaseModel):
    lat: float = Field(..., ge=-90, le=90, description="Latitude coordinate")
    lng: float = Field(..., ge=-180, le=180, description="Longitude coordinate")


class PropertyListing(BaseModel):
    id: int = Field(..., gt=0)
    title: str = Field(..., min_length=5)
    property_type: str = Field(..., pattern="^(house|apartment|villa|townhouse)$")
    price_usd: float = Field(..., gt=0)
    area_sqft: float = Field(..., gt=100)
    bedrooms: int = Field(..., ge=0)
    city: str
    location: GeoLocation
    is_active: bool
    