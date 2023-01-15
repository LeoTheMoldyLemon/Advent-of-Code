f=open("input.txt", "rt")
l=[]
a=f.readline()
while(a!=""):
    a=a.replace("\n", "").replace(" ", "")
    l.append(a)
    a=f.readline()

rocks=["AY","BX","CZ"]
papers=["AZ", "BY", "CX"]
points={"X":0, "Y":3, "Z":6}
score=0
for i in range(len(l)):
    score+=points[l[i][1]]
    if l[i] in rocks:
        score+=1
    elif l[i] in papers:
        score+=2
    else:
        score+=3
    
