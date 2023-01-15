f=open("input.txt")
a=f.readline()
l=[]
while a!="":
    a=a.replace("\n", "").split()
    if len(a)==2:
        a[1]=int(a[1])
    l.append(a)
    a=f.readline()

cy=0
val=1
res=[""]


def addcy():
    global cy, val, res
    if abs(cy%40-val)<2:
        res[len(res)-1]+="#"
    else:
        res[len(res)-1]+="."
    if len(res[len(res)-1])==40:
        res.append("")
    
    cy+=1


for i in range(len(l)):
    if(l[i][0]=="addx"):
        addcy()
        addcy()
        val+=l[i][1]
    else:
        addcy()

for i in res:
    print(i)
