#!/usr/local/bin/python3

run_env = "prod"  # test or prod

if run_env == "test":
    input = "input-test.txt"
else:
    input = "input.txt"

totalFuel1 = 0
totalFuel2 = 0


def fuelneeded(startingFuel):
    return int((truncate((int(startingFuel)/3))-2))


def additionalfuelneeded(startingFuel):
    securityswitch = 0
    totalfuel = 0

    startingFuel = fuelneeded(startingFuel)

    while(startingFuel > 0):
        securityswitch += 1
        totalfuel += startingFuel
        startingFuel = fuelneeded(startingFuel)

        if securityswitch > 25:
            break
    return totalfuel


def truncate(n, decimals=0):
    multiplier = 10 ** decimals
    return int(n * multiplier) / multiplier


with open(input) as blockstream:
    for row in blockstream:
        newFuel = fuelneeded(row)
        totalFuel1 += newFuel
        totalFuel2 += newFuel + additionalfuelneeded(newFuel)

print("P1: Total fuel:", totalFuel1)
print("P2: Total fuel:", totalFuel2)
