#!/usr/bin/env python
# coding: utf-8

# In[26]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[3]:


data=pd.read_csv(r"C:\Users\Arigala.Adarsh\Downloads\archive\covid19_Confirmed_dataset.xls")


# In[4]:


data.head()


# In[5]:


data.drop(["Lat","Long"],axis=1,inplace=True)


# In[6]:


data.head(100)


# In[16]:


grouped_data=data.groupby('Country/Region').sum()


# In[17]:


grouped_data.tail()


# In[18]:


grouped_data.shape


# In[22]:


grouped_data


# In[31]:


grouped_data.loc['China'].plot()
grouped_data.loc['Italy'].plot()
grouped_data.loc['Spain'].plot()
plt.legend(loc="lower right")
plt.show()


# In[32]:


grouped_data.loc['China'].plot()


# In[33]:


grouped_data.loc['China'][:3].plot()


# In[36]:


grouped_data.loc['China'].diff().plot()


# In[37]:


grouped_data.loc['China'].diff().max()


# In[38]:


grouped_data.loc['Spain'].diff().min()


# In[40]:


grouped_data.loc['italy'].diff().max()


# In[45]:


countries=list(grouped_data.index)
max_infection_rates=[]
for c in countries:
    max_infection_rates.append(grouped_data.loc[c].diff().max())
grouped_data["max_infection_rates"]=max_infection_rates


# In[43]:


grouped_data.head()


# In[47]:


new=pd.DataFrame(grouped_data["max_infection_rates"])


# In[48]:


new.head()


# In[56]:


happiness=pd.read_csv(r"C:\Users\Arigala.Adarsh\Downloads\worldwide_happiness_report.xls")


# In[61]:


happiness.head()


# In[66]:


columns=['Overall rank','Score','Generosity','Perceptions of corruption']


# In[67]:


happiness.drop(columns,axis=1,inplace=True)
happiness.head()


# In[68]:


happiness.set_index('Country or region',inplace=True)
happiness.head()


# In[70]:


new.head()


# In[86]:


final=new.join(happiness,how='inner')


# In[87]:


final.head(100)


# In[90]:


x=final["GDP per capita"]
y=final["max_infection_rates"]
sns.scatterplot(x,y)
plt.show()


# In[92]:


sns.regplot(x,np.log(y))


# In[93]:


x=final["Social support"]
y=final["max_infection_rates"]
sns.scatterplot(x,np.log(y))


# In[94]:


sns.regplot(x,np.log(y))


# In[95]:


x=final["Healthy life expectancy"]
y=final["max_infection_rates"]
sns.scatterplot(x,np.log(y))


# In[96]:


sns.regplot(x,np.log(y))


# In[97]:




x=final["Freedom to make life choices"]
y=final["max_infection_rates"]
sns.scatterplot(x,np.log(y))


# In[98]:


sns.regplot(x,np.log(y))


# In[ ]:




