import re
rex = r'[aeiouAEIOU]' #[]方括号内的任意字符
vowelRegex = re.compile(rex)
matchList = vowelRegex.findall('RoboCop eats baby food. BABY FOOD.accout')
print(matchList)
rex1 = r'[0-5.]'
Regex = re.compile(rex1)
match =Regex.findall('123.6')
print(match)
#在方括号内加上^符号，将匹配不在自定义的字符类中的字符
consonantRegex = re.compile(r'[^aeiouAEIOU]')
matchList1 = consonantRegex.findall('RoboCop eats baby food. BABY FOOD.accout')
print(matchList1)