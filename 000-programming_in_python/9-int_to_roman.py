# NASR TECH ARDHI UNIVERSITY
# BSc. Computer System AND  network
# 2024

def int_to_roman(n):
    # List of Roman numerals and their corresponding values
    val = [
        1000, 900, 500, 400,
        100, 90, 50, 40,
        10, 9, 5, 4,
        1
    ]
    syb = [
        "M", "CM", "D", "CD",
        "C", "XC", "L", "XL",
        "X", "IX", "V", "IV",
        "I"
    ]
    
    # Initialize the result string
    roman_num = ''
    
    # Iterate through the values and symbols, constructing the Roman numeral
    for i in range(len(val)):
        while n >= val[i]:
            roman_num += syb[i]
            n -= val[i]
    
    return roman_num

# test function
if __name__ == "__main__":
    number = int(input("Enter an integer to convert to Roman numeral: "))
    print("Roman numeral:", int_to_roman(number))

