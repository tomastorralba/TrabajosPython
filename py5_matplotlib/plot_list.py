import matplotlib.pyplot as plot
lista =[]
numero = int(input('ingrese el numero a evaluar :'))
lista.append(numero)
while numero != 1:
  
  if (numero % 2)== 0:
    numero=numero // 2
  else:
    numero = numero * 3 + 1 
  lista.append(numero)     
print("la lista de numero es :" , lista)


 
