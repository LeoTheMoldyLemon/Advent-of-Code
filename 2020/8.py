a=[]
f=open(r"D:\desktop\Programming\Advent of code\2020\input.txt", "r")
length=len(f.readlines())
f.seek(0)
for i in range(length):
    x=f.readline()
    a.append([x[0:3], int(x[4:len(x)-1])])



for j in range(len(a)):
    if a[j][0]=="nop":
        a[j][0]="jmp"
    elif a[j][0]=="jmp":
        a[j][0]="nop"
    
    used=[]
    i=0
    acc=0
    print(j)
    while not i in used:
        if i == 641:
            print("RESULT:",acc)
            break
        x=a[i]
        used.append(i)
        if x[0]=="acc":
            i+=1
            acc+=x[1]
        elif x[0]=="jmp":
            i+=x[1]
        elif x[0]=="nop":
            i+=1
        else:
            print(error, i, x)
    if a[j][0]=="nop":
        a[j][0]="jmp"
    elif a[j][0]=="jmp":
        a[j][0]="nop"
        
