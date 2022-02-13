# A Simple Example
cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car == 'bmw':
        print(car.upper()) 
    else:
        print(car.title())

# Conditional Tests

# Checking for Equality
car = 'bmw'
car == 'bmw'


# Ignoring Case When Checking for Equality
car = 'Audi'
car == 'audi'

car = 'Audi'
car.lower() == 'audi'

# Checking for Inequality
car = 'Audi'
if car != 'bmw':
    print("its not bmw!")


# Numerical Comparisons
age = 18
age == 18

answer = 17
if answer != 42:
    print("That is not the correct answer. Please try again!")


age = 19
age < 21 
age <= 21 
age > 21 
age >= 21


# Checking Multiple Conditions
age_0 = 22
age_1 = 18
(age_0 >= 21) and (age_1 >= 21)


age_1 = 22
age_0 >= 21 and age_1 >= 21

# Using or to Check Multiple Conditions
age_0 = 22 
age_1 = 18
age_0 >= 21 or age_1 >= 21 
age_0 = 18
age_0 >= 21 or age_1 >= 21 


# Checking Whether a Value Is in a List

requested_toppings = ['mushrooms', 'onions', 'pineapple']
'mushrooms' in requested_toppings
'pepperoni' in requested_toppings

# Checking Whether a Value Is Not in a List
banned_users = ['andrew', 'carolina', 'david'] 
user = 'marie'
if user not in banned_users:
    print(f"{user.title()}, you can post a response if you wish.")


# Boolean Expressions
game_active = True 
can_edit = False

# Sample if Statements

# if conditional_test: 
#     do something

age = 19
if age >= 18:
    print("You are old enough to vote!")

age = 19
if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")


# if-else Statements
age = 17
if age >= 18:
    print("You are old enough to vote!") 
    print("Have you registered to vote yet?")
else:
    print("Sorry, you are too young to vote.")
    print("Please register to vote as soon as you turn 18!")


# The if-elif-else Chain
age = 12
if age < 4:
    print("Your admission cost is $0.")
elif age < 18:
    print("Your admission cost is $25.")
elif age < 18:
    print("Your admission cost is $25.")
else:
    print("Your admission cost is $40.")

age = 12
if age < 4:
    price = 0 
elif age < 18:
    price = 25
else:
    price = 40
print(f"Your admission cost is ${price}.")


# Omitting the else Block
age = 12
if age < 4: 
    price = 0
elif age < 18: 
    price = 25 
elif age < 65:
     price = 40
elif age >= 65: 
    price = 20

print(f"Your admission cost is ${price}.")