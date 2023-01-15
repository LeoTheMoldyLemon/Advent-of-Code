f=open("input.txt", "rt")
a=f.readline()
l=[]
while a!="":
    a=a.replace("\n", "").replace(":", "").replace(",", "").replace("=", " ").split(" ")
    l.append([[int(a[3]), int(a[5])], [int(a[11]), int(a[13])]])
    a=f.readline()

def dist(a,b):
    return abs(a[0]-b[0])+abs(a[1]-b[1])

ranges=[]
for i in range(len(l)):
    ranges.append([l[i][0], dist(l[i][0], l[i][1])])


m=[]


for i in range(len(l)):
    print(i)
    m.append([])
    for x in range(ranges[i][0][0]-ranges[i][1]-1, ranges[i][0][0]+ranges[i][1]+2):
        if 0<=x<=4000000 and 0<=ranges[i][0][1]-abs(abs(x-ranges[i][0][0])-ranges[i][1]-1)<=4000000 and 0<=ranges[i][0][1]+abs(abs(x-ranges[i][0][0])-ranges[i][1]-1)<=4000000:
            m[-1].append(x*4000000+ranges[i][0][1]-abs(abs(x-ranges[i][0][0])-ranges[i][1]-1))
            m[-1].append(x*4000000+ranges[i][0][1]+abs(abs(x-ranges[i][0][0])-ranges[i][1]-1))


print("going")




res={}
for i in range(len(m)):
    print(i)
    for j in range(len(m)):
        print(j)
        if i!=j:
            af=list(set(m[i]).intersection(m[j]))
            for k in af:
                if k in res.keys():
                    res[k]+=1
                else:
                    res[k]=1
for i in res.keys():
    if res[i]>3:
        print(i)
        
ress=[]
print(len(res))
for i in range(len(res)):
    if(i%10000==0):
        print(i)
    if res.count(res[i])>3:
        print(res[i])
        ress.append([res[i]//4000000, res[i]%4000000])
print(len(ress))
for i in ress:
    yiss=True
    for j in ranges:
        if dist(i, j[0])<=j[1]:
            yiss=False
    if yiss:
        print(i)
        



