f=open("input.txt")
a=f.readline()
l=[]
while a!="":
    l.append(int(a)*811589153)
    a=f.readline()

ind=[]
le=len(l)
for i in range(len(l)):
    ind.append(i)




def mix():
    global l, ind, le
    for i in range(len(ind)):
        ine=ind.index(i)
        val=l[ine]
        mov=(val+ine)
        if mov>=le:
            mov%=le-1
        if mov<0:
            mov%=le-1
        del l[ine]
        del ind[ine]
        l.insert(mov, val)
        ind.insert(mov, i)
for i in range(10):
    mix()
print(l[(l.index(0)+1000)%le],l[(l.index(0)+2000)%le],l[(l.index(0)+3000)%le])
print(l[(l.index(0)+1000)%le]+l[(l.index(0)+2000)%le]+l[(l.index(0)+3000)%le])

