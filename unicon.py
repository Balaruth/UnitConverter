print "Welcome to the unit converter! This program convers kilometres into miles."
print

while True:
  value = raw_input("Please enter the number of kilometres you'd like to convert into miles, or enter 0 to quit: ")

  try:
    value = float(value)

    if value > 0:
      value2 = value * 0.621371
      print str(value) + " kilometres is " + str(round(value2, 2)) + " miles."
    else:
      print "Thanks for using the unit converter!"
      break

  except ValueError:
    print "Please enter a number to be converted!"


