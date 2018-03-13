#创建一个列表
spam = ['cat','bat','rat','elephant']
print(spam)
# 用下标访问列表，下表0开始依次数
print(spam[0])
print(spam[1])
print(spam[2])
print(spam[3])
spam1 = [['cat','bat'],[10,20,30,40,50]]
print(spam1[0][0])
print(spam1[0][1])
print(spam1[1][0])
print(spam1[1][1])
print(spam1[1][2])
print(spam1[1][3])
print(spam1[1][4])
#负数下表
print(spam[-1])
print(spam[-4])
#切片
print(spam[1:4])
print(spam[0:-1])
print(spam[:4])
print(spam[1:])
print(spam[:])
#len()取得列表的长度
print(len(spam))
#改变列表中的元素
spam[-1] = 'dog'
print(spam)
#'+''*'实现列表的拼接和复制
list1 = [1,2,3]
list2 = ['a','b','c']
print(list1 + list2)
print(list1 * 2)
#del 列表表项
print(list1)