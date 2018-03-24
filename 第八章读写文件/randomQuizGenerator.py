import random
#首先构建一个字典 存放美国的州和其对应的首都
capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'NewMexico':
'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh',
'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'WestVirginia':
'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

#接下里创建35份试卷 （其实是35分测试试卷文件和35份测试试卷的答案文件）
#文件的名字应该是不相同的，否则会覆盖
for quizNum in range(35):
    quizFile = open('capitalsQuiz%s.txt' % (quizNum + 1),'w')
    answerFile = open('capitalsQuizAnswer%s.txt' % (quizNum + 1),'w')

    quizFile.write('Name:\n\nDate:\n\nPeriod:\n\n')
    quizFile.write((' '* 20) + 'State Capitals Quiz (Form %s)' % (quizNum + 1))
    quizFile.write('\n\n')

    states = list(capitals.keys())#将keys生成一个列表
    random.shuffle(states) #重新随机排列一个列表

    #每个测试试卷中有50个问题，这个循环就是为每个问题生成答案选项
    #A 到 D的多重选择
    #在嵌套三个for循环，为每个问题生成多重选项
    for questionNum in range(50):
        correctAnswer = capitals[states[questionNum]]
        wrongAnswers = list(capitals.values())
        #del 方法删除正确的答案 del 是通过访问列表的下标
        #先通过index（列表值）放回列表中的值的小标
        del wrongAnswers[wrongAnswers.index(correctAnswer)]
        wrongAnswers = random.sample(wrongAnswers,3)
        answerOption = wrongAnswers + [correctAnswer]
        random.shuffle(answerOption)

        quizFile.write('%s.what\'s the capital of %s?\n' % (questionNum + 1,states[questionNum]))

        for i in range(4):
            quizFile.write(' %s,%s\n ' % ('ABCD'[i],answerOption[i]))
        quizFile.write('\n')

        answerFile.write('%s,%s\n' % (questionNum + 1 ,'ABCD'[answerOption.index(correctAnswer)]))
    quizFile.close()
    answerFile.close()