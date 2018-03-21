#？ 指这个模式是可选的，不论文本中是否出现，正则表达式都是认为匹配的
import re
rex = r'Bat(wo)?man'
batRegex = re.compile(rex)
match = batRegex.search('The Adventures of Batman')
print(match.group())
match1 = batRegex.search('The Adventures of Batwoman')
print(match1.group())
#如果文本中不存在要匹配的字符就会出现异常NoneType
#match2 = batRegex.search('The Adventures of Baoman')
#print(match2.group())
phoneRex = r'(\d{3}-)?\d{3}-\d{4}'
phRegex = re.compile(phoneRex)
phMatch = phRegex.search('My number is 415-555-4232')
print(phMatch.group())
phMatch1 = phRegex.search('My number is 555-4232')
print(phMatch1.group())
