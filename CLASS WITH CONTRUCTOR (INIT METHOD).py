#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Employee():
    def __init__(self,name,age,salary,gender):
        self.name=name
        self.age=age
        self.salary=salary
        self.gender=gender
        
    def show_employee_details(self):
        print('The Name of Employee is ',self.name)
        print('The Age of Employee is ',self.age)
        print('The salary of employee is',self.salary)
        print('The Gender of Employee is',self.gender)
e1=('Ram','35','55000','Male')


# In[2]:


e1


# In[ ]:




