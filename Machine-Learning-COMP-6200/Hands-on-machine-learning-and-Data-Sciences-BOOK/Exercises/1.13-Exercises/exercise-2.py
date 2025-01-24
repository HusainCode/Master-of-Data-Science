# Write a Python program that takes two numbers from the user and finds their power, that is, ( x^y ).

# This function does the math
def calculate_power(base, exponent):
  power = pow(round (base,exponent),2) 
  return power

# Map numbers to their Unicode characters
def convert_to_superscript(base, exponent):

    superscripts = {
        "0": "\u2070", "1": "\u00B9", "2": "\u00B2", "3": "\u00B3",
        "4": "\u2074", "5": "\u2075", "6": "\u2076", "7": "\u2077",
        "8": "\u2078", "9": "\u2079"
    }
    #
    exponent_str = ''.join(superscripts[digit] for digit in str(exponent))
    return str(base) + exponent_str

base = int(input("Enter a base number:"))
exponent  = int(input("Enter an exponent:"))

print( "The power of", convert_to_superscript(base, exponent), "is" , calculate_power(base, exponent))

# Sample of the output: 
Enter a base number:2
Enter an exponent:2
The power of 2² is 4
