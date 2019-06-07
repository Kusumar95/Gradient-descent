import numpy as np
def fh(x):
    x1 = x[0]  # changed
    x2 = x[1] 
    y= x1+x2
    return y

maxit=100
i=1
x=np.random.rand(2,1)
f1=x[0]+x[1]
for j in range(0,maxit):
  while(i<=4):
    v = x+np.random.rand(2,1)
    #print(v)
    #print(f1)
    f2=fh(v)
    #print(f2)
    if(f2<f1):
      x=v
      i=5
    f1=f2
  if(f1!=f2):
    maxit=maxit+1
print(f1)

