# Task:
# For each of the questions below, perform the following:
#
# Convert the question into a task description using Munzner's task framework to describe the action and the target.
# Create one or more visualizations to answer the question and perform the task.
# Write a brief reflection on why you chose the type of visualization(s) that you used

# Munzner's Task Framework is a method for breaking down data visualization tasks into clear steps. It helps decide what to visualize and how to design it effectively.

# 3 Main Levels:
# Why? (User’s Goal) → What do users want to achieve? (e.g., analyze trends, compare values)
# What? (Data Type) → What kind of data? (e.g., tables, networks, time-series)
# How? (Interaction & Encoding) → How to present and interact with the data? (e.g., bar charts, scatter plots, zoom, filter)

# Example: If you're visualizing sales trends:
# Why? → Find patterns over time
# What? → Sales data (time-series)
# How? → Line chart with filters for years

import pandas as pd
import matplotlib.pyplot as plt
import os # to check if the file already exist before download
import requests # to download the data from the given URLs

# STEP 1: Downloading the cvs dataset

# URLs for datasets
NATIONAL_NAMES_URL = "https://github.com/kbvatral/TeachingDatasets/raw/refs/heads/main/NationalNames.csv"
TOTAL_BIRTHS_URL = "https://github.com/kbvatral/TeachingDatasets/raw/refs/heads/main/TotalBirths.csv"

# Download the cvd files if they do already not exist
def download_csv_files(url, filename):
    if not os.path.exists(filename):
        response = requests.get(url)
        with open(filename, "wb") as file:
            file.write(response.content)
        print(filename," has been downloaded successfully")
    else:
        print(filename,"already exists")

# Download datasets if they do not already exist
download_csv_files(NATIONAL_NAMES_URL, "NationalNames.csv")
download_csv_files(TOTAL_BIRTHS_URL, "TotalBirths.csv")

# STEP 2: Loadin the data using panda

NAMES_DATA = pd.read_csv("NationalNames.csv")
BIRTHS_DATA = pd.read_csv("TotalBirths.csv")

# convertin THE Year column to int
NAMES_DATA['Year'] = NAMES_DATA['Year'].astype(int)
BIRTHS_DATA['Year'] = BIRTHS_DATA['Year'].astype(int)

# 1- What were the 5 most popular male and female baby names in 2023, and how has their frequency changed in the past 10 years?
# Hint: Remember to normalize the frequency of each name by the total number of births that year so that the data is directly comparable from year to year.

# STEP 4: mergin the data adn normalizing frequencies

from tabulate import tabulate

merged_df = NAMES_DATA.merge(BIRTHS_DATA, on="Year")

# normalizing frequencies by the total births
merged_df['NormalizedFrequency'] = merged_df['Count'] / merged_df['Births']

# sort the dataframe by specific  column,for 2023
TOP_NAMES_YEAR23 = merged_df[merged_df["Year"] == 2023].sort_values(by="Count", ascending=False)

# Get top 5 male names
TOP_5_MALE_NAMES = TOP_NAMES_YEAR23[TOP_NAMES_YEAR23["Sex"] == "M"].head(5)

#  Get top 5 female names
TOP_5_FEMALE_NAMES = TOP_NAMES_YEAR23[TOP_NAMES_YEAR23["Sex"] == "F"].head(5)

print("Top 5 male names for year 2023:")
print(tabulate(TOP_5_MALE_NAMES, headers="keys", tablefmt="double_grid"))

print("\nTop 5 female names for year 2023:")
print(tabulate(TOP_5_FEMALE_NAMES, headers="keys", tablefmt="double_grid"))



# plot trends from 2013 to 2023
plt.figure(figsize=(15, 6))

for name in TOP_5_MALE_NAMES["Name"].tolist() + TOP_5_FEMALE_NAMES["Name"].tolist():
    subgroup = merged_df[merged_df["Name"] == name]
    plt.plot(subgroup["Year"], subgroup["NormalizedFrequency"], label=name)

plt.xlabel("Year")
plt.ylabel("Normalized Frequency")
plt.title("Trends of Top 5 Male & Female Names from 2013 to 2023")
plt.legend()
plt.show()


# 2- What were the 5 most popular male and female baby names on average over the last 5 years, and how has their frequency changed in the past 20 years?

# STEP 5:

last_5years = merged_df[merged_df["Year"] >= 2018]

top_names_recent_last_5years = last_5years.groupby(["Name", "Sex"])["Count"].sum().reset_index()
top_names_recent_last_5years = top_names_recent_last_5years.sort_values(by="Count", ascending=False)

top_male_last_5years = top_names_recent_last_5years[top_names_recent_last_5years["Sex"] == "M"].head(5)
top_female_recent_last_5years = top_names_recent_last_5years[top_names_recent_last_5years["Sex"] == "F"].head(5)

# Plot trends from 2003 to 2023
plt.figure(figsize=(15, 6))

for name in top_male_last_5years["Name"].tolist() + top_female_recent_last_5years["Name"].tolist():
    subgroup = merged_df[merged_df["Name"] == name]
    plt.plot(subgroup["Year"], subgroup["NormalizedFrequency"], label=name)

plt.xlabel("Year")
plt.ylabel("Normalized Frequency")
plt.title("Trends of Top 5 Names from 2003 to 2023")
plt.legend()
plt.show()


_# 3- Common baby names are often inspired by cultural trends. How do the frequencies of the names Tiana, Elsa, Anna (or Ana), Moana, and Ariel change over time? How does this relate to the release date of the Disney movies with characters of the same name?
# Hint: Lookup the release dates for (1) Princess and the Frog; (2) Frozen; (3) Moana; (4) Frozen 2; (5) The Little Mermaid (Original and Live Action Remake); (6) Moana 2. Annotate these release dates on your visualization and see how they relate to frequency of the names.

# STEP 6: disney baby name poplarity

hot_disney_names = ["Tiana", "Elsa", "Anna", "Moana", "Ariel"]

plt.figure(figsize=(16, 6))

for name in hot_disney_names:
    subgroup = merged_df[merged_df["Name"] == name]
    plt.plot(subgroup["Year"], subgroup["NormalizedFrequency"], label=name)

disney_movies = {
    "Princess & Frog": 2009,
    "Frozen": 2013,
    "Moana": 2016,
    "Frozen 2": 2019,
    "Little Mermaid (Remake)": 2023,
    "Moana 2": 2024
}

for movie, year in disney_movies.items():
    plt.axvline(year, linestyle="dashed", color="gray")
    plt.text(year, 0.00001, movie, rotation=90, verticalalignment="bottom")

plt.xlabel("Year")
plt.ylabel("Normalized Frequency")
plt.title("Trends in Baby Names by Inspired Disney")
plt.legend()
plt.show()

# 4- How has the percentage of babies with names represented in the top 1000

# STEP 7: Percentage of newborns assigned names in the 1000 most popular

top_1000_percentage = merged_df.groupby("Year").agg({"Count": "sum", "Births": "mean"})
top_1000_percentage["Percentage"] = top_1000_percentage["Count"] / top_1000_percentage["Births"]

plt.figure(figsize=(16, 6))
plt.plot(top_1000_percentage.index, top_1000_percentage["Percentage"], marker='o', linestyle="-")
plt.xlabel("Year")
plt.ylabel("Top 1000 Names Percentage of Babies")
plt.title("Popularity of top 1000 baby names")
plt.show()
