**Project Overview**

This project explores the fascinating question:

What makes a business survive for hundreds or even thousands of years?

Using three structured datasets of world businesses, countries, and business categories, this analysis identifies:

- The oldest operating business on each continent

- Countries missing business longevity data (with and without new business records)

- The business categories that have historically lasted the longest across regions

This project highlights practical data-engineering skills including data joining, cleaning, aggregation, and cross-table analysis.

**Project Objectives**

Using Python (pandas), the analysis answers:

1. What is the oldest business on each continent?

Output: oldest_business_continent.csv
Fields: continent, country, business, year_founded

2. Which countries lack historical business data?

Including both businesses and new_businesses datasets.
Output: count_missing.csv
Fields: continent, count_missing

3. Which business categories are most historically durable?

Oldest year founded per continent + category.
Output: oldest_by_continent_category.csv
Fields: continent, category, year_founded

**About the Dataset**

The dataset was compiled by BusinessFinancing.co.uk, documenting the oldest known still-operating business in nearly every country. 
It has been pre-cleaned and split into:

businesses.csv — primary dataset

new_businesses.csv — supplemental entries

countries.csv — country + continent mapping

categories.csv — business category lookup

**Files Included**

- 4 CSV files containing the raw datasets in the "data" folder

- 3 output CSV files onbtained by running the python script

- the raw python script titled "old_businesses_analysis.py"

**Key Insights**

-Asia is home to the world’s oldest continuously operating businesses
(e.g., Japan’s Kongō Gumi, founded in 578 AD)

- Oceania has the highest number of countries without reliable business longevity data

- Categories like Hospitality, Postal Services, and Banking consistently appear among the oldest surviving industries

- There is a strong correlation between cultural continuity and long-term business survival
