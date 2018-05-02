import os, fnmatch


def findReplace(directory, find, replace, filePattern):
    for path, dirs, files in os.walk(os.path.abspath(directory)):
        for filename in fnmatch.filter(files, filePattern):
            filepath = os.path.join(path, filename)

            with open(filepath) as f:
                s = f.read()
            s = s.replace(find, replace)
            with open(filepath, "w") as f:
                f.write(s)




#rootdir = "Documents/Ayurveda/TESI/Python/dir/"

#print "PATH: " + os.path.abspath(rootdir)

file = open("terms.txt", "r") 
for line in file: 
    print line
    index = line.index(";")
    find= line[:index]
    replace= line[index+1:len(line)-1]
    print "find: " + find
    print "replace: " + replace
    #findReplace('..', find, replace, "*.tex")
    findReplace('.', find, replace, "*.tex")

    
    #for root, dirs, files in os.walk('..'):
#        for name in files:
#            print(os.path.join(root, name))
#        for name in dirs:
#            print(os.path.join(root, name))


    

