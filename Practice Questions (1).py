#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#1. Take two int values from the user and print the greatest among them.
#2. Write a program to check whether a person is eligible for voting or not. (accept age from the user)
#3. Write a program to check whether a number is divisible by 7 or not.
#4. Write a program to display "Hello" if a number entered by the user is a multiple of five, 
 ##  otherwise print "Bye".


# In[2]:


#Take two int values from the user and print the greatest among them.
num1=input('enter a number')
num2=input('enter a number')
if num1>num2:
    print(num1)
else:
    print(num2)



# In[8]:


#Write a program to check whether a person is eligible for voting or not. (accept age from the user)

age = int(input('enter a number'))
if age==18 or age>18:
    print('you are eligible for voting')
else:
    print('buddy your not eligible for voting')


# In[12]:


#Write a program to check whether a number is divisible by 7 or not.

num=int(input('enter a number'))
if num%7 == 0:
    print('Number is divisible by 7')
else:
    print('Number is not divisible by 7')


# In[22]:


#Write a program to display "Hello" if a number entered by the user is a multiple of five
Numb=int(input('enter a number'))
if Numb%5==0:
    print('Hellow')
else:
    print('Bye')
    


# In[ ]:




