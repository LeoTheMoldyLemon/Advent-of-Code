f=open(r"D:\desktop\Programming\Advent of code\2020\input.txt","r")
length=len(f.readlines())
f.seek(0)
a=[]
b=2**36
for i in range(length):
    x=f.readline()
    if len(x)>30:
        a.append(["mask", 0, x[7:len(x)-1]])
    else:
        a.append([x.split(" = ")[0].split("]")[0].split("[")[0], int(x.split(" = ")[0].split("]")[0].split("[")[1]) , int(x.split(" = ")[1].split("\n")[0])])
        if int(x.split(" = ")[0].split("]")[0].split("[")[1])>b:
            b=int(x.split(" = ")[0].split("]")[0].split("[")[1])
mask=a[0][2]
mem={}



def applymask(value):
    global mask
    value=str(bin(value))[2:]
    value="0"*(36-len(value))+value
    newvalue=""
    for i in range(len(mask)):
        if mask[i]!="X":
            newvalue+=mask[i]
        else:
            newvalue+=value[i]
    return(int(newvalue, 2))

def decode(value):
    global mask
    value=str(bin(value))[2:]
    value="0"*(36-len(value))+value
    newvalue=""
    floating=[]
    for i in range(len(mask)):
        if mask[i]=="1":
            newvalue+="1"
        elif mask[i]=="0":
            newvalue+=value[i]
        else:
            newvalue+="X"
            floating.append(i)
    value=[]
    a=bin(int("0b"+"1"+"0"*len(floating), 2))
    for i in range(2**len(floating)):
        newnewvalue="0b"
        for j in range(len(newvalue)):
            if j in floating:
                newnewvalue+=str(a[3+floating.index(j)])
            else:
                newnewvalue+=newvalue[j]
        value.append(int(newnewvalue, 2))
        a=int(a,2)
        a+=1
        a=bin(a)
    return(value)
for i in range(1, len(a)):
    if a[i][0]=="mem":
        value=a[i][2]
        address=decode(a[i][1])
        for i in range(len(address)):
            mem[address[i]]=value
    else:
        mask=a[i][2]


b=0
keys=list(mem.keys())
for i in range(len(keys)):

    b+=mem[keys[i]]
print(b)
