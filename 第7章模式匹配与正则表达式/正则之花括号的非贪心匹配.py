# 在字符串'HaHaHaHaHa'中，因为(Ha){3,5}可以匹配 3 个、 4 个或 5 个实例，你可能
# 会想，为什么在前面花括号的例子中， Match 对象的 group()调用会返回'HaHaHaHaHa'，
# 而不是更短的可能结果。
import re
rex = r'(Ha){3,5}'
greedyHaRegex = re.compile(rex)
match = greedyHaRegex.search('HaHaHaHaHa')
print(match.group())
rex1 = r'(Ha){3,5}?'
nongreedyHaRegex = re.compile(rex1)
match1 = nongreedyHaRegex.search('HaHaHaHaHa')
print(match1.group())
