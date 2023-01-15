f=open("inputf.txt", "rt")
a=f.readline()
l=[]
while a!="":
    l.append(a.replace("\n", ""))
    a=f.readline()

res=0
for i in l:
    num=0
    for j in range(len(i)):
        if i[j]=="2":
            num+=2*5**(len(i)-j-1)
        elif i[j]=="1":
            num+=1*5**(len(i)-j-1)
        elif i[j]=="0":
            num+=0*5**(len(i)-j-1)
        elif i[j]=="-":
            num+=-1*5**(len(i)-j-1)
        elif i[j]=="=":
            num+=-2*5**(len(i)-j-1)
    res+=num

def tosnafu(num):
    if num==0:
        return ""
    nex=num//5
    res=num%5
    if res>=3:
        nex+=1
        res-=5
    if res==-1:
        res="-"
    elif res==-2:
        res="="
    else:
        res=str(res)
    return tosnafu(nex)+res

    
print(res)
print(tosnafu(res))
        
