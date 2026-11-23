import pytest
import requests
from pydantic import ValidationError
from schemas import PropertyListing

BASE_URL = "https://httpbin.org"


def test_create_and_validate_property_listing():
    """POST: Create a real estate listing and validate full JSON schema via Pydantic"""
    listing_payload = {
        "id": 1001,
        "title": "Modern Waterfront Villa with Private Dock",
        "property_type": "villa",
        "price_usd": 1250000.0,
        "area_sqft": 3400.5,
        "bedrooms": 4,
        "city": "Seattle",
        "location": {
            "lat": 47.6062,
            "lng": -122.3321
        },
        "is_active": True
    }

    response = requests.post(f"{BASE_URL}/post", json=listing_payload)
    assert response.status_code == 200

    returned_data = response.json()["json"]
    # Validate response structure, types, and geo boundaries via Pydantic
    validated_property = PropertyListing(**returned_data)

    assert validated_property.city == "Seattle"
    assert validated_property.location.lat == 47.6062
    assert validated_property.is_active is True


@pytest.mark.parametrize("city, max_price, min_beds", [
    ("Ottawa", 900000, 3),
    ("Seattle", 1500000, 4),
    ("Charlotte", 750000, 3),
])
def test_search_properties_by_filters(city, max_price, min_beds):
    """GET: Verify search query parameters for real estate filtering"""
    params = {
        "city": city,
        "max_price": max_price,
        "min_bedrooms": min_beds
    }
    response = requests.get(f"{BASE_URL}/get", params=params)
    assert response.status_code == 200

    query_args = response.json()["args"]
    assert query_args["city"] == city
    assert int(query_args["max_price"]) == max_price
    assert int(query_args["min_bedrooms"]) == min_beds


def test_invalid_property_data_rejected_by_schema():
    """NEGATIVE: Ensure schema validation catches corrupted price and geo coordinates"""
    corrupted_data = {
        "id": 1002,
        "title": "Corrupted Listing Data",
        "property_type": "house",
        "price_usd": -50000.0,  # Invalid negative price
        "area_sqft": 1800.0,
        "bedrooms": 3,
        "city": "Bellevue",
        "location": {
            "lat": 145.0,  # Invalid latitude (> 90)
            "lng": -122.2015
        },
        "is_active": True
    }

    with pytest.raises(ValidationError):
        PropertyListing(**corrupted_data)
