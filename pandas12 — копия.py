#!/usr/bin/env python
# coding: utf-8

# In[ ]:


Задание 1

Напишите функцию, которая классифицирует фильмы из материалов занятия по следующим правилам:
- оценка 2 и меньше - низкий рейтинг
- оценка 4 и меньше - средний рейтинг
- оценка 4.5 и 5 - высокий рейтинг

Результат классификации запишите в столбец class


# In[69]:



import pandas as pd
rating_data = pd.read_csv('ratings.csv')
rating_data
def class_ (value):
    if value  <= 2:
        return ( 'низкий рейтинг' )
    elif value  <= 4:
        return( 'средний рейтинг' )
    elif value  >= 4.5:
        return( 'высокий рейтинг' )
rating_data ['class_'] = rating_data['rating'].apply(class_)
rating_data.head()


# In[ ]:


Задание 2

Используем файл keywords.csv.

Необходимо написать гео-классификатор, который каждой строке сможет выставить географическую принадлежность 
определенному региону. Т. е. если поисковый запрос содержит название города региона, то в столбце ‘region’ 
пишется название этого региона. Если поисковый запрос не содержит названия города, то ставим ‘undefined’.
Результат классификации запишите в отдельный столбец region.


# In[40]:


geo_data = {
'Центр': ['москва', 'тула', 'ярославль'],

'Северо-Запад': ['петербург', 'псков', 'мурманск'],

'Дальний Восток': ['владивосток', 'сахалин', 'хабаровск']
}
print (geo_data)


# In[70]:


import pandas as pd
data = pd.read_csv('keywords.csv')
data.head()
def set_region(value):
    for region in geo_data.keys():
        if any (city in value for city in geo_data.get(region)):
            return 'region'
        return 'undefined'
data['region'] = data ['keyword'].apply(set_region)
#data.head(10)
result = data[data['keyword'].str.contains('москва')]
result.head()              
    
   

    
    


# In[ ]:




