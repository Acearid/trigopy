import math
# define variables from user input. We get the measurements of d1 and d2 and h1 and h2, 1 being the ones closer and 2 the furthr peak.
peak1_height = float(input("Enter the height of the first peak in meters: "))
peak1_distance = float(input("Enter the distance of the first peak from you in meters: "))
peak2_height = float(input("Enter the height of the second peak in meters: "))
peak2_distance = float(input("Enter the distance of the second peak from you meters: "))
# angle = arctan((h2-h1) / (d2-d1))
tan_angle = (peak1_height - peak2_height) / (peak1_distance - peak2_distance)
# converting radians to degrees
angle = math.degrees(math.atan(tan_angle))
#  If the angle is less than 0 degrees, then the second peak isn't visible; if it's greater than 0 degrees, then the second peak is visible.
if angle <= 0:
        print("The second peak is not visible.")
else:
        print("The second peak is visible.")
        