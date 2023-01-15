
from copy import *
f=open("inputtest.txt", "rt")
ss=4
a=f.readline()
m=[]
while a!="\n":
    m.append(a.replace("\n", ""))
    a=f.readline()
nm=[]
for i in range(ss):
    nm.append("")
    for j in range(ss*2):
        nm[-1]+=" "
    for j in range(ss):
        nm[-1]+=m[i][j+ss]
    for j in range(ss):
        nm[-1]+=""

for i in range(ss):
    nm.append("")
    for j in range(ss):
        nm[-1]+=m[4*ss-j-1][i]
    for j in range(ss):
        nm[-1]+=m[3*ss-j-1][i]
    for j in range(ss):
        nm[-1]+=m[ss+i][ss+j]
    for j in range(ss):
        nm[-1]+=" "
        
for i in range(ss):
    nm.append("")
    for j in range(ss*2):
        nm[-1]+=" "
    for j in range(ss):
        nm[-1]+=m[i+2*ss][j+ss]
    for j in range(ss):
        nm[-1]+=m[ss-i-1][3*ss-j-1]

def printm():
    global nm
    for i in range(len(nm)):
        print(nm[i])

        

    
