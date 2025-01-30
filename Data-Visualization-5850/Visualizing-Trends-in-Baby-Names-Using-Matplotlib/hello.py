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

# Questions:
# 1- What were the 5 most popular male and female baby names in 2023, and how has their frequency changed in the past   10 years?
    # Hint: Remember to normalize the frequency of each name by the total number of births that year so that the data is directly comparable from year to year.

# What were the 5 most popular male and female baby names on average over the last 5 years, and how has their frequency changed in the past 20 years?

# Common baby names are often inspired by cultural trends. How do the frequencies of the names Tiana, Elsa, Anna (or Ana), Moana, and Ariel change over time? How does this relate to the release date of the Disney movies with characters of the same name?
#Hint: Lookup the release dates for (1) Princess and the Frog; (2) Frozen; (3) Moana; (4) Frozen 2; (5) The Little Mermaid (Original and Live Action Remake); (6) Moana 2. Annotate these release dates on your visualization and see how they relate to frequency of the names.

# How has the percentage of babies with names represented in the top 1000 changed over time? What does this suggest about naming patterns overall?

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the data
FILE_PATH_NATIONAL_NAMES = 'NationalNames.csv'
FILE_PATH_TOTAL_BIRTHS = 'TotalBirths.csv'

# data file paths
NATIONAL_NAMES_DATA = pd.read_csv(FILE_PATH_NATIONAL_NAMES)
TOTAL_BIRTHS_DATA = pd.read_csv(FILE_PATH_TOTAL_BIRTHS)

# Question: 1
five_most_popular_male_names_2023 = NATIONAL_NAMES_DATA[NATIONAL_NAMES_DATA[NATIONAL_NAMES_DATA[(NATIONAL_NAMES_DATA[NATIONAL_NAMES_DATA['Sex'] == 'Male')]
                                                                            & (NATIONAL_NAMES_DATA[NATIONAL_NAMES_DATA['Year'] == "2023" )]
# five_most_popular_female_names_2023 = NATIONAL_NAMES_DATA['Name']
