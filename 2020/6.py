a=[]
f=open(R"D:\desktop\Programming\Advent of code\2020\input.txt", "r")
new=True
length=len(f.readlines())
f.seek(0)
for i in range(length):
    inn=f.readline()
    if new:
        a.append([inn[0: len(inn)-1]])
        new=False
    else:
        if inn=="\n":
            new=True
        else:
            a[len(a)-1].append(inn[0: len(inn)-1])
result=0
for i in range(len(a)):
    b=[]
    for j in range(len(a[i][0])):
        if not a[i][0][j] in b:
            b.append(a[i][0][j])
    for j in range(1, len(a[i])):
        c=[]
        for k in range(len(a[i][j])):
            if a[i][j][k] in b:
                c.append(a[i][j][k])
        b=[]
        for k in range(len(c)):
            b.append(c[k])
    result+=len(b)
print(result)
