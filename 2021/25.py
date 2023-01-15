f=open("input.txt", "r")
a=f.readline()
b=""
while a!="":
    b+=a
    a=f.readline()
a=b.split("\n")
del b

def moveh():
    global a
    b=list(a)
    result=False
    for i in range(len(a)):
        for j in range(len(a[i])):
            if a[i][j]==">":
                if (j+1)==len(a[i]):
                    if a[i][0]==".":
                        b[i]=">"+b[i][1:]
                        b[i]=b[i][:j]+"."
                        result=True
                else:
                    if a[i][j+1]==".":
                        result=True
                        b[i]=b[i][:j+1]+">"+b[i][j+2:]
                        b[i]=b[i][:j]+"."+b[i][j+1:]
    a=list(b)
    return result

def movev():
    global a
    b=list(a)
    result=False
    for i in range(len(a)):
        for j in range(len(a[i])):
            if a[i][j]=="v":
                if (i+1)==len(a):
                    if a[0][j]==".":
                        
                        b[0]=b[0][:j]+"v"+b[0][j+1:]
                        b[i]=b[i][:j]+"."+b[i][j+1:]
                        result=True
                else:
                    if a[i+1][j]==".":
                        result=True
                        b[i+1]=b[i+1][:j]+"v"+b[i+1][j+1:]
                        b[i]=b[i][:j]+"."+b[i][j+1:]
    a=list(b)
    return result

def printa(g):
    for i in range(len(g)):
        print(g[i])


        
step=0
result=True
while result:
    result=moveh()
    result=movev() or result
    step+=1

    

print(step)





