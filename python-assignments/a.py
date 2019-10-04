'''
python code to find the current working directory also do the following operations:
A. creating a new directory.
B. create a new text file in the new directory.
C. delete the new directory.
'''

import os

cwd = os.getcwd()
print(cwd)

try:
    os.mkdir('NewDirectory')
except FileExistsError:
    print("Directory already exists")

with open(cwd+"/NewDirectory"+"/"+"NewFile.txt", "w") as f:
    f.write("")


'''
METHOD 2
import shutil
shutil.rmtree(path)
'''