"""
    练习使用字符串方法
    .upper(),.lower()返回一个新的字符串，而非在原有的字符串去修改的
    字符串是不可变的数据类型
    .islower() .isupper()是判断字符串中至少有一个字母，并且字母都是大写或者小写返回True
"""
spam = 'Hello World'
spam.upper()
print(spam)
spam = spam.upper()
print(spam)
spam = spam.lower()
print(spam)
#spam[1] = 'E'
#print(spam)
print(spam.islower())
print('123456ABC'.isupper())
#由于.low()和.upper是返回一个新的字符串就可以进行链式的调用
spam1 = 'hello world'
print(spam1.upper().isupper())
print('hello'.isalpha())
print('hello123'.isalnum())
print('12345'.isdecimal())
print('     '.isspace())
print('Title'.istitle())
#startwith(),endwith()
print('hello world'.startswith('hello'))
print('hello world'.endswith('world'))
#split()方法
spam2 = '''Dear Alice,
How have you been? I am fine.
There is a container in the fridge
that is labeled "Milk Experiment".
Please do not drink it.
Sincerely,
Bob
'''
print(spam2.split('\n'))
print(','.join(['cata','rat','bats']))
