#!/usr/local/bin/python3

# input = "input-test.txt"
input = "input.txt"
totalFuel1 = 0
totalFuel2 = 0


def fuelneeded(startingFuel):
    return int(int(startingFuel)/3)-2


def additionalfuelneeded(startingFuel):
    totalfuel = 0
    startingFuel = fuelneeded(startingFuel)

    while(startingFuel > 0):
        totalfuel += startingFuel
        startingFuel = fuelneeded(startingFuel)
    return totalfuel


with open(input) as blockstream:
    for row in blockstream:
        newFuel = fuelneeded(row)
        totalFuel1 += newFuel
        totalFuel2 += newFuel + additionalfuelneeded(newFuel)

print("P1:", totalFuel1, "P2:", totalFuel2)
