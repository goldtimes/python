import pprint
#统计字符串当中个字符出现的次数
message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
#用字典的想法很不错，字符和它出现的次数关联起来，
count={}
for character in message:
    #这里用到了setdefault函数，当字典中含有键时，返回对应的值
    #字典中没有该键值，设置一个对应键值对
    count.setdefault(character,0)
    count[character] = count[character] + 1
pprint.pprint(count)