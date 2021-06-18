dict = {1:' ',2:' ',3:' ',4:' ',5:' ',6:' ',7:' ',8:' ',9:' '}
while True:
    x = int(input("Where do you want to input your X? (1-9): "))
    while dict[x]!= ' ':
        print ("you can't input it here, try again")
        x = int(input("Where do you want to input your X? (1-9): "))
    dict[x] = 'X'
    print (dict[1]+"|"+dict[2]+"|"+dict[3]+'\n'+dict[4]+"|"+dict[5]+"|"+dict[6]+'\n'+dict[7]+"|"+dict[8]+"|"+dict[9])
    if (dict[1] == dict[2] == dict[3] and dict[1] !=' ') or  (dict[4] == dict[5] == dict[6] and dict[4] !=' ') or (dict[7] == dict[8] == dict[9] and dict[7] !=' ') or (dict[1] == dict[4] == dict[7] and dict[1] !=' ') or (dict[2] == dict[5] == dict[8] and dict[2] !=' ') or (dict[3] == dict[6] == dict[9] and dict[3] !=' ') or (dict[1] == dict[5] == dict[9] and dict[5] !=' ') or (dict[3] == dict[5] == dict[7] and dict[7] !=' '):
        print ("X won!")
        break
    o = int(input("Where do you want to input your O? (1-9): "))
    while dict[o]!= ' ':
        print ("you can't input it here, try again")
        o = int(input("Where do you want to input your O? (1-9): "))
    dict[o] = 'O'
    print (dict[1]+"|"+dict[2]+"|"+dict[3]+'\n'+dict[4]+"|"+dict[5]+"|"+dict[6]+'\n'+dict[7]+"|"+dict[8]+"|"+dict[9])
    if (dict[1] == dict[2] == dict[3] and dict[1] !=' ') or  (dict[4] == dict[5] == dict[6] and dict[4] !=' ') or (dict[7] == dict[8] == dict[9] and dict[7] !=' ') or (dict[1] == dict[4] == dict[7] and dict[1] !=' ') or (dict[2] == dict[5] == dict[8] and dict[2] !=' ') or (dict[3] == dict[6] == dict[9] and dict[3] !=' ') or (dict[1] == dict[5] == dict[9] and dict[5] !=' ') or (dict[3] == dict[5] == dict[7] and dict[7] !=' '):
        print ("Y won!")
        break

    

