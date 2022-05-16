#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
import json
import os
import pandas as pd
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
from pathlib import Path


# In[2]:


# URL Required to retrieve the client specific URL for accesing the RMS API
url_auth = "https://restapi8.rmscloud.com/clienturl/11281"

# JSON schema to create authentication token
headers = {
  "agentId": 15,
  "agentPassword": "1h&29$vk449f8",
  "clientId": 11281,
  "clientPassword": "6k!Dp$N4",
  "useTrainingDatabase": "false",
  "moduleType": [
    "pointOfSale",
    "kiosk"
  ]
}


# In[3]:


# Retrieve the client specific URL for accesing the RMS API 
response = requests.get(url=url_auth)


# In[4]:


# URL for RMS API
url_response = response.text
url_response


# In[5]:


# Create authentication token
url_dest = url_response + '/authToken'
url_dest


# In[6]:


# Auth Token Response
resp_dest = requests.post(url = url_dest, json = headers).json()
resp_dest 


# In[7]:


# Token obtained
token = resp_dest['token']
token


# In[8]:


# Method for grouping Allotments
groupallot_inf = url_response + '/groupAllotments'
response_groupallot_inf = requests.get(url=groupallot_inf,  params = {'modelType':'basic','limit': 500}, headers = {'authtoken': token}).json()
df_groupallot_inf = pd.json_normalize(response_groupallot_inf)
df_groupallot_inf


# In[9]:


# Method for Properties
properties_inf = url_response + '/properties'


# In[10]:


response_properties_inf = requests.get(url=properties_inf, headers = {'authtoken': token}).json()
response_properties_inf
df_properties_inf = pd.json_normalize(response_properties_inf)
df_properties_inf
df_properties_inf.to_csv('Properties_Prueba.csv')


# In[22]:


res_idguest = df_res_inf['guestId'].to_list()
res_idguest


# In[20]:


# Method for meal plans
mealplans_inf = url_response + '/mealPlans'


# In[21]:


response_mealplans_inf = requests.get(url=mealplans_inf, headers = {'authtoken': token}).json()
response_mealplans_inf
df_mealplans_inf = pd.json_normalize(response_mealplans_inf)
df_mealplans_inf
df_mealplans_inf.to_csv('MealPlan_Prueba.csv')


# In[ ]:


# Method for guest
mealplans_inf = url_response + '/mealPlans'


# In[15]:


# Method for GL ACC Codes
gl_inf = url_response + '/glAccountCodes'


# In[16]:


response_gl_inf = requests.get(url=gl_inf, params = {'limit': 500}, headers = {'authtoken': token}).json()
df_gl_inf = pd.json_normalize(response_gl_inf)
df_gl_inf
df_gl_inf.to_csv('GL_AccCodes.csv')


# In[8]:


# Method to obtain reservations
res_inf = url_response + '/reservations/search'
res_inf


# In[9]:


# parameter of yesterday
yesterday = datetime.now() - timedelta(1)
yesterday = yesterday.strftime("%Y-%m-%d %H:%M:%S")
yesterday


# In[13]:


# Retrieve reservations 
resp_res_inf = requests.post(url = res_inf , params = {'modelType':'full','limit': 500}, json = {"createdFrom": "2022-01-01 00:00:00"}, headers = {'authtoken': token}).json()


# In[14]:


# JSON Reservations Response
resp_res_inf


# In[15]:


# Response Reservations Method 
df_res_inf = pd.json_normalize(resp_res_inf)
df_res_inf
df_res_inf.to_csv('Reservas_Prueba.csv')


# In[24]:


res_id = df_res_inf['guestId'].to_list()
res_id


# In[27]:


iterable = []
for i in res_id:
    res_guest = url_response + '/guests/' + str(i) 
    resp_res_guest = requests.get(url = res_guest , params = {'id': i}, headers = {'authtoken': token}).json()
    iterable.append(resp_res_guest)

 


# In[ ]:





# In[28]:


df_res_guest = pd.json_normalize(iterable)
df_res_guest
df_res_guest.to_csv('Guest_Prueba.csv')


# In[30]:


# Method for Agents
agents_inf = url_response + '/travelAgents'


# In[31]:


response_travelAgents_inf = requests.get(url=agents_inf,params = {'modelType':'full','limit': 500}, headers = {'authtoken': token}).json()
response_travelAgents_inf
df_travelAgents_inf = pd.json_normalize(response_travelAgents_inf)
df_travelAgents_inf
df_travelAgents_inf.to_csv('Agents_Prueba.csv')


# In[ ]:




