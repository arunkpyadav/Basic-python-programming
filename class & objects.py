#!/usr/bin/env python
# coding: utf-8

# In[1]:


class phone():
    def make_call(self):
        print('i am making a call')
    def play_games(self):
        print('i m playing games')
        


# In[2]:


p1=phone()


# In[3]:


p1.make_call()


# In[4]:


p1.play_games()


# In[9]:


class phone():
    def set_color(self,color):
        self.color=color
    def set_cost(self,cost):
        self.cost=cost
    def show_color(self):
        return self.color
    def show_cost(self):
        return self.cost
p2=phone()
p2.set_color("blue")
p2.set_cost("5000")


# In[10]:


p2.show_cost()


# In[11]:


p2.show_color()


# In[ ]:




