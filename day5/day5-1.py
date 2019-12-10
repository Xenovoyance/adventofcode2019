#!/usr/local/bin/python3

#input_data = "input-test.txt"
input_data = "input.txt"
position = 0

with open(input_data) as blockstream:
    for row in blockstream:
        itemized = row.split(",")
        position = 0
        while(position <= len(itemized)):
            if (len(itemized[position]) > 2):
                opcode = int(str(itemized[position])[-2:])
                parameters = str(itemized[position])[:-2]
                while(len(parameters) < 3):
                    parameters = "0" + parameters
            else:
                opcode = int(itemized[position])
                parameters = "000"
            if opcode == 1:
                if parameters[2] == "0":
                    parameter_one = int(itemized[int(itemized[position + 1])])
                else:
                    parameter_one = int(itemized[position + 1])
                if parameters[1] == "0":
                    parameter_two = int(itemized[int(itemized[position + 2])])
                else:
                    parameter_two = int(itemized[position + 2])
                if parameters[0] == "0":
                    itemized[int(itemized[position + 3])] = str(parameter_one + parameter_two)
                else:
                    itemized[position + 3] = str(parameter_one + parameter_two)
                position += 4
            elif opcode == 2:
                if parameters[2] == "0":
                    parameter_one = int(itemized[int(itemized[position + 1])])
                else:
                    parameter_one = int(itemized[position + 1])
                if parameters[1] == "0":
                    parameter_two = int(itemized[int(itemized[position + 2])])
                else:
                    parameter_two = int(itemized[position + 2])
                if parameters[0] == "0":
                    itemized[int(itemized[position + 3])
                             ] = str(parameter_one * parameter_two)
                else:
                    itemized[position + 3] = str(parameter_one * parameter_two)
                position += 4
            elif opcode == 3:
                parameter_input = input(">")
                itemized[int(itemized[position + 1])] = int(parameter_input)
                position += 2
            elif opcode == 4:
                print(str(itemized[int(itemized[position + 1])]))
                position += 2
            elif opcode == 5:
                # Opcode 5 is jump-if-true: if the first parameter is non-zero, it sets the instruction pointer to the value from the second parameter. Otherwise, it does nothing.
                if parameters[2] == "0":
                    if itemized[int(itemized[position + 1])] != "0":
                        position = int(itemized[int(itemized[position + 2])])
                    else:
                        position += 3
                else:
                    if itemized[position + 1] != "0":
                        position = int(itemized[position + 2])
                    else:
                        position += 3
            elif opcode == 99:
                break
            else:
                break
