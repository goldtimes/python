# 通过正则表达式来找到文本中的电话号码
import re
phoneNumRegex = re.compile(r'\d{3}-\d{3}-\d{4}')
match = phoneNumRegex.search('My number is 415-555-4242')
print('Phone number found: ' + match.group())
