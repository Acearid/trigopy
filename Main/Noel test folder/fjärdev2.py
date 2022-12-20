def can_see_higher_peak(height1, height2, distance):
  # Calculate the angle between the two peaks
  angle = abs(height1 - height2) / distance

  # If the angle is less than 1 degree, the higher peak is not visible
  if angle < 1:
    return False
  else:
    return True

# Prompt the user for input
height1 = float(input("Enter the height of the first peak: "))
height2 = float(input("Enter the height of the second peak: "))
distance = float(input("Enter the distance between the two peaks: "))

# Test the function
if can_see_higher_peak(height1, height2, distance):
  print("You can see the higher peak!")
else:
  print("You cannot see the higher peak.")
