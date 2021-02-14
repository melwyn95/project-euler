lookup = {
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen",
    20: "twenty",
    30: "thirty",
    40: "forty",
    50: "fifty",
    60: "sixty",
    70: "seventy",
    80: "eighty",
    90: "ninety",
    100: "onehundred",
    200: "twohundred",
    300: "threehundred",
    400: "fourhundred",
    500: "fivehundred",
    600: "sixhundred",
    700: "sevenhundred",
    800: "eighthundred",
    900: "ninehundred",
    1000: "onethousand"
}

def to_words(n):
    if n == 0: return ""
    if n >= 1 and n <= 20: return lookup[n]
    elif n > 20 and n <= 99: return lookup[(n//10)*10] + to_words(n%10)
    elif n >= 100 and n <= 999:
        x, y = lookup[(n//100)*100], to_words(n%100)
        return x + "and" + y if len(y) > 0 else x
    elif n == 1000: return lookup[n]

N = 1000

print(sum([len(to_words(i)) for i in range(1, N + 1)]))
