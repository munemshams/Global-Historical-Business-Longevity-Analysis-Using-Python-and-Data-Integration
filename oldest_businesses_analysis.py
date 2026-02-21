import pandas as pd
import os

# -----------------------------------------------------------
# Global Historical Business Longevity Analysis
# -----------------------------------------------------------
# This script loads four CSV datasets, performs data merging,
# aggregation, and analysis to determine:
#   1) The oldest business on each continent
#   2) Countries missing business data (including new businesses)
#   3) The oldest business category per continent
# It outputs three clean CSV files for portfolio use.
# -----------------------------------------------------------

# Paths
DATA_DIR = "data"
OUTPUT_DIR = "outputs"

os.makedirs(OUTPUT_DIR, exist_ok=True)

# Load datasets
businesses = pd.read_csv(os.path.join(DATA_DIR, "businesses.csv"))
new_businesses = pd.read_csv(os.path.join(DATA_DIR, "new_businesses.csv"))
countries = pd.read_csv(os.path.join(DATA_DIR, "countries.csv"))
categories = pd.read_csv(os.path.join(DATA_DIR, "categories.csv"))

# -----------------------------------------------------------
# 1. Oldest business on each continent
# -----------------------------------------------------------

# Merge businesses with country information
businesses_countries = businesses.merge(countries, on="country_code")

# Get the oldest founding year per continent
continent_min_year = businesses_countries.groupby("continent")["year_founded"].min().reset_index()

# Merge to recover country + business name for those years
oldest_business_continent = continent_min_year.merge(
    businesses_countries,
    on=["continent", "year_founded"],
    how="left"
)[["continent", "country", "business", "year_founded"]]

# Save output
oldest_business_continent.to_csv(os.path.join(OUTPUT_DIR, "oldest_business_continent.csv"), index=False)

# -----------------------------------------------------------
# 2. Countries missing business data (including new businesses)
# -----------------------------------------------------------

# Combine old + new business records
all_businesses = pd.concat([businesses, new_businesses], ignore_index=True)

# Outer merge to identify countries without business entries
merged_countries = all_businesses.merge(
    countries,
    on="country_code",
    how="outer",
    indicator=True
)

# Filter countries with no matching business records
missing_rows = merged_countries[merged_countries["_merge"] != "both"]

count_missing = (
    missing_rows.groupby("continent")["country"]
    .count()
    .reset_index()
    .rename(columns={"country": "count_missing"})
)

# Save output
count_missing.to_csv(os.path.join(OUTPUT_DIR, "count_missing.csv"), index=False)

# -----------------------------------------------------------
# 3. Oldest founding year by continent & business category
# -----------------------------------------------------------

# Merge businesses with category descriptions
businesses_categories = businesses.merge(categories, on="category_code")

# Merge with country information
businesses_full = businesses_categories.merge(countries, on="country_code")

# Group by continent + category to find earliest year founded
oldest_by_continent_category = (
    businesses_full.groupby(["continent", "category"])["year_founded"]
    .min()
    .reset_index()
)

# Save output
oldest_by_continent_category.to_csv(
    os.path.join(OUTPUT_DIR, "oldest_by_continent_category.csv"),
    index=False
)

print("Analysis complete. CSV files saved in 'outputs/'")
