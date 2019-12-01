#!/usr/bin/python3

def fuel(fuelm): 
    fuelt = 0   
    fuel = int(int(fuelm) / 3) - 2
    while(fuel > 0):
        print("Mass: " + str(fuelm) + " Requires: " + str(fuel))
        fuelt += fuel
        fuelm = fuel
        fuel = int(int(fuelm) / 3) - 2
        print("New "+ str(acount))
    
    return fuelt

file = open("day01.dat", "r")
lines = file.read().splitlines()
file.close()

acount = 0
bcount = 0
array = []
for line in lines:
    val = int(int(line) / 3) - 2
    print("Line: " + line + "- Val: " + str(val))
    acount = acount + val
    #print("Input: "+ str(val) + " Fuel: " + str(fuel(val)))
    acount += fuel(val)

print("part02: " +  str(acount))
