import zipfile
exampleZip = zipfile.ZipFile('C:\\Users\\lh101\\Desktop\\example.zip')
print(exampleZip.namelist())
spamInfo = exampleZip.getinfo('spam.txt')
print(spamInfo.file_size)
print(spamInfo.compress_size)
exampleZip.close()

exampleZip = zipfile.ZipFile('C:\\Users\\lh101\\Desktop\\example.zip')
exampleZip.extractall('C:\\Users\\lh101\\Desktop\\example')

newZip = zipfile.ZipFile('C:\\Users\\lh101\\Desktop\\newZip.zip','w')
newZip.write('C:\\Users\\lh101\\Desktop\\spam.txt',compress_type=zipfile.ZIP_DEFLATED)
newZip.close()
