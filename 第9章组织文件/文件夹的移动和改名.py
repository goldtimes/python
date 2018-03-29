import shutil

#shutil.move('F:\\python\\第9章组织文件\\spam.txt','C:\\Users\\lh101\\Desktop')
#这里成功的将spam.txt文件移动到了桌面
#shutil.move('F:\\python\\第9章组织文件\\delicious\\spam.txt','C:\\Users\\lh101\\Desktop\\spam1.txt')
#这里成功的将delicious下的spam.txt文件移动到了桌面并更改了名字
shutil.move('F:\\python\\第9章组织文件\\delicious','C:\\Users\\lh101\\Desktop\\move_delicious')
#这里将整个文件夹delicious移动到了桌面并更改了名字 destination构成的文件路径一定要存在，否则就会抛出异常
