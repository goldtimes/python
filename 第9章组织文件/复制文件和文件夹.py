import shutil

shutil.copy('F:\\python\\第9章组织文件\\spam.txt','F:\\python\\第9章组织文件\\delicious')
#这里执行完之后打开delicious文件夹，有一个spam.txt文件
shutil.copy('F:\\python\\第9章组织文件\\spam.txt','F:\\python\\第9章组织文件\\delicious\\spam1.txt')
##这里执行完之后打开delicious文件夹，有一个spam1.txt文件
# shutil.copy('F:\\python\\第9章组织文件\\spam.txt','F:\\dsadadad') 如果destination是一个不存在的路径，那么创建一个新的文件
shutil.copytree('F:\\python\\第9章组织文件\\bacon','F:\\python\\第9章组织文件\\bacon_backup')
#可以得到一个和bacon一样的文件夹，包括其中的子文件夹和文件