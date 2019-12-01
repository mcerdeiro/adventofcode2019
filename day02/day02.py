#!/usr/bin/python3

file = open("day02.dat", "r")
lines = file.read().splitlines()
file.close()

result = 0
for line in lines:
    print("Line: " + line)
    result = line

print("part01: " +  str(line))
