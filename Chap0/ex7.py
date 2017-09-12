weekday = int(input("今天周几?"))
whichhalf = int(input("上午选1下午选2"))
if weekday < 6:
  print ("keep working")
  if whichhalf==1:
    print ("make a plan for the whole working day")
  else:
    print ("act as planed")
else:
  print ("aha,it's weekdend")
  if whichhalf==1:
    print ("have a nice dream")
  else:
    print ("play games")
