import re
haRegex = re.compile(r'(Ha){3,5}')
haRegex1 = re.compile(r'(HA){,5}')
match = haRegex.search('HaHaHa')
print(match.group())
print(haRegex.search('HaHaHaHa').group())
print(haRegex.search('HaHaHaHaHa').group())
print(haRegex1.search('dasda').group() == '')
print(haRegex1.search('HA').group())
print(haRegex1.search('HAHAHAHAHA').group())
