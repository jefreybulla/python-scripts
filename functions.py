def display_info(first_name, last_name):
    print('First Name:', first_name)
    print('Last Name:', last_name)

# keyword arguments: arguments are assigned based on the name of the arguments. For example,
display_info(last_name = 'Colliman', first_name = 'Will')


# function to sum any number of arguments
def add_all(*numbers):
    return sum(numbers)

# pass any number of arguments
print(add_all(1, 2, 3, 4))   


# function to print keyword arguments
def greet(**words):
    for key, value in words.items():
        print(f"{key}: {value}")

# pass any number of keyword arguments
greet(name="John", greeting="Hello")



# global variable
c = 1 

def add():

    # use of global keyword
    global c

    # increment c by 2
    c = c + 2 

    print(c)

add()

# Output: 3 