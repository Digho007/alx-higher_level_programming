#!/usr/bin/python

for i in reversed(range(26)):
    if i % 2 == 0:
        val = 65 + i
    else:
        val = 97 + i
    print("{:c}".format(val) end="")
