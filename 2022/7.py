f=open("input.txt", "rt")
a=f.readline()
l={}
curr=[]
cdir=[]
def tostring(li):
    res=""
    for i in li:
        res+=i
        if i!="/":
            res+="/"
    return res[0:len(res)-1]

while a!="":
    a=a.split()
    if len(a)==3:
        if a[1]=="cd":
            if curr!=[]:
                l[curr[0]]=curr[1]
                curr=[]
            if a[2]!="..":
                cdir.append(a[2])
                curr=[tostring(cdir),[]]
            else:
                cdir.pop(len(cdir)-1)
    else:
        if a[0]=="dir":
            curr[1].append(["dir", tostring(cdir)+"/"+a[1]])
        elif a[0]!="$":
            curr[1].append(["file", int(a[0])])
    a=f.readline()
l[curr[0]]=curr[1]
s={}
def calcSize(d):
    global s
    res=0
    print(d)
    for i in range(len(l[d])):
        if l[d][i][0]=="file":
            res+=l[d][i][1]
        else:
            res+=calcSize(l[d][i][1])
    s[d]=res
    return res
    
def part1():
    global s
    res=0
    for i in s.keys():
        if s[i]<100000:
            res+=s[i]
    return res

def part2():
    global s
    m=70000000
    nam=""
    for i in s.keys():
        if s[i]<m and s[i]>=(30000000-(70000000-44804833)):
            nam=i
            m=s[i]

    print(nam)
    return m





