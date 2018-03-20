tableData = [['apples', 'oranges', 'cherries', 'banana'], ['Alice', 'Bob', 'Carol', 'David'],['dogs', 'cats', 'moose', 'goose']]
#将上述的字符串的列表的列表格式化打印出来
"""  apples Alice dogs
    oranges Bob   cats
   cherries Caol  moose
     banana David goose"""


def printTable(strList):
    colwidths = [0] * len(strList)#创建一个存放每个表项中最长字符串的列表，长度为列表的长度[0,0,0]
    for i in range(len(strList)):
        colwidths[i] = lenStr(strList[i])
    # [0,0],[1,0],[2,0]
    # [0,1] [1,1] [2,1]
    # [0,2] [1,2] [2,2]
    # [0,3] [1,3] [2,3]
    maxlength = colwidths[0]
    for i in range(1,len(colwidths)):
        if maxlength < colwidths[i]:
            maxlength = colwidths[i]
    for i in range(4):
        for j in range(len(strList)):
            print(strList[j][i].rjust(maxlength),end='')
        print('\n')

def lenStr(list):
    maxlength = 0
    for i in range(len(list)):
        if maxlength < len(list[i]):
            maxlength = len(list[i])
    return maxlength

printTable(tableData)
