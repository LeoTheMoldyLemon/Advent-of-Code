a=[]
f=open(r"D:\desktop\Programming\Advent of code\2020\input.txt", "r")
length=len(f.readlines())
f.seek(0)
for i in range(length):
    x=f.readline()
    a.append(int(x[0:len(x)-1]))
joltdif=[0,0,0]
curjolt=0
a.sort()
print(a)
jl=[]
for i in range(len(a)):
    done=False
    for j in range(len(a)):
        if a[j]==curjolt+1:
            curjolt=a[j]
            joltdif[0]+=1
            jl.append(1)
            done=True
            break  
    if not done:
        for j in range(len(a)):
            if a[j]==curjolt+2:
                curjolt=a[j]
                joltdif[1]+=1
                jl.append(1)
                done=True
                break  
    if not done:
        for j in range(len(a)):
            if a[j]==curjolt+3:
                curjolt=a[j]
                joltdif[2]+=1
                jl.append(3)
                done=True
                break
    if not done:
        print("error ", a[i], curjolt)
print(jl)
jl.append(3)
jline=0
ml=1
for i in range(len(jl)):
    if jl[i]==1:
        jline+=1
    if jl[i]==3:
        if jline==2:
            ml*=2
        if jline==3:
            ml*=4
        if jline==4:
            ml*=7
        if jline==5:
            ml*=8
            print("error", i)
        jline=0
