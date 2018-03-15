# 你在创建一个好玩的视频游戏。用于对玩家物品清单建模的数据结构是一个字
# 典。其中键是字符串，描述清单中的物品，值是一个整型值，说明玩家有多少该物
# 品。例如，字典值{'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}意味着玩
# 家有 1 条绳索、 6 个火把、 42 枚金币等。
stuff ={
    'rope':1,'torch':6,'gold coin':42,'dagger':1,'arrow':12
}
def displayInventory(dicStuff):
    print('Inventory:')
    total = 0
    for key,value in dicStuff.items():
        print(key+': ' + str(value))
        total = total + value
    print('Total numbers of items: ' + str(total))
    return total
displayInventory(stuff)

