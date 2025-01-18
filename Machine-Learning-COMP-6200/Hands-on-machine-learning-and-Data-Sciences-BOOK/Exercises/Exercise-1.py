# Write a Python program that takes an input as length in centimeters and converts it to meter and kilometer


"""
To convert:
Centimeters to Meters: Divide by 100.
meters = centimeters / 100

Centimeters to Kilometers: Divide by 100000.
kilometers = centimeters / 100000
"""

# converts centimeters to meters
def convert_to_meter(centimeter):
   meters = round(centimeter / 100, 2)
   return meters 
  
# converts kilometers to meters
def convert_to_kilometer(centimeter):
  kilometer = round(centimeter / 100000, 2)
  return kilometer 

centimeters = int(input(("Please enter length in centimeters:")))

print(centimeters, " centimeters are equivalent to ", convert_to_meter(centimeters), " meters")
print(centimeters, " centimeters are equivalent to ", convert_to_kilometer(centimeters), " kilometers")
