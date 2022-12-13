import math

def distance_to_star(parallax_angle, baseline_distance):
  distance = (baseline_distance * math.sin(parallax_angle)) / parallax_angle  
  return distance
parallax_angle = float(input("Enter the parallax angle of the star (in arcseconds): "))
baseline_distance = float(input("Enter the baseline distance (in AU): "))
distance = distance_to_star(parallax_angle, baseline_distance)
print("The distance from the Earth to the star is: " + str(distance) + " parsecs")
