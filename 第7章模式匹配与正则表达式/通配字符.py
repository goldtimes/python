# '.'句号通配字符匹配除了换行符外的所有字符，但是只能匹配一个字符
import re
rex = r'.at'
atRegex = re.compile(rex)
print(atRegex.findall('The cat in the hat sat on the flat mat.'))
#根据输出的flat来看 ，之输出了flat，所以句号是匹配一个字符
