#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Pandas version
pd.__version__

#Reading the CSV data
df = pd.read_csv('car_fuel_efficiency_2026.csv')
df.head(n) #Shows the first "n" lines
df.columns #Shows the columns
df.dtypes #Shows the types of each column

#Data Cleaning: removing spaces and transform it in lowercase string
df.columns.str.lower().str.replace(' ', '_')

#Counting Values
df.shape #Shows the table size (lines, columns)
len(df) # Counts the # of lines
df['fuel_type'].nunique() #counts the unique values from a given column
df['fuel_type'].value_counts() #shows the values and the number of appearences

#Counting null values
df.isnull().sum() #sum all the null values from the columns in the dataset
(df.isnull().sum() / len(df)) * 100 #percentage of null values

#Max and min values
df.max() #returns the max value from all the columns. The min() function does the opposite
df.idxmax() #returns the index of the max value
df.groupby('origin')['fuel_consumption'].max() #With filters
df.loc[df['origin'] == 'Asia', 'fuel_consumption'].max() #With filters option 2

#Avg, median, mode
df.describe() #returns max, min, avg, median,std deviation etc
#There are also individual functions: mean(), median(), mode(), std(), var(), quantile(0.25)
#NOTE: mode() returns an array

#Filling missing cells
#Using the fillna function creates a new dataset rather than modifying the original, so it's advisable to modify a copy of the dataset using .copy()!!!
df['Columname'].fillna(0) #to fill the missing values with 0
df_filled = df.copy()
df_filled['horsepower']=df['horsepower'].fillna(df['horsepower'].mode()[0])

#Filtering using "Loc": chosing the filters, then the colums and getting the first 7 values
df_pais = df.loc[df['country'] == 'Brasil', ['col1', 'col2']].head(n).copy()

#Matrix operations
x = df_pais.to_numpy() #convert a matrix to a numpy matrix
xtx = x.T @ x #matrix-matrix multiplication with the transposed
i_xtx = np.linalg.inv(xtx) #Calculating the inverse
w.sum() #Sum of all elements of the matrix


# In[ ]:


import pandas as pd
import numpy as np


# In[ ]:


#Q1. Pandas version
#What version of Pandas did you install?
#You can get the version information using the __version__ field:

pd.__version__


# In[ ]:


#Q2. Records count
#How many records are in the dataset?

df = pd.read_csv('car_fuel_efficiency_2026.csv')
df.columns.str.lower().str.replace(' ', '_')
df.shape


# In[ ]:


#Q3. Fuel types
#How many fuel types are presented in the dataset?

df['fuel_type'].value_counts()


# In[ ]:


#Q4. Missing values
#How many columns in the dataset have missing values?

df.isnull().sum()


# In[ ]:


#Q5. Max fuel efficiency
#What's the maximum fuel efficiency of cars from Asia?

df.loc[df['origin'] == 'Asia', 'fuel_efficiency_mpg'].max()


# In[ ]:


#Q6. Median value of horsepower
#Find the median value of the horsepower column in the dataset.
#Next, calculate the most frequent value of the same horsepower column.
#se the fillna method to fill the missing values in the horsepower column with the most frequent value from the previous step.
#Now, calculate the median value of horsepower once again.
#Has it changed?

df['horsepower'].median()
df['horsepower'].mode()
df_filled = df.copy()
df_filled['horsepower']=df['horsepower'].fillna(df['horsepower'].mode()[0])
df_filled['horsepower'].median()


# In[ ]:


#Q7. Sum of weights
#Select all the cars from Asia
#Select only columns vehicle_weight and model_year
#Select the first 7 values
#Get the underlying NumPy array. Let's call it X.
#Compute matrix-matrix multiplication between the transpose of X and X. To get the transpose, use X.T. Let's call the result XTX.
#Invert XTX.
#Create an array y with values [1100, 1300, 800, 900, 1000, 1100, 1200].
#Multiply the inverse of XTX with the transpose of X, and then multiply the result by y. Call the result w.
#What's the sum of all the elements of the result?

df_pais = df.loc[df['origin'] == 'Asia', ['vehicle_weight', 'model_year']].head(7).copy()
x = df_pais.to_numpy()
xtx = x.T @ x
i_xtx = np.linalg.inv(xtx)
y = ([1100, 1300, 800, 900, 1000, 1100, 1200])
w = (i_xtx @ x.T) * y
w.sum()

