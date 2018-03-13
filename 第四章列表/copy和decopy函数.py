#在程序的设计当中，如果希望列表和字典中的数据在赋值过程中是不希望被修改的
import copy
spam = ['a','b','c','c']
cheese = copy.copy(spam)
cheese[1] = 'B'
print(cheese)
print(spam)
#从结果看出来，修改cheese[1]之后，spam原列表并没有被修改
spam1 = ['a',['b','c']]
cheese1 = copy.copy(spam1)
print(cheese1)
cheese1[1][0] = 'B'
#当列表中含有列表的时候，copy复制之后，通过修改cheese1[1][0]而修改了spam[1],这不是想要的情况
print(spam1)
cheese2 = copy.deepcopy(spam1)
cheese2[1][0] = 'b'
#这里就达到了深度复制之后，修改cheese2[1][0]。而spam1并没有被修改，而是修改的cheese2
print(spam1)
print(cheese2)