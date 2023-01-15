f=open("input.txt")
a=f.readline()
x=[]
while a!="":
    if a[len(a)-1]=="\n":
        a=a[:len(a)-1]
    x.append(a)
    a=f.readline()

result=0
corrupted=[]
for i in range(len(x)):
    b=""
    for j in range(len(x[i])):
        if x[i][j] in "([{<":
            b+=")]}>"["([{<".index(x[i][j])]
        else:
            if x[i][j]==b[len(b)-1]:
                b=b[:len(b)-1]
            else:
                if x[i][j]==")":
                    result+=3
                elif x[i][j]=="]":
                    result+=57
                elif x[i][j]=="}":
                    result+=1197
                elif x[i][j]==">":
                    result+=25137
                else:
                    print("aaaaaaAAAAAAAAAAA")
                corrupted.append(i)
                break
y=[]
for i in range(len(x)):
    if not i in corrupted:
        y.append(x[i])

result=[]

for i in range(len(y)):
    b=""
    for j in range(len(y[i])):
        if y[i][j] in "([{<":
            b+=")]}>"["([{<".index(y[i][j])]
        else:
            b=b[:len(b)-1]
    score=0
    print(b)
    for j in range(len(b)-1, -1, -1):
        score*=5
        score+=1
        if b[j]=="]":
            score+=1
        elif b[j]=="}":
            score+=2
        elif b[j]==">":
            score+=3
    print(score)
    result.append(score)
result.sort()
print(result[round((len(result))/2-0.1)])

























