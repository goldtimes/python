import pprint
cats = [{'name':'Zophie','dec':'chubby'},{'name':'Pooka','dec':'fluffy'}]
str = pprint.pformat(cats)
print(str)
fileObj = open('myCats.py','w')
fileObj.write('cats = ' + str + '\n')
fileObj.close()