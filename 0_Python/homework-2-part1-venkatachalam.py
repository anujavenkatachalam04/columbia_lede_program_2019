#Anuja Venkatachalam
#2019-05-30
#Homework 2 - PART ONE
#Number of lines of code: 85

#PART ONE - LISTS
#Question 1
numbers=[22,90,0,-10,3,22,48]
print(f"This is the list of numbers {numbers}.")

#Question 2
print(f"The number of numbers in this list is {len(numbers)}.")

#Question 3
print(f"The fourth number in the list is {numbers[3]}.")

#Question 4
print(f"The sum of the second and fourth numbers is {sum([numbers[1], numbers[3]])}.")

#Question 5
numbers_sorted=sorted(numbers)
print(f"The second largest number in the list is {numbers[-2]}.")

#Question 6
print(f"The last number in the original unsorted list is {numbers[-1]}.")

#Question 7
print(f"The sum of all the numbers divided by 2 is {sum(numbers)/2}.")

#Question 8
import statistics
mean=statistics.mean(numbers)
median=statistics.median(numbers)

if mean>median:
      print(f"The mean {mean} is greater than the median {median}")
elif median>mean:
      print(f"The median{median} is greater than the mean {mean}")
else:
      print(f"The median and the mean are the same {median}")

#PART ONE - DICTIONARIES
#Question 1

movie={
  "title": "A Beautiful Mind",
  "year": 2001,
  "director": "Ron Howard"
}

print(f"My favorite movie is {movie['title']} which was released in {movie['year']}, and was directed by {movie['director']}.")

#Question 2
movie["budget"]=60000000
movie["revenue"]=313000000

print("The profit from the movie was", movie["revenue"] - movie["budget"])

#Question 3
if movie["budget"]>movie["revenue"]:
  print("That was a bad investment")
elif movie["revenue"]>(movie["budget"]*5):
  print("That was a great investment!")
else:
  print("That was an okay investment")

#Question 4
population_millions={
  "Manhattan":1.6,
  "Brooklyn":2.6,
  "Bronx":1.4,
  "Queens":2.3,
  "Staten Island":0.47
}

print(f"Here is a dictionary showing the population (in millions) of all the boroughs in NYC {population_millions.items()}.")

#Question 5
print("The population of Brooklyn is", population_millions["Brooklyn"], "million.")

#Question 6
print("The combined population of all five boroughs is", sum(population_millions.values()), "million.")

#Question 7
print(round((population_millions["Manhattan"]/sum(population_millions.values()))*100,2), "% of NYC's population lives in Manhattan.")