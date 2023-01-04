#!/usr/bin/python3

def fizzbuzz():
    for i in range (1, 101):
        print (i, end=" ")
        if i % 3 == 0:
            print ("Fizz", end=" ")
        if i % 5 == 0:
            print ("Buzz", end=" ")
        elif i % 15 == 0:
            print ("FizzBuzz", end=" ")
