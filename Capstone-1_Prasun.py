#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Import Required packages
import mysql.connector
from mysql.connector import Error
import pandas as pd


# In[2]:


#Connect to MySQL
connection = mysql.connector.connect(host='cpanel.insaid.co',
                                     database='Capstone1',
                                         user='student',
                                         password='student')
if connection.is_connected():
    db_Info = connection.get_server_info()
    print("Connected to MySQL Server version ", db_Info)
    cursor = connection.cursor()
    cursor.execute("select database();")
    record = cursor.fetchone()
    print("You're connected to database: ", record)


# In[3]:


#Fetching data from MySQL
cursor.execute("select * from gender_age_train")
data1=cursor.fetchall()
cursor.execute("select * from phone_brand_device_model")
data2=cursor.fetchall()


# In[4]:


#Converting to DataFrame
gender_age_train=pd.DataFrame(data1)
phone_brand_device_model=pd.DataFrame(data2)


# In[5]:


#Viewing data of gender_age_train
gender_age_train.head()


# In[6]:


#Viewing data of phone_brand_device_model
phone_brand_device_model.head()


# In[7]:


#Read data from events_data
events_data=pd.read_csv("events_data.csv")
events_data.head()


# In[10]:


print(gender_age_train.shape)
print(phone_brand_device_model.shape)
print(events_data.shape)


# In[ ]:




