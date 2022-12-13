import math
def tree_height(baseline_distance, base_angle, top_angle):
  height = (baseline_distance * math.tan(top_angle)) - (baseline_distance * math.tan(base_angle))
  return height
baseline_distance = float(input("Enter the baseline distance (in meters): "))

base_angle = float(input("Enter the base angle (in degrees): "))

top_angle = float(input("Enter the top angle (in degrees): "))

height = tree_height(baseline_distance, base_angle, top_angle)

print("The height of the tree is: " + str(height) + " meters")
