f=open("input.txt", "rt")
a=f.readline()
l=[]
while a!="":
    l.append(a.replace("\n", ""))
    a=f.readline()
res=0
priomap={}
for i in range(26):
    priomap[chr(ord("a")+i)]=i+1
for i in range(26):
    priomap[chr(ord("A")+i)]=i+27

for i in range(len(l)//3):
    rep=""
    for j in range(len(l[i*3])):
        if (l[i*3][j] in l[i*3+1]) and (l[i*3][j] in l[i*3+2]):
            
            rep=l[i*3][j]
            break
    res+=priomap[rep]
print(res)
    
