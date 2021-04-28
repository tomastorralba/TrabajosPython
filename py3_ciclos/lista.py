def llena_lista(A,B):
  n=len(A)//2
  C=[]
  for i in range(n):
    d=A[i+1]**2
    e=d*B[2*i]
    f=e+B[n+i]
    C.append(f)
  print(C)
  return C
A=[1,2,3,4]
B=[4,3,2,1]
llena_lista(A,B)
