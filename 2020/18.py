f=open(r"D:\desktop\Programming\Advent of code\2020\input.txt", "r")
length=len(f.readlines())
f.seek(0)
a=[]
for i in range(length):
    x=f.readline()
    a.append(x[:len(x)-1])

def domath(izraz):
    l=[]
    n=-1
    print(izraz)
    while True:
        n+=1
        try:
            x=izraz[n]
        except IndexError:
            break
        if 47<ord(x)<58:
            broj=""
            
            while x!=" ":
                n+=1
                broj+=x
                try:
                    x=izraz[n]
                except IndexError:
                    break
            l.append(int(broj))
        if x=="*" or x=="+":
            l.append(x)
        if x=="(":
            boz=1
            zagrada=""
            while True:
                n+=1
                x=izraz[n]
                if x==")":
                    boz-=1
                if x=="(":
                    boz+=1
                if boz==0:
                    break
                zagrada+=x
            l.append(domath(zagrada))
    print(l)
    n=-1
    while True:
        n+=1
        try:
            x=l[n]
        except IndexError:
            break
        if x=="+":
            zbroj=l[n-1]+l[n+1]
            del(l[n-1:n+1])
            l[n-1]=zbroj
            n-=1
    n=-1
    result=1
    print(l)
    while True:
        n+=1
        try:
            x=l[n]
        except IndexError:
            break
        if x!="*":
            result*=x
            
        

    print(result)
    return(result)
result=0
for i in range(len(a)):
    result+=domath(a[i])
