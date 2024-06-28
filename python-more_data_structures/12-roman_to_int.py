#!/usr/bin/python3
def roman_to_int(roman_string):
    num = roman_string
    if not isinstance(num, str) or num is None:
        return 0

    # Dictionary to map Roman numerals to integers
    roman_dict = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    # Initialize the integer result
    result = 0

    # Iterate over the Roman numeral string
    for i in range(len(num)):
        # If the current value is less than the next value, subtract it
        if i + 1 < len(num) and roman_dict[num[i]] < roman_dict[num[i + 1]]:
            result -= roman_dict[num[i]]
        else:
            result += roman_dict[num[i]]

    return result
