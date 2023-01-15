from time import time
f=open(r"D:\desktop\Programming\Advent of code\2020\input.txt", "r")
a=f.readline().split(",")
for i in range(len(a)):
    a[i]=int(a[i])
n=0
ln=-1
l={}
tim=time()
for i in range(len(a)):
    n+=1
    l[a[i]]=n-1
    print(a[i])
while n!=30000000:
    try:
        nn=n-l[ln]-1
    except KeyError:
        nn=0
    l[ln]=n-1
    ln=nn
    n+=1
print(time()-tim)
print(ln)
