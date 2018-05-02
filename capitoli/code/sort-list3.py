import os, fnmatch, pickle


file = open("terms3.txt", "r") 
aList = file.readlines()
bList = []


for s in aList:
    line = s.capitalize()
    index = line.index(",")
    name= line[:index]
    diac= line[index+1:len(line)-1].capitalize()
    if diac.startswith( '{', 2 ):
        if diac.startswith('\\', 3):
            diac = diac.replace(diac[4],diac[4].capitalize(),1)
        else:
            diac = diac.replace(diac[3],diac[3].capitalize(),1)

    index = diac.index(",")
    diacnew= diac[:index]
    nome = diac[index+1:len(diac)].capitalize()
    line = name + "," + diacnew + "," + nome + "\n"
    print line
    bList.append(line)

aList.extend(bList);

aList.sort();
bList.sort();

print "List : ", aList

with open('glossario.txt', 'w') as f:
    
    for s in bList:
        f.write(s)

