
str='hi Jef'

# Get the character at a specific position
str[0]

# Get a substring from starting to ending index (exclusive)
str[0:2]

# Concatenate strings with +
"Data" + "Framed" # 'DataFramed'

# Repeat strings with *
3 * "data " # 'data data data '


# Split a string on a delimiter
"Jefrey".split("e") # ['J', '', 'fr', '', 'y']


str = "Jack and Jill"

# Convert a string to uppercase
str.upper() # 'JACK AND JILL'

# Convert a string to lowercase
str.lower() # 'jack and jill'

# Convert a string to title case
str.title() # 'Jack And Jill' 

# Replaces matches of a substring with another
str.replace("J", "P") # 'Pack and Pill'


# Find substring index 
print('find subtrings')
str = "Yes, let's go"
print(str.find('go'))   #11


# Reverse string
print('reverse string')
str_reversed = str[::-1]
print(str_reversed) 

