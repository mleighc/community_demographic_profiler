import pandas as pd

# Resource: https://www.ers.usda.gov/data-products/food-access-research-atlas/download-the-data

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

df_usda_fara = pd.read_excel(
    "../data_raw/FoodAccessResearchAtlasData2019.xlsx",
    sheet_name="Food Access Research Atlas",
)

print(df_usda_fara.head())
