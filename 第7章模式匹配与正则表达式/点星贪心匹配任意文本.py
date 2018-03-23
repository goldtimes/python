# '.'代表除换行符的任意字符
# '*'匹配的字符出现零次或者多次
# python 默认是贪心的匹配原则,所以.*组合在一起可以匹配任意的字符
import re
rex = r'First Name:(.*) Last Name:(.*)'
nameRegex = re.compile(rex)
match = nameRegex.search('First Name:Al Last Name:Sweigar')
print(match.group(1))
print(match.group(2))
print(match.groups())