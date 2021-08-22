x=int(input('Ingrese el primer numero'))
y=int(input('Ingrese el segundo numero'))
lista=[]
suma=0

if x<y:
  lista.append(x)
  while x<y:    
    suma=suma+x
    x=x+1
    lista.append(x)
  suma=suma+y    
  

else:
  lista.append(y)
  while y<x:
    suma=suma+y
    y=y+1
    lista.append(y)
  suma=suma+x  
print ('La lista de numeros es : ', lista)
print('La suma es :' , suma)


