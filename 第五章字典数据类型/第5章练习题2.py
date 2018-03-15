# 将列表转换成字典
# 还是联系上一个练习题
# 征服一条龙所得到的战利品
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
#原始的物品信息
stuff ={'gold coin':42,'rope':1}
#添加一个addToInventory函数将战利品添加至字典的信息
def addToInventory(stuff,addItems):
    for i in range(len(addItems)):
        stuff.setdefault(addItems[i],0)
        stuff[addItems[i]] = stuff[addItems[i]] + 1
def displayInventory(dicStuff):
    print('Inventory:')
    total = 0
    for key,value in dicStuff.items():
        print(key+': ' + str(value))
        total = total + value
    print('Total numbers of items: ' + str(total))
    return total
addToInventory(stuff,dragonLoot)
displayInventory(stuff)