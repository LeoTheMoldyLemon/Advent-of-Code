f=open("input.txt", "rt")
a=f.readline()
l=[]
while a!="":
    a=a.split(",")
    a[0]=a[0].split("-")
    a[1]=a[1].split("-")
    for i in range(len(a)):
        for j in range(len(a[i])):
            a[i][j]=int(a[i][j])
    l.append(a)
    a=f.readline()
print(l)
res=0
for i in range(len(l)):
    if((l[i][0][0]<=l[i][1][1] and l[i][0][0]>=l[i][1][0])or(l[i][1][0]<=l[i][0][1] and l[i][1][0]>=l[i][0][0])):
       res+=1
print(res)        
        
