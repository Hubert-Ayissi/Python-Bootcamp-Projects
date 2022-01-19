#!/usr/bin/env python
# coding: utf-8

# # Assignment \#2 - the Facebook dataset
# 
# Exploratory Data Analysis giving insights from the Facebook dataset.
# 
# Source: http://www.kaggle.com
# 
# **Features description**
# - *userid*: anonymized user id
# - *age*: age in years
# - *dob_day*: date of birth (day)
# - *dob_year*: date of birth (year)
# - *dob_month*: date of birth (month)
# - *gender*: gender
# - *tenure*: number of days in Facebook
# - *friend_count*: number of friends
# - *friendships_initiated*: number of friends initiated
# - *likes*: number of likes performed
# - *likes_received*: number of likes received
# - *mobile_likes*: number of mobile likes performed
# - *mobile_likes_received*: number of mobile likes received
# - *www_likes*: number of web likes performed
# - *www_likes_received*: number of web likes received

# #### Checklist before submitting your assignment:
# - Check individually each function by invoking it.
# - Check that functions which return floating point number, you round them to 1 decimal point.
# - Clean up your notebook before exporting it to Python format: remove unnecessary cells where you performed tests...
# - Check that the Python file do not contain any syntax error:
#     * Open a command window and type: python assignment_2.py
#     * Or copy paste the whole content of your Python file into a cell of your notebook and run it
#     * No error should be output!
# - Upload your file in the Google drive folder and check that the name of the file is appropriate, with no extra character, here: `assignment_2.py`

# **Questions**
# 
# Load the dataset and answer to all questions by implementing a function with no arguments.
# 
# The dataset should be downloaded, saved and unzip along with your notebook, NOT in a specific folder.
# 
# The different functions should use one of the variables defined below (`df`, `df_female`, `df_male`) and perform the appropriate computation.
# 
# Many questions deal with differences between females and males in the dataset.
# Therefore, we have computed and prepared 3 datasets which are to be used:
# - `df`: whole dataset,
# - `df_female`: dataset with females only,
# - `df_male`: dataset with males only.
# 
# **Caution**: Questions asking to return a floating point number (mean, percentage) should round it to 1 decimal place:
# - Such questions are marked with `(°)`.
# - For instance, if the variable `result` is a floating point number, e.g. `3.14159265359`
# - The function should return `round(result, 1)` instead of `result`, e.g. `3.1`
# - Percentages should be returned as floating point numbers and not with the `%` mark.
# 
# **Tip**: All questions might be answered without implementing any loop nor any if/else statement.
# 
# **General questions**
# 
# 0) How many rows does the whole DataFrame have?
# 
# 1) How many columns does the whole DataFrame have?
# 
# **Females and males**
# 
# 2) How many females are there in the dataset?
# 
# 3) How many males are there in the dataset?
# 
# **Total number of likes performed**
# 
# 4) What is the total number of likes performed by females?
# 
# 5) What is the total number of likes performed by males?
# 
# **Total number of likes received**
# 
# 6) What is the total number of likes received by females?
# 
# 7) What is the total number of likes received by males?
# 
# **Mean age (°)**
# 
# 8) What is the mean age of females (°)?
# 
# 9) What is the mean age of males (°)?
# 
# **Mean friend count (°)**
# 
# 10) What is the mean friend count of females (°)?
# 
# 11) What is the mean friend count of males (°)?
# 
# **Mean number of likes performed (°)**
# 
# 12) What is the mean number of likes performed by females (°)?
# 
# 13) What is the mean number of likes performed by males (°)?
# 
# **Mean number of likes received (°)**
# 
# 14) What is the mean number of likes received by females (°)?
# 
# 15) What is the mean number of likes received by males (°)?
# 
# **Percentage who did not performed any like (°)**
# 
# 16) What is the percentage of females who did not performed any like (°)?
# 
# 17) What is the percentage of males who did not performed any like (°)?
# 
# **Percentage who did not received any like (°)**
# 
# 18) What is the percentage of females who did not received any like (°)?
# 
# 19) What is the percentage of males who did not received any like( °)?
# 
# **Percentage of mobile likes performed compared to all likes performed (°)**
# 
# 20) What is the percentage of mobile likes performed by females compared to all likes performed by females (°)?
# 
# 21) What is the percentage of mobile likes performed by males compared to all likes performed by males (°)?
# 
# **Percentage of mobile likes received compared to all likes received (°)**
# 
# 22) What is the percentage of mobile likes received by females compared to all likes received by females (°)?
# 
# 23) What is the percentage of mobile likes received by males compared to all likes received by males (°)?
# 
# **Most frequent age**
# 
# 24) What is the most frequent age of all users?
# 
# **Friendship vs friendships initiated (°)**
# 
# 25) What is the mean of the difference between friend count and friendships initiated for females (°)?
# 
# 26) What is the mean of the difference between friend count and friendships initiated for males (°)?
# 
# **Months and days of the given date of birth (°)**
# 
# The last 4 questions deal with the months and days used by Facebook users for their date of birth.
# 
# The idea is that people do not give their actual date of birth. They often switch the actual month to Januray and the actual day to the first day of a month.
# 
# The percentage of people being born in January is *circa* $100 \times \frac{1}{12}$ since there are 12 months in a year.
# 
# We are going to compute the difference between the percentage found in the dataset and this theorical percentage.
# 
# 27) What is the difference between the percentage of females born in January and 100/12 (°)?
# 
# 28) What is the difference between the percentage of males born in January and 100/12 (°)?
# 
# The percentage of people being born the first day of a month is *circa* $100 \times \frac{12}{365}$ since there are 12 days which are the first day of a month in a year and there are 365 days in a year (forget the leap years).
# 
# We are going to compute the difference between the percentage found in the dataset and this theorical percentage.
# 
# 29) What is the difference between the percentage of females born the first day of a month and 1200/365 (°)?
# 
# 30) What is the difference between the percentage of males born the first day of a month and 1200/365 (°)?
# 
# (°) Result of functions should be rounded to 1 decimal place.
# 
# **Now you have a better idea of some differences between female and male Facebook users!**

# In[1]:


# usual import and options
import pandas as pd
pd.set_option("display.max_rows", 16)
pd.set_option("display.max_columns", 30)


# In[2]:


# DO NOT MODIFY THIS CELL
# MAKE SURE THAT THE FILE 'pseudo_facebook.csv' IS ALONG WITH THE DATASET 'pseudo_facebook.csv'
# USE THE 3 VARIABLES: df, df_female, df_male IN YOUR FUNCTIONS
# ALL FUNCTIONS SHOULD HAVE NO ARGUMENT

# load the dataset and build subsets with females and males
df = pd.read_csv('pseudo_facebook.csv')
df_female = df.loc[df['gender'] == 'female']
df_male = df.loc[df['gender'] == 'male']
df.head()


# In[3]:


# THIS IS AN EXAMPLE. THERE IS NOTHING TO DO. IT WILL NOT BE GRADED.
# ALL FUNCTIONS SHOULD FOLLOW THE SAME PATTERN:
# - DEFINITION OF THE FUNCTION: def exercise_XX():
# - COMPUTATION OF THE RESULT: result = ...
# - RETURN OF THE RESULT: return result

# 0) How many rows does the dataFrame have?
def exercise_00():
    result = len(df)
    return result

# run and check
exercise_00()


# In[4]:


# 1) How many columns does the DataFrame have?
def exercise_01():
    result = len(df.columns)
    return result

# run and check
exercise_01()


# In[5]:


# 2) How many females are there in the dataset?
def exercise_02():
    result = df_female['gender'].count()
    return result

#run and check
exercise_02()


# In[6]:


# 3) How many males are there in the dataset?
def exercise_03():
    result = df_male['gender'].count()
    return result

# run and check
exercise_03()


# In[7]:


# 4) What is the total number of likes performed by females?
def exercise_04():
    result = df_female["likes"].sum()
    return result

# run and check
exercise_04()


# In[8]:


# 5) What is the total number of likes performed by males?
def exercise_05():
    result = df_male["likes"].sum()
    return result

# run and check
exercise_05()


# In[9]:


# 6) What is the total number of likes received by females?
def exercise_06():
    result = df_female["likes_received"].sum()
    return result

# run and check
exercise_06()


# In[10]:


# 7) What is the total number of likes received by males?
def exercise_07():
    result = df_male["likes_received"].sum()
    return result

# run and check
exercise_07()


# In[11]:


# 8) What is the mean age of females (°)?
def exercise_08():
    result = round(df_female["age"].mean(), 1)
    return result

# run and check
exercise_08()


# In[12]:


# 9) What is the mean age of males (°)?
def exercise_09():
    result = round(df_male["age"].mean(), 1)
    return result

# run and check
exercise_09()


# In[13]:


# 10) What is the mean friend count of females (°)?
def exercise_10():
    result = round(df_female["friend_count"].mean(), 1)
    return result

# run and check
exercise_10()


# In[14]:


# 11) What is the mean friend count of males (°)?
def exercise_11():
    result = round(df_male["friend_count"].mean(), 1)
    return result

# run and check
exercise_11()


# In[15]:


# 12) What is the mean number of likes performed by females (°)?
def exercise_12():
    result = round(df_female["likes"].mean(), 1)
    return result

# run and check
exercise_12()


# In[16]:


# 13) What is the mean number of likes performed by males (°)?
def exercise_13():
    result = round(df_male["likes"].mean(), 1)
    return result

# run and check
exercise_13()


# In[17]:


# 14) What is the mean number of likes received by females (°)?
def exercise_14():
    result = round(df_female["likes_received"].mean(), 1)
    return result

# run and check
exercise_14()


# In[18]:


# 15) What is the mean number of likes received by males (°)?
def exercise_15():
    result = round(df_male["likes_received"].mean(), 1)
    return result

# run and check
exercise_15()


# In[19]:


# 16) What percentage of females did not performed any like (°)?
def exercise_16():
    result = round(((df_female.loc[df_female["likes"] == 0, "likes"].count()) / df_female["gender"].count())*100, 1)
    return result

# run and check
exercise_16()


# In[25]:


# 17) What percentage of males did not performed any like (°)?
def exercise_17():
    result = round(((df_male.loc[df_male["likes"] == 0, "likes"].count()) / df_male["gender"].count())*100, 1)
    return result

# run and check
exercise_17()


# In[33]:


# 18) What percentage of females did not received any like (°)?
def exercise_18():
    result = (df_female.loc[df_female["likes_received"] == 0, "likes_received"].count()) / df_female["gender"].count()
    result = round(result*100, 1)
    return result

# run and check
exercise_18()


# In[31]:


# 19) What percentage of males did not received any like (°)?
def exercise_19():
    result = (df_male.loc[df_male["likes_received"] == 0, "likes_received"].count()) / df_male["gender"].count()
    result = round(result*100, 1)
    return result

# run and check
exercise_19()


# In[30]:


# 20) What is the percentage of mobile likes performed by females compared to all likes performed by females (°)?
def exercise_20():
    result = (df_female["mobile_likes"].sum())/ df_female["likes"].sum()
    result = round(result*100, 1)
    return result

# run and check
exercise_20()


# In[29]:


# 21) What is the percentage of mobile likes performed by males compared to all likes performed by males (°)?
def exercise_21():
    result = (df_male["mobile_likes"].sum())/ df_male["likes"].sum()
    result = round(result*100, 1)
    return result

# run and check
exercise_21()


# In[26]:


# 22) What is the percentage of mobile likes received by females compared to all likes received by females (°)?
def exercise_22():
    result = df_female["mobile_likes_received"].sum() / (df_female["likes_received"].sum())
    result = round(result*100, 1)
    return result

# run and check
exercise_22()


# In[27]:


# 23) What is the percentage of mobile likes received by males compared to all likes received by males (°)?
def exercise_23():
    result = (df_male["mobile_likes_received"].sum())/ df_male["likes_received"].sum()
    result = round(result*100, 1)
    return result

# run and check
exercise_23()


# In[28]:


# 24) What is the most frequent age of users?
def exercise_24():
    result = df["age"].value_counts().idxmax()
    result = round(result, 1)
    return result

# run and check
exercise_24()


# In[67]:


# 25) What is the mean of the difference between friend count and friendships initiated for females (°)?
def exercise_25():
    FrCo_FrIni = df_female["friend_count"] - df_female["friendships_initiated"]
    result = FrCo_FrIni.mean()
    result = round(result, 1)
    
    return result

# run and check
exercise_25()


# In[95]:


# 26) What is the mean of the difference between friend count and friendships initiated for males (°)?
def exercise_26():
    FrCo_FrIni = df_male["friend_count"] - df_male["friendships_initiated"]
    result = round(FrCo_FrIni.mean(), 1)
    return result

# run and check
exercise_26()


# In[75]:


# 27) What is the difference between the percentage of females born in January and 100/12 (°)?
def exercise_27():
    P1 = (df_female.loc[df_female["dob_month"] == 1, "dob_month"].count())/(df_female['gender'].count())*100
    result = P1 - 100/12
    result = round(result, 1)
    return result

# run and check
exercise_27()


# In[81]:


# 28) What is the difference between the percentage of males born in January and 100/12 (°)?
def exercise_28():
    P1 = (df_male.loc[df_male["dob_month"] == 1, "dob_month"].count())/(df_male['gender'].count())*100
    result = P1 - 100/12
    result = round(result, 1)
    return result

# run and check
exercise_28()


# In[78]:


# 29) What is the difference between the percentage of females born the first of a month and 1200/365 (°)?
def exercise_29():
    P1 = (df_female.loc[df_female["dob_day"] == 1, "dob_day"].count())/(df_female['gender'].count())*100
    result = P1 - 1200/365
    result = round(result, 1)
    return result

# run and check
exercise_29()


# In[96]:


# 30) What is the difference between the percentage of males born the first of a month and 1200/365 (°)?
def exercise_30():
    P1 = (df_male.loc[df_male["dob_day"] == 1, "dob_day"].count())/(df_male['gender'].count())*100
    result = P1 - 1200/365
    result = round(result, 1)
    return result

# run and check
exercise_30()

