import math

def distance_between_stars(distance_to_star_1, distance_to_star_2, angle_between_stars):
  # Räkna ut längden på den sida av triangeln som ligger mellan stjärnorna genom att använda sinusregeln
  side_length = distance_to_star_1 * math.sin(angle_between_stars) / math.sin(math.pi - angle_between_stars - math.acos(distance_to_star_1 / distance_to_star_2))
  
  # Räkna ut avståndet mellan stjärnorna genom att använda pythagoras sats
  distance = math.sqrt(distance_to_star_1**2 + side_length**2 - 2 * distance_to_star_1 * side_length * math.cos(angle_between_stars))
  
  return distance

# Läs in avståndet från jorden till varje stjärna och vinkeln mellan stjärnorna sett från jorden från användaren
distance_to_star_1 = float(input("Ange avståndet från jorden till den första stjärnan: "))
distance_to_star_2 = float(input("Ange avståndet från jorden till den andra stjärnan: "))
angle_between_stars = math.radians(float(input("Ange vinkeln mellan stjärnorna sett från jorden i grader: ")))

# Anropa funktionen och skriv ut resultatet
distance = distance_between_stars(distance_to_star_1, distance_to_star_2, angle_between_stars)
print(f"Avståndet mellan stjärnorna är: {distance} enheter")
