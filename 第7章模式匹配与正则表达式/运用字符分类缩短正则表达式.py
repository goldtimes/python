import re
#一个或多个数字后面跟空白字符接下来是一个或者多个单词
rex = r'\d+\s\w+'
xmasRexgex = re.compile(rex)
resultList = xmasRexgex.findall('12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, 7 '
                           'swans, 6 geese, 5 rings, 4 birds, 3 hens, 2 doves, 1 partridge')
print(resultList)