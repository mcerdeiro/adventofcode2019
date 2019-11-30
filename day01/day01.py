file = open("day01.dat", "r")
lines = file.readlines()
file.close()

for line in lines:
    line = line.rstrip()
    print("Line: " + line)
    for c in line:
        print("C: " + c)