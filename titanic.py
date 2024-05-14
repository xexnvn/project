# 1. Import the Required Libraries
import pandas as pd
import matplotlib.pyplot as plt

# 2. Load the Dataset
df = pd.read_csv("/Users/mooon/Desktop/mon_python/titanic.csv")

# 3. Data Exploration
# Display the first few rows of the dataset to understand its structure.
df.head()

# Print information about the columns and their data types.
df.info()

# Show summary statistics for numerical columns (e.g., mean, min, max, etc.).
df.describe()

# 4. Data Cleaning
# Identify and handle missing values in the dataset (e.g., fill missing age values with median).
df['Age'].fillna(df['Age'].median(), inplace = True)

# Perform any necessary data transformations or cleaning steps.
df.drop('Cabin', axis = 1, inplace = True)

# 5. Data Analysis
# Calculate and display the count of passengers by gender.
df[["Sex", "PassengerId"]].groupby(["Sex"]).count()
# Compute the average age of passengers.
df["Age"].mean()
# Determine the survival rate by passenger class.
# Method 1:
survival_rates = df.groupby('Pclass')['Survived'].mean()
# Method 2:
# survival_rates = df[['Pclass', 'Survived']].groupby(['Pclass']).mean()


# 6. Data Visualization
# Create a bar chart to visualize the survival rate by passenger class.
# Add appropriate labels and a title to the chart.
# Method 1: 
plt.bar(survival_rates.index, survival_rates.values, width = 0.4)
plt.xlabel('Passenger Class')
plt.ylabel('Survival Rate')
plt.title('Survival Rate by Passenger Class')
plt.xticks(survival_rates.index)
plt.show()

# Method 2:
# plt.bar(survival_rates.index, survival_rates['Survived'])
# plt.xlabel('Passenger Class')
# plt.ylabel('Survival Rate')
# plt.title('Survival Rate by Passenger Class')
# plt.xticks(survival_rates.index)
# plt.show()