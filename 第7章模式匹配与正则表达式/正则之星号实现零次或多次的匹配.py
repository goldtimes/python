import re
rex = r'Bat(wo)*man'
batRegex = re.compile(rex)
match = batRegex.search('The Adventures of Batman')
print(match.group())
match1 = batRegex.search('The Adventures of Batwoman')
print(match1.group())
match2 = batRegex.search('The Adventures of Batwowowowoman')
print(match2.group())