f=open("input.txt", "rt")
l=[0]
le=len(f.readlines())
f.close()
f=open("input.txt", "rt")
k=0
for i in range(le):
    a=f.readline()
    if(a!="\n"):
        l[k]+=int(a[:len(a)-1])
    else:
        l.append(0)
        k+=1
ma=0
for k in range(3):
    ma+=l.pop(l.index(max(l)))
print(ma)
        
    

    
