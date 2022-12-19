import math
# input the distance from Earth to each of the stars in light years
star1_distance = float(input("Enter the distance to the first star in light years: "))
star2_distance = float(input("Enter the distance to the second star in light years: "))

# input the angle between the two stars as seen from Earth
angle = float(input("Enter the angle between the two stars in degrees: "))

# convert the angle to radians
angle_radians = angle * (math.pi / 180)

print(math.pi)

# calculate the distance between the stars using the law of cosines
star_distance =((star1_distance**2) + (star2_distance**2) - (2 * star1_distance * star2_distance) * (math.cos(angle_radians)))
dis=math.sqrt(star_distance)
# print the distance between the stars
print("The distance between the stars is %.2f light years." % dis)
