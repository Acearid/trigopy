def distance_between_stars(angular_separation, parallax1, parallax2):
  distance = (parallax1 * parallax2) / angular_separation
  return distance
angular_separation = float(input("Enter the angular separation of the two stars (in degrees): "))
parallax1 = float(input("Enter the parallax of star 1 (in arcseconds): "))
parallax2 = float(input("Enter the parallax of star 2 (in arcseconds): "))
distance = distance_between_stars(angular_separation, parallax1, parallax2)
print("The distance between the two stars is: " + str(distance) + " light-years")
