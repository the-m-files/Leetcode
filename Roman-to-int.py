#the biggest roman numeral symbol is M(1000)

#simple way to decode: find the biggest symbol and split the string into two peices
#from left to right.

#subtract everything from left
s = "MCMXCIV"
numerals = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
numbers = [numerals.get(char) for char in tuple(s)]
print(numbers)
total = 0
for number in numbers:
    if total >= number:
        total += number
    else:
        total-=number
print(total)