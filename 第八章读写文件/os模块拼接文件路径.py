#windows下的拼接符为'\' 而os\linux为 '/'拼接符
#那么为了避免在不用操作系统，而导致程序等崩溃，应当用系统自带的拼接符来拼接文件路径

import os
myFiles=['account.txt','details.csv','invite.doc']
for file in myFiles:
    print(os.path.join('C:\\Users\\asweigart',file))
