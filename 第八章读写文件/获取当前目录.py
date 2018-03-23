#有些文件夹并不是从C:\根目录开始的
#通过os的方法来获得当前文件的目录
import os
print(os.getcwd())
# 通过os.chdir('C:\\Windows\\System32')将文件改变目录到\\Windows\\System32
# 如果更改的目录不存在就会报错

#运行下面的代码，可以在C盘查看到新建的目录
#dirs = os.path.join('delicious','walnut','waffles')
#os.makedirs('C:\\'+ dirs)