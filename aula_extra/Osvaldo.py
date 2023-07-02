#a table of people names, weights and heights
people = [("John", 1.757, 64.5), ("Mary", 1.65, 55.5), ("Peter", 1.8, 80.5), ("Jane", 1.6, 45.5)]
#List comprehensions can easily describe a mix of map and filter operations
#create a list of squares of odd numbers in list:
[ x**2 for x in people if x%2==1]



#filter the list of people to get only those with weight > 75kg
[ (name, weight) for (name, height, weight) in people if weight > 75]

#filter the list of people to get only those with height > 1.7m
[ (name, height) for (name, height, weight) in people if height > 1.7]

#filter the list of people to get only those with height > 1.7m and weight > 75kg
[ (name, height, weight) for (name, height, weight) in people if height > 1.7 and weight > 75]

#filter the list of people to get only those with height > 1.7m or weight > 75kg
[ (name, height, weight) for (name, height, weight) in people if height > 1.7 or weight > 75]

