import os
import shutil

#current working directory
path = os.getcwd()
print(path)

#name of new directory
folderName = 'newDir'

#creating new directory
os.mkdir(folderName)

#creating file inside new directory
f = open(folderName + '/' + 'newfile', 'w')
f.close()

#removing new directory
shutil.rmtree(folderName)

