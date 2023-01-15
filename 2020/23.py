from time import *
a=input()
b=[]
for i in range(len(a)):
    b.append(a[i])
a=b.copy()
cur=a[0]
des="1"
side=[]
tim=time()
def timestamp():
    global tim
    print(time()-tim)
    tim=time()
for i in range(10, 1000001):
    a.append(str(i))
for i in range(10000000):
    if i%1000==0:
        print(i)
        timestamp()
    for i in range(3):
        ind=a.index(cur)+1
        if ind>=len(a):
            ind-=len(a)
        side.append(a[ind])
        del(a[ind])
    des=str(int(cur)-1)
    if int(des)<1:
            des="1000000"
    while des in side:
        des=str(int(des)-1)
        if int(des)<1:
            des="1000000"
    des=a.index(des)+1
    if des>=len(a):
        des-=len(a)
    for i in range(3):
        a.insert(des, side[i])
        des+=1
    side=[]
    ind=a.index(cur)+1
    if ind>=len(a):
        ind-=len(a)
    cur=a[ind]
    
    
