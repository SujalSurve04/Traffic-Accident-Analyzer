import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset

df = pd.read_csv('RTA Dataset.csv')

# Display the first few rows of the dataset
print(df.head())

# Visualize distribution of accidents by day of the week
plt.figure(figsize=(10, 6))
sns.countplot(x='Day_of_week', data=df, order=df['Day_of_week'].value_counts().index)
plt.title('Accidents by Day of the Week')
plt.xlabel('Day of the Week')
plt.ylabel('Number of Accidents')
plt.show()

# Visualize distribution of accidents by road surface conditions
plt.figure(figsize=(10, 6))
sns.countplot(x='Road_surface_conditions', data=df, order=df['Road_surface_conditions'].value_counts().index)
plt.title('Accidents by Road Surface Conditions')
plt.xlabel('Road Surface Conditions')
plt.ylabel('Number of Accidents')
plt.xticks(rotation=45)
plt.show()

# Visualize distribution of accidents by light conditions
plt.figure(figsize=(10, 6))
sns.countplot(x='Light_conditions', data=df, order=df['Light_conditions'].value_counts().index)
plt.title('Accidents by Light Conditions')
plt.xlabel('Light Conditions')
plt.ylabel('Number of Accidents')
plt.xticks(rotation=45)
plt.show()
