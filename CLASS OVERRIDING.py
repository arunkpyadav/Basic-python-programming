#!/usr/bin/env python
# coding: utf-8

# In[13]:


class employee():
    def __init__(self,name,age,salary,gender):
        self.name=name
        self.age=age
        self.salary=salary
        self.gender=gender
    def show_employee_details(self):
        print('The name of the employee is',self.name)
        print('The age of the employee is',self.age)
        print('The salary of employee is',self.salary)
        print('The gender of the employee is',self.gender)


# In[14]:


e=employee('Arun',24,14400,'male')


# In[15]:


e.show_employee_details()


# In[16]:


class senior_employee(employee):
    def __init__(self,name,age,salary,gender,passion,work):
        self.name=name
        self.age=age
        self.salary=salary
        self.gender=gender
        self.passion=passion
        self.work=work
    def show_senior_employee(self):
        print('name of the employee is ',self.name)
        print('age of the employee is ',self.age)
        print('the salary of the employee is',self.salary)
        print('the gender of the employee is',self.gender)
        print('the passion of the employee is',self.passion)
        print('work of the employee is',self.work)


# In[17]:


s=senior_employee('Ram',35,550000,'male','cricket','engineer')


# In[18]:


s.show_senior_employee()


# In[ ]:




