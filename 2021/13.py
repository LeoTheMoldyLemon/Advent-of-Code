f=open("input.txt", "r")
b=f.readline()
a=[]
while b!="":
    if b[len(b)-1]=="\n":
        b=b[:len(b)-1]
    a.append(b.split(","))
    b=f.readline()
    
for i in range(len(a)):
    a[i][0]=int(a[i][0])
    a[i][1]=int(a[i][1])


fold=[[0,655],[1,447],[0,327],[1,223],[0,163],[1,111],[0,81],[1,55],[0,40],[1,27],[1,13],[1,6]]
#fold=[[1,7],[0,5]]
deletelist=[]
for k in range(len(fold)):

    for i in range(len(a)):
        if a[i][fold[k][0]]>fold[k][1]:
            a[i][fold[k][0]]=2*fold[k][1]-a[i][fold[k][0]]
        for j in range(len(a)):
            if a[i]==a[j] and j not in deletelist and i!=j:
                deletelist.append(i)
    deletelist.sort(reverse=True)
    for i in range(len(deletelist)):
        del(a[deletelist[i]])
    deletelist=[]
    print(a)

for i in range(20):
    thing=""
    for j in range(40):
        if [j,i] in a:
            thing+="#"
        else:
            thing+="."
    print(thing)
            
    

print(len(a)-len(deletelist))
