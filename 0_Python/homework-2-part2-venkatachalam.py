#Anuja Venkatachalam
#2019-05-30
#Homework 2 - PART TWO
#Number of lines of code: 123

#PART TWO - Lists
#Question 1
countries=["United States of America", "Nigeria", "China", "Australia", "New Zealand", "India", "South Korea"]
print(f"Here is a list of countries {countries}.")

#Question 2
count=0
for country in countries:
  count=count+1
  print (f"Country number {count} is {country}.")

#Question 3
countries=sorted(countries)

#Question 4
print(f"The first country in the alphabetically sorted version of the list is {countries[0]}.")

#Question 5
print(f"The second last country in alphabetically sorted version of the list is {countries[-2]}.")

#Question 6
countries.remove("China")

#Question 7
print("After removing China..")

count=0
for country in countries:
  count=count+1
  print(f"Country number {count} is {country.upper()}.")

#PART TWO - DICTIONARIES
#Question 1
tree={
  "name": "The Great Banyan",
  "species":"Banyan",
  "age":250,
  "location_name": "Kolkata",
  "latitude": 22.5608,
  "longitude": 88.2868 
}
print(f"Here is a dictionary of the tree {tree.items()}.")

#Question 2
print(tree["name"], "is a", tree["age"], "year old tree that is in", tree["location_name"],".")

#Question 3
NYC={
  "latitude": 40.7128,
  "longitude": 74.0059
}

if NYC["latitude"]>tree["latitude"]:
  print("The tree", tree["name"], "in", tree["location_name"], "is south of NYC.")
else:
  print("The tree", tree["name"], "in", tree["location_name"], "is north of NYC.")

#Question 4
age=input("How old are you? [Enter your answer in years]")
age=int(age)

if age>tree["age"]:
  diff=age-tree["age"]
  print("You are", diff, "years older than", tree["name"])
else:
  diff=tree["age"]-age
  print(tree["name"], "was", diff, "years old when you were born.")

#PART TWO - DICTIONARIES
#Question 1
moscow={
  "name":"Moscow",
  "latitude":55.7558, 
  "longitude":37.6173
}

tehran={
  "name":"Tehran",
  "latitude": 35.6892,
  "longitude":51.3890
}

falkland={
  "name":"Falkland Islands",
  "latitude":-51.7963,
  "longitude":-59.5236
}

seoul={
  "name":"Seoul",
  "latitude": 37.5665,
  "longitude": 126.9780
}

santiago={
  "name":"Santiago",
  "latitude": -33.4489,
  "longitude": -70.6693
}

list=[moscow,falkland,seoul,santiago]
print("The list of dictionaries is", list)

#Question 2
for l in list:
  if l["latitude"]>0:
   print(l["name"], "is above the equator.")
  else:
    print(l["name"], "is below the equator.")
  if l["name"]=="Falkland Islands":
    print("The Falkland Islands are a biogeographical part of the mild Antarctic zone.")

#Question 3
for l in list:
  if l["latitude"]>tree["latitude"]:
   print(l["name"], "is north of the", tree["name"], "located in", tree["location_name"])
  else:
    print(l["name"], "is south of the", tree["name"], "located in", tree["location_name"])