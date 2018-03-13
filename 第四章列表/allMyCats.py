#创建一个列表值来存储相关的信息，猫的名字
catNames = [] #创建一个空的列表
while True:
    print('Enter the name of cat ' + str(len(catNames) + 1) + ' (or enter nothing to stop.')
    catName = input()
    if catName == '':
        break
    catNames = catNames + [catName] #使用列表的拼接特性
print('The cat names are: ')
for name in catNames:
    print(' ' + name)