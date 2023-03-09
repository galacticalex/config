
# pythonCheatSheet.py
#
# SPDX-FileCopyrightText: 2023 Alexander Murphy <supernova@alexmurphy.uk>
#
# SPDX-License-Identifier: Apache-2.0
#
# Reviewing some Python, collection of less-obvious language syntax.


############################
# Primitives and operators #
############################


"""
multiline strings
are
ignored
like
comments
"""


# Integer division rounds DOWN (both +-)
5 // 3      # -> 1
-5 // 3     # -> -2
5.0 // 3    # -> 1      same result on floats


10 / 3      # -> 3.3333... division always returns a float


8 % 3       # -> 2


2**3        # -> 8      exponentiation


# Bools must have capitals
True
False
not True
not False   # not "!"


True and False      # -> False
False or True       # -> True


# True and False are actually 1 and 0!
True * 8        # -> 8
False + 3       # -> 3


bool(None)      # -> False
bool(0)         # -> False
bool("")        # -> False
bool([])        # -> False
bool({})        # -> False
bool(())        # -> False
bool(set())     # -> False
# Everything else is True


2 < 3 < 5       # -> True
2 < 1 < 3       # -> False


# Test equality with 'is' and ==
# is checks that variables refer to the same object
# == checks that objects pointed to have the same value
a = [1, 2, 3, 4]
b = a
b is a      # -> True
c = [1, 2, 3, 4]
c is b      # -> False
a == b == c # -> True!


# Concatenate strings with +
"Hello" + " " + "world!"    # -> "Hello world!"


# Strings act like lists of characters
"Hello there!"[2]       # -> 'l'


len("onetwothree")      # -> 11


# The following is an f-string:
name = "Reiker"
f"The name's {name}"    # -> "The name's Reiker"
f"My name, {name}, has {len(name)} characters."  # Any valid Python expression can go in f-string curly braces!!


#############################
# Variables and collections #
#############################


variable_name_convention = True
NotTypicallyFOUND = False


# if is a valid expression
"awesome" if 1 < 0 else "not so great"  # -> 'not so great'


l = []
l.append(1)
l.append(2)
l.append(3)
l.pop()
l[1]        # -> 2
l[-1]       # -> 2  "last element"


l2 = ['a', 'b', 'c', 'd', 'e']
l2[2:4]     # -> ['c', 'c']
l2[2:]      # -> ['c', 'd', 'e']
l2[::2]     # -> ['a', 'c', 'e']
l2[::-1]    # -> ['e', 'd', 'c', 'b', 'a']


l3 = l      # "Shallow" copy
l3 is l     # -> True
l3 == l     # -> True
l4 = l[:]   # "Deep" copy
l4 is l     # -> False
l4 == l     # -> True


# Remove arbitrarily indexed element of a list with "del"
li = ['a', 'b', 'c', 'd', 'e']
del li[2]
li          # -> ['a', 'b', 'd', 'e']


# and first occurence of a value with .remove()
li.remove('b')
li          # -> ['a', 'd', 'e']


# Insert element X at index Y with
X = 'A'
Y = 0
li.insert(Y, X)
li          # -> ['A', 'a', 'd', 'e']


# Index of first match in list for value V
V = 'e'
li.index(V) # -> 3


# Concatenate lists eith .extend()
l1 = [1, 2]
l2 = [3, 4]
l1.extend(l2)
l1          # -> [1, 2, 3, 4]


# Check for presence with in
1 in l1     # -> True
"B" in l1   # -> False


# Tuples are like lists but immutable
t = ("a", "b", "c")
t[1]        # -> 'b'
t[1] = "d"  # -> TypeError


# Beware!
type((1))       # -> <class 'int'>
type((1,))      # -> <class 'tuple'>
type(())        # -> <class 'tuple'>
type((1, 2))    # -> <class 'tuple'>


# You can do non-mutable list operations on tuples


# Unpack lists/tuples into variables
a, b, c = (1, 2, 3)
a       # -> 1
b       # -> 2
c       # -> 3


# Dictionaries map keys to heterogenous values,
d = { "First": 1, "Second": 2, "Etc": "..." }


# Search for key X with brackets
d["First"]      # -> 1


list(d.keys())      # -> ['First', 'Second', 'Etc']
list(d.values())    # -> [1, 2, '...']


# Check keys with in
'First' in d        # ->  True


# Non-existant key throws KeyError, avoid with .get()
d.get("not here")           # -> None
d.get("not here", "aww..")  # -> "aww.."


# Delete via key with del
del d["Etc"]


# Two ways to add with different behaviour:
d.setdefault("Last", 99)    # -> 99
d.setdefault("Last", 100)   # -> 99
d                           # -> {'First': 1, 'Second': 2, 'Last': 99}


d.update({"Last": 100})     # -> None  ... but ...
d                           # -> {'First': 1, 'Second': 2, 'Last': 100}


# Sets have unique heterogeneous values
s = set({1, 1, "a"})
s       # -> {1, 'a'}


s.add(3)
s       # -> {1, 3, 'a'}


s2 = set({1, 'b', 5})
s & s2  # -> {1}
s | s2  # -> {1, 3, 5, 'b', 'a'}


5 in s      # -> False
5 in s2     # -> True
5 in s | s2 # -> True


################
# Control flow #
################


# Checkout indentation (4 spaces are OK too)
if 5 < 3:
    False
elif 5 is 3:
    False
else:
    True


# Basic for loop (notice var *in* *iterable*)
for animal in ["dog", "cat", "mouse"]:
    print(f"A {animal} is an animal.")


# Produce sequence of numbers with range()
range(2, 8, 2)      # -> range(2, 8, 2)
range(2, 8, 2)[1]   # -> 4      range() is lazy!
list(range(1, 3))   # -> [1, 2] inclusive/exclusive bounds


# range() implements the Iterable interface, a fundamental Pythonic abstraction
# But an Iterator is a special type of Iterable
an_iterator = iter(range(1,3))
next(an_iterator)   # -> 1
next(an_iterator)   # -> 2 the Iterator has a memory!
next(an_iterator)   # -> StopIteration exception, so you can do other stuff


# Use enumerate() to iterate over both index and value of a list
cars = ["red", "blue", "yellow"]
for i, car in enumerate(cars):
    print(f"Car {i} is {car}.")


i = 0
while i < 5:
    print(i**2)
    i += 1


try:
    raise IndexError("This is an index error!")
except IndexError as e:
    print("It's ok") # this is run because we caught it
else:
    print("No exceptions")
finally:
    print("Always run")


# Write to files with 'with' and file()
with open("myfile1.txt", "w+") as file:
    file.write("here's some text") # note that this will overwrite the file


# Read the same way
with open("myfile1.txt") as f:
    print(f.read())


# Or with a loop
with open("myfile1.txt") as f:
    for line in f:
        print(line)


# JSON library is handy for files
import json
contents = {"a": 12, "b": 34}
with open("myfile1.txt", "w+") as file: # note the w+ here!
    file.write(json.dumps(contents))


# Deleting a file requires os
import os
os.remove("myfile1.txt")






