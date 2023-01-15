x=input()
a=[]
while x!="stop":
    x=x.split(",")
    a.append([])
    for i in range(len(x)):
        a[len(a)-1].append(int(x[i]))
    x=input()
print(len(a))
def getcon(a):
    if a==[]:
        return([])
    else:
        b=[a[0]]
        a.remove(a[0])
        olda=[]
        while olda!=a:
            olda=a.copy()
            dellist=[]
            for i in range(len(a)):
                for j in range(len(b)):
                    md=0
                    for k in range(len(a[i])):
                        md+=abs(a[i][k]-b[j][k])
                    if md<4:
                        b.append(a[i])
                        dellist.append(a[i])
                        break
            for i in range(len(dellist)):
                a.remove(dellist[i])
            print(len(a))
        return(b)
b=[getcon(a)]
while True:
    x=getcon(a)
    if x==[]:
        break
    print(x)
    b.append(x)
print(len(b),b)
        
            
