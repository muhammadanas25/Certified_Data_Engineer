# Defining a Function

def greet_user():
    """Display a simple greeting."""
    print("Hello!") 

greet_user()


# Passing Information to a Function

def greet_user(username):
    """Display a simple greeting with username.
    params: 
        username(string): a username to be printed
    """
    print(f"Hello, {username.title()}!") 

greet_user(username='awais')

# Arguments and Parameters

# The variable username in the definition of greet_user() is an example of a parameter, 
# a piece of information the function needs to do its job. The value 'jesse' in greet_user('jesse') is an example of an argument. An argument
# is a piece of information that’s passed from a function call to a function.

# note People sometimes speak of arguments and parameters interchangeably. 
# Don’t be surprised if you see the variables in a function definition referred to as arguments or the variables in a function call referred to as parameters.

# Passing Arguments

# Positional Arguments
def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet(
    pet_name='harry', 
    animal_type='hamster')


# Order Matters in Positional Arguments
describe_pet('harry', 'hamster')


# Keyword Arguments
describe_pet(animal_type='hamster', pet_name='harry')
describe_pet(pet_name='harry', animal_type='hamster')

# Default Values
def describe_pet(pet_name, animal_type='hamster'):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet(pet_name='willie', animal_type='dog')

# # Return Values

# Returning a Simple Value

def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)


# Making an Argument Optional
def get_formatted_name(first_name, middle_name, last_name): 
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {middle_name} {last_name}" 
    return full_name.title()

musician = get_formatted_name('john', 'lee', 'hooker') 
print(musician)


def get_formatted_name(first_name, last_name, middle_name=''):
    """Return a full name, neatly formatted."""
    # if middle_name:
    full_name = f"{first_name} {middle_name} {last_name}"
    # # else:
    #     full_name = f"{first_name} {last_name}"
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix') 
print(musician)
musician = get_formatted_name('john', 'hooker', 'lee') 
print(musician)


# Returning a Dictionary
def build_person(first_name, last_name):
    """Return a dictionary of information about a person."""
    person = {'first': first_name, 'last': last_name} 
    return person

musician = build_person('jimi', 'hendrix') 
print(musician)

# # Passing a List

def greet_users(names):
    """Print a simple greeting to each user in the list.""" 
    for name in names:
        msg = f"Hello, {name.title()}!" 
        print(msg)

usernames = ['hannah', 'ty', 'margot'] 
greet_users(usernames)


# Passing an Arbitrary Number of Arguments
def make_pizza(*toppings):
    """Print the list of toppings that have been requested.""" 
    print(toppings)

make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')



def make_pizza(*toppings):
    """Summarize the pizza we are about to make.""" 
    print("\nMaking a pizza with the following toppings:") 
    for topping in toppings:
        print(f"- {topping}")

make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')


# Mixing Positional and Arbitrary Arguments
def make_pizza(size, *toppings):
    """Summarize the pizza we are about to make."""
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings: 
        print(f"- {topping}")

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')


# Using Arbitrary Keyword Arguments

def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile(
    'albert', 'einstein', 
    location='princeton',field='physics'
)
print(user_profile)


def build_profile(**user_info):
    """Build a dictionary containing everything we know about a user."""
    # user_info['first_name'] = first
    # user_info['last_name'] = last
    return user_info

build_profile(location = 'paris', field = 'physics')
