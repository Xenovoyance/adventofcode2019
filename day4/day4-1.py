#!/usr/local/bin/python3

input_min = 130254
# input_max = 678275

input_max = 678275

correct_passwords = []


def correct_length(input):
    if len(str(input)) == 6:
        return True


def correct_range(input):
    global input_max
    global input_min

    if (input >= input_min) and (input <= input_max):
        return True


def correct_amount_doubles(input):
    input = str(input)
    for i in range(0, len(input)-1):
        if input[i] == input[i+1]:
            return True


def correct_increasing_values(input):
    input = str(input)
    for i in range(0, len(input)-1):
        if (input[i] > input[i+1]):
            return False
    return True


for i in range(input_min, input_max):
    if correct_length(i) and correct_range(i) and correct_amount_doubles(i) and correct_increasing_values(i):
        correct_passwords.append(i)

print(len(correct_passwords))
