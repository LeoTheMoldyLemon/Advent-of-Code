
a=open(r"D:\desktop\Programming\Advent of code\2020\input.txt", "r").readlines()
n=0
b=[]
for i in range(len(a)):
    b.append([])
for i in range(len(a)):
    top=127
    bot=0
    for j in range(7):
        if a[i][j]=="F":
            top=(top-bot-1)//2+bot
        else:
            bot=(top-bot+1)//2+bot
    b[i].append(top)
    top=7
    bot=0
    for j in range(3):
        if a[i][j+7]=="L":
            top=(top-bot-1)//2+bot
        else:
            bot=(top-bot+1)//2+bot
    b[i].append(top)
    
    if b[i][0]*8+b[i][1]>n:
        n=b[i][0]*8+b[i][1]
print(n)
c=[]
for i in range(128*8+7):
    c.append(i)
d=[]
for i in range(len(c)):
    ex=False
    for j in range(len(b)):
        if c[i]==b[j][0]*8+b[j][1]:
            ex=True
    print(c[i], ex)
    if not ex:
        d.append(c)
print(d)
    
