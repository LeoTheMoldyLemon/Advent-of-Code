x=[]
y=[]
f=open("input.txt", "r")
a=f.readline().split("|")
while a!=[""]:
    x.append(a[0].split())
    y.append(a[1].split())
    a=f.readline().split("|")
b=0

def merge(a, b):
    result=0
    for i in range(len(a)):
        if a[i] in b:
            result+=1
    return result
def findint(a):
    for i in range(len(z)):
        b=0
        for j in range(len(a)):
            if a[j] in z[i]:
                b+=1
        if b==len(a) and len(a)==len(z[i]):
            return(i)

for i in range(len(x)):
    z=["","","","","","","","","",""]
    for j in range(len(x[i])):
        if len(x[i][j])==2:
            z[1]=x[i][j]
            continue
        elif len(x[i][j])==3:
            z[7]=x[i][j]
            continue
        elif len(x[i][j])==7:
            z[8]=x[i][j]
            continue
        elif len(x[i][j])==4:
            z[4]=x[i][j]
            continue
    for j in range(len(x[i])):
        if len(x[i][j])==6:
            if merge(z[1], x[i][j])==2:
                if merge(z[4], x[i][j])==4:
                    z[9]=x[i][j]
                else:
                    z[0]=x[i][j]
            else:
                z[6]=x[i][j]
        elif len(x[i][j])==5:
            if merge(z[1], x[i][j])==2:
                z[3]=x[i][j]
            else:
                if merge(z[4], x[i][j])==2:
                    z[2]=x[i][j]
                else:
                    z[5]=x[i][j]
    c=0
    for j in range(len(y[i])):
        c*=10
        c+=findint(y[i][j])
    print(i)
    b+=c
print(b)
    
    
    













    

