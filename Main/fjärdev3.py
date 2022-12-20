import math

def compare_fractions():
  x = float(input("Enter a value for the second peak: "))
  y = float(input("Enter a value for the first peak: "))

  alpha = math.atan(x/y)
  theta = math.atan(y/x)

  if alpha > theta:
    print("you can see the top")
  elif alpha < theta:
    print("you can not see top")
  else:
    print("both tops are equal")

compare_fractions()
