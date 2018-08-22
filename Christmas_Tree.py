# Christmas-Tree
#AIgorithm drawing Christmas Tree :)
def choinka():  #this program is drawing christmas tree
  z = range(1, 12)
  h = range(1, 7)
  for j in h:
    for x, y in enumerate(z):
      if j>1 and j<6 and (x+y) <= 5*j and (x+y)>2*j:
        print((len(z)-x)*' ', (x+y)*'*')
      elif j==1 and (x+y) <= 5*j:
        print((len(z)-x)*' ', (x+y)*'*')
      elif j==6 and (x+y)<=5:
        print((len(z)-1)*' ', 3*'*') #one christmas tree
  print(26*'*')
zagajnik = int(input("wprowadź liczbę: ")) #number of trees according to input
for t in range(zagajnik):
  choinka()  