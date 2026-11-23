# Real Estate API Test Automation (Pytest + Pydantic)

Automated REST API test suite for a Real Estate platform built with Python, Pytest, Requests, and Pydantic. Validates property listing data contracts, geolocation boundaries, search query filtering, and negative error handling.

## Tech Stack
* Python 3.14
* Pytest — test execution, fixtures, and @pytest.mark.parametrize
* Pydantic — strict JSON schema, data type, and coordinate boundary validation
* Requests — HTTP client for API interaction
* Pytest-HTML — self-contained HTML test reporting

## Project Structure
* schemas.py — Pydantic data models (PropertyListing, GeoLocation) enforcing business rules (positive pricing, valid latitude/longitude ranges, allowed property types).
* test_real_estate_api.py — automated positive, parameterized search, and negative contract tests.
* requirements.txt — project dependencies.

## How to Run Locally

1. Clone the repository:
  
   git clone https://github.com
   cd real-estate-api-testing
   
2. Install dependencies:
  
   pip install -r requirements.txt
   
3. Run tests with HTML report generation:
  
   python -m pytest -v --html=report.html --self-contained-html
