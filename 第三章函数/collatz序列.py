def collatz(number):
    try:
        if number % 2 == 0:
            return number // 2
        else:
            return 3 * number + 1
    except ValueError:
        print('请输入一个整数，而非字符串')
print('Enter number: ')
while True:
    enterNumber = 0
    try:
        enterNumber = int(input())
        result = collatz(enterNumber)
        print(result)
        if result == 1:
            break
    except ValueError:
        print('请输入一个整数，而非字符串')
