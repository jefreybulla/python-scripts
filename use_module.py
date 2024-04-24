# Option 1 to import the module
#import module_addition

# Option 2 to import the module
#import module_addition as addition

# Option 3 to import the module
from module_addition import add

# Option 1 to use the module
#r = module_addition.add(4,5) # returns 9

# Option 2 to use the module
#r = addition.add(5,7) # returns 12

# Option 3 to use the module
r = add(2,3) # returns 5

print(r)