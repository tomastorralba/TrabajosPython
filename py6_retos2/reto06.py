import random 
x=random.randint(1,120)

if x<10:
  print ("el numero es menor a 10 :" , x)
elif x<50:
  print ("el numero esta entre 10 y 50 :" , x)
elif x<100:
  print ("el numero esta entre 50 y 100 :" , x)
else :
  print("el numero es mayor a 100 :" , x)
