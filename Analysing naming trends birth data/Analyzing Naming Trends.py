#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


data=pd.read_csv(r"C:\Users\Arigala.Adarsh\Downloads\names\yob2022.txt",names=['Name','Sex','Birth']) 


# In[3]:


data.head()


# In[4]:


data.groupby('Sex').Birth.sum()


# In[5]:


years=range(1880,2022)
array=[]
columns=['Name','Sex','Birth']
for year in years:
    path=r"C:\Users\Arigala.Adarsh\Downloads\names\yob%d.txt" %year
    dataset=pd.read_csv(path,names=columns)
    dataset['year']=year
    array.append(dataset)
new_dataset=pd.concat(array,ignore_index=True)
new_dataset


# In[6]:


new_dataset.head()


# In[7]:


#finding total birth of male and female in each year
total_birth=new_dataset.pivot_table('Birth',index='year',columns='Sex' ,aggfunc=sum)


# In[8]:


total_birth.head()


# In[9]:


total_birth.plot( )
plt.title("Total birth by sex and year wise",color='red')
plt.show()


# In[10]:


#counting the no of names and sex according to Birth
Count_sex=new_dataset.groupby('Sex').count().reset_index()
Count_sex


# In[11]:


a=Count_sex['Sex']
b=Count_sex['Birth']
sns.barplot(a,b)
plt.title("Bar gaph between Female and Male Birth rate")
plt.show()


# In[12]:


def popularnamefunc(Popular_name):
    Popular_name['name_percentage']=((Popular_name.Birth/Popular_name.Birth.sum())*100)
    return Popular_name
    
new_dataset=new_dataset.groupby(['year','Sex']).apply(popularnamefunc)
new_dataset


# In[13]:


#grouping popular data according to year
groupby_year=new_dataset.groupby('year').count().reset_index()
groupby_year


# In[14]:


#ploting bar graph between the year birth rate
a=groupby_year['year']
b=groupby_year['Birth']
sns.barplot(a,b)
plt.title('Total Birth rate in each year')
plt.show()


# In[27]:


def top_name(name_percentage):
    return name_percentage.sort_values(by='Birth',ascending=False)
p_name=new_dataset.groupby(['Sex','Birth'])

top_names=p_name.apply(top_name)
top_names.reset_index(inplace=True,drop=True) 


# In[18]:


boy_name = top_names[top_names.Sex == 'M']
girl_name = top_names[top_names.Sex == 'F']
total_birth = top_names.pivot_table('Birth', index = 'year', columns = 'Name', aggfunc = sum)


# In[19]:


boy_name.head(150)


# In[20]:


girl_name.head()


# In[22]:


girl_name=pd.DataFrame(girl_name)


# In[25]:


a=Count['Birth'].head(20)
b=Count['Sex'].head(20)
plt.bar(a,b)
plt.title('Count According to birth')
plt.show()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




