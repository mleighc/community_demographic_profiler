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
counties = {
    "Wayne": "163",
    "Oakland": "125",
    "Washtenaw": "161",
    "Macomb": "099",
    "Livingston": "093",
    "Lapeer": "087",
    "St. Clair": "147",
}

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

# store data in a dataframe
rows = []
for name, fips in counties.items():
    result = c.acs5.get(
        list(variables.keys()), {"for": f"county:{fips}", "in": f"state:{state_fips}"}
    )[0]
    row = {variables[k]: result[k] for k in variables}
    row["county"] = name
    row["fips"] = fips
    rows.append(row)

df = pd.DataFrame(rows)

# calculate additional columns
df["poverty_rate_pct"] = round(
    (df["num_below_pov_level"] / df["pov_status_universe_total"]) * 100, 1
)

degree_cols = [
    "num_with_bachelors",
    "num_with_masters",
    "num_with_professional_degree",
    "num_with_doctorate",
]
df["bachelors_or_higher"] = df[degree_cols].sum(axis=1)
df["pct_higher_ed"] = round((df["bachelors_or_higher"] / df["pop_over_25"]) * 100, 1)

# write csv to data_clean folder
df.to_csv("../data_clean/census_acs5_clean.csv", index=False)
