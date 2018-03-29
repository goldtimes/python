import os
for folderName,subFolders,fileNames in os.walk('F:\\迅雷下载'):
    print('The Current folder is: ' + folderName)
    for subFolder in subFolders:
        print('Subfolder of ' + folderName + ': ' + subFolder)
    for  fileName in fileNames:
        print('file inside ' + folderName + ': ' + fileName)
    print(' ')