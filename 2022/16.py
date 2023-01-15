import sys
import functools

sys.setrecursionlimit(2000)


f=open("input.txt", "rt")
a=f.readline()
l={}
while a!="":
    a=a.replace("Valve ", "").replace("has flow rate=", "").replace("; tunnels lead to valves", "").replace("; tunnel leads to valve", "").replace(",", "").replace("\n", "").split()
    l[a[0]]=[int(a[1]), a[2:]]
    a=f.readline()



pressures=[]
@functools.lru_cache(maxsize=None)
def testpath(valvee, valvem, timeleft, valves):
    if(timeleft==0):
        return 0

    best=0
    for i in l[valvee][1]:
        for j in l[valvem][1]:
            best=max(best, testpath(i,j, timeleft-1, valves))

    rele=0
    relm=0
    if valvee not in valves:
        rele=l[valvee][0]*(timeleft-1)
    if valvem not in valves:
        relm=l[valvem][0]*(timeleft-1)

    if relm>0:
        for i in l[valvee][1]:
            best=max(best, relm+testpath(i,valvem, timeleft-1, valves+(valvem,)))
    if rele>0:    
        for j in l[valvem][1]:
            best=max(best, rele+testpath(valvee,j, timeleft-1, valves+(valvee,)))
            
    if valvee!=valvem and rele>0 and relm>0:
        best=max(best, rele+relm+testpath(valvee,valvem, timeleft-1, valves+(valvee,valvem)))


        
            
    return best




print(testpath("AA", "AA", 26, ()))
        
