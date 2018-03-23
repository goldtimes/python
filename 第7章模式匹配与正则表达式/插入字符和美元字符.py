import re
startRex = r'^Hello'
startRegex = re.compile(startRex)
match= startRegex.search('Hello world')
print(match.group())
print(startRegex.search('he said hello.') == None)

endsWithNumber = r'\d+$'
endsWithNumRegex = re.compile(endsWithNumber)
match1 = endsWithNumRegex.findall('your  number is 17333436')
print(match1)