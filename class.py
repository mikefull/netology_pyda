#!/usr/bin/env python
# coding: utf-8

# In[1]:


#1 задание
class Rate:
    def __init__(self, value):
        self.value = value
    def exchange_rates(self):
        r = requests.get('https://www.cbr-xml-daily.ru/daily_json.js')
        return r.json()['Valute']
    
    
    def max_value (self, Name):
        """
       Ищем максимальное значение
        """
        value = self.exchange_rates()
        for Name in value:
            if value [Name]['Value'] == max:
                return value [Name] ['Name']


# In[2]:


#2 задание
class Rate:
    def __init__(self, format_, diff):
        self.format = format_
        self.format = diff
    
    def exchange_rates(self):
        r = requests.get('https://www.cbr-xml-daily.ru/daily_json.js')
        return r.json()['Valute']

    def make_format_diff(self, value):
        diff_ = self.exchange_rates()
        if value in diff_:
            if  "Value" > "Previous":
                return "True"
            
            if  "Value" < "Previous":
                return "False"
        
    
    def eur(self):
        return make_format_diff('EUR')
    
    def usd(self):
        return make_format_diff('USD')


# In[10]:


#3 задание
class Employee:
    def __init__(self, name, seniority, awards):
        self.name = name
        self.seniority = seniority
        self.awards = awards
     
    
    def grade_up(self):
        """Повышает уровень сотрудника"""
        self.grade += 1
    
    def publish_grade(self):
        """Публикация результатов аккредитации сотрудников"""
        print(self.name, self.grade)
        class Designer(Employee):
            def __init__(self, name, seniority, awards):
                super().__init__(name, seniority, awards)
            def check_if_it_is_time_for_upgrade(self):
        # для каждой аккредитации увеличиваем счетчик на 1
                self.seniority =  self.seniority + (1 * awards)
       
        
        # условие повышения сотрудника из презентации
            if self.seniority % 7 == 0:
                self.grade_up()
        
        # публикация результатов
        return self.publish_grade()


# In[ ]:


elena = Designer('Елена', seniority = 0, awards = 2)


# In[ ]:


for i in range(20):
    elena.check_if_it_is_time_for_upgrade()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




