def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
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
    for i in range(len(roman_string)):
        # If the current value is less than the next value, subtract it
        if i + 1 < len(roman_string) and roman_dict[roman_string[i]] < roman_dict[roman_string[i + 1]]:
            result -= roman_dict[roman_string[i]]
        else:
            result += roman_dict[roman_string[i]]
    
    return result
