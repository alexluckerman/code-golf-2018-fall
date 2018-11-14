for a in range(1,999999):
 if (a % 3 == 0 or a % 5 == 0 or a % 7 == 0) and str(a)[0] == str(a)[len(str(a))-1]:
  print(a)