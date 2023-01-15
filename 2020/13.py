f=open(r"D:\desktop\Programming\Advent of code\2020\input.txt","r")
x=f.readline()
target=int(x[0:len(x)-1])
x=f.readline().split(",")
a=[]
for i in range(len(x)):
    if x[i]!="x":
        a.append(int(x[i]))
    else:
        a.append(x[i])
m=a[a[0]]*a[0]
t=a[a[0]]*a[0]*(100000000000000//(a[a[0]]*a[0]))-a[0]
t=100512000003531
n=t
while True:
    check=True
    for i in range(1, len(a)):
        if a[i]!="x":
            if t%a[i]!=a[i]-i:
                check=False
    if check:
        print("result: "+str(t))
        break
    t+=m
    if t>n:
        n+=1000000000
        print(t)

