import math

#define a function to calculate the distance from the Earth to a star
def distance_to_star(parallax_angle, baseline_distance):
  #calculate the distance using the formula:
  #distance = (baseline_distance * sin(parallax_angle)) / parallax_angle
  distance = (baseline_distance * math.sin(parallax_angle)) / parallax_angle
  
  #return the calculated distance
  return distance

#ask the user to input the parallax angle of the star
parallax_angle = float(input("Enter the parallax angle of the star (in arcseconds): "))

#ask the user to input the baseline distance
baseline_distance = float(input("Enter the baseline distance (in AU): "))

#calculate the distance from the Earth to the star
distance = distance_to_star(parallax_angle, baseline_distance)

#print the distance from the Earth to the star
print("The distance from the Earth to the star is: " + str(distance) + " parsecs")
