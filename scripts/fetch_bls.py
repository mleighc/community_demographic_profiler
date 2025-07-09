import yaml
import pandas as pd

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

# Load BLS unemployment spreadsheet
df_bls_counties_23 = pd.read_excel("../data_raw/laucnty23.xlsx", skiprows=1)

# Clean up variable names
df_bls_counties_23.columns = (
    df_bls_counties_23.columns.str.strip()
    .str.lower()
    .str.replace(" ", "_")
    .str.replace("-", "_")
)

df_bls_counties_23["county_fips_code"] = (
    df_bls_counties_23["county_fips_code"].astype("Int64").astype(str).str.zfill(3)
)

df_bls_counties_23["state_fips_code"] = df_bls_counties_23["state_fips_code"].astype(
    "Int64"
)

fips_codes = list(counties.values())

df_bls_metro_det_23 = df_bls_counties_23[
    df_bls_counties_23["county_fips_code"].isin(list(counties.values()))
    & (df_bls_counties_23["state_fips_code"] == 26)
]

df_bls_metro_det_23.drop(columns=["laus_code", "year"], inplace=True)

# print(df_bls_metro_det_23)

df_bls_metro_det_23.to_csv("../data_clean/bls_laus_2023_clean.csv", index=False)
