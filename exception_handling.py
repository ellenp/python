try:
  print(x)
except:
  print("An exception occurred")


try:
  print("x")
except:
  print("Something went wrong")
else:
  print("Else")
finally:
  print("The 'try except' is finished")