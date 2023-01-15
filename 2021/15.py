from time import *

f=open("input.txt", "r")
b=f.readline()
a=[]
t=time()
while b!="":
    if b[len(b)-1]=="\n":
        b=b[:len(b)-1]
    a.append(b)
    b=f.readline()



risklvl=100000000000

def pathing(y, x, risk, path):
    global risklvl
    if y==(len(a)-1) and x==(len(a)-1):
        if risk<risklvl:
            risklvl=risk
            print(risk)
        return True
    if y<(len(a)-1) and [y+1, x] not in path:
        path1=list(path)
        path1.append([y+1,x])
        pathing(y+1, x, risk+int(a[y+1][x]),path1)
    if x<(len(a)-1) and [y,x+1] not in path:
        path1=list(path)
        path1.append([y,x+1])
        pathing(y, x+1, risk+int(a[y][x+1]),path1)
    if y>0 and [y-1,x] not in path:
        path1=list(path)
        path1.append([y-1,x])        
        pathing(y-1, x, risk+int(a[y-1][x]),path1)
    if x>0 and [y,x-1] not in path:
        path1=list(path)
        path1.append([y,x-1])        
        pathing(y, x-1, risk+int(a[y][x-1]),path1)
    
    

pathing(0,0,0, [0,0])
print(risklvl)
print(time()-t)
