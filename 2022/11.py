import math
f=open("input.txt", "rt")
l=[]
while True:
    a=f.readline()
    if a=="":
        break
    a=f.readline()
    a=a.replace(",", "").replace("\n", "").split()
    l.append([])
    for i in range(2,len(a)):
        a[i]=int(a[i])
    l[-1].append(a[2:])
    a=f.readline()
    a=a.replace("\n", "").split()
    l[-1].append(a[3:])
    a=f.readline()
    a=a.replace("\n", "").split()
    l[-1].append(int(a[3]))
    a=f.readline()
    a=a.replace("\n", "").split()
    l[-1].append(int(a[5]))
    a=f.readline()
    a=a.replace("\n", "").split()
    l[-1].append(int(a[5]))
    a=f.readline()
    
# element: [[items],[operation],test,if true,if false]

def operation(inst, val):
    if (inst[0]=="old"):
        a=val
    else:
        a=int(inst[0])
    if (inst[2]=="old"):
        b=val
    else:
        b=int(inst[2])
    if (inst[1]=="*"):
        return a*b
    else:
        return a+b
    

throws=[]
for i in range(len(l)):
    throws.append(0)
divi=1
for i in range(len(l)):
    divi*=l[i][2]


for z in range(10000):
    if (z%100==0):
        print(z)
    for i in range(len(l)):
        for j in range(len(l[i][0])):
            l[i][0][j]=operation(l[i][1],l[i][0][j])%divi
            if l[i][0][j]%l[i][2]==0:
                l[l[i][3]][0].append(l[i][0][j])
            else:
                l[l[i][4]][0].append(l[i][0][j])
            throws[i]+=1
        l[i][0]=[]
print(throws)
            




























            
