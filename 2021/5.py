f=open("input.txt", "r")
a=f.readline().split(",")
x=[]
while a!=[""]:
    for i in range(len(a)):
        a[i]=int(a[i])
    x.append(list(a))
    a=f.readline().split(",")
y=[]
for i in range(1000):
    y.append([])
    for j in range(1000):
        y[i].append(0)

def hor(x1, x2, y1):
    for i in range(x2-x1+1):
        y[y1][x1+i]+=1
def ver(x1, y1, y2):
    #for i in range(y2-y1+1):
        #y[y1+i][x1]+=1
    k=1
def dia(x1, x2, y1, y2):
    if((x1>x2 and y1>y2) or (x1<x2 and y1<y2)):
        for i in range(abs(x1-x2)+1):
            y[min(y1, y2)+i][min(x1, x2)+i]+=1
    else:
        for i in range(abs(x1-x2)+1):
            y[max(y1, y2)-i][min(x1, x2)+i]+=1
def printy(xx, yy):
    for i in range(yy):
        a=""
        for j in range(xx):
            a+=str(y[i][j])
        print(a)

for i in range(len(x)):
    if x[i][0]==x[i][2]:
        if x[i][1]>x[i][3]:
            ver(x[i][0], x[i][3], x[i][1])
        else:
            ver(x[i][0], x[i][1], x[i][3])
    elif x[i][1]==x[i][3]:
        if x[i][0]>x[i][2]:
            hor(x[i][2], x[i][0], x[i][1])
        else:
            hor(x[i][0], x[i][2], x[i][1])
    #else:
        #dia(x[i][0], x[i][2], x[i][1], x[i][3])
b=0
for i in range(len(y)):
    for j in range(len(y[i])):
        if y[i][j]>1:
            b+=1
print(b)
