#!/usr/bin/env python
# coding: utf-8

# In[ ]:


Write a Python program to reverse a string.



﻿Sample String : "1234abcd"

Expected Output : "dcba4321"


# In[1]:


def reverse_of_string(sample_string):
    reverse_string = sample_string[::-1]         # using slicing to reverse the string
    return (reverse_string)
sample_string = input("Enter any string of your choice :- ")     # taking an input from user 
str = reverse_of_string(sample_string)
print(f"The reverse string :- {str}")    # usin


# In[ ]:




