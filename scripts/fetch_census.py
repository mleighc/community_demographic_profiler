# fetch_census.py

from census import Census
import yaml

# Load API key
with open("config/credentials.yaml", "r") as f:
    config = yaml.safe_load(f)

c = Census(config["census"]["api_key"])

# Example: Fetch median household income from ACS 5-year 2022 by ZIP code
data = c.acs5.zipcode(
    ["B19013_001E"], config["project"]["zip_codes"]  # Median household income
)

for row in data:
    print(row["zip code tabulation area"], row["B19013_001E"])
