import os, fnmatch, pickle


file = open("terms.txt", "r") 
aList = file.readlines()
print aList

aList.sort();
print "List : ", aList
with open('sorted-terms.txt', 'w') as f:
    for s in aList:
        f.write(s)
    

    
