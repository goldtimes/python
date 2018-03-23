import re
regex = r'Agent \w+'
namesRegex = re.compile(regex)
result = namesRegex.sub('CENSORED','Agent Alice gave the secret documents to Agent Bob.')
print(result)
agentNamesRegex = re.compile(r'Agent (\w)\w*')
print(agentNamesRegex.sub('r\1****', 'Agent Alice told Agent Carol that Agent Eve knew Agent Bob was a double agent.'))

