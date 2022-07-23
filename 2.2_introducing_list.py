bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)

names = ['string', 1, True, 1.0, ['list', 'one']]

# Accessing Elements in a List
print(bicycles[0])
print(names[0])

print("title",bicycles[0].title())

# Using Individual Values from a List
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
message = f"My first bicycle was a {bicycles[0].title()}."
print(message)


names = ['awais', 'usama', 'waqar']
for name in names:
    pass

name = 'awais'

print(f'hello {name}!')

# Try these short programs to get some firsthand experience with Python’s lists. You might want to create a 

# 3-1. Names: Store the names of a few of your friends in a list called names. 
# Print each person’s name by accessing each element in the list, one at a time.

# 3-2. Greetings: Start with the list you used in Exercise 3-1, but instead of just printing each person’s name, 
# print a message to them. The text of each message should be the same, but each message should be personalized with the person’s name.

# 3-3. Your Own List: Think of your favorite mode of transportation, such as a motorcycle or a car, 
# and make a list that stores several examples. Use your list to print a series of statements about these items, such as “I would like to own a Honda motorcycle.”

# Changing, Adding, and Removing Elements

motorcycles = ['honda', 'yamaha', 'suzuki'] 
print(motorcycles)
motorcycles[0] = 'ducati' 
print(motorcycles)

# Adding Elements to a List
motorcycles = ['honda', 'yamaha', 'suzuki'] 
print(motorcycles)

motorcycles.append('ducati')
print(motorcycles)


# Inserting Elements into a List
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.insert(0, 'ducati') 

print(motorcycles)

# Removing Elements from a List
# Removing an Item Using the del Statement
motorcycles = ['honda', 'yamaha', 'suzuki'] 
print(motorcycles)
del motorcycles[0] 
print(motorcycles)


motorcycles = ['honda', 'yamaha', 'suzuki'] 
print(motorcycles)
del motorcycles[1]
print(motorcycles)

# Removing an Item Using the pop() Method
motorcycles = ['honda', 'yamaha', 'suzuki'] 
print(motorcycles)
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

# Removing an Item Using the pop() with index Method
motorcycles = ['honda', 'yamaha', 'suzuki'] 
print(motorcycles)
popped_motorcycle = motorcycles.pop(0)
print(motorcycles)
print(popped_motorcycle)

# Removing an Item by Value
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati'] 
print(motorcycles)
motorcycles.remove('ducati')


# Sorting a List Permanently with the sort() Method

cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)

cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort(reverse=True) 
print(cars)

# Sorting a List Temporarily with the sorted() Function
cars = ['bmw', 'audi', 'toyota', 'subaru']
print("Here is the original list:") 
print(cars)
print("\nHere is the sorted list:") 
print(sorted(cars))
print("\nHere is the original list again:") 
print(cars)

# Printing a List in Reverse Order
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
cars.reverse() 
print(cars)

print(cars)
'\n'.join(cars)


for i in range(1, len(cars), 2):
    print(i, len(cars[i]))

