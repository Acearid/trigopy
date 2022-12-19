import math
def calculate_distance(dec1, dec2 , RA1, RA2):
  delta_RA = RA2 - RA1
    
 # Calculate the angular separation
  angular_separation = math.sqrt((delta_RA * math.cos(dec2))**2 + (dec1 - dec2)**2)

  print(angular_separation)


# Get input from the user
dec1 = float(input("Enter the declination of star 1, in degrees: "))
dev2 = float(input("Enter the declination of star 2, in degrees: "))
RA1 = float(input("Enter the right ascension of star 1, in hours: "))
RA2 = float(input("Enter the right ascension of star 2, in hours: "))

