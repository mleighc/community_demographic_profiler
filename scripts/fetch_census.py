from census import Census
import yaml
import pandas as pd

# ACS5 docs: https://www.census.gov/data/developers/data-sets/acs-5year.html
# Variable Names/Codes: https://api.census.gov/data/2021/acs/acs5/variables.html

# Load credentials
with open("../config/credentials.yaml") as f:
    config = yaml.safe_load(f)

c = Census(config["census"]["api_key"])

# Define counties (FIPS): Wayne=163, Oakland=125, Washtenaw=161, Macomb=099
state_fips = "26"
counties = {"Wayne": "163", "Oakland": "125", "Washtenaw": "161", "Macomb": "099"}

# Variables to fetch
variables = {
    "B01003_001E": "population",
    "B19013_001E": "median_income",
    "B01002_001E": "median_age",
    "B17001_001E": "pov_status_universe_total",
    "B17001_002E": "num_below_pov_level",
    "B15003_001E": "pop_over_25",
    "B15003_022E": "num_with_bachelors",
    "B15003_023E": "num_with_masters",
    "B15003_025E": "num_with_doctorate",
    "B15003_021E": "num_with_associates",
    "B15003_024E": "num_with_professional_degree",
}

rows = []
for name, fips in counties.items():
    result = c.acs5.get(
        list(variables.keys()), {"for": f"county:{fips}", "in": f"state:{state_fips}"}
    )[0]
    row = {variables[k]: result[k] for k in variables}
    row["county"] = name
    rows.append(row)

df = pd.DataFrame(rows)
print(df)
