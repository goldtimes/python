""" ---PICNIC ITEMS--
    sandwiches.. 4
    apples...... 12
    cups........ 4
    cookies..... 8000
    -------PICNIC ITEMS-------
    sandwiches.......... 4
    apples.............. 12---PICNIC ITEMS--
sandwiches.. 4
apples...... 12
cups........ 4
cookies..... 8000
-------PICNIC ITEMS-------
sandwiches.......... 4
apples.............. 12
cups................ 4
cookies............. 8000
    cups................ 4
    cookies............. 8000   """
#通过rjust()右对齐，ljust()左对齐,center()居中三个方法实现这样的列表
#标题是一个字符串，下面是一个字典。要对这两种数据类型去实现两次不同格式的对齐，那么需要去定义一个函数来完成
#第一次字典左边是12个宽度，采用'.'左对齐，右边是数字5个宽度，采用' '对齐
#第二次字典左边是20个宽度，采用'.'左对齐，右边是数字6个宽度，采用' '对齐
def printPicnic(itemDict,leftWidth,rightWidth):
    print('PICNIC ITEMS'.center(leftWidth+rightWidth,'-'))
    for key,value in itemDict.items():
        print(key.ljust(leftWidth,'.') + str(value).ljust(rightWidth))
picnicItems = {'sandwiches':4,'apple':12,'cups':4,'cookies':8000}
printPicnic(picnicItems,12,5)
printPicnic(picnicItems,20,6)