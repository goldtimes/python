absHelloFile = open('C:\\Users\\lh101\\Desktop\\absHelloWorld.txt','r')#以读的模式打开文件，而不对文件进行任何的修改
content = absHelloFile.read()
print(content)

relHelloFile = open('relHelloWorld')
content1 = relHelloFile.read()
print(content1)

absHelloFile.close()
relHelloFile.close()
#通过readlines 方法取得字符串列表

sonnetFile = open('sonnet29')
#这里同时用了readline()和readlines()方法，从输出可以看出
#对于文件之打开了一个读的游标，当readline()并不打印换行符，而是输出换行。读完，游标移到了下一行开始，readlines从这个游标开始读取
print(sonnetFile.readline())
contentList = sonnetFile.readlines()#将末尾的换行符也会显示在字符串中
print(contentList)
sonnetFile.close()


