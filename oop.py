#! /usr/bin/env python

""" Basic example for teaching people a few fundamentals about
 Object-Oriented Programming in Python - Shane Engelman"""

import json

class Animal:

    legs = 0

    def sleep(self):
        print "zzz"


    def count_legs(self):
        print "Alice has {} legs.".format(alice.number_of_legs)
        # Takes "alice" class and returns number of legs from that instance
        print "This one has {} legs.".format(self.number_of_legs)
        # Takes this class and returns number of legs from an instance


alice = Animal()
alice.number_of_legs = 4
#alice.count_legs()
fish = Animal()
fish.number_of_legs = 0
#fish.count_legs()

class Dog(Animal):

    def sleep(self):
        print "Dog is chasing its tail while it sleeps" # overwrite Animal sleep()

    def bark(self):
        print "woof"


spunky = Dog() # Instantiate a Dog Instance (inheriting Animal's attributes)
#spunky.bark() # Run bark method inside the spunky instance
spunky.number_of_legs = 3 # spunky is a 3-legged dog
#spunky.count_legs()
spunky.sleep()

class Human:

    hair_color = ""
    height = 0
    weight = 0
    name = ""
    age = 0
    language = "English" # We won't overwrite this in any inherited classes

    def __init__(self): # runs this code immediately no matter what
        print "Hello there"


    def walk(self):
        print "I am walking"


class Enemy:

    def __init__(self, x):
        self.energy = x # Set this instance's energy variable to x when called


    def get_energy(self):
        print self.energy


jason = Enemy(5)
sandy = Enemy(18)
jason.get_energy()
sandy.get_energy()

class Shane(Human):

    def print_stats(self):
        print "{} is {}, {} inches, {} lbs., speaks {} and has {} hair.".format(
        self.name, self.age, self.height, self.weight, self.language, self.hair_color)
         # language comes from the Human class


shane = Shane()
shane.hair_color = "black"
shane.height = 70
shane.weight = 15
shane.name = "Shane"
shane.age = 27
print "Human default language: ", Human.language
print "Inherited language from Human in shane instance: ", shane.language
shane.print_stats()

print json.dumps(vars(shane)) # Returns variables as a dict, then as JSON
# {'name': 'Shane', 'age': 27, 'weight': 150, 'hair_color': 'black',
# 'height': 70}
