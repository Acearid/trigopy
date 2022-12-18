import math

def calculate_distance(distance1, distance2, dec1, dec2 , RA1, RA2):
  # Convert declination and right ascension to radians
  dec1 = math.radians(dec1)
  dec2  = math.radians(dec2 )
  RA1 = math.radians(RA1)
  RA2 = math.radians(RA2)

  # Calculate angular separation
  angular_separation = math.acos(math.sin(dec1) * math.sin(dec2 ) + math.cos(dec1) * math.cos(dec2 ) * math.cos(RA1 - RA2))

  # Convert angular separation to linear distance
  distance = distance1 * distance2 * math.sin(angular_separation / 2) / math.sin(angular_separation)

  return distance

# Test the function with some sample inputs
distance1 = 860 # distance from Earth to star 1, in light years
distance2 = 643 # distance from Earth to star 2, in light years
declination1 = 5.242 # declination of star 1, in degrees
declination2 = 5.919 # declination of star 2, in degrees
right_ascension1 = -8.202 # right ascension of star 1, in hours
right_ascension2 = 7.407 # right ascension of star 2, in hours

distance = calculate_distance(distance1, distance2, declination1, declination2, right_ascension1, right_ascension2)

print(f"The distance between the two stars is {distance:.2f} light years.")
