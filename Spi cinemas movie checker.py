
import xml.etree.ElementTree as ET
import requests
import string
import pandas as pd
from lxml import html


# In[204]:


cuss_words_df = pd.DataFrame()

url = "https://www.spicinemas.in/chennai/now-showing"
XML = requests.get(url)

tree = html.fromstring(XML.content)


# In[205]:


movies = tree.xpath('//body//div[1]//article//div[1]//div[2]//section//section//section[1]')[1].getchildren()[0].getchildren()


# In[206]:


movie_list_html = movies[0].xpath("//li//div//dl//dt")
current_movie_list = [each.text_content().strip() for each in movie_list_html]
current_movie_list


# In[207]:


old_movie_list = ['2.0 TAMIL',
 'ADANGA MARU',
 'AQUAMAN',
 'BUMBLEBEE',
 'KANAA',
 'K.G.F.',
 'MAARI 2',
 'MARY POPPINS RETURNS',
 'NJAN PRAKASHAN',
 'NTR KATHANAYAKUDU',
 'PRETHAM 2',
 'SILUKKUVARPATTI SINGAM',
 'SIMMBA',
 'THATTUMPURATHU ACHUTHAN']


# In[208]:


new_movies = [each for each in current_movie_list if each not in old_movie_list]
new_movies


# In[209]:

from notify_run import Notify
notify = Notify()
if len(new_movies) > 0:
    notify.send('SATHYAM BOOKINGS OPEN')

