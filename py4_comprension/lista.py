A=[1,2,3]
B=[3,4,5,2]
C=[]
n=len(A)//2
[(((A[i+1])**2)*B[2*i])+B[n+i]for  i in range(n)]