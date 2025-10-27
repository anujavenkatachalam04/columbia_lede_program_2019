#!/usr/bin/env python
# coding: utf-8

# # Homework 3 
# ## Anuja Venkatachalam
# ### 04-June-2019
# 
# ### PART ONE

# #### Question 1 - Count number of units in the list using the for loop

# In[11]:


numbers=[4, 5, 1, 10, 200, 34, 22, 19, 43, 56, 32, 11, 40, 82, 23, 43, 12, 65, 10]


# In[12]:


count=0
for number in numbers:
    count=count+1
print(f"The list has {count} units.")


# #### Question 2 - Add a new number to the list

# In[13]:


numbers.append(25)


# In[14]:


print(numbers)


# In[15]:


print(len(numbers))


# #### Question 3 - Count the number of even numbers using a for loop

# In[16]:


count=0
for number in numbers:
    if number%2==0:
        count=count+1
print(f"The total number of even numbers is {count}.")


# #### Question 4 - How many numbers are above the mean and how many are below the mean?

# In[17]:


above=0
below=0
import statistics
for number in numbers:
    if number>statistics.mean(numbers):
        above=above+number
    elif number<statistics.mean(numbers):
        below=below+number
print(f"The total number of numbers above the mean is {above}, and the total number of numbers below the mean is {below}.")


# #### Question 5 - Total up the numbers with a for loop

# In[18]:


sum=0
for number in numbers:
    sum=sum+number
print(f"The sum of all the numbers in the list is {sum}")


# #### Question 6 - Total up the numbers that are above the mean, and total up the numbers below the mean using the for loop.

# In[19]:


above=0
below=0

import statistics
for number in numbers:
    if number>statistics.mean(numbers):
        above=above+number
    elif number<statistics.mean(numbers):
        below=below+number
print(f"The sum of numbers above the mean is {above}, and the sum of numbers below the mean is {below}.")       


# #### Question 7 - Find the largest number using the for loop.

# In[20]:


largest=0
for number in numbers:
    if number>largest:
        largest=number
print(f"The largest number is {largest}.")


# #### Question 8 - Add a dog, "Maxwell" to this list

# In[21]:


dogs = ["Sparky", "Jane", "Matilda", "Blartsburg"]


# In[22]:


dogs.append("Maxwell")


# In[17]:


print(dogs)


# #### Question 9 - Make a list of all dogs that have names of 5 characters or less using a for loop.

# In[23]:


count=0
for dog in dogs:
    if len(dog)<=5:
        count=count+1
print(f"The number of dogs that have names of 5 characters or less is {count}.")


# #### Question 10 - Run a loop for URLs.
# 

# In[24]:


cantons = [ "ZH", "BE", "LU", "UR", "SZ", "OW", "NW", "GL", "ZG", "FR", "SO", "BS", "BL", "AR", "AI", "SG", "GR", "AG", "TG", "TI", "VD", "VS", "NE", "GE", "JU"]


# In[8]:


url="http://important-swiss-things.ch/docs/download/"
for canton in cantons:
    print (url+canton)


# #### Question 11 - URLs and pdf links

# In[25]:


documents=["qq7lthm", "jemsqhg", "O6itcke", "cp4Iua0", "bkijcmo", "ctoyjrm", "z8wc6xy", "zk4Bmm0"]


# In[26]:


def function (document, number):
    print(f"www.top-secret-pdfs.com/content/secrets/{document}/page/{number:03}.pdf")


# In[63]:


for document in documents:
    document=document.upper()
    for number in range(1,13):
        function(document,number)


# ### PART TWO

# #### Question 1 - Create a dictionary

# In[27]:


patient={
    "name": "Joe",
    "complaint": "Joint pain"
}


# In[28]:


print("Doctor, it looks like the patient named", patient["name"], "is complaining about", patient["complaint"])


# #### Question 2 - Add items and values to the dictionary

# In[29]:


patient["heart rate"]=70
patient["temperature"]=98.6
patient["infection"]=False


# In[30]:


print(patient.items())


# #### Question 3 - Conduct a diagnosis

# In[36]:


if patient["temperature"]>102 and patient["infection"]==False:
    patient["diagnosis"]="Heat stroke"
elif patient["temperature"]>102 and patient["infection"]==True:
    patient["diagnosis"]="Flu"
elif patient["temperature"]==98.6 and patient["infection"]==True:
    patient["diagnosis"]="Cold"
else:
    patient["diagnosis"]="Nil. Take an aspirin and call me in the morning"

print("Your diagnosis is", patient["diagnosis"])
    


# #### Question 4 - Make a list of 3 different patients, each with different complaint, heart rate, temperature, and whether they have an infection or not (this will be a list of dictionaries). Use a for loop to diagnose each of them.

# In[37]:


Jill={
    "name":"Jill",
    "complaint":"Back pain",
    "heart rate": 70,
    "temperature": 98.6,
    "infection": True
    }

Jane={
    "name":"Jane",
    "complaint":"Fever",
    "heart rate": 90,
    "temperature": 100,
    "infection": False
    }

Rob={
    "name":"Rob",
    "complaint":"Dizziness",
    "heart rate": 100,
    "temperature": 101,
    "infection": False
    }
   


# In[39]:


patients=[Jill, Jane, Rob]


# In[40]:


for patient in patients:
    if patient["temperature"]>102 and patient["infection"]==False:
        patient["diagnosis"]="Heat stroke"
    elif patient["temperature"]>102 and patient["infection"]==True:
        patient["diagnosis"]="Flu"
    elif patient["temperature"]==98.6 and patient["infection"]==True:
        patient["diagnosis"]="Cold"
    else:
        patient["diagnosis"]="Nil. Take an aspirin and call me in the morning"

    print("Your diagnosis is", patient["diagnosis"])
    


# ### PART THREE

# In[41]:


import csv

csvfile = open('countries.csv', 'r')
reader = csv.DictReader(csvfile)
data = list(reader)
csvfile.close()
print("The data looks like", data)


# #### Question 1 - What are the columns in our dataset?

# In[42]:


print(len(data))


# In[43]:


print(type(data))


# In[44]:


print(data[0])


# In[45]:


print(data[187])


# ##### Answer - The columns are Country, Continent, GDP_per_capita, Life_expectancy and Population

# #### Question 2 - How many countries do we have in our dataset?

# In[46]:


#Each item in the list seems to be for a country

print(f"The number of countries is {len(data)}")


# #### Question 3 - How many countries in Asia? How about North America?

# In[47]:


asia=0
north_america=0
for country in data:
    if country["Continent"]=="Asia":
        asia=asia+1
    elif country["Continent"]=="N. America":
        north_america=north_america+1

print(f"There are {asia} countries in Asia, and {north_america} countries in North America.")


# #### Question 4 - What is the total population of the world?

# In[48]:


total_population=0

for country in data:
    total_population=total_population+int(country["Population"])

print(f"The total population is {round(total_population/1000000000,2)} billion.")


# #### Question 5 - Which has a larger population, Africa or South America?

# In[49]:


population_south=0
population_africa=0

for country in data:
    if country["Continent"]=="S. America":
        population_south=population_south+int(country["Population"])
    elif country["Continent"]=="Africa":
        population_africa=population_africa+int(country["Population"])
        
if population_south>population_africa:
    print("South America has a larger population than Africa")
else:
    print("Africa has a larger population than South America")


# #### Question 6 - Calculate the total GDP of each country and print it out (right now it's per capita).

# In[50]:


pop=data[0]
print(type(pop))


# In[51]:


print(pop.keys())


# In[42]:


for country in data:
    print("The GDP of", country["Country"], "is", (int(country["GDP_per_capita"])*int(country["Population"]))/1000000000, "billion")


# #### Question 7 - What is the median life expectancy of the world?

# In[52]:


life_expectancy=[]

for country in data:
    life_expectancy.append(float(country["life_expectancy"]))

import statistics
print("The median life expectancy of all countries in the dataset is", statistics.median(life_expectancy),"years")                          


# #### Question 8 - What is the median life expectancy of Europe?

# In[53]:


years_europe=[]

for country in data:
    if country["Continent"]=="Europe":
        years_europe.append(float(country["life_expectancy"]))

import statistics
print("The median life expectancy of all countries in the dataset is", statistics.median(years_europe),"years")                          


# In[55]:


import statistics
average_life=statistics.mean(life_expectancy)
print("The average life expectancy is", average_life, "years.", "The following countries have a life expectancy below average:")

for country in data:
    if float (country["life_expectancy"])<average_life:
        print(country["Country"]) 


# #### Question 10 - Print out each country that has a below-average GDP but an above-average life expectancy.

# In[56]:


gdp_list=[]

for country in data:
    gdp_list.append(int(country["GDP_per_capita"])*int(country["Population"]))
   
import statistics
average_gdp=statistics.mean(gdp_list)

#The average life expectancy is already calculated above
for country in data:
    if int(country["GDP_per_capita"])*int(country["Population"])<average_gdp and float(country["life_expectancy"])>average_life:
        print(country["Country"])


# #### Q11. Calculate the 75th percentile of GDP.

# In[61]:


import numpy as np
percentile=np.percentile(gdp_list,75)

print("The 75th percentile of GDP is", percentile)


# #### Q12. What percent of the world population has a life expectancy of below 50 years? Above 80 years?

# In[66]:


population_50=0
population_80=0

for country in data:
    if float(country["life_expectancy"])<50:
        population_50=population_50+int(country["Population"])
    if float(country["life_expectancy"])>80:
        population_80=population_80+int(country["Population"])
        
#The total population is already calculated above
print("The percentage of the world population that has a life expectancy of below 50 years is", round(population_50/total_population*100,2))

print("The percentage of the world population that has a life expectancy of above 80 years is", round(population_80/total_population*100,2))
  

   


# #### The End 

# In[ ]:




