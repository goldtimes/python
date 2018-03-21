import re
regex = r'(\d{3})-(\d{3}-\d{4})'
phoneNumRegex = re.compile(regex)
match = phoneNumRegex.search('My number is 415-555-4242')
print(match.group(1))
print(match.group(2))
print(match.groups())
#如果区号是括号的电话格式
regex1 = r'(\(\d{3}\)) (\d{3}-\d{4})'
match1 = re.compile(regex1).search('My number is (425) 555-4343')
print(match1.groups())