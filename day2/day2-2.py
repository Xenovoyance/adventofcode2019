#!/usr/local/bin/python3

# input = "input-test.txt"
input = "input.txt"
position = 0

with open(input) as blockstream:
    for row in blockstream:
        itemized = row.split(",")
        position = 0

        for i in range(0, 100):
            for j in range(0, 100):
                itemized = row.split(",")
                position = 0
                itemized[1] = i
                itemized[2] = j
                while(position < len(itemized)):
                    if itemized[position] == "1":
                        itemized[int(itemized[position + 3])] = str(
                            int(itemized[int(itemized[position + 1])]) + int(itemized[int(itemized[position + 2])]))
                    elif itemized[position] == "2":
                        itemized[int(itemized[position + 3])] = str(int(itemized[int(itemized[position + 1])])
                                                                    * int(itemized[int(itemized[position + 2])]))
                    elif itemized[position] == "99":
                        break
                    position += 4
                if (itemized[0] == "19690720"):
                    print("Answer:", 100 * int(itemized[1]) + int(itemized[2]))
