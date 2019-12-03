#!/usr/local/bin/python3

#input = "input-test.txt"
input = "input.txt"
position = 0

with open(input) as blockstream:
    for row in blockstream:
        itemized = row.split(",")
        # print(itemized)
        while(position < len(itemized)):
            # print(itemized)
            # for i in range(0, len(itemized)):
            if itemized[position] == "1":
                itemized[int(itemized[position+3])] = str(int(itemized[int(itemized[position+1])]) +
                                                          int(itemized[int(itemized[position+2])]))
            elif itemized[position] == "2":
                itemized[int(itemized[position+3])] = str(int(itemized[int(itemized[position+1])]) *
                                                          int(itemized[int(itemized[position+2])]))
            elif itemized[position] == "99":
                break
            position += 4

print(itemized)
