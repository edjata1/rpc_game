# modules: small code libraries based on related features

import kansas
from rps7 import rock_paper_scissors
# math module library
import math

# other libraries
import sys


# pull out what's needed from libray
from enum import Enum
from math import pi

# give nick name
import random as rdm

print(pi)
print(math.sqrt(16))
print(math.log(9))
print(math.cos)

# exit program
# sys.exit()

# random choice from string
pick = rdm.choice("12356")
print(pick)


# print what's in modules
print(dir(rdm))
print()

# loop through dir
for item in dir(rdm):
    print(item)

print("--------- import created module ---------")
# python.org ->> Python Module Index list of all modules
print(kansas.capital)
kansas.randomfunfact()

# names of modules
print(__name__) # main file being run 
print(kansas.__name__) # file being imported

rock_paper_scissors()




