import functools
import multiprocessing
from copy import *
f=open("input.txt", "rt")
a=f.readline()
blue=[]
while a!="":
    a=a.split()
    blue.append(((int(a[6]),0,0,0),(int(a[12]),0,0,0),(int(a[18]),int(a[21]),0,0),(int(a[27]), 0, int(a[30]),0)))
    a=f.readline()


print(blue)
times={}
for i in range(25):
    times[i]=0
@functools.lru_cache
def build(t, res, rob, blue):
    res=list(res)
    rob=list(rob)
    if t==0:
        return res[3]
    nrob=deepcopy(rob)
    nres=deepcopy(res)
    for i in range(4):
        nres[i]+=rob[i]
    best=0
    if res[0]>=blue[3][0] and res[1]>=blue[3][1] and res[2]>=blue[3][2]:
        for i in range(4):
            nres[i]-=blue[3][i]
        nrob[3]+=1
        best=build(t-1, tuple(nres),tuple(nrob), blue)
    elif res[0]>=blue[2][0] and res[1]>=blue[2][1] and res[2]>=blue[2][2] and rob[2]<blue[3][2]:
        for i in range(4):
            nres[i]-=blue[2][i]
        nrob[2]+=1
        best=build(t-1, tuple(nres),tuple(nrob), blue)
    else:
        if res[0]>=blue[1][0] and res[1]>=blue[1][1] and res[2]>=blue[1][2] and rob[1]<blue[2][1]:
            nnres=deepcopy(nres)
            for i in range(4):
                nnres[i]-=blue[1][i]
            nnrob=deepcopy(nrob)
            nnrob[1]+=1
            best=max(best, build(t-1, tuple(nnres),tuple(nnrob), blue))
        if res[0]>=blue[0][0] and res[1]>=blue[0][1] and res[2]>=blue[0][2] and rob[0]<max(blue[1][0],blue[2][0],blue[3][0]):
            nnres=deepcopy(nres)
            for i in range(4):
                nnres[i]-=blue[0][i]
            nnrob=deepcopy(nrob)
            nnrob[0]+=1
            best=max(best, build(t-1, tuple(nnres),tuple(nnrob), blue))
        best=max(best, build(t-1, tuple(nres),tuple(nrob), blue))

    
    



    
    return best

res=0

def printres(n):
    global blue
    print(n)
    print(build(32,(0,0,0,0),(1,0,0,0), blue[n]))
    return 1

if __name__ == "__main__":
    t1 = multiprocessing.Process(target=printres, args=(0,))
    t2 = multiprocessing.Process(target=printres, args=(1,))
    t3 = multiprocessing.Process(target=printres, args=(2,))
    t1.start()
    t2.start()
    t3.start()
    t1.join()
    t2.join()
    t3.join()
    print("done")

#for i in range(len(blue)):
#    a=build(32,(0,0,0,0),(1,0,0,0),blue[i])
#    print(a)
#    res+=(i+1)*a
#print(res)






    
