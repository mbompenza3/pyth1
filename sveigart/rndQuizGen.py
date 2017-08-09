import random
capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix', 'Arkansas': 'Little Rock',
            'California': 'Sacramento', 'Colorado': 'Denver', 'Connecticut': 'Hartford', 'Delaware': 'Dover',
            'Florida': 'Tallahassee', 'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise',
            'Illinois': 'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas': 'Topeka',
            'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine': 'Augusta', 'Maryland': 'Annapolis',
            'Massachusetts': 'Boston', 'Michigan': 'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson',
            'Missouri': 'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada': 'Carson City',
            'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New Mexico': 'Santa Fe', 'New York': 'Albany',
            'North Carolina': 'Raleigh', 'North Dakota': 'Bismarck', 'Ohio': 'Columbus',
            'Oklahoma': 'Oklahoma City', 'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg',
            'Rhode Island': 'Providence', 'South Carolina': 'Columbia', 'South Dakota': 'Pierre',
            'Tennessee': 'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont': 'Montpelier',
            'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia': 'Charleston', 'Wisconsin': 'Madison',
            'Wyoming': 'Cheyenne'}

for quizn in range(35):
    quizf=open('1\\capitals%s.txt' % (quizn + 1), 'w')
    answf=open('1\\capital_answ%s.txt' % (quizn + 1), 'w')
    quizf.write('Name:\n\nDate:\n\nCourse:\n\n')
    quizf.write((' '*15) +'Bilet %s' % (quizn + 1))
    quizf.write('\n\n')
    states=list(capitals.keys())
    random.shuffle(states)
    for questn in range(50):
        corrAnsw=capitals[states[questn]]
        wrongAnsw=list(capitals.values())
        del wrongAnsw[wrongAnsw.index(corrAnsw)]
        wrongAnsw=random.sample(wrongAnsw,3)
        answOpt=wrongAnsw+[corrAnsw]
        random.shuffle(answOpt)

        quizf.write('%s. Vybor stolicy stata %s.\n'%(questn+1,states[questn]))
        for i in range(4):
            quizf.write(' %s. %s\n' %('ABCD'[i],answOpt[i]))
        quizf.write('\n')
        answf.write('%s. %s\n' % (questn+1,'ABCD'[answOpt.index(corrAnsw)]))
    quizf.close()
    answf.close()