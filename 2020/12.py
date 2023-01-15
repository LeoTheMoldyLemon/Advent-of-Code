f=open(r"D:\desktop\Programming\Advent of code\2020\input.txt", "r")
length=len(f.readlines())
f.seek(0)
a=[]
for i in range(length):
    x=f.readline().split("\n")[0]
    a.append([x[0],int(x[1:len(x)])])

coords=[0,0]
direct=[1, 10]
for i in range(len(a)):
    
    if a[i][0]=="N":
        direct[0]+=a[i][1]
        
    if a[i][0]=="S":
        direct[0]-=a[i][1]
        
    if a[i][0]=="E":
        direct[1]+=a[i][1]
        
    if a[i][0]=="W":
        direct[1]-=a[i][1]
        
    if a[i][0]=="F":
        coords[0]+=a[i][1]*direct[0]
        coords[1]+=a[i][1]*direct[1]
        
    if a[i][0]=="R":
        for j in range(a[i][1]//90):
            vert=direct[0]
            horiz=direct[1]
            direct[0]=-horiz
            direct[1]=vert
           
    if a[i][0]=="L":
        for j in range(a[i][1]//90):
            vert=direct[0]
            horiz=direct[1]
            direct[0]=horiz
            direct[1]=-vert
            
    print(coords, direct, a[i], i)
print(abs(coords[0])+abs(coords[1]), coords)

        
        
