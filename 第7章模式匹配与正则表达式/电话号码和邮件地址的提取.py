#！python3
import re
import pyperclip

phoneRegex = re.compile(r'''
     (\d{3}| \(\d{3}\))?          #区号 两种形式，用管道符号来匹配多个表达式
     (\s|-|\.)?
     (\d{3})
     (\s|-|\.)
     (\d{4})
''',re.VERBOSE)