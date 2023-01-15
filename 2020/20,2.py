f=open(r"D:\desktop\Programming\Advent of code\2020\input.txt", "r")
a=[]
length=len(f.readlines())
f.seek(0)
for i in range(length//12+1):
    x=f.readline()
    a.append([int(x.split()[1][:len(x.split()[1])-1]), []])
    for j in range(10):
        x=f.readline()
        a[i][1].append(x[:len(x)-1])
    x=f.readline()

print(a)
b=[]
