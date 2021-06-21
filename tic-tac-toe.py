from random import randint
dict = {1:' ',2:' ',3:' ',4:' ',5:' ',6:' ',7:' ',8:' ',9:' '}                                           
def print_board():
    print (dict[1]+"|"+dict[2]+"|"+dict[3]+'\n'+dict[4]+"|"+dict[5]+"|"+dict[6]+'\n'+dict[7]+"|"+dict[8]+"|"+dict[9])
def check_win(x_o):
    yy = 0
    if (dict[1] == dict[2] == dict[3] and dict[1] !=' ') or  (dict[4] == dict[5] == dict[6] and dict[4] !=' ') or (dict[7] == dict[8] == dict[9] and dict[7] !=' ') or (dict[1] == dict[4] == dict[7] and dict[1] !=' ') or (dict[2] == dict[5] == dict[8] and dict[2] !=' ') or (dict[3] == dict[6] == dict[9] and dict[3] !=' ') or (dict[1] == dict[5] == dict[9] and dict[5] !=' ') or (dict[3] == dict[5] == dict[7] and dict[7] !=' '):
        print ("{} won!".format(x_o))
        yy = 1
    return yy
choice = int(input("Would you like to play with computer (1) or human (2)?"))
if choice == 2:
    while True:
        x = int(input("Where do you want to input your X? (1-9): "))
        while dict[x]!= ' ':
            print ("you can't input it here, try again")
            x = int(input("Where do you want to input your X? (1-9): "))
        dict[x] = 'X'
        print_board()
        xx = check_win('X')
        if xx == 1:
            break
        o = int(input("Where do you want to input your O? (1-9): "))
        while dict[o]!= ' ':
            print ("you can't input it here, try again")
            o = int(input("Where do you want to input your O? (1-9): "))
        dict[o] = 'O'
        print_board()
        yy = check_win('Y')
        if yy == 1:
            break
else:
    while True:
        x = int(input("Where do you want to input your X? (1-9): "))
        while dict[x]!= ' ':
            print ("you can't input it here, try again")
            x = int(input("Where do you want to input your X? (1-9): "))
        dict[x] = 'X'
        print_board()
        check_win('X')
        if check_win('X') == 1:
            break
        o = randint(1,9)
        while dict[o]!= ' ':
            o = randint(1,9)
        dict[o] = 'O'
        print("PC has put Y in {}".format(o))
        print_board()
        check_win('Y')
        if check_win == 1:
            break




    

