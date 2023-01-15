f=open("testinput.txt", "r")
b=f.readline()
f.readline()
void=f.readline()
im=""
while void!="":
    im+=void
    void=f.readline()
im=im.split("\n")


def printim():
    f=open("output.txt", "w")
    for i in range(len(im)):
        f.write(im[i]+"\n")




def enhance(y,x):
    num=im[y-1][x-1:x+2]+im[y][x-1:x+2]+im[y+1][x-1:x+2]
    num=num.replace("#", "1")
    num=num.replace(".", "0")
    num=int(num, 2)
    return b[num]

for j in range(len(im)):
    im[j]=("."*300)+im[j]+("."*300)
for j in range(300):
    im.append(len(im[0])*".")
    im.insert(0,len(im[0])*".")

printim()




for i in range(50):
    nim=[]
    for y in range(1, len(im)-1):
        nim.append("")
        for x in range(1, len(im[y])-1):
            nim[y-1]+=enhance(y,x)
    im=list(nim)
    print(i)

for i in range(0):
    del im[0]
    
for i in range(0):
    del im[len(im)-1]

for i in range(len(im)):
    im[i]=im[i][3*50:len(im[i])-(3*50)]



counter=0
for i in range(len(im)):
    counter+=im[i].count("#")
print(counter)







