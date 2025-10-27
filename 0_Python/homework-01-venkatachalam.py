#Anuja Venkatachalam
#2019-05-28
#Homework 1
#Number of lines of code: 108

#Question 1
yob=input("Which year were you born in? [Enter in YYYY format]")
yob=int(yob)

while yob>2019:
      print("Try again")
      yob=input("Which year were you born in? [Enter in YYYY format]")
      yob=int(yob)

age=2019-yob
print(f"You are around {age} years old.")

#The following questions entail calculating the number of minutes that a person has lived based on their age.
#As this is a repeated operation, I am creating a function that sets up the multiplication of days, hours and minutes.
def calculate(t):
      return(t*age*365*24*60)

#Question 3
print(f"The human heart beats at an average of 80 times per minute. Your heart has beaten approximately {calculate(80):,} times.")

#Question 4
print(f"In comparison, a blue whale's heart beats an average of 9 times per minute. If you were a blue whale, your heart would have beaten {calculate(9):,} times.")

#Question 5
print(f"Now, did you know that a rabbit's heart beats an average of 135 times per minute? If you were a rabbit, your heart would have beaten real fast - {calculate(135):,} times!")

#Question 6
if len(str(calculate(135)))>6:
      print (f"That is - {calculate(135)/1000000:,} million times.")

#Question 7
print(f"Now, I'm going to tell you how old you are in different planets!")
print(f"Venus..")
print(f"You would be {round((age*0.6152),2)} years on the planet Venus!")

#Question 8
print(f"Neptune..")
print(f"You would be {round((age/165),2)} years on the planet Neptune!")

#Question 9
myage=2019-1990
if age>myage:
      str="older than me"
elif age<myage:
      str="younger than me"
elif age==myage:
      str="the same age as me"

print(f"You are {str}.")

#Question 10
if str=="older than me":
      print(f"You are older than me by approximately {age-myage} years.")
if str=="younger than me":
      print(f"You are younger than me by approximately {abs(age-myage)} years.")

#Question 11
if age%2==0:
      print("You were born in an even year!")
else:
      print("You were born in an odd year!")

#Question 12
if yob<1935:
  print("The end!")
else:
  print("Now, I'll tell you which US President was in office the year you were born! You might see two Presidents if there was a change in government the same year.")

#Creating a function that will keep standard text

  def lookup(name):
      print(f"The President elect was {name}.")

  if yob in range(1935,1946):
      lookup("FD Roosevelt")
  if yob in range(1945,1954):
      lookup("HS Truman")
  if yob in range(1953,1962):
      lookup("DD Eisenhower")
  if yob in range(1961,1964):
      lookup("JF Kennedy")
  if yob in range(1963,1970):
      lookup("LB Johnson")
  if yob in range(1969,1975):
      lookup("RM Nixon")
  if yob in range(1974,1978):
      lookup("GR Ford")
  if yob in range(1977,1982):
      lookup("Jimmy Carter")
  if yob in range(1981,1990):
      lookup("Ronald Reagan")
  if yob in range(1989,1994):
      lookup("George Bush")
  if yob in range(1993,2002):
      lookup("Bill Clinton")
  if yob in range(2001,2010):
      lookup("George W Bush")
  if yob in range(2009,2018):
      lookup("Barack Obama")
  if yob in range(2017,2020):
      lookup("Trump")

  print("The end!")