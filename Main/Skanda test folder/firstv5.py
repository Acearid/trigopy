import math
def calculate_distance(distance1, distance2, dec1, dec2 , RA1, RA2):
  delta_RA = RA2 - RA1
    
 # Calculate the angular separation
  angular_separation = math.sqrt((delta_RA * math.cos(dec2))**2 + (dec1 - dec2)**2)

  print(angular_separation)

  # Convert angular separation to linear distance
  distance = distance1 * distance2 * math.sin(angular_separation / 2) / math.sin(angular_separation)

  return distance

# Get input from the user
distance1 = float(input("Enter the distance from Earth to star 1, in light years: "))
distance2 = float(input("Enter the distance from Earth to star 2, in light years: "))
dec1 = float(input("Enter the declination of star 1, in degrees: "))
dev2 = float(input("Enter the declination of star 2, in degrees: "))
RA1 = float(input("Enter the right ascension of star 1, in hours: "))
RA2 = float(input("Enter the right ascension of star 2, in hours: "))

distance = calculate_distance(distance1, distance2, dec1, dev2, RA1, RA2)

print(f"The distance between the two stars is {distance:.2f} light years.")
