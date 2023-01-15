a=[]
f=open(r"D:\desktop\Programming\Advent of code\2020\input.txt", "r")
endl=True
line=-1
for i in range(1102):
    x=f.readline()
    if endl:
        endl=False
        a.append(x.split())
        line+=1
    elif x!="\n":
        a[line].extend(x.split())
    else:
        endl=True
stuff={"byr":False, "iyr":False, "eyr":False, "hgt":False, "hcl":False, "ecl":False, "pid":False}
result=0
for i in range(len(a)):
    stuff={"byr":False, "iyr":False, "eyr":False, "hgt":False, "hcl":False, "ecl":False, "pid":False}
    for j in range(len(a[i])):
        if a[i][j][0:3] in stuff.keys():
            if a[i][j][0:3]=="byr":
                try:
                    if 1919<int(a[i][j][4:len(a[i][j])])<2003:
                        stuff[a[i][j][0:3]]=True
                except (ValueError, IndexError):
                    print("Error:invalid", a[i][j])
            elif a[i][j][0:3]=="iyr":
                try:
                    if 2009<int(a[i][j][4:len(a[i][j])])<2021:
                        stuff[a[i][j][0:3]]=True
                except (ValueError, IndexError):
                    print("Error:invalid", a[i][j])
            elif a[i][j][0:3]=="eyr":
                try:
                    if 2019<int(a[i][j][4:len(a[i][j])])<2031:
                        stuff[a[i][j][0:3]]=True
                except (ValueError, IndexError):
                    print("Error:invalid", a[i][j])
            
            elif a[i][j][0:3]=="hgt":
                try:
                    if a[i][j][len(a[i][j])-2:len(a[i][j])]=="cm":
                        if 149<int(a[i][j][4:len(a[i][j])-2])<194:
                            stuff[a[i][j][0:3]]=True
                    elif a[i][j][len(a[i][j])-2:len(a[i][j])]=="in":
                        if 58<int(a[i][j][4:len(a[i][j])-2])<77:
                            stuff[a[i][j][0:3]]=True
                except (ValueError, IndexError):
                    print("Error:invalid", a[i][j])
                            
            elif a[i][j][0:3]=="hcl":
                try:
                    if a[i][j][4]=="#" and len(a[i][j])==11:
                        provjera=True
                        for k in range(5, 11):
                            if 96<ord(a[i][j][k])<103 or 47<ord(a[i][j][k])<58: 
                                stuff[a[i][j][0:3]]=True
                        
                except (ValueError, IndexError):
                    print("Error:invalid", a[i][j])
                        
            elif a[i][j][0:3]=="ecl":
                print(a[i][j][0:3])
                try:
                    if a[i][j][4:len(a[i][j])] in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
                        stuff[a[i][j][0:3]]=True

                except (ValueError, IndexError):
                    print("Error:invalid", a[i][j])
            
            elif a[i][j][0:3]=="pid":
                try:
                    if int(a[i][j][4:len(a[i][j])]) and len(a[i][j][4:len(a[i][j])])==9:
                        stuff[a[i][j][0:3]]=True

                except (ValueError, IndexError):
                    print("Error:invalid", a[i][j])



    proof=True
    key=list(stuff.keys())
    print(stuff)
    for j in range(len(key)):
        if not stuff[key[j]]:
            proof=False
    if proof:
        result+=1
print(result)
        
