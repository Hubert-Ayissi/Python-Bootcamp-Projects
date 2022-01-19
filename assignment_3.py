#!/usr/bin/env python
# coding: utf-8

# # Assignment \#3 the Olympic dataset
# 
# #### Features description
# - *City*: City
# - *Edition*: Year
# - *Sport*: Sport
# - *Discipline*: Discipline
# - *Athlete*: Athlete's last name and first name (generally separated by a comma and a space)
# - *NOC*: Country, National Olympic Committee, ISO 3166-1 alpha-3
# - *Gender*: Men, Women
# - *Event*: Event
# - *Event_gender*: Event gender (F = Women, M = Men, X = NA)
# - *Medal*: Metal of medal (Bronze, Silver, Gold)

# In[4]:


# usual import and options
import pandas as pd
pd.set_option("display.max_rows", 16)


# ### Loading the dataset
# 
# **file**: `'Summer Olympic medallists 1896 to 2008 - ALL MEDALISTS.txt'`
# 
# **separator**: tab: `\t`

# In[13]:


# LOADING THE DATASET
# DO NOT CHANGE THIS CELL FOR GRADING
# THE DATASET SHOULD BE ALONG WITH THE NOTEBOOK AND THE PYTHON FILE
                                                
df = pd.read_csv('Summer Olympic medallists 1896 to 2008 - ALL MEDALISTS.txt', sep='\t')
df


# #### Questions
# 
# 1) How many different cities have organized Olympic games?
# 
# 2) How many different editions of Olympic games are in the dataset?
# 
# 3) How many cities have organized more than one edition of Olympic games?
# 
# 4) Which sport distributed the most medals?
# 
# 5) Which discipline distributed the most medals?
# 
# 6) How many gold medals have been distributed?
# 
# 7) Which edition distributed the most silver medals?
# 
# 8) In how many different disciplines did men received medals (°)?
# 
# 9) In how many different disciplines did women received medals (°)?
# 
# 10) How many disciplines are dedicated to women (°)?
# 
# 11) How many countries have won a medal with an event gender equal to 'X'?
# 
# 12) How many countries have won a gold medal with an event gender equal to 'X'?
# 
# 13) How many different countries have an athlete whose surname is 'SCHMIDT'?
# 
# 14) How many different sports have the word 'ball' in their name?
# 
# 15) How many Bronze or Silver medals have been won by any athlete whose surname is 'KIM'?
# 
# 16) How many different events are in the dataset?
# 
# 17) How many different events including numbers in their description are in the dataset?
# 
# 18) Which athlete has participated in the most editions?
# 
# 19) How many sports have the same number of Gold, Silver and Bronze medals?
# 
# 20) How many athletes have strictly more Gold medals than Silver and more Silver medals than Bronze?
# 
# 21) Which country has won at least one medal in each olympic edition?
# 
# 22) Add a column named 'Score' with 1 for Bronze, 2 for Silver and 3 for Gold medals. What is the total sum of scores?
# 
# 23) Which athlete has the largest sum of scores?
# 
# 24) Which woman athlete has the largest sum of scores?
# 
# 25) For how many countries the sum of men's scores is equal to the sum of women's scores?
# 
# 26) Add a column named 'Trial' with the concatenation of columns 'Discipline', 'Sport' and 'Event' separated by a space. How many different trials are in the dataset?
# 
# 27) Which edition has the largest number of different trials?
# 
# 28) Add a column 'First Name' with the first name of athletes. How many different first names are in the dataset?
# 
# 29) Which athlete's first name has the largest sum of scores?
# 
# 30) Which woman athlete's first name has the largest sum of scores (°)?
# 
# (°) Use the 'Gender' column.

# In[10]:


# 1) How many different cities have organized Olympic games?
def exercise_01():
    result = df["City"].nunique()
    return result

# run and check
exercise_01()


# In[11]:


# 2) How many different editions of Olympic games are in the dataset?
def exercise_02():
    result = df["Edition"].nunique()
    return result

# run and check
exercise_02()


# In[41]:


# 3) How many cities have organized more than one edition of Olympic games?

def exercise_03():
    result = (df.groupby('City')['Edition'].nunique()>(1)).sum()
    return result

# run and check
exercise_03()


# In[62]:


# 4) Which sport distributed the most medals?

def exercise_04():
    tb = df.groupby('Sport')['Medal'].count()
    result = tb.idxmax(axis='Sport')
    return result

# run and check
exercise_04()


# In[64]:


# 5) Which discipline distributed the most medals?

def exercise_05():
    tb = df.groupby('Discipline')['Medal'].count()
    result = tb.idxmax(axis='Discipline')
    return result

# run and check
exercise_05()


# In[75]:


# 6) How many gold medals have been distributed?

def exercise_06():
    result = df.loc[(df["Medal"] == "Gold"), "Medal"].count()
    return result

# run and check
exercise_06()


# In[128]:


# 7) Which edition distributed the most silver medals?

def exercise_07():
    result = df.loc[df['Medal'] == 'Silver'].groupby('Edition')['Medal'].count().idxmax('Edition')
    return result

# run and check
exercise_07()


# In[142]:


# 8) In how many different disciplines did men received medals (°)?

def exercise_08():
    result = df.loc[df['Gender'] == 'Men'].groupby('Discipline')['Discipline'].nunique().sum()
    return result

# run and check
exercise_08()


# In[143]:


# 9) In how many different disciplines did women received medals (°)?

def exercise_09():
    result = df.loc[df['Gender'] == 'Women'].groupby('Discipline')['Discipline'].nunique().sum()
    return result

# run and check
exercise_09()


# In[295]:


# 10) How many disciplines are dedicated to women (°)?

def exercise_10():
    tb = pd.crosstab(df ['Discipline'], df['Event_gender']).reset_index()
    result = len(tb.loc[(tb['M'] == 0) & (tb['X'] == 0)])
    return result

# run and check
exercise_10()


# In[155]:


# 11) How many countries have won a medal with an event gender equal to 'X'?

def exercise_11():
    result = df.loc[df['Event_gender'] == 'X'].groupby('NOC')['NOC'].nunique().sum()
    return result

# run and check
exercise_11()


# In[156]:


# 12) How many countries have won a gold medal with an event gender equal to 'X'?

def exercise_12():
    result = df[(df['Event_gender']=='X') & (df['Medal'] == 'Gold')].groupby('NOC')['NOC'].nunique().sum()
    return result

# run and check
exercise_12()


# In[166]:


# 13) How many different countries have an athlete whose surname is 'SCHMIDT'?

def exercise_13():
    result = df[df['Athlete'].str.startswith('SCHMIDT')].groupby('NOC')['NOC'].nunique().sum()
    return result

# run and check
exercise_13()


# In[270]:


# 14) How many different sports have the word 'ball' in their name?

def exercise_14():
    result = df[df['Sport'].str.contains('ball')].nunique()['Sport']
    return result

# run and check
exercise_14()


# In[188]:


# 15) How many Bronze or Silver medals have been won by any athlete whose surname is 'KIM'?

def exercise_15():
    
    result = df.loc[(df['Athlete'].str.startswith('KIM,')) & ((df['Medal']=='Silver') | (df['Medal'] == 'Bronze'))].count()['Medal']
    return result

# run and check
exercise_15()


# In[190]:


# 16) How many different events are in the dataset?

def exercise_16():
    result = df['Event'].nunique()
    return result


# run and check
exercise_16()


# In[271]:


# 17) How many different events including numbers in their description are in the dataset?

def exercise_17():
    result = df.loc[df['Event'].str.contains('[0-9]')].nunique()['Event']
    return result


# run and check
exercise_17()


# In[272]:


# 18) Which athlete has participated in the most editions?

def exercise_18():
    result = df.groupby('Athlete')['Edition'].nunique().idxmax()
    return result

# run and check
exercise_18()


# In[234]:


# 19) How many sports distributed exactly the same number of Gold, Silver and Bronze medals?

def exercise_19():
    tb = df.pivot_table(values= "Athlete", index ='Sport', columns ='Medal', aggfunc = 'count')
    result = tb.loc[(tb['Gold'] == tb['Silver']) & (tb['Bronze'] == tb['Silver']), 'Silver'].count()
    return result

# run and check
exercise_19()


# In[274]:


# 20) How many athletes received strictly more Gold medals than Silver and strictly more Silver medals than Bronze?

def exercise_20():
    tb = df.pivot_table(values = 'Sport', index ='Athlete', fill_value =0, columns='Medal', aggfunc = 'count')
    result = len(tb.loc[(tb['Gold'] > tb['Silver']) & (tb['Silver'] > tb['Bronze'])])
    return result

# run and check
exercise_20()


# In[269]:


# 21) Which country has won at least one medal in each olympic edition?

def exercise_21():
    tb = df.pivot_table(values = 'Medal', index ='Edition', columns='NOC', aggfunc = 'count')
    result = tb.ge(1).all().idxmax()
    return result

# run and check
exercise_21()


# In[284]:


# 22) What is the total sum of scores?

def exercise_22():
    df["Goals"]= df["Medal"].map({'Gold':3, 'Silver':2, 'Bronze':1 })
    result= df['Goals'].sum()
    return result

# run and check
exercise_22()


# In[285]:


# 23) Which athlete has the largest sum of scores?

def exercise_23():
    result = df["Goals"]= df["Medal"].map({'Gold':3, 'Silver':2, 'Bronze':1 })
    result = df.groupby('Athlete').sum()['Goals'].idxmax()
    return result

# run and check
exercise_23()


# In[286]:


# 24) Which woman athlete has the largest sum of scores (°)?

def exercise_24():
    df["Goals"]= df["Medal"].map({'Gold':3, 'Silver':2, 'Bronze':1 })
    result = df.loc[df['Gender'] == 'Women'].groupby('Athlete')['Score'].sum().idxmax()
    return result

# run and check
exercise_24()


# In[287]:


# 25) For how many countries the sum of men' scores is equal to the sum of women' scores?

def exercise_25():
    df["Goals"]= df["Medal"].map({'Gold':3, 'Silver':2, 'Bronze':1 })
    tb = df.pivot_table(values ='Goals', index ='NOC',columns ='Gender', aggfunc = sum, fill_value = 0)
    result= tb.loc[tb['Men'] == tb['Women']].count()['Men']
    return result

# run and check
exercise_25()


# In[290]:


# 26) How many different trials are in the dataset?

def exercise_26():
    result = (df['Discipline'] + " " + df['Sport'] + ' ' + df['Event']).nunique()
    return result

# run and check
exercise_26()


# In[288]:


# 27) Which edition has the most different trials?

def exercise_27():
    df['Trials'] = df['Discipline'] + " " + df['Sport'] + ' ' + df['Event']
    result= df[['Edition','Trials']].groupby('Edition').nunique()['Trials'].idxmax()
    return result

# run and check
exercise_27()


# In[289]:


# 28) How many different first names are in the dataset?

def exercise_28():
    tb = df ['Athlete'].str.split(',', n=2, expand=True)
    result= tb[1].nunique()
    return result

# run and check
exercise_28()


# In[291]:


# 29) Which athlete's first name has the largest sum of scores?

def exercise_29():
    df["Goals"] = df["Medal"].map({'Gold':3, 'Silver':2, 'Bronze':1 })
    df['First_Name'] = df['Athlete'].str.split(',', n=2, expand=True)[1]
    result= df.groupby('First_Name')['Score'].sum().idxmax()
    return result

# run and check
exercise_29()


# In[292]:


# 30) Which woman athlete's first name has the largest sum of scores (°)?

def exercise_30():
    df["Goals"]= df["Medal"].map({'Gold':3, 'Silver':2, 'Bronze':1 })
    df['First_Name']= df['Athlete'].str.split(',', n=2, expand=True)[1]
    result= df[df['Gender'] == 'Women'].groupby('First_Name')['Score'].sum().idxmax()
    return result

# run and check
exercise_30()

