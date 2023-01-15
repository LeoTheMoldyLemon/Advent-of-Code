f=open(r"D:\desktop\Programming\Advent of code\2020\input.txt","r")
length=len(f.readlines())
f.seek(0)
a=[]
for i in range(length):
    x=f.readline()
    a.append(int(x[0:len(x)]))

target=1721308972
br=0
for i in range(len(a)):
    for j in range(i+1, len(a)):
        x=a[i:j]
        br=0
        for k in range(len(x)):
            br+=x[k]
        if br==target:
            print(min(x)+max(x))

