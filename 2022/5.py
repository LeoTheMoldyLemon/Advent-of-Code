f=open("input.txt", "rt")
l=[]
c=[]
for i in range(9):
    l.append([])
a=f.readline()
while a!=" 1   2   3   4   5   6   7   8   9 \n":
    for i in range(9):
        if a[i*4+1]!=" ":
            l[i].append(a[i*4+1])
    a=f.readline()
for i in range(len(l)):
    l[i].reverse()
a=f.readline()
a=f.readline()
while a!="":
    a=a.split()
    c.append([int(a[3])-1,int(a[5])-1, int(a[1])])
    a=f.readline()


for i in range(len(c)):
    l[c[i][1]].extend(l[c[i][0]][len(l[c[i][0]])-c[i][2]:len(l[c[i][0]])])
    del l[c[i][0]][len(l[c[i][0]])-c[i][2]:len(l[c[i][0]])]
    
#HBTMTBSDC
