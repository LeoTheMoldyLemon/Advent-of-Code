f=open(r"D:\desktop\Programming\Advent of code\2020\input.txt","r")
leng=len(f.readlines())
f.seek(0)
a={}
for i in range(leng):
    item=f.readline()
    item=item.split("bag")
    item[0]=item[0].strip()
    item[1]=item[1][10:len(item[1])-1]
    for j in range(len(item)-3):
        if item[j+2][0]=="s":
            item[j+2]=item[j+2][3:len(item[j+2])-1]
        else:
            item[j+2]=item[j+2][2:len(item[j+2])-1]
    del(item[len(item)-1])
    a[item[0]]=item[1:len(item)]



n=0

def bags(target, num):
    result=0
    if a[target][0]!="no other":
        for i in range(len(a[target])):
            result+=bags(a[target][i][2:len(a[target][i])], int(a[target][i][0]))*num
    return(result+num)
        

    
print(bags("shiny gold", 1)-1)#ovaj program će raditi i izbaciti točan rezultat, -1 je tu jer on broji i samu shiny gold torbu, koju ne trebamo brojati

