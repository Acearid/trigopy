#Imported the module math
import math
#Make a function named tree_height
def tree_height(baseline_distance, base_angle, top_angle):
  height = (baseline_distance * math.sin(base_angle)) / (math.sin(top_angle))
  return height
#Get the imput for the distanse from you and the tree, the bottom angel and the top angel of the tree
baseline_distance = float(input("Enter the baseline distance (in meters): "))

base_angle = float(input("Enter the base angle (in degrees): "))

top_angle = float(input("Enter the top angle (in degrees): "))
#Use the function with the inputs
height = tree_height(baseline_distance, base_angle, top_angle)
#Print the answer as a string
print("The height of the tree is: " + str(height) + " meters")
