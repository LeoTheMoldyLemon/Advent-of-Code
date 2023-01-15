f=open("input.txt")
a=f.readline().split(",")
x=[]
for i in range(len(a)):
    x.append(int(a[i]))


def far(a):
    result=0
    for i in range(len(x)):
        n=abs(x[i]-a)
        result+=n*(n+1)/2
    return result
b=166906717
c=0

for i in range(1900):
    d=far(i)
    if d<b:
        b=d
        c=i
print(c)
print(b)
