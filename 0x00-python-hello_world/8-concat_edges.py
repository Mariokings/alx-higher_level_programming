#!/usr/bin/python3
str = "Python is an interpreted, interactive, object-oriented programming\
 language that combines remarkable power with very clear syntax"
str = str[str.find("ob"):str.find("g")+8]+str[str.rfind(" w"):str.rfind("h")+1]+" "+str[str.find("P"):str.find("n")+1]
print(str)
