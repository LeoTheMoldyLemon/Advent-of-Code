from numpy import *
f=open("input.txt", "r")
a=f.readline()
xa=""
for i in range(len(a)):
    b=bin(int(a[i], 16))[2:]
    b="0"*(4-len(b))+b
    xa+=b
    


def calc(x, y):
    res=[]
    k=0
    i=0
    while i+10<len(x) and k<y:
        k+=1
        t=x[i+3:i+6]
        i+=6
        result=0
        if t=="100":
            result=""
            while x[i]=="1":
                result+=x[i+1:i+5]
                i+=5
            result+=x[i+1:i+5]
            i+=5
            result=int(result, 2)
            res.append(result)
        else:
            if x[i]=="0":
                results=calc(x[i+16:i+16+int(x[i+1:i+16],2)], 1000000)
                i+=16+results[len(results)-1]
                results=results[0]
            else:
                results=calc(x[i+12:], int(x[i+1:i+12],2))
                i+=12+results[len(results)-1]
                results=results[0]
            if t=="000":
                res.append(sum(results))
            elif t=="001":
                res.append(prod(results))
            elif t=="010":
                res.append(min(results))
            elif t=="011":
                res.append(max(results))
            elif t=="101":
                if results[0]>results[1]:
                    res.append(1)
                else:
                    res.append(0)
                if len(results)!=2:
                    print("error")
            elif t=="110":
                print(results)
                if results[0]<results[1]:
                    res.append(1)
                else:
                    res.append(0)
                if len(results)!=2:
                    print("error")
            elif t=="111":
                if results[0]==results[1]:
                    res.append(1)
                else:
                    res.append(0)
                if len(results)!=2:
                    print("error")           
    print("TYPE: "+t)
    print(res[0])  
    return [res, i]


print(calc(xa, 1))
