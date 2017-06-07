#008 is run by commenting some lines

# print(dir()) #dir() is short for directory.  Displays of available objects.  We focus on '__builtins__' which is a module of common objects always available.
# print(dir('__builtins')) #contains functions and types ready for use
# print(help(pow)) #to learn one of these functions and objects, type print(help(*objectname*)); for example, we learn the power function pow() or x**y
# print(help(hex))
#PRESS LEFT CTRL + Z to exit, at least in Ubuntu

print(help("modules")) #gathers list of available modules
import math
print(dir(math)) #displays of available objects in the math module common objects always available
print(help(math.radians))