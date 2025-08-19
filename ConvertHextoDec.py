# Converts a string hexadecimal number into an integer decimal
# If hexNum is not a valid hexadecimal number, returns None
# write a function to convert hexadecimal string (up to three character long) into decimal integer
# Do not use python function int(hexNum, 16) to convert this, write your own function
# hexNumbers dictionary is provided 

hexNumbers = {
    '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
    'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15
}

def hexToDec(hexNum):
    list = hexNum
    for i in hexNum:
        if i not in hexNumbers:
            return None
    if len(hexNum) > 3:
        return None
    else:
        if len(hexNum) == 3:
            result = hexNumbers[hexNum[0]] * 256 + hexNumbers[hexNum[1]] * 16 + hexNumbers[hexNum[2]] * 1
            return result
        elif len(hexNum) == 2:
            result = hexNumbers[hexNum[0]] * 16 + hexNumbers[hexNum[1]] * 1
            return result
        else:
            result = hexNumbers[hexNum[0]] * 1
            return result

#test cases working
print("CAB Converts into: ",hexToDec('CAB'))
print("ABC Converts into: ",hexToDec('ABC'))
print("A6G Converts into: ",hexToDec('A6G'))
print("A2 Converts into: ",hexToDec('A2'))
print("B Converts into: ",hexToDec('B'))
print("ZZTOP Converts into: ",hexToDec('ZZTOP'))