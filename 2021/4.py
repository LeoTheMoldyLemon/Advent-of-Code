f=open("input.txt", "r")
x=f.readline().split(",")
x[len(x)-1]=x[len(x)-1][0:len(x[len(x)-1])-1]
y=[]
k=True
while k:
    f.readline()
    y.append([])
    for i in range(5):
        a=f.readline().split()
        if a!=[]:
            y[len(y)-1].append(a)
        else:
            k=False
            break
y=y[:len(y)-1]
z=[]
for i in range(len(y)):
    z.append([])
    for j in range(5):
        z[len(z)-1].append(["o","o","o","o","o"])

def check(z):
    for i in range(5):
        if z[i][0]=="x" and z[i][1]=="x" and z[i][2]=="x" and z[i][3]=="x" and z[i][4]=="x":
            return True
    for i in range(5):
        if z[0][i]=="x" and z[1][i]=="x" and z[2][i]=="x" and z[3][i]=="x" and z[4][i]=="x":
            return True
    return False    

removelist=[]
for i in range(len(x)):
    for j in range(len(y)):
        done=False
        for xc in range(5):
            for yc in range(5):
                if y[j][xc][yc]==x[i]:
                    z[j][xc][yc]="x"
                if check(z[j]):
                    if len(y)==1:
                        print(y)
                        a=y[0]
                        b=z[0]
                        c=x[i]
                    if j==85:
                        print(len(y))
                    removelist.append(j)
                    done=True
                    break
            if done:
                break
    for j in range(len(removelist)-1, -1 , -1):
        del y[removelist[j]]
        del z[removelist[j]]
    removelist=[]


score=0
for i in range(5):
    for j in range(5):
        if b[i][j]=="o":
            print(a[i][j])
            score+=int(a[i][j])
            print(score)
score*=int(c)
print(score)
