About Dataset
This dataset provides a daily, county-level integration of COVID-19 health data and human behavior metrics across the United States for the entire year of 2021.
While epidemiological and mobility datasets are often released separately, this collection is unique because it has been rigorously cleaned, normalized, and integrated into a single high-density record for each day and county. This allows researchers to immediately begin analyzing the complex feedback loops between viral spread and human activity without the need for extensive data engineering.

The dataset encompasses approximately 935,000 records covering over 3,000 US counties from January 1, 2021, to December 31, 2021.
Key features include:

Epidemiological Metrics: Cumulative and daily new cases/deaths.
Mobility Metrics: Percentage changes from baseline across six sectors (Retail, Grocery, Parks, Transit hubs, Workplaces, and Residential).
Temporal Indicators: Day of the week, weekend flags, and US Federal Holiday indicators.
Data Engineering Pipeline
Acquisition: Data was harvested via the disease.sh API and Google’s Global Mobility database.
Cleaning: Standardized geographic identifiers (State/County names), padded FIPS codes to 5 digits, and resolved logical reporting errors (e.g., negative daily counts or deaths exceeding cases).
Integration: Merged using a compound spatio-temporal key [State, County, Date].
Refinement: Applied 7-day rolling averages (not included in the raw file but used in analysis) to handle weekend reporting drops.
Inspiration & Use Cases
Reverse Causality: Study how rising infection rates drive voluntary social distancing (fear-driven behavior).
Sector Analysis: Identify which mobility sectors (e.g., Public Transit) are most sensitive to pandemic waves.
Event Impact: Measure the "super-spreader" effect of major federal holidays.
Acknowledgements
Health Data: Provided by the New York Times and Johns Hopkins University via the disease.sh API.
Mobility Data: Google LLC "COVID-19 Community Mobility Reports".
Column Descriptions
date: The observation date (YYYY-MM-DD).
county: Standardized name of the US county (lowercase, suffixes like "County" removed).
state: Standardized name of the US state (lowercase).
fips: 5-digit Federal Information Processing System unique identifier for the county.
cases: Cumulative confirmed COVID-19 cases up to this date.
deaths: Cumulative confirmed COVID-19 deaths up to this date.
daily_cases: New COVID-19 cases reported on this specific day.
daily_deaths: New COVID-19 deaths reported on this specific day.
day_of_week: Numerical day of the week (0=Monday, 6=Sunday).
is_weekend: Binary flag (1 = Saturday or Sunday, 0 = Weekday).
is_holiday: Binary flag (1 = US Federal Holiday, 0 = Normal day).
retail_recreation: % change in visits to places like restaurants, cafes, shopping centers, and museums.
grocery_pharmacy: % change in visits to markets, food warehouses, and pharmacies.
parks: % change in visits to local parks, public beaches, and plazas.
transit: % change in visits to public transport hubs like subway, bus, and train stations.
workplaces: % change in visits to places of work.
residential: % change in duration of time spent at places of residence.
