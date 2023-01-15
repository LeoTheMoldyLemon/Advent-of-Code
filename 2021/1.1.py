f=open("input.txt")
x=[]
a=f.readline()
while a!="":
    x.append(int(a))
    a=f.readline()
b=x[0]+x[1]+x[2]
y=0
for i in range(1, len(x)-2):
    if (x[i]+x[i+1]+x[i+2])>b:
        y+=1
    b=x[i]+x[i+1]+x[i+2]
print(y)
