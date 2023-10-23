#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Introduction
# The California Housing dataset is a popular dataset in machine learning and data science. This dataset contains information about the housing districts in California. The data has 10 different features, including information about the district’s population, median income, median house value, and more.

# The features in the dataset are as follows:

# longitude: continuous.
# latitude: continuous.
# housing_median_age: ordinal.
# total_rooms: discrete.
# total_bedrooms: discrete.
# population: discrete.
# households: discrete.
# median_income: continuous.
# median_house_value: continuous.
# ocean_proximity: nominal.


# In[ ]:


Introduction:
The project focuses on the analysis of a California housing dataset. This dataset provides 
information about various features related to housing in California, including median income, 
housing median age, median house values, total bedrooms, latitude, longitude, and ocean proximity. 
The goal of this project is to perform data analysis and visualization to gain insights into the housing 
market in California.

Problem Statement:
The project aims to address several questions and perform specific tasks related to the California housing dataset, 
such as calculating average median income, visualizing the distribution of housing median age, exploring the relationship 
between median income and median house values, handling missing data, creating a user-defined function to calculate the 
median, and more.

Datasets:
The primary dataset used in this project is the "California housing dataset." This dataset contains the following features:

1. Median Income (Continuous)
2. Housing Median Age (Continuous)
3. Median House Value (Continuous)
4. Total Bedrooms (Continuous)
5. Latitude (Continuous)
6. Longitude (Continuous)
7. Ocean Proximity (Nominal)

Insights:
1. The average median income was calculated, and its distribution was visualized, indicating a slightly 
right-skewed distribution with most incomes clustered around a specific range.

2. The distribution of housing median age was visualized, revealing a higher frequency of housing units with a 
median age of around 15-30 years.

3. A scatter plot was used to show the positive correlation between median income and median house values, 
suggesting that areas with higher median incomes tend to have higher median house values.

4. Two datasets were created by removing rows with missing total bedrooms data and by filling missing total 
bedrooms with the mean value.

5. A user-defined function to calculate the median value was provided.

6. A scatter plot of latitude versus longitude was used to visualize the geographical distribution of the housing data.

7. A dataset was created specifically for housing units near the ocean, and the mean and median of median income for 
this subset were calculated.

8. A new column, "total_bedroom_size," was added based on the total bedrooms' values, categorizing them as small, medium, 
or large.

Conclusion:
In conclusion, the project explored and analyzed the California housing dataset, providing valuable insights into the 
housing market. We observed relationships between median income and median house values, visualized the geographical 
distribution of data, and handled missing data. Additionally, a user-defined function was created for calculating medians. 
This analysis can be useful for real estate professionals and policymakers to make informed decisions in the 
California housing market.


# In[3]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_excel(r"C:\Users\sreekar\Downloads\housing.xlsx")
print(df)


# In[5]:


# 1. What is the average median income of the data set and check the distribution of data using appropriate plots. 
# Please explain the distribution of the plot.


avg_median_income = df['median_income'].mean()
print("The average median income of the dataset is:", avg_median_income)

# We can visualize the distribution of the median income using a histogram
sns.histplot(df['median_income'], kde=True)
plt.title('Distribution of Median Income')
plt.show()


# From the histogram, we can see that the distribution of median income is slightly right-skewed. 
# The majority of the districts have a median income in the range of 1-6.

# # Question 1: Calculate the average median income and visualize its distribution
# average_median_income = df['median_income'].mean()
# plt.figure(figsize=(8, 5))
# plt.hist(df['median_income'], bins=50, edgecolor='k', alpha=0.7)
# plt.xlabel('Median Income')
# plt.ylabel('Frequency')
# plt.title(f'Average Median Income: ${average_median_income:.2f}')
# plt.grid(True)
# plt.show()
# which involves calculating the average median income and visualizing its distribution. 
# The code calculates the mean of the 'median_income' column and then creates a histogram to visualize the 
# distribution of median income in the dataset. The histogram is labeled and displayed with an average income line, 
# providing an overview of the income distribution.


# In[7]:


# 2. Draw an appropriate plot to see the distribution of housing_median_age and explain your observations.

# We can visualize the distribution of the housing median age using a histogram as shown below:


sns.histplot(df['housing_median_age'], kde=True)
plt.title('Distribution of Housing Median Age')
plt.show()


# From the histogram, we can see that the distribution of housing median age is almost normal. 
# The majority of the districts have a housing median age in the range of 15-35.

# # Question 2: Visualize the distribution of housing median age
# plt.figure(figsize=(8, 5))
# plt.hist(df['housing_median_age'], bins=50, edgecolor='k', alpha=0.7)
# plt.xlabel('Housing Median Age')
# plt.ylabel('Frequency')
# plt.title('Distribution of Housing Median Age')
# plt.grid(True)
# plt.show()
# which focuses on visualizing the distribution of housing median age. 
# It creates a histogram to display the distribution of housing median age in 
# the dataset, providing insights into the age distribution of housing units.


# In[8]:


# 3. Show with the help of visualization, how median_income and median_house_values are related?

# We can use a scatter plot to visualize the relationship between median_income and median_house_value as shown below:


sns.scatterplot(x='median_income', y='median_house_value', data=df)
plt.title('Relationship between Median Income and Median House Value')
plt.show()


# From the scatter plot, we can see that there is a positive correlation between median_income and median_house_value.
# This indicates that as the median_income increases, the median_house_value also tends to increase.

# Question 3: Visualize the relationship between median income and median house values
# plt.figure(figsize=(8, 5))
# plt.scatter(df['median_income'], df['median_house_value'], alpha=0.5)
# plt.xlabel('Median Income')
# plt.ylabel('Median House Value')
# plt.title('Relationship between Median Income and Median House Value')
# plt.grid(True)
# plt.show()
# which involves visualizing the relationship between median income and median house values.
# It creates a scatter plot to show how these two variables are related. The scatter plot provides 
# insights into the correlation between income and house values.


# In[3]:


# 4. Create a data set by deleting the corresponding examples from the data set for which total_bedrooms are not available.

# We can create a new dataset by deleting the rows where the total_bedrooms are not available 


df_clean = df.dropna(subset=['total_bedrooms'])
df_clean


# In[2]:


# 5. Create a data set by filling the missing data with the mean value of the total_bedrooms in the original data set.

# We can create a new dataset by filling the missing data with the mean value of the total_bedrooms 


mean_total_bedrooms = df['total_bedrooms'].mean()
df_imputed = df.fillna(value={'total_bedrooms': mean_total_bedrooms})
df_imputed


# In[13]:


# 6. Write a programming construct (create a user defined function) to calculate the median value of the data set 
# wherever required.

# We can create a user-defined function to calculate the median value of the dataset 


def calculate_median(column):
    return np.median(df[column])


median_total_rooms = calculate_median('total_rooms')
print("The median total rooms is:", median_total_rooms)


# In[14]:


# 7. Plot latitude versus longitude and explain your observations.
# We can plot the latitude versus longitude using a scatter plot as shown below:


sns.scatterplot(x='longitude', y='latitude', data=df)
plt.title('Latitude vs Longitude')
plt.show()


# From the scatter plot, we can see that the majority of the housing districts are concentrated around the latitude of 35-40 and longitude of -125 to -115. 
# This corresponds to the state of California in the USA.

# Question 7: Plot latitude versus longitude
# plt.figure(figsize=(10, 6))
# plt.scatter(df['longitude'], df['latitude'], alpha=0.3, s=10)
# plt.xlabel('Longitude')
# plt.ylabel('Latitude')
# plt.title('Geographical Distribution (Latitude vs. Longitude)')
# plt.show()
# Scatter Plot: The code creates a scatter plot using the plt.scatter function, with 'longitude' on the x-axis and 
#     'latitude' on the y-axis. 
#     This type of plot is suitable for visualizing geographical data.


# In[4]:


# 8. Create a data set for which the ocean_proximity is ‘Near ocean’.
df_near_ocean = df[df['ocean_proximity'] == 'NEAR OCEAN']
df_near_ocean


# In[16]:


# 9. Find the mean and median of the median income for the data set created in question 8.
mean_median_income_near_ocean = df_near_ocean['median_income'].mean()
median_median_income_near_ocean = df_near_ocean['median_income'].median()

print("The mean median income for districts near the ocean is:", mean_median_income_near_ocean)
print("The median median income for districts near the ocean is:", median_median_income_near_ocean)



# In[7]:


# 10. Please create a new column named total_bedroom_size. If the total bedrooms is 10 or less,it should be quoted as small.
# If the total bedrooms is 11 or more but less than 1000, it should be medium, otherwise it should be considered large.

def categorize_bedrooms(num_bedrooms):
    if num_bedrooms <= 10:
        return 'small'
    elif num_bedrooms < 1000:
        return 'medium'
    else:
        return 'large'

df['total_bedroom_size'] = df['total_bedrooms'].apply(categorize_bedrooms)

df['total_bedroom_size']
print(df)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




