import os
print(os.path.getsize('F:\\kindle电子书系列\\documents\\白夜行.mobi'))

print(os.listdir('F:\\kindle电子书系列\\documents'))

totalSize = 0
for filename in os.listdir('F:\\kindle电子书系列\\documents'):
     totalSize = totalSize + os.path.getsize(os.path.join('F:\\kindle电子书系列\\documents',filename))
print(totalSize)