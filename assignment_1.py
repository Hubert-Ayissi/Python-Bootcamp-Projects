#!/usr/bin/env python
# coding: utf-8

# # Assignment \#1 - the Python beginner
# 
# 0) Create a function which computes the area of a rectangle given its height and width. Example: given 10 and 20, should return 200.
# 
# 1) Create a function which given 2 booleans computes the exclusive OR (should return True if one boolean is True and the other boolean is False; and False if both booleans are True or both booleans are False). Example: given True and False, should return True.
# 
# 2) Create a function which given hours, minutes and seconds computes the total number of seconds. Example: given 1 hour, 1 minute and 1 second, should return 3661.
# 
# 3) Create a function which given an integer, compute the sum of all integers between this integer and its double included. Example: given 3, should return 18 (3 + 4 + 5 + 6).
# 
# 4) Create a function which given a string produces a 2 characters string with the first character of the initial string and the last one. If the initial string is empty, it should return an empty string. Example: given 'Python', should return 'Pn'.
# 
# 5) Create a function which given a string returns the sentence: 'The reverse of X is Y!' where X is the initial string and Y is the reverse of the initial string. Example: given 'Paris', should return 'The reverse of Paris is siraP!'.
# 
# 6) Create a function which given a string returns True if the letters of the string are unique and False otherwise. Example: given 'Python', should return True; and given 'alphabet', should return False.
# 
# 7) Create a function which given a string returns True if the string is a palindrome (e.g., a word which has the property of reading the same forwards as it does backwards) and False otherwise. Example, given 'tattarrattat', should return True; and given 'alphabet', should return False.
# 
# 8) Create a function which given 3 numbers returns the one which is in the middle. Example: given 9, 5 and 6, should return 6.
# 
# 9) Create a function which given a list of strings produces a string with the first character of each non empty string of the list. Example: given ['Hi', 'elephants', '', 'like', 'lazy', 'olives'], should return 'Hello'.
# 
# 10) Create a function which given a list of strings returns the longest one. Example: given ['Hi', 'elephants', '', 'like', 'lazy', 'olives'], should return 'elephants'.

# In[ ]:


# THIS IS AN EXAMPLE. THERE IS NOTHING TO DO. IT WILL NOT BE GRADED.
# 0) Create a function which computes the area of a rectangle given its height and width.
def exercise_00(height, width):
    result = height * width
    return result


# In[ ]:


# run and check
exercise_00(10, 20)


# In[1]:


# 1) Create a function which given 2 booleans computes the exclusive OR.
# (should return True if one boolean is True and the other boolean is false, False if both booleans are True or both booleans are False).
def exercise_01(bool1, bool2):
    print (bool1 != bool2)


# In[5]:


# run and check
exercise_01(True, False)


# In[6]:


# 2) Create a function which given hours, minutes and seconds computes the total of seconds.
def exercise_02(hours, minutes, seconds):
    return hours*(60**2) + minutes*60 + seconds


# In[7]:


# run and check
exercise_02(1, 1, 1)


# In[65]:


# 3) Create a function which given an integer, compute the sum of all integers between this integer and its double included.
def exercise_03(integer):
    result = 0
    for i in range (integer, integer*2+1):
        result = result + i
    return result


# In[67]:


# run and check
exercise_03(3)


# In[21]:


# 4) Create a function which given a string produces a 2 characters string with the first character of the initial string and the last one.
# If the initial string is empty, it should return an empty string.
def exercise_04(string):
    result = string[0] + string[-1]
    return result


# In[24]:


# run and check
exercise_04('Python')


# In[26]:


# 5) Create a function which given a string returns the sentence: 'The reverse of X is Y!'
def exercise_05(string):
    result = string[::-1]
    print('The reverse of '+ str(string) + " is " + str(result) + "!")


# In[27]:


# run and check
exercise_05('Paris')


# In[30]:


# 6) Create a function which given a string returns True if the letters of the string are unique and False otherwise.
def exercise_06(string):
    print(len(set(string)) == len(string))


# In[34]:


# run and check
exercise_06('Python')


# In[3]:


# 7) Create a function which given a string returns True if the string is a palindrome
# (e.g., a word which has the property of reading the same forwards as it does backwards) and False otherwise.
def exercise_07(string):
    if string == string[::-1]:
        return True
    else :
        return False


# In[5]:


# run and check
exercise_07('tattarrattat')


# In[43]:


# 8) Create a function which given 3 numbers returns the one which is in the middle.
def exercise_08(number1, number2, number3):
    D = (number1, number2, number3)
    sorted(D)
    return D[1]


# In[47]:


# run and check
exercise_08(9, 5, 6)


# In[37]:


# 9) Create a function which given a list of strings produces a string with the first character of each non empty string of the list.
def exercise_09(list_of_strings):
    D = [i for i in list_of_strings if i]
    result = ''
    for n in range(0, len(D)):
        result += str(D[n][0])
    return result


# In[39]:


# run and check
exercise_09(['Hi', 'elephants', '', 'like', 'lazy', 'olives'])


# In[40]:


# 10) Create a function which given a list of strings returns the longest one.
def exercise_10(list_of_strings):
     return max(list_of_strings, key=len)


# In[42]:


# run and check
exercise_10(['Hi', 'elephants', '', 'like', 'lazy', 'olives'])

