for i in range(0,input()):
  L = sorted(set(list(map(int, str(raw_input()).split()))))
  k = int(input())
  print(L[len(L)-k])