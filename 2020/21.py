f=open(r"D:\desktop\Programming\Advent of code\2020\input.txt", "r")
length=len(f.readlines())
f.seek(0)
a=[]
for i in range(length):
    x=f.readline()
    x=[x.split(" (contains ")[0].split(" "), x[:len(x)-2].split(" (contains ")[1].split(", ")]
    a.append(x)
alergens={}

for i in range(len(a)):
    for j in range(len(a[i][1])):
        if not a[i][1][j] in alergens:
            alergens[a[i][1][j]]=[]
            
def combine(l1, l2):
    result=[]
    for i in range(len(l1)):
        for j in range(len(l2)):
            if l1[i]==l2[j]:
                result.append(l1[i])
    return result

for i in range(len(a)):
    for j in range(len(a[i][1])):
        if alergens[a[i][1][j]]==[]:
            alergens[a[i][1][j]]=a[i][0]
        else:
            alergens[a[i][1][j]]=combine(a[i][0], alergens[a[i][1][j]])

keys=list(alergens.keys())

for k in range(len(keys)):
    for i in range(len(keys)):
        if len(alergens[keys[i]])==1:
            for j in range(len(keys)):
                if i!=j and alergens[keys[i]][0] in alergens[keys[j]]:
                    alergens[keys[j]].remove(alergens[keys[i]][0])
alerlist=[]
for i in range(len(keys)):
    alerlist.append(alergens[keys[i]][0])
result=0
for i in range(len(a)):
    for j in range(len(alerlist)):
        if alerlist[j] in a[i][0]:
            a[i][0].remove(alerlist[j])
    result+=len(a[i][0])
print(result)
result=""
keys=list(alergens.keys())
keys.sort()
for i in range(len(keys)):
    result+=alergens[keys[i]][0]+","
print(result[:len(result)-1])
                    
    
        
    
               
