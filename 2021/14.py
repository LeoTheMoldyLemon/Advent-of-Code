from collections import Counter
f=open("input.txt", "r")
x=f.readline()
x=x[:len(x)-1]
a=f.readline()
a=f.readline()
y=[]
while a!="":
    if "\n"==a[len(a)-1]:
        a=a[:len(a)-1]
    y.append(a.split(" -> "))
    a=f.readline()

z=[]
for i in range(len(x)-1):
    z.append(x[i:i+2])
c=Counter(z)
for n in range(40):
    nc=Counter()
    dc=Counter()
    for j in range(len(y)):
        if y[j][0] in c.keys():
            nc+=Counter({y[j][0][0]+y[j][1]:c[y[j][0]], y[j][1]+y[j][0][1]:c[y[j][0]]})
            dc+=Counter({y[j][0]:c[y[j][0]]})
            
    c+=nc
    c-=dc




ele="NHCBPFKVSO"
num=[0,0,0,0,0,0,0,0,0,0]
for i in range(len(list(c.keys()))):
    num[ele.index(list(c.keys())[i][0])]+=c[list(c.keys())[i]]
    num[ele.index(list(c.keys())[i][1])]+=c[list(c.keys())[i]]
    
