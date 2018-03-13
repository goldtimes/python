#假设一个字典管理朋友的生日信息，程序判断是否有这个信息，有则打印出来，没有就添加到字典中
birthdays={'Alice':'Apr 1','Bob':'Dec 12','Carol': 'Mar 4'}
while True:
    print('Enter a name:(blank to quic')
    name = input()
    if name == '':
        break
    if name in birthdays:#通过键查询字典里面是否包括这样的键值对，否则键不存在会出现异常
        print(birthdays[name] + ' is  the birthday of ' + name)
    else:
        print('I don\'t have information for ' + name)
        print('What\'s their birthday?')
        bday = input()
        birthdays[name] = bday #通过这样的赋值语句将键值对关联起来
        print('Birthday database updated')