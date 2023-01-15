
x=[]
for i in range(200):
    x.append(int(input()))

for i in range(len(x)):
    for j in range(len(x)):
        for k in range(len(x)):
            if i!=j and i!=k and x[i]+x[j]+x[k]==2020:
                print(x[i]*x[j]*x[k])
