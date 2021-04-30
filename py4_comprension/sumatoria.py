A=[1,2,3]
B=[3,4,5]
C=[5,4,3]

n=len(A)
f=sum(((A[i]*B[i])+C[i])for i in range (n))+(n**2)
print(f)
