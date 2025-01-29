# Student Name: Husain Alshaikhahmed
# Student ID: T004560868
# Class: COMP 5850
# Instructor: Professor Dr. Caleb Vatral
# Assignment: Python Review
# Due Date: January 22, 2025, 11:59 PM

# Part 1: Data Preparation
# Using Pandas, download and load the fish dataset from the provided URL.
# Using Scikit-learn’s train_test_split function, create an 80/20 train/test split of the data, ensuring that the split is stratified by species (to maintain representation in both splits).

# Description
# This section loads usinf the pandas the the cvs data then prepares it for trainin
# we Select tje numerical features for regression purpose then we Split the data to 80 - 20 into `x train  and x test, to make sure the stratification by species.

    
from sklearn.model_selection import train_test_split
import pandas as pd


# Load dataset
DATA_PATH = '/root/development_tools/fish.csv'
fish_data = pd.read_csv(DATA_PATH)

# the numerical features that will be used for the regression
Inputs = ["Length1", "Length2", "Length3", "Height", "Width"]
# this is the outcome we want to achive
outcome = "Weight"

# creating the 80-20 train and test split for the fish the data
x_train, x_test, y_train, y_test = train_test_split(
    fish_data.drop(columns=["Species"]), fish_data["Species"], test_size=0.2, random_state=42, stratify=fish_data["Species"]
)

# END OF PART 1

# Part 2: Statistics
# Slice the full dataset by fish species
# For each species, calculate and print the mean, standard deviation, and interquartile range (IQR) for each numerical feature
# (e.g., length1, length2, length3, height, width, and weight). Use Pandas and NumPy for your calculations. 
# You can calculate the IQR using the difference between the 75th and 25th percentiles.

# # Description
# This part calculates the descriptive statistics for each fish type 
# 1- the average values for the numerical features
# 2- Standard deviation to estimate data spread.
# 3- Interquartile range to understand data distribution
# Then we print thme using the tabulate for a better output

import numpy
from tabulate import tabulate

# the panda groupby function splits the dataframe into groups bases on the coumne we sleteced, in this case its species
print("average values for each fish")
avg_val_per_fish = fish_data.groupby('Species').mean(numeric_only=True).round(2)
print(tabulate(avg_val_per_fish, headers='keys', tablefmt='double_grid'))

print("\nStandard deviation fo each fish")
std_val_per_fish = fish_data.groupby('Species').std(numeric_only=True).round(2)
print(tabulate(std_val_per_fish, headers='keys', tablefmt='fancy_outline'))

print("\nInterquartile range for each species")
iqr_range = fish_data.groupby('Species').agg(lambda x: numpy.percentile(x, 75) - numpy.percentile(x, 25)).round(2)
print(tabulate(iqr_range, headers='keys', tablefmt='heavy_grid'))

# END OF PART 2

# Part 3: Regression
# Using Scikit-learn, create a linear regression model to predict a fish’s weight based on the other numerical features (length1, length2, length3, height, and width). Ensure the model is trained only on the training split.
# Print the coefficients and intercept of the trained regression model.
# Calculate and print the model’s accuracy (e.g., R^2 score) on both the training and testing splits.

# Description 
# This is the part where we build the regression Model to predict  the fish's weight
# We split the data again for the regression.
# Then we Handle the missing values for a better clean training.
# Now the model fits a Linear Regression mode on chosen features.
# then we print model intercept and coefficients 
# at the end, we evaluate the performance using r2 score

from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

# regression for the datase
x_regression = fish_data[Inputs]
y_regression = fish_data[outcome]

# regression train and test split
x_train_regression, x_test_regression, y_train_regression, y_test_regression = train_test_split(
    x_regression, y_regression, test_size=0.2, random_state=42
)

# making sure the y traning for egression dont have missing or undefined values 
y_train_regression = y_train_regression.dropna()
x_train_regression = x_train_regression.loc[y_train_reg.index]   

# Train Linear Regression model
regression_modle = LinearRegression()
regression_modle.fit(x_train_regression, y_train_regression)

# Print the modle Intercept and coefficients
features = ["Length1", "Length2", "Length3", "Height", "Width"]
# Create table data
coefficients = regression_modle.coef_
regression_modle_data = list(zip(features, coefficients))
print(tabulate(regression_modle_data, headers=['features','coefficient'], tablefmt='heavy_grid'))

print("Intercept:", round(regression_modle.intercept_, 2))
 
# measurin model performance 
y_train_predication = regression_modle.predict(x_train_regression)
y_test_predication = regression_modle.predict(x_test_regression)

print("train the R2 Score:", round(r2_score(y_train_regression, y_train_predication),3))
print("Test the R2 Score:", round(r2_score(y_test_regression, y_test_predication),3))

# END OF PART 3

# Part 4: Classification
# Using Scikit-learn, create a fully-grown decision tree classifier to predict a fish’s species using its length, width, and height measurements. Ensure that the model does not use the fish’s weight in the calculations, and that it is trained only on the training split.
# Calculate and print the model’s accuracy on both the training and testing splits. Additionally, print the depth of the fully grown decision tree.
# Optimize the decision tree by determining the best maximum depth:
# Train multiple decision tree models with the max_depth parameter ranging from 1 to the depth of the fully-grown tree.
# For each depth, record the training and testing accuracy.
# Use this information to identify the depth that provides the best generalization performance.
# Initialize and train a decision tree classifier to predict fish species

# Description:
# In the final section the classification model 
# We build  the decision tree classifier to predict fish species
# First we fit the decision tree model  on the x train and  the  y train 
# then we predict the species for both training and test sets
# Then we evaluate the accuracy of the module 
# Then we print the results along with the optimized tree depth for the generalization

from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# Trainaining the decision tree
classifier = DecisionTreeClassifier(max_depth=5,random_state=42)
classifier.fit(x_train, y_train)

# predication and evaluatation
y_train_predication = classifier.predict(x_train)
y_test_predication = classifier.predict(x_test)

# optimization
best_depth, best_accuracy = 1, 0
for depth in range(1, classifier.get_depth() + 1):
    temporary_classifier = DecisionTreeClassifier(max_depth=depth, random_state=42)
    temporary_classifier.fit(x_train, y_train)
    
    accuracy = accuracy_score(y_test, temporary_classifier.predict(x_test))
    if accuracy > best_accuracy:
        best_accuracy, best_depth = accuracy, depth
        
decision_treec_lassifier = [
    ["Train Accuracy", round(accuracy_score(y_train, y_train_predication),2)],
    ["Test Accuracy", round(accuracy_score(y_test, y_test_predication),2)],
    ["generalization best depth", best_depth]
]

print(tabulate(decision_treec_lassifier , headers=["Decision Tree Classifier","Percentage"], tablefmt="heavy_grid"))

# END OF PART 4
