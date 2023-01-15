import copy


f=open("input.txt", "rt")
a=f.readline()
l=[]
v=[]
st=[]
en=[]
t=[]
while a!="":
    l.append([])
    for i in a.replace("\n", ""):
        l[-1].append(i)
    v.append([])
    for i in range(len(l[-1])):
        
        v[-1].append(0)
        if (l[-1][i]=="E"):
            l[-1][i]="z"
            v[-1][-1]=1
            st=[len(l)-1, i]
            t.append(st)
        elif (l[-1][i]=="a"):
            l[-1][i]="a"
            en.append([len(l)-1, i])
    a=f.readline()

step=[[0,1],[0,-1],[1,0],[-1,0]]
def path(x,y):
    global t,l,step
    res=[]
    for i in step:
        if -1<x+i[0]<len(l) and -1<y+i[1]<len(l[0]):
            if -ord(l[x][y])+ord(l[x+i[0]][y+i[1]])>=-1:
                res.append([x+i[0],y+i[1]])
    return res
    


while t!=[]:
    nt=[]
    for i in t:
        pos=path(i[0], i[1])
        for j in pos:
            
            if j in en:
                print(v[i[0]][i[1]])
                print(i)
            if v[j[0]][j[1]]==0:
                nt.append(j)
                v[j[0]][j[1]]=v[i[0]][i[1]]+1
    t=copy.deepcopy(nt)
                
