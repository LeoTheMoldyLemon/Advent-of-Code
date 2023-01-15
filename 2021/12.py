f=open("input.txt", "r")
a=f.readline()
x=[]
while a!="":
    if a[len(a)-1]=="\n":
        a=a[:len(a)-1]
    x.append(a.split("-"))
    a=f.readline()
res=0
def travel(node, path, twice):
    global res
    if node=="end":
        res+=1
    else:
        for i in range(len(x)):

            if node==x[i][0]:
                if x[i][1]!="start" and (x[i][1].upper()==x[i][1] or path.count(x[i][1])==0 or twice):
                    twice1=True
                    if (x[i][1].upper()!=x[i][1] and path.count(x[i][1])==1) or not twice:
                        twice1=False
                    path1=list(path)
                    path1.append(x[i][1])
                    travel(x[i][1], path1, twice1)
                    
            if node==x[i][1]:
                if x[i][0]!="start" and (x[i][0].upper()==x[i][0] or path.count(x[i][0])==0 or twice):
                    twice1=True
                    if (x[i][0].upper()!=x[i][0] and path.count(x[i][0])==1) or not twice:
                        twice1=False
                    path1=list(path)
                    path1.append(x[i][0])
                    travel(x[i][0], path1, twice1)
            
travel("start", ["start"], True)
print(res)
