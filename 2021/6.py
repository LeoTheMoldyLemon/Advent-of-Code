f=open("input.txt", "r")
from time import *
now =time()
a=f.readline().split(",")
x=[]
for i in range(len(a)):
    x.append(int(a[i]))
y=[]
for i in range(9):
    y.append(0)
for i in range(len(x)):
    y[x[i]]+=1

for i in range(256):
    a=y[0]
    del y[0]
    y.append(a)
    y[6]+=a
    b=0
for j in range(len(y)):
    b+=y[j]
print(str(i)+": "+str(b))

    
print(time()-now)








#for i in range(256):
 #   for j in range(len(x)):
  #      if x[j]==0:
  #          x.append(8)
  #          x[j]=6
  #      else:
  #          x[j]-=1
   # print(str(i)+": "+str(len(x)))
