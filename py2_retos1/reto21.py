 def BMI(masa,peso):  
   Indice_de_masa=peso/a**2  
   return(Indice_de_masa)  
 altura = float(input('Dime tu altura por favor') or 1.7)  
 print('Altura=',altura,'m')  
 peso = float(input('Dime tu peso por favor')or 60)   
 print('Peso=',peso,'Kg')  
 print('Tu Indice de Masa Corporal es',round(Indice_de_masa(altura,peso),2)) 