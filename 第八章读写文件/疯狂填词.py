import re
madFile = open('mad libs','r')
content = madFile.read()
print(content)

contentList = content.split()

rex1 = 'ADJECTIVE'
regex1 = re.compile(rex1)
rex2 = 'NOUN'
regex2 = re.compile(rex2)
rex4 = 'VERB'
regex4 = re.compile(rex4)
#for word in contentList:
#这里还是得用正则表达式去匹配，并替换
"""   if 'ADJECTIVE' in word:
        print('Enter an adjective:')
        contentList[contentList.index(word)] = input()
    if 'NOUN' in word:
        print('Enter an noun:')
        contentList[contentList.index(word)] = input()
    if 'ADVERB' in word:
        print('Enter an adverb:')
        contentList[contentList.index(word)] = input()
    if 'VERB' in word:
        print('Enter an verb:')
        inputStr = input()
        contentList[contentList.index(word)]
"""
for word in contentList:
    if regex1.search(word) != None:
        print('Enter an adjective:')
        inputStr = input()
        contentList[contentList.index(word)] = regex1.sub(inputStr,word)

    if regex2.search(word) != None:
        print('Enter an NOUN:')
        inputStr = input()
        contentList[contentList.index(word)] = regex2.sub(inputStr, word)
    if regex4.search(word)!= None:
        print('Enter an VERB:')
        inputStr = input()
        contentList[contentList.index(word)] = regex4.sub(inputStr, word)
print(contentList)
print(' '.join(contentList))
madFile.close()
madFile = open('new mad libs','w')
madFile.write(' '.join(contentList))
madFile.close()