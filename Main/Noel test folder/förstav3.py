import numpy as np

# input the distance from Earth to each of the stars in light years
star1_distance, star2_distance = (float(input(f"Enter the distance to star {i} in light years: ")) for i in range(1, 3))

# input the angle between the two stars as seen from Earth
angle = float(input("Enter the angle between the two stars in degrees: "))

# convert the angle to radians
angle_radians = np.radians(angle)

# calculate the distance between the stars using the law of cosines
star_distance = np.linalg.norm(star1_distance - star2_distance)

# print the distance between the stars using f-strings
print(f"The distance between the stars is {star_distance:.3f} light years.")

