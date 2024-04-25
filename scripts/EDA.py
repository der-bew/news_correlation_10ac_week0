#!/usr/bin/env python


#import the required libraries for the EDA
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# Convert CSV file into Panadas Dataframe
benin_df = pd.read_csv("../data/benin-malanville.csv")
sierraleone_df = pd.read_csv("../data/sierraleone-bumbuna.csv")
togo_df = pd.read_csv("../data/togo-dapaong_qc.csv")


# ## Assessing Data

# ### Visual Assessemnt

benin_df


# - Missing values in the `comments` column
# - `GHI`, `DNI`, and `DHI` columns contains negative values


sierraleone_df


# - Missing values in the `comments` column
# - `GHI`, `DNI`, and `DHI` columns contains negative values


togo_df


# - Missing values in the `comments` column
# - `GHI` column contains negative values

# ### Programmatic Assessement

# In[6]:


benin_df.info()


# - Erroneous datatype `Timestamp` column should be `Datatime`

# In[7]:


#check duplicated values in benin_df 
sum(benin_df.duplicated())


# In[8]:


# check null values in benin_df
benin_df.isna().sum()


# In[9]:


# Summary Statistics
benin_df.describe()


# In[10]:


sierraleone_df.info()


# - Erroneous datatype `Timestamp` column should be `Datatime`

# In[11]:


#check duplicated values in benin_df 
sum(sierraleone_df.duplicated())


# In[12]:


# check null values in benin_df
sierraleone_df.isna().sum()


# In[13]:


# Summary Statistics
sierraleone_df.describe()


# In[14]:


togo_df.info()


# - Erroneous datatype `Timestamp` column should be `Datatime`

# In[15]:


#check duplicated values in benin_df 
sum(togo_df.duplicated())


# In[16]:


# check null values in benin_df
togo_df.isna().sum()


# In[17]:


# Summary Statistics
togo_df.describe()


# ### Quality issues
# 1. Missing values in the `comments` column.
# 2. `GHI`, `DNI`, and `DHI` columns contains negative values.
# 3. Erroneous datatype `Timestamp` column should be `Datatime`.

# ## Data Cleaning

# ### Quality issues

# In[18]:


# make a copies of the original data
benin_df_clean = benin_df.copy()
sierraleone_df_clean = sierraleone_df.copy()
togo_df_clean = togo_df.copy()


# #### Issue #1:
# The `comments` column contains missing values

benin_df_clean.drop("Comments", axis = 1, inplace=True)
sierraleone_df_clean.drop("Comments", axis = 1, inplace=True)
togo_df_clean.drop("Comments", axis = 1, inplace=True)


# #### Test

# In[20]:


print(benin_df_clean.columns)
print(sierraleone_df_clean.columns)
print(togo_df_clean.columns)


# ### Issue #2:
# `GHI`, `DNI`, and `DHI` columns contains negative values.

benin_df_clean[['GHI', 'DNI', 'DHI']] = benin_df_clean[['GHI', 'DNI', 'DHI']].abs()
sierraleone_df_clean[['GHI', 'DNI', 'DHI']] = sierraleone_df_clean[['GHI', 'DNI', 'DHI']].abs()
togo_df_clean[['GHI', 'DNI', 'DHI']] = togo_df_clean[['GHI', 'DNI', 'DHI']].abs()


# #### Test

# In[22]:


benin_df_clean[['GHI', 'DNI', 'DHI']]


# In[23]:


sierraleone_df_clean[['GHI', 'DNI', 'DHI']]


# In[24]:


togo_df_clean[['GHI', 'DNI', 'DHI']]


# ### Issue #3:
# Erroneous datatype `Timestamp` column should be Datatime.


# convert the datatype 
benin_df_clean['Timestamp'] = pd.to_datetime(benin_df_clean['Timestamp']).dt.normalize()
sierraleone_df_clean['Timestamp'] = pd.to_datetime(sierraleone_df_clean['Timestamp']).dt.normalize()
togo_df_clean['Timestamp'] = pd.to_datetime(togo_df_clean['Timestamp']).dt.normalize()


# #### Test

# In[27]:


# check the datatype
print(benin_df_clean['Timestamp'].dtype)
print(sierraleone_df_clean['Timestamp'].dtype)
print(togo_df_clean['Timestamp'].dtype)



# Concatinate all the three dataframe into one dataframe.

all_clean_df = pd.concat([benin_df_clean, sierraleone_df_clean, togo_df_clean], axis=0)
all_clean_df.sample(5)


all_clean_df.shape



# group data by Timestamp column for Timeseries plot
grouped_df = all_clean_df.groupby(['Timestamp']).mean()[['GHI', 'DNI', 'DHI', 'Tamb']]
grouped_df.reset_index(inplace=True)



cols = ['GHI', 'DNI', 'DHI', 'Tamb']
colors = ['b', 'g', 'r', 'm']  # blue, green, red, magenta
fig = plt.subplots(figsize=(20, 5))
for col, color in zip(cols, colors):
    plt.plot(grouped_df['Timestamp'], grouped_df[col], label=col, color=color)
plt.title('Time Series Plot of GHI, DNI, DHI, and Tamb', fontsize=20)
plt.xlabel('Timestamp', fontsize=15)
plt.ylabel('GHI, DNI, DHI, and Tamb Values', fontsize=15)
plt.xticks(rotation=30)
plt.legend()


#Calculate correlation coefficients
correlation_matrix = all_clean_df[["GHI", "DHI", "DNI", "TModA", "TModB"]].corr()
print(correlation_matrix)


wind_speed_stats = all_clean_df[["WS", "WSgust", "WSstdev"]].describe()
print(wind_speed_stats)


wind_data = all_clean_df.groupby(['Timestamp']).mean()[['WS', 'WSgust', 'WSstdev', 'WD', 'WDstdev']]
wind_data.reset_index(inplace=True)


# Plotting time-series graphs for each column
plt.figure(figsize=(14, 10))

# WS
plt.subplot(3, 2, 1)
plt.plot(wind_data['Timestamp'], wind_data['WS'], color='blue')
plt.title('Wind Speed (WS)')
plt.xlabel('Time')
plt.ylabel('Wind Speed (m/s)')

# WSgust
plt.subplot(3, 2, 2)
plt.plot(wind_data['Timestamp'], wind_data['WSgust'], color='orange')
plt.title('WSgust')
plt.xlabel('Time')
plt.ylabel('WSgust (m/s)')

# WSstdev
plt.subplot(3, 2, 3)
plt.plot(wind_data['Timestamp'], wind_data['WSstdev'], color='green')
plt.title('Wind Speed Standard Deviation (WSstdev)')
plt.xlabel('Time')
plt.ylabel('Wind Speed Std Dev (m/s)')

# WD
plt.subplot(3, 2, 4)
plt.plot(wind_data['Timestamp'], wind_data['WD'], color='red')
plt.title('Wind Direction (WD)')
plt.xlabel('Time')
plt.ylabel('Wind Direction (degrees)')

# WDstdev
plt.subplot(3, 2, 5)
plt.plot(wind_data['Timestamp'], wind_data['WDstdev'], color='purple')
plt.title('Wind Direction Standard Deviation (WDstdev)')
plt.xlabel('Time')
plt.ylabel('Wind Direction Std Dev (degrees)')

plt.tight_layout()


# calculate the correlation coefficient
correlation_matrix = all_clean_df[["TModA", "TModB", "Tamb"]].corr()
print(correlation_matrix)


# ploting Scatter plot

plt.figure(figsize=(14, 10))

#TModA vs Tamb
plt.subplot(3, 3, 1)
plt.scatter(all_clean_df["Tamb"], all_clean_df["TModA"], label="TModA vs. Tamb")
plt.xlabel("Ambient Temperature")
plt.ylabel("Module Temperature A (TModA) ")
plt.title("TModA vs. Tamb")
plt.grid(True)
plt.legend()

# TModB vs Tamb
plt.subplot(3, 3, 2)
plt.scatter(all_clean_df["Tamb"], all_clean_df["TModB"], label="TModB vs. Tamb")
plt.xlabel("Ambient Temperature")
plt.ylabel("Module Temperature B (TModB)")
plt.title("TModB vs. Tamb")
plt.grid(True)
plt.legend()

# TModA vs TModB
plt.subplot(3, 3, 3)
plt.scatter(all_clean_df["TModA"], all_clean_df["TModB"], label="TModA vs. TModB")
plt.xlabel("Module Temperature A (TModA)")
plt.ylabel("Module Temperature B (TModB)")
plt.title("TModB vs. Tamb")
plt.grid(True)
plt.legend()


# Histograms plot
plt.figure(figsize=(14, 10))

plt.subplot(2, 3, 1)
sns.histplot(all_clean_df['GHI'], bins=20, kde=True, color='blue')
plt.title('Global Horizontal Irradiance (GHI) Histogram')

plt.subplot(2, 3, 2)
sns.histplot(all_clean_df['DNI'], bins=20, kde=True, color='orange')
plt.title('Direct Normal Irradiance (DNI) Histogram')

plt.subplot(2, 3, 3)
sns.histplot(all_clean_df['DHI'], bins=20, kde=True, color='green')
plt.title('Diffuse Horizontal Irradiance (DHI) Histogram')

plt.subplot(2, 3, 4)
sns.histplot(all_clean_df['WS'], bins=20, kde=True, color='red')
plt.title('Wind Speed (WS) Histogram')

plt.subplot(2, 3, 5)
sns.histplot(all_clean_df['Tamb'], bins=20, kde=True, color='purple')
plt.title('Ambient Temperature (Tamb) Histogram')

plt.tight_layout()
plt.show()


# Box Plots
plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
sns.boxplot(data=all_clean_df[['GHI', 'DNI', 'DHI']])
plt.title('Solar Radiation Boxplot')

plt.subplot(1, 2, 2)
sns.boxplot(data=all_clean_df[['Tamb', 'TModA', 'TModB']])
plt.title('Temperature Boxplot')

plt.tight_layout()
plt.show()


# Scatter Plots
plt.figure(figsize=(14, 5))

plt.subplot(1, 2, 1)
sns.scatterplot(x='GHI', y='Tamb', data=all_clean_df, color='blue')
plt.title('GHI vs. Ambient Temperature')

plt.subplot(1, 2, 2)
sns.scatterplot(x='WS', y='Tamb', data=all_clean_df, color='green')
plt.title('Wind Speed (WS) vs. Ambient Temperature')

plt.tight_layout()
plt.show()
