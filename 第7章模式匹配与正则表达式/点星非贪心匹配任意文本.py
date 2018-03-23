import re
rex = r'<.*?>'
nongreedyRegex = re.compile(rex)
match = nongreedyRegex.search('<To serve man> for dinner')
print(match.group())

greedyRegex = re.compile(r'<.*>')
match1 = greedyRegex.search('<To serve man> for dinner>' )
print(match1.group())

#re.compile(rex,arg2)
# 通过传入指定的参数可以改变通配符的匹配规则

nonNewLineRegex = re.compile(r'.*')
match2 = nonNewLineRegex.search('Serve the public trust.\nProtect the innocent.\nUphold the law')
print(match2.group())

NewLineRegex = re.compile(r'.*',re.DOTALL)
match3 = NewLineRegex.search('Serve the public trust.\nProtect the innocent.\nUphold the law')
print(match3.group())