f=open("input.txt", "r")
a=f.readline()
xl=[]
while a!="":
    a=a.replace("\n", "")
    xl.append(a.split(","))
    try:
        a=f.readline()
    except IndexError:
        break


for i in range(len(xl)):
    if "on" in xl[i][0]:
        thing=True
    else:
        thing=False
    for j in range(len(xl[i])):
        xl[i][j]=xl[i][j].replace("on ", "").replace("off ", "").replace("x=", "").replace("y=", "").replace("z=", "").split("..")
        for k in range(len(xl[i][j])):
            xl[i][j][k]=int(xl[i][j][k])+50
    xl[i].insert(0, thing)

c=[]
for i in range(0, 130000):
    if i%1000==0:
        print(i)
    c.append([])
    for j in range(0, 130000):
        c[i].append([])
        for k in range(0, 130000):
            c[i][j].append(False)
            


def switch(state, x1, x2, y1, y2, z1, z2):
    for x in range(x1, x2+1):
        for y in range(y1, y2+1):
            for z in range(z1, z2+1):
                c[x][y][z]=state
for i in range(len(xl)):
    print(i)
    switch(xl[i][0], xl[i][1][0], xl[i][1][1], xl[i][2][0], xl[i][2][1], xl[i][3][0], xl[i][3][1])
counter=0
for i in range(len(c)):
    for j in range(len(c[i])):
        counter+=c[i][j].count(True)
print(counter)
