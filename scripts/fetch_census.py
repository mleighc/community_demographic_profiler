from census import Census
import yaml

# Load credentials
with open("../config/credentials.yaml") as f:
    config = yaml.safe_load(f)

c = Census(config["census"]["api_key"])

# Define variables to fetch
variables = ["B19013_001E"]  # Median household income

# You must use `.get()` and specify the geography explicitly
data = c.acs5.get(variables, {"for": "zip code tabulation area:*"})

# Filter for specific ZCTAs if needed
target_zips = {"48104", "48201", "49001"}
filtered_data = [row for row in data if row["zip code tabulation area"] in target_zips]

# Display
for row in filtered_data:
    print(row["zip code tabulation area"], row["B19013_001E"])
