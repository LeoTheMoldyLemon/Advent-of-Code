from math import *
f=open("input.txt", "r")
x=""
a=f.readline()
while a!="":
    x+=a
    a=f.readline()
x=x.split("\n")
for i in range(len(x)):
    x[i]=x[i].split()
var=["x", "y", "z", "w"]
inpu="99999999999999"







def run(inp):
    mem=[0,0,0,0]
    for i in range(len(x)):
        if x[i][0]=="inp":
            mem[var.index(x[i][1])]=int(inp[0])
            inp=inp[1:]
        elif x[i][0]=="add":
            if x[i][2] in var:
                void=mem[var.index(x[i][2])]
            else:
                void=int(x[i][2])
            mem[var.index(x[i][1])]+=void
        elif x[i][0]=="mul":
            if x[i][2] in var:
                void=mem[var.index(x[i][2])]
            else:
                void=int(x[i][2])
            mem[var.index(x[i][1])]*=void
        elif x[i][0]=="div":
            if x[i][2] in var:
                void=mem[var.index(x[i][2])]
            else:
                void=int(x[i][2])
            mem[var.index(x[i][1])]=trunc(mem[var.index(x[i][1])]/void)
        elif x[i][0]=="mod":
            if x[i][2] in var:
                void=mem[var.index(x[i][2])]
            else:
                void=int(x[i][2])
            mem[var.index(x[i][1])]%=void
        elif x[i][0]=="eql":
            if x[i][2] in var:
                void=mem[var.index(x[i][2])]
            else:
                void=int(x[i][2])
            if mem[var.index(x[i][1])]==void:
                mem[var.index(x[i][1])]=1
            else:
                mem[var.index(x[i][1])]=0
        else:
            print("ERROR")
    return(mem[var.index("z")])
i=0
while True:
    i+=1
    if i%100000==0:
        print(inpu)
        print(run(inpu))
    if run(inpu)==0:
        print(inpu)
        break
    else:
        inpu=str(int(inpu)-1)
        while "0" in inpu:
            inpu=str(int(inpu)-1)
            





            
