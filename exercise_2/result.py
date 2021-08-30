import os
import glob
from sys import platform



if platform.startswith('linux'):
    slash ='/'
elif platform.startswith('win32'):
    slash = '\\'

path = os.getcwd()
print(path)
#(dirname, filename) = os.path.split(path)
#dirname1 = os.path.expanduser(dirname)
#home = os.path.expanduser("~")
dirPhoto = path+slash+'main_folder'

dataList = list(os.walk(dirPhoto))
pathList = list(set(map(lambda i:dataList[i][0],range(len(dataList)))))
photoList = list(filter(None,(map(lambda i:glob.glob(pathList[i]+slash+'*.jpg'),range(len(pathList))))))
photoList = sum(photoList,[])
#printing photo namprint(len(pathList))
photoName = list(map(lambda i:os.path.basename(photoList[i]),range(len(photoList))))
print('3.Names of all the pictures:')
print('\n'.join(map(str, photoName)))

print('4.The numbers of all the pictures:')
print(len(photoName))
print('5.The number of all the folders:')
print(len(pathList))
print('6.The full paths to all the folders:')
print('\n'.join(map(str, pathList)))
print('\n7.Dictionary with the key is the name of each picture is parent folder and value is a list of all of the pictures inside the parent folder.')
#print(photoList)



print('\n8.Print a filtered list with the name of the folders that contains the letter i ')
filesName  = list(map(lambda i:os.path.basename(pathList[i]),range(len(pathList))))
filesNameWithI = list(filter(lambda file: file.find("i") > -1, filesName))
print(filesNameWithI)
