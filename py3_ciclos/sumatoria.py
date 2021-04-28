def sumatoria(A,B,C):
  n=len(A)
  sumatoria_total=0
  for i in range(n):
    r=A[i]*B[i]
    f=r+C[i]
    sumatoria_total=sumatoria_total+f
  resultado=sumatoria_total+n**2
  print(resultado)
  return resultado

A=[1,1,1]
B=[1,1,1]
C=[1,1,1]

sumatoria(A,B,C)

