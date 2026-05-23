#Students have to check the spread of values of different features using various Distribution charts.
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# creating a dataframe
data = pd.DataFrame({
    'Age': [25, 30, 35, 40, 45, 50, 55, 60],
    'Salary': [50000, 60000, 70000, 80000, 90000, 100000, 110000, 120000]
})
# Distribution plot for Age and Salary
plt.figure(figsize=(10, 5))
sns.histplot(data['Age'], kde=True)
sns.histplot(data['Salary'], kde=True)
plt.title('Distribution of Age')
plt.xlabel('Age')
plt.ylabel('Salary')
plt.show()

#pairplot to see the relationship between Age and Salary
sns.pairplot(data)
plt.show()
