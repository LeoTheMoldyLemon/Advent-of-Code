from time import *
test=False
if test:
    xt=[20, 30]
    yt=[-10, -5]
else:
    xt=[281, 311]
    yt=[-74, -54]

f=open("input.txt", "r")
a=f.readline()
g=""
while a!="":
    if a[len(a)-1]=="\n":
        a=a[:len(a)-1]
        a+="  "
    g+=a
    a=f.readline()
g=g.split()
for i in range(len(g)):
    g[i]=g[i].split(",")
    for j in range(2):
        g[i][j]=int(g[i][j])





xva=round((-1+(1+8*xt[0])**(1/2))/2)
b=0


def test(xv, yv):
    x=0
    y=0

    while True:
        if xt[0]<=x<=xt[1] and yt[0]<=y<=yt[1]:
            return True
        elif y<yt[0]:
            return False
        x+=xv
        y+=yv

        if xv>0:
            xv-=1
        elif xv<0:
            xv+=1
        yv-=1


b=[]
for i in range(-300,300):
    if i%100==0:
        print(i)
    for j in range(-300, 300):
        if test(xva+j, i):
            b.append([xva+j, i])











