import binascii

def toHex(dec):
    x = (dec % 16)
    digits = "0123456789ABCDEF"
    rest = dec / 16
    if (rest == 0):
        return digits[x]
    return toHex(rest) + digits[x]

numbers = range(0,256)
numbers = [hex(x) for x in numbers]

for number in numbers:
	prefix, number = number.split("x")
	if number == "0": number = "00"
	if number == "1": number = "01"
	if number == "2": number = "02"
	if number == "3": number = "03"
	if number == "4": number = "04"
	if number == "5": number = "05"
	if number == "6": number = "06"
	if number == "7": number = "07"
	if number == "8": number = "08"
	if number == "9": number = "09"
	if number == "a": number = "0a"
	if number == "b": number = "0b"
	if number == "c": number = "0c"
	if number == "d": number = "0d"
	if number == "e": number = "0e"
	if number == "f": number = "0f"

	#hex_value.append(number)

	print (number)

