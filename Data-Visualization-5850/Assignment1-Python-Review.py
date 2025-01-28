# Student Name: Husain Alshaikhahmed
# Student ID: T004560868
# Class: COMP 5850
# Instructor: Professor Dr. Caleb Vatral
# Assignment: Python Review
# Due Date: January 22, 2025, 11:59 PM

# Description :



# Task:
# Part 3: Regression
# Using Scikit-learn, create a linear regression model to predict a fish’s weight based on the other numerical features (length1, length2, length3, height, and width). Ensure the model is trained only on the training split.
# Print the coefficients and intercept of the trained regression model.
# Calculate and print the model’s accuracy (e.g., R^2 score) on both the training and testing splits.

# Part 4: Classification
# Using Scikit-learn, create a fully-grown decision tree classifier to predict a fish’s species using its length, width, and height measurements. Ensure that the model does not use the fish’s weight in the calculations, and that it is trained only on the training split.
# Calculate and print the model’s accuracy on both the training and testing splits. Additionally, print the depth of the fully grown decision tree.
# Optimize the decision tree by determining the best maximum depth:
# Train multiple decision tree models with the max_depth parameter ranging from 1 to the depth of the fully-grown tree.
# For each depth, record the training and testing accuracy.
# Use this information to identify the depth that provides the best generalization performance.



# Part 1: Data Preparation
# Using Pandas, download and load the fish dataset from the provided URL.
# Using Scikit-learn’s train_test_split function, create an 80/20 train/test split of the data, ensuring that the split is stratified by species (to maintain representation in both splits).

import pandas as pd
from sklearn.model_selection import train_test_split

# Data path
FILE_PATH = '/root/development_tools/fish (1).csv'
# Loading the csv data with pandas
data = pd.read_csv(FILE_PATH)

# We drop "Species" to predict the species
x_features = data.drop(columns=['Species']) # x is the input

# predcting the fish species is a classification task, hence:
y_target = data["Species"] # target value: Bream, Pike, Perch, 
                                   #               Roach, Whitefish, Parkki,
                                   #               Perch, Pike, Smelt 


# Preparing and training the 
x_train, y_train, x_test, y_test = train_test_split(x_features,y_target, test_size=0.2, stratify=y_target)

# END OF PART 1



# Part 2: Statistics
# Slice the full dataset by fish species
# For each species, calculate and print the mean, standard deviation, and interquartile range (IQR) for each numerical feature
# (e.g., length1, length2, length3, height, width, and weight). Use Pandas and NumPy for your calculations. 
# You can calculate the IQR using the difference between the 75th and 25th percentiles.

import matplotlib.pyplot as plt
import seaborn as sns

# slice the data using groupby() from pandas 
sliced_species = data.groupby('Species')

bream = sliced_species.get_group('Bream')
# pike = sliced_species.get_group("Pike")
# perch = sliced_species.get_group("Perch")
# roach = sliced_species.get_group("Roach")
# whitefish = sliced_species.get_group("Whitefish")
# parkki = sliced_species.get_group("Parkki")
# Perch = sliced_species.get_group("Perch")
# Pike = sliced_species.get_group("Pike")
# smelt = sliced_species.get_group("Smelt")

# Calculate mean & standard deviation for ALL species
species_stats = data.groupby('Species').agg(['mean', 'std']).round(2)
print(species_stats)  # Print overall stats

# Calculate mean and standard deviation for Bream only
bream_mean = bream.mean(numeric_only=True).round(2).to_frame().T  # Convert to DataFrame
bream_standard_deviation = bream.std(numeric_only=True).round(2).to_frame().T  # Convert to DataFrame

# Add a column for 'Species' (since we filtered only Bream before)
bream_mean['Species'] = 'Bream'
bream_standard_deviation['Species'] = 'Bream'

# Plot the Mean and Standard Deviation for Bream
plt.figure(figsize=(12,6))
sns.barplot(x='Species', y='Weight', data=bream_mean, yerr=bream_standard_deviation['Weight'])
plt.xticks(rotation=45)
plt.ylabel("Mean Weight")
plt.title("Mean and Standard Deviation of Bream Weight")
plt.show()

