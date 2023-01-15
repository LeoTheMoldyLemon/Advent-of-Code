import copy
f=open("input.txt", "rt")
a=f.readline()
l=[]

while a!="":
    l.append(eval(a))
    l.append(eval(f.readline()))
    f.readline()
    a=f.readline()
    

r=[]
def order(a,b):
    
    if a==[] and b!=[]:
        return [True,True]
    elif b==[] and a!=[]:
        return [True,False]
    elif a==[] and b==[]:
        return [False, False]

    if(isinstance(a[0],list) and isinstance(b[0],int)):
        b[0]=[b[0]]
    elif(isinstance(b[0],list) and isinstance(a[0],int)):
        a[0]=[a[0]]
    


    
    for i in range(max(len(a),len(b))):
        if a==[] and b!=[]:
            return [True,True]
        elif b==[] and a!=[]:
            return [True,False]
        
        if(isinstance(a[0],list) and isinstance(b[0],int)):
            b[0]=[b[0]]
        elif(isinstance(b[0],list) and isinstance(a[0],int)):
            a[0]=[a[0]]

        if(isinstance(a[0],list) and isinstance(b[0],list)):
            ch=order(a[0],b[0])
            if ch[0]:
                return ch
        else:
            if(a[0]>b[0]):
                return [True, False]
            elif(b[0]>a[0]):
                return [True,True]
        a.pop(0)
        b.pop(0)
    return [False, False]


l.append([[2]])
l.append([[6]])
promjena=True
while promjena:
    print("a")
    promjena=False
    for i in range(len(l)-1):
        if not order(copy.deepcopy(l[i]),copy.deepcopy(l[i+1]))[1]:
            h=l[i]
            l[i]=copy.deepcopy(l[i+1])
            l[i+1]=copy.deepcopy(h)
            promjena=True
res=1
for i in range(len(l)):
    if l[i]==[[2]] or l[i]==[[6]]:
        res*=i+1



































