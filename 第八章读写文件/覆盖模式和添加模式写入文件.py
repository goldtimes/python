baconFile = open('bacon.txt','w')
baconFile.write('Hello world')
baconFile.close()

baconFile = open('bacon.txt','a')
baconFile.write('Bacon is not a vegetable.')
baconFile.close()

baconFile = open('bacon.txt','r')
content = baconFile.read()
print(content)
baconFile.close()