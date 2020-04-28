age = 23
message = "Happy " + str(age) + "rd Birthday!"
print (message)

#Python knows that the variable could represent either the numerical
#value 23 or the characters 2 and 3. When you use integers within strings
#like this, you need to specify explicitly that you want Python to use the integer
#as a string of characters. You can do this by wrapping the variable in the
#str() function, which tells Python to represent non-string values as strings: