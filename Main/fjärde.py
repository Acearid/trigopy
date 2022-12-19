import math
# define variables from user input. We get the measurements of the peaks and distance from the person. Peak1 is the peak closet and Peak2 is the further peak. 
peak1_height = float(input("Enter the height of the first peak in meters: "))
peak1_distance = float(input("Enter the distance of the first peak from you in meters: "))
peak2_height = float(input("Enter the height of the second peak in meters: "))
peak2_distance = float(input("Enter the distance of the second peak from you meters: "))
# angle = arctan((h2-h1) / (d2-d1))
tan_angle = (peak1_height - peak2_height) / (peak1_distance - peak2_distance)
print(tan_angle)
# calculate the angle
angle = math.degrees(math.atan(tan_angle))
#  If the angle is less than 0 degrees, then the second peak isn't visible; if it's greater than 0 degrees, then the second peak is visible.
if angle <= 0:
        print("The second peak is not visible.")
else:
        print("The second peak is visible.")       