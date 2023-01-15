n=[]
for i in range(1000):
    a=input()
    n.append([int(a.split(":")[0].split()[0].split("-")[0]), int(a.split(":")[0].split()[0].split("-")[1]), a.split(":")[0].split()[1], a.split(":")[1]])
    
b=0
for i in range(len(n)):
    if n[i][3][n[i][0]]==n[i][2] and n[i][3][n[i][1]]!=n[i][2] or n[i][3][n[i][0]]!=n[i][2] and n[i][3][n[i][1]]==n[i][2]:
        print(n[i][3], n[i][0], n[i][1], True)
        b+=1
    print(n[i][3], n[i][0], n[i][1], False)
print(b)
