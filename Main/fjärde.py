import math
peak1_height = float(input("Enter the height of the first peak: "))
peak1_distance = float(input("Enter the distance of the first peak from you: "))
peak2_height = float(input("Enter the height of the second peak: "))
peak2_distance = float(input("Enter the distance of the second peak from you: "))
tan_angle = (peak1_height - peak2_height) / (peak1_distance - peak2_distance)
angle = math.degrees(math.atan(tan_angle))
if angle <= 0:
        print("The second peak is not visible.")
else:
        print("The second peak is visible.")
        