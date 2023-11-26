#!/usr/bin/env python
# coding: utf-8

# ## Lab Session 

# ### Learning Objective:
# - Working with data using python libaries.
# - Data Visualization.
# - Exploratory data analysis and data preprocessing.
# - Building a Linear regression model to predict the tip amount based on different input features.

# ### About the dataset (Customer Tip Data)
# 
# #### Dataset Source: https://www.kaggle.com/datasets/ranjeetjain3/seaborn-tips-dataset
# 
# The dataset contains information about the 244 orders served at a restaurant in the United States. Each observation includes the factors related to the order like total bill, time, the total number of people in a group, gender of the person paying for the order and so on.
# 
# #### Attribute Information:
# 
# - **total_bill:** Total bill (cost of the meal), including tax, in US dollars
# - **tip:** Tip in US dollars
# - **sex:** Sex of person paying for the meal
# - **smoker:** There is a smoker in a group or not
# - **day:** Day on which the order is served
# - **time:** Time of the order
# - **size:** Size of the group
# 
# Food servers’ tips in restaurants may be influenced by many factors, including the nature of the restaurant, size of the party, and table locations in the restaurant. Restaurant managers need to know which factors matter when they assign tables to food servers. For the sake of staff morale, they usually want to avoid either the substance or the appearance of unfair
# treatment of the servers, for whom tips (at least in restaurants in the UnitedStates) are a major component of pay.

# ### Import required libraries

# In[2]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')

import sklearn
from sklearn.preprocessing import StandardScaler,LabelEncoder


# ### Load the dataset

# In[3]:


df = pd.read_csv('tips.csv')
df


# ### 1. Make a list of categorical and numerical columns in the data.

# In[4]:


df.info()


# In[52]:


data = pd.read_csv('tips.csv')

# Get the data types of each column
data.dtypes


# In[5]:


df.describe()


# In[ ]:


df.describe(include='0')


# In[53]:


# Create two empty lists, one for categorical columns and one for numerical columns
categorical_columns = []
numerical_columns = []


# In[103]:


# Iterate over the columns in the DataFrame and add each column to the appropriate list based on its data type
for column in df.columns:
    if dtypes[column] == 'object':
        categorical_columns.append(column)
    else:
        numerical_columns.append(column)
return  categorical_columns, numerical_columns


# ### 2. Compute the average bill amount for each day.

# In[26]:


df.groupby('day')[['total_bill']].mean()


# ### 3. Which gender is more generous in giving tips?

# In[89]:


df.groupby('sex')[['tip']].sum()


# ### 4. According to the data, were there more customers for dinner or lunch?

# In[ ]:





# ### 5. Based on the statistical summary, comment on the variable 'tip'

# In[ ]:





# ### 6. Find the busiest day in terms of the orders?

# In[87]:


df.groupby('day')[['size']].max()


# ### 7. Is the variable 'total_bill' skewed? If yes, identify the type of skewness. Support your answer with a plot

# In[ ]:





# ### 8. Is the tip amount dependent on the total bill? Visualize the relationship with a appropriate plot and metric and write your findings.

# In[ ]:





# ### 9. What is the percentage of males and females in the dataset? and display it in the plot

# In[ ]:





# ### 10. Compute the gender-wise count based on smoking habits and display it in the plot

# In[85]:


df.groupby('sex') [['smoker']].count()


# ### 11. Compute the average tip amount given for different days and display it in the plot.

# In[47]:


df.groupby('day')[['tip']].mean()


# In[48]:


df.groupby('day')[['tip']].mean().plot()


# ### 12. Is the average bill amount dependent on the size of the group? Visualize the relationship using appropriate plot and write your findings.

# In[ ]:





# ### 13. Plot a horizontal boxplot to compare the bill amount based on gender

# In[ ]:





# ### 14. Find the maximum bill amount for lunch and dinner on Saturday and Sunday

# In[50]:


df.groupby(['day','time'])[['total_bill']].max()


# ### 15. Compute the percentage of missing values in the dataset.

# In[ ]:





# ### 16. Is there are any duplicate records in the dataset? If yes compute the count of the duplicate records and drop them.

# In[41]:


df[df.duplicated()]


# In[42]:


df[df.duplicated()].count()


# ### 17. Is there are any outliers present in the column 'total_bill'? If yes treat them with transformation approach, and plot a boxplot before and after the treatment

# In[ ]:





# ### 18. Is there are any outliers present in the column 'tip'? If yes remove them using IQR techinque.

# In[ ]:





# ### 19. Encode the categorical columns in the dataset and print the random 5 samples from the dataframe.

# In[ ]:





# ### 20. Check the range of the column 'total_bill' and transform the values such that the range will be 1.

# In[ ]:





# ### 21. Load the dataset again by giving the name of the dataframe as "tips_df"
# - i) Encode the categorical variables.
# - ii) Store the target column (i.e.tip) in the y variable and the rest of the columns in the X variable

# In[ ]:





# ### 22. Split the dataset into two parts (i.e. 70% train and 30% test), and Standardize the columns "total_bill" and "Size" using the mim_max scaling approach

# In[ ]:





# ### 23. Train a linear regression model using the training data and print the r_squared value of the prediction on the test data.

# In[ ]:





# ### Happy Learning:)
