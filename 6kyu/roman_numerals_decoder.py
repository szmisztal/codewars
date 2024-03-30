"""Create a function that takes a Roman numeral as its argument and returns its value as a numeric decimal integer. You don't need to validate the form of the Roman numeral.

Modern Roman numerals are written by expressing each decimal digit of the number to be encoded separately, starting with the leftmost digit and skipping any 0s. So 1990 is rendered "MCMXC" (1000 = M, 900 = CM, 90 = XC) and 2008 is rendered "MMVIII" (2000 = MM, 8 = VIII). The Roman numeral for 1666, "MDCLXVI", uses each letter in descending order.

Example:
"MM"      -> 2000
"MDCLXVI" -> 1666
"M"       -> 1000
"CD"      ->  400
"XC"      ->   90
"XL"      ->   40
"I"       ->    1
Help:
Symbol    Value
I          1
V          5
X          10
L          50
C          100
D          500
M          1,000"""


def solution(roman):
    result = 0
    decode_dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    decoded_roman = [decode_dict.get(i) for i in roman]
    i = 0
    while i < len(decoded_roman):
        if i + 1 < len(decoded_roman) and decoded_roman[i] < decoded_roman[i + 1]:
            result += decoded_roman[i + 1] - decoded_roman[i]
            i += 2
        else:
            result += decoded_roman[i]
            i += 1
    return result
