
# coding: utf-8

# # Assignment 4
# 
# Before working on this assignment please read these instructions fully. In the submission area, you will notice that you can click the link to **Preview the Grading** for each step of the assignment. This is the criteria that will be used for peer grading. Please familiarize yourself with the criteria before beginning the assignment.
# 
# This assignment requires that you to find **at least** two datasets on the web which are related, and that you visualize these datasets to answer a question with the broad topic of **sports or athletics** (see below) for the region of **Ann Arbor, Michigan, United States**, or **United States** more broadly.
# 
# You can merge these datasets with data from different regions if you like! For instance, you might want to compare **Ann Arbor, Michigan, United States** to Ann Arbor, USA. In that case at least one source file must be about **Ann Arbor, Michigan, United States**.
# 
# You are welcome to choose datasets at your discretion, but keep in mind **they will be shared with your peers**, so choose appropriate datasets. Sensitive, confidential, illicit, and proprietary materials are not good choices for datasets for this assignment. You are welcome to upload datasets of your own as well, and link to them using a third party repository such as github, bitbucket, pastebin, etc. Please be aware of the Coursera terms of service with respect to intellectual property.
# 
# Also, you are welcome to preserve data in its original language, but for the purposes of grading you should provide english translations. You are welcome to provide multiple visuals in different languages if you would like!
# 
# As this assignment is for the whole course, you must incorporate principles discussed in the first week, such as having as high data-ink ratio (Tufte) and aligning with Cairo’s principles of truth, beauty, function, and insight.
# 
# Here are the assignment instructions:
# 
#  * State the region and the domain category that your data sets are about (e.g., **Ann Arbor, Michigan, United States** and **sports or athletics**).
#  * You must state a question about the domain category and region that you identified as being interesting.
#  * You must provide at least two links to available datasets. These could be links to files such as CSV or Excel files, or links to websites which might have data in tabular form, such as Wikipedia pages.
#  * You must upload an image which addresses the research question you stated. In addition to addressing the question, this visual should follow Cairo's principles of truthfulness, functionality, beauty, and insightfulness.
#  * You must contribute a short (1-2 paragraph) written justification of how your visualization addresses your stated research question.
# 
# What do we mean by **sports or athletics**?  For this category we are interested in sporting events or athletics broadly, please feel free to creatively interpret the category when building your research question!
# 
# ## Tips
# * Wikipedia is an excellent source of data, and I strongly encourage you to explore it for new data sources.
# * Many governments run open data initiatives at the city, region, and country levels, and these are wonderful resources for localized data sources.
# * Several international agencies, such as the [United Nations](http://data.un.org/), the [World Bank](http://data.worldbank.org/), the [Global Open Data Index](http://index.okfn.org/place/) are other great places to look for data.
# * This assignment requires you to convert and clean datafiles. Check out the discussion forums for tips on how to do this from various sources, and share your successes with your fellow students!
# 
# ## Example
# Looking for an example? Here's what our course assistant put together for the **Ann Arbor, MI, USA** area using **sports and athletics** as the topic. [Example Solution File](./readonly/Assignment4_example.pdf)

# In[15]:

import pandas as pd
import matplotlib.pyplot as plt

get_ipython().magic('matplotlib notebook')
plt.style.use('seaborn-colorblind')


# In[ ]:




# In[16]:

pd.read_csv('balance.csv').head()


# In[ ]:




# In[17]:

list(pd.read_csv('balance.csv').columns.values)


# In[ ]:




# In[18]:

pd.read_csv('balance.csv', index_col=' Variables ').transpose().columns.values


# In[ ]:




# In[19]:

import locale
from locale import atof

locale.setlocale(locale.LC_NUMERIC, '')


# In[20]:

df_balance = pd.read_csv('balance.csv', index_col=' Variables ', thousands=',').transpose().applymap(lambda x: x.replace(',', '') if type(x)==str else x)
df_balance = df_balance[[' D Overall Balance (A-B+C) ', '         Goods Balance ', '         Services Balance ']]
df_balance.head()


# In[21]:

df_balance = df_balance.astype(float)


# In[ ]:




# In[22]:

pd.read_csv('gdp.csv').head()


# In[ ]:




# In[23]:

pd.read_csv('gdp.csv', index_col=' Variables ').transpose().columns.values


# In[ ]:




# In[10]:

df_gdp = pd.read_csv('gdp.csv', index_col=' Variables ', thousands=',').transpose().applymap(lambda x: x.replace(',', '') if type(x)==str else x)
df_gdp.head()


# In[ ]:




# In[24]:

df_gdp = df_gdp[[' Gross Domestic Product At 2010 Market Prices ', '     Goods Producing Industries ', '     Services Producing Industries ']]
df_gdp = df_gdp[df_gdp.index>' 1986']
df_gdp.head()


# In[ ]:




# In[50]:

all_data = df_gdp.join(df_balance)
all_data.head()


# In[ ]:




# In[ ]:




# In[51]:

all_data.rename(columns = {' Gross Domestic Product At 2010 Market Prices ': 'GDP', 
                           '     Goods Producing Industries ': 'Goods', 
                           '     Services Producing Industries ': 'Services', 
                           ' D Overall Balance (A-B+C) ': 'Balance', 
                           '         Goods Balance ': 'Goods Bal', 
                           '         Services Balance ': 'Service Bal'}, inplace = True)


# In[ ]:




# In[136]:

plt = all_data.plot.line()
plt.set_title("Corelation between Singapore's GDP Vs Balances")
plt.axes.grid(False)
#plt.axes.set_axis_bgcolor("w")
plt.patch.set_facecolor('pink')


# In[ ]:




# In[134]:

plt2 = all_data.plot.kde(use_index=True, title="KDE Map", grid=None, subplots=True, legend=True, sharey=True);


# In[ ]:



