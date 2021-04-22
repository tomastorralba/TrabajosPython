def año_bisiesto(x):
  if x % 4==0:
    print("El año ", x ," es bisiesto")
  else:
    print ("no es bisiesto")

i=int(input("introdusca el año que quiere saber si es bisiesto"))

año_bisiesto(i)