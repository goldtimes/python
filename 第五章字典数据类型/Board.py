# 创建一个＃字的键盘游戏，一方填入'X',一方填入'O'.
# ＃字游戏是9个位置，再任意的一个位置去填入'X','O',''三种字符
theBoard ={
    'top-L':' ','top-M':' ','top-R':' ',
    'mid-L':' ','mid-M':' ','mid-R':' ',
    'low-L':' ','low-M':' ','low-R':' '}
#将键盘打印出来
def printBoard(theBoard):
    print(theBoard['top-L']+'|'+theBoard['top-M'] + '|'+theBoard['top-R'])
    print('-+-+-')
    print(theBoard['mid-L'] + '|' + theBoard['mid-M'] + '|' + theBoard['mid-R'])
    print('-+-+-')
    print(theBoard['low-L'] + '|' +theBoard['low-M'] + '|' + theBoard['low-R'])
    print('-+-+-')

turn = 'X'
#模拟两个人互相的去下子
for i in range(9):
    printBoard(theBoard)
    print('Turn for ' + turn + '.Move on which space? ')
    move = input()
    moveTrue = theBoard.get(move,'NoneSpace')
    if moveTrue != 'NoneSpace':
        theBoard[move] = turn
    else:
        print('请输入正确的位置')
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'
printBoard(theBoard)