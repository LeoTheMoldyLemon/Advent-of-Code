f=open("input.txt", "rt")
a=f.readline()
l={}
while a!="":
    a=a.replace(":", "").replace("\n", "").split()
    if len(a)==2:
        l[a[0]]=(float(a[1]),)
    else:
        l[a[0]]=tuple(a[1:])
    a=f.readline()


s1=[]
s2=[]
def calc(monkey):
    global l
    if len(l[monkey])==1:
        if monkey=="humn":
            return ["humn"]
        else:
            return [l[monkey][0]]
    else:
        res1=calc(l[monkey][0])
        res2=calc(l[monkey][2])
        if "humn" in res2:
            res2.append(l[monkey][1])
            res2.extend(res1)
            return res2
        elif "humn" in res1:
            res1.append(l[monkey][1])
            res1.extend(res2)
            return res1
        else:
            return([oldcalc(monkey)])
    
def oldcalc(monkey):
    global l
    if len(l[monkey])==1:
        if monkey=="humn":
            print("AAAAAAAAAAAAAAAAAAA")
        return l[monkey][0]
    else:
        if l[monkey][1]=="+":
            return oldcalc(l[monkey][0])+oldcalc(l[monkey][2])
        elif l[monkey][1]=="-":
            return oldcalc(l[monkey][0])-oldcalc(l[monkey][2])
        elif l[monkey][1]=="*":
            return oldcalc(l[monkey][0])*oldcalc(l[monkey][2])
        elif l[monkey][1]=="/":
            return oldcalc(l[monkey][0])/oldcalc(l[monkey][2])
        

    
s1=calc(l["root"][0])
s2=oldcalc(l["root"][2])
s22=s2
vv=1
sv=0
op=""
for i in range(1,len(s1)):
    if isinstance(s1[i], (int, float)):
        print(vv, sv, op, s1[i])
        if op=="+":
            sv+=s1[i]
            s22-=s1[i]
        elif op=="-":
            sv-=s1[i]
            s22+=s1[i]
        elif op=="*":
            sv*=s1[i]
            vv*=s1[i]
            s22/=s1[i]
        elif op=="/":
            sv/=s1[i]
            vv/=s1[i]
            s22*=s1[i]

    else:
        op=s1[i]
s3=str(vv)+" humn + "+str(sv)
            
        
    















print(s3)
print(s2)
print(s22)
print((s2-sv)/vv)

    
