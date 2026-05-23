#Check if any null values are present in the dataset (handle if any)
#Check the details of the dataset (types of features etc.)
#Check the distribution of all the quantitative features using boxplot
#Check the distribution of CO2 emissions for different vehicle class using a boxplot
#Check the distribution of CO2 emissions for different fuel type using a using violin plot
#Check the distribution of CO2 emissions for different vehicle class using a violin plot
#Create density plots for all the quantitative features
#Create histograms to check the distribution of data of all the quantitative features
#Create dist plots to check the distribution and skewness for all the quantitative features
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
# Load the dataset
data = pd.read_csv('FuelConsumption.csv')
# Check for null values
print(data.isnull().sum())
# Check the details of the dataset
print(data.info())
# Check the distribution of all the quantitative features using boxplot
quantitative_features = ['ENGINESIZE', 'CYLINDERS', 'FUELCONSUMPTION_CITY', 
                         'FUELCONSUMPTION_HWY', 'FUELCONSUMPTION_COMB', 
                         'CO2EMISSIONS']
for feature in quantitative_features:
    plt.figure(figsize=(10, 5))
    sns.boxplot(x=data[feature])
    plt.title(f'Boxplot of {feature}')
    plt.show()
# Check the distribution of CO2 emissions for different vehicle class using a boxplot
plt.figure(figsize=(12, 6))
# Column names in this CSV are: VEHICLECLASS and CO2EMISSIONS
sns.boxplot(x='VEHICLECLASS', y='CO2EMISSIONS', data=data)
plt.title('Boxplot of CO2 Emissions by Vehicle Class')
plt.xticks(rotation=45)
plt.show()
# Check the distribution of CO2 emissions for different fuel type using a violin plot
plt.figure(figsize=(12, 6))
sns.violinplot(x='FUELTYPE', y='CO2EMISSIONS', data=data)
plt.title('Violin Plot of CO2 Emissions by Fuel Type')
plt.show()
# Check the distribution of CO2 emissions for different vehicle class using a violin plot
plt.figure(figsize=(12, 6))
sns.violinplot(x='VEHICLECLASS', y='CO2EMISSIONS', data=data)
plt.title('Violin Plot of CO2 Emissions by Vehicle Class')
plt.xticks(rotation=45)
plt.show()
# Create density plots for all the quantitative features
for feature in quantitative_features:
    plt.figure(figsize=(10, 5))
    sns.kdeplot(data[feature], shade=True)
    plt.title(f'Density Plot of {feature}')
    plt.show()
# Create histograms to check the distribution of data of all the quantitative features
for feature in quantitative_features:
    plt.figure(figsize=(10, 5))
    sns.histplot(data[feature], bins=30, kde=False)
    plt.title(f'Histogram of {feature}')
    plt.show()
# Create dist plots to check the distribution and skewness for all the quantitative features
for feature in quantitative_features:
    plt.figure(figsize=(10, 5))
    sns.histplot(data[feature], bins=30, kde=True)
    plt.title(f'Dist Plot of {feature}')
    plt.show()