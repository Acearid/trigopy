#imported math module
import math
#define the function distance_to_star
def distance_to_star(parallax_angle, baseline_distance):
  distance = (baseline_distance * math.sin(parallax_angle)) / parallax_angle  
  return distance
#ask user for the angle and distance using arcseconds and AU
parallax_angle = float(input("Enter the parallax angle of the star (in arcseconds): "))
baseline_distance = float(input("Enter the baseline distance (in AU): "))
#make use of the function defined with the inputs added to the function
distance = distance_to_star(parallax_angle, baseline_distance)
#print the answer as a string
print("The distance from the Earth to the star is: " + str(distance) + " parsecs")
