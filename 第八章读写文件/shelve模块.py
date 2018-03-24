import shelve
shelveFile = shelve.open('mydata')
cats = ['Zopheis','Pooka','Simon']
#shelve是通过字典的方式保存变量的值 key = 'cats' value = cats
shelveFile['cats'] = cats
shelveFile.close()

shelveFile = shelve.open('mydata')
print(shelveFile['cats'])
shelveFile.close()

#使用shelve模块保存变量可以看到生成了三个文件 mydata.bak mydata.dat mydata.dir