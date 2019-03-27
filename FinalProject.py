
one='1'
two='2'
three='3'
four='4'
five='5'
six='6'
seven='7'
eight='8'
nine='9' 
turnCount = 0
choice = ' '
player1Name= ' '
player2Name= ' '
player1Symbol= ' '
player2Symbol= ' '
player1T= 0
player2T= 0
doubles=[]
xtally=0
ytally=0


def nameSet():
    player1Name= str(input("Please, enter Player 1's name: "))
    print(' ')
    player2Name= str(input("Please, enter Player 2's name: "))
    print(' ')

def playerSet():
    player1Symbol = str(input(player1Name+ ", Choose a symbol to play with, \"x\" or \"o\"? \n :"))
    if player1Symbol == 'x' or player1Symbol== 'X':
        player1Symbol='X'
        player2Symbol='O'
    else:
        player1Symbol='O'
        player2Symbol='X'
    print(player1Name+'plays as '+player1Symbol)
    print(player2Name+'plays as '+player2Symbol)

def playOrder():
    answer = str(input(player1Name+' Do you wish to move first? Yes or No'))
    if answer == 'yes' or answer == 'Yes' or answer == 'YES':
        player1T = 0
        player2T = 1
    else:
        player1T = 1
        player2T = 0

def draw():
    print('\n'+'   |  '+one +'  |  '+two+'  |  '+three+'  |  ' + '\n'+ '   ___________________'+'\n'+'   |  '+four+'  |  '+five+'  |  '+six+'  |' + '\n'+ '   ___________________'+'\n'+'   |  '+seven+'  |  '+eight+'  |  '+nine+'  | \n')

def clearBoard():
    doubles.clear()
    doubles
    one='1'
    two='2'
    three='3'
    four='4'
    five='5'
    six='6'
    seven='7'
    eight='8'
    nine='9'
    turnCount=0

def play():
    clearBoard()
    draw()
    turnCount=0
    while turnCount<=8:
        if player1T==0:
            player1()
            checkWin()
            player2()
            checkWin()
        else:
            player2()
            checkWin()
            player1()
            checkWin()

def player1():
    turnCount=turnCount+1
    retryCount=0
    choice= str(input(player1Name+", enter the number that corresponds to the cell: "))
    if turnCount >=4:
        checkWin()

    elif one==choice & one not in doubles:
        doubles.insert(0,choice)
        one = player1Symbol 
        draw()

    elif two==choice & two not in doubles:
        doubles.insert(0,choice)
        two = player1Symbol
        draw()

    elif three==choice & three not in doubles:
        doubles.insert(0,choice)
        three = player1Symbol
        draw()

    elif four==choice & four not in doubles:
        doubles.insert(0,choice)
        four = player1Symbol
        draw()

    elif five==choice & five not in doubles:
        doubles.insert(0,choice)
        five = player1Symbol
        draw()

    elif six==choice & six not in doubles:
        doubles.insert(0,choice)
        six = player1Symbol
        draw()

    elif seven==choice & seven not in doubles:
        doubles.insert(0,choice)
        seven = player1Symbol
        draw()

    elif eight==choice & eight not in doubles:
        doubles.insert(0,choice)
        eight = player1Symbol
        draw()

    elif nine==choice & nine not in doubles:
        doubles.insert(0,choice)
        nine = player1Symbol
        draw()
    else:
        print('INVALID INPUT \n Try again please: ')
        retryCount=retryCount+1
        if retryCount==3:
            print('Max amount of retrys has been reached ' + player2Name +' your turn')
            turnCount=turnCount-1
            player2()
        else:
            player1()
    retryCount=0

def player2():
    turnCount=turnCount+1
    retryCount=0
    choice= str(input(player2Name+", enter the number that corresponds to the cell: "))
    if turnCount >=4:
        checkWin()

    elif one==choice & one not in doubles:
        doubles.insert(0,choice)
        one = player2Symbol 
        draw()

    elif two==choice & two not in doubles:
        doubles.insert(0,choice)
        two = player2Symbol
        draw()

    elif three==choice & three not in doubles:
        doubles.insert(0,choice)
        three = player2Symbol
        draw()

    elif four==choice & four not in doubles:
        doubles.insert(0,choice)
        four = player2Symbol
        draw()

    elif five==choice & five not in doubles:
        doubles.insert(0,choice)
        five = player2Symbol
        draw()

    elif six==choice & six not in doubles:
        doubles.insert(0,choice)
        six = player2Symbol
        draw()

    elif seven==choice & seven not in doubles:
        doubles.insert(0,choice)
        seven = player2Symbol
        draw()

    elif eight==choice & eight not in doubles:
        doubles.insert(0,choice)
        eight = player2Symbol
        draw()

    elif nine==choice & nine not in doubles:
        doubles.insert(0,choice)
        nine = player2Symbol
        draw()
    else:
        print('INVALID INPUT \n Try again please: ')
        retryCount=retryCount+1
        if retryCount==3:
            print('Max amount of retrys has been reached ' + player1Name +' your turn')
            turnCount=turnCount-1
            player1()
        else:
            player2()
    retryCount=0

def checkWin():
    '''----------------------1-----------------------'''
    if one==two & two==three:
        if one=='X':
            xtally=xtally+1
        else:
            ytally= ytally+1
        print('Player'+one+'wins \n')
        if player1Symbol=='X':
            print('winner tally'+ player1Name+': '+xtally+', '+player2Name+': '+ytally+'\n')
        elif player1Symbol == 'O':
            print('winner tally'+ player1Name+': '+ytally+', '+player2Name+': '+xtally+'\n')
        newGame = int(input('enter 1 to play agaion or 0 to exit the game: '))
        if newGame==1:
            play()
        else:
            print('GAME OVER')
        '''----------------------2-----------------------'''
    elif one==four & four==seven:
        if one=='X':
            xtally=xtally+1
        else:
            ytally= ytally+1
        print('Player'+one+'wins \n')
        if player1Symbol=='X':
            print('winner tally'+ player1Name+': '+xtally+', '+player2Name+': '+ytally+'\n')
        elif player1Symbol == 'O':
            print('winner tally'+ player1Name+': '+ytally+', '+player2Name+': '+xtally+'\n')
        newGame = int(input('enter 1 to play agaion or 0 to exit the game: '))
        if newGame==1:
            play()
        else:
            print('GAME OVER')
        '''-----------------------3----------------------'''
    elif one==five & five==nine:
        if one=='X':
            xtally=xtally+1
        else:
            ytally= ytally+1
        print('Player'+one+'wins \n')
        if player1Symbol=='X':
            print('winner tally'+ player1Name+': '+xtally+', '+player2Name+': '+ytally+'\n')
        elif player1Symbol == 'O':
            print('winner tally'+ player1Name+': '+ytally+', '+player2Name+': '+xtally+'\n')
        newGame = int(input('enter 1 to play agaion or 0 to exit the game: '))
        if newGame==1:
            play()
        else:
            print('GAME OVER')
        '''------------------------4---------------------'''  
    elif two==five & five==eight:
        if two=='X':
            xtally=xtally+1
        else:
            ytally= ytally+1
        print('Player'+two+'wins \n')
        if player1Symbol=='X':
            print('winner tally'+ player1Name+': '+xtally+', '+player2Name+': '+ytally+'\n')
        elif player1Symbol == 'O':
            print('winner tally'+ player1Name+': '+ytally+', '+player2Name+': '+xtally+'\n')
        newGame = int(input('enter 1 to play agaion or 0 to exit the game: '))
        if newGame==1:
            play()
        else:
            print('GAME OVER')
        '''-----------------------5----------------------'''
    elif three==six & six==nine:
        if three=='X':
            xtally=xtally+1
        else:
            ytally= ytally+1
        print('Player'+three+'wins \n')
        if player1Symbol=='X':
            print('winner tally'+ player1Name+': '+xtally+', '+player2Name+': '+ytally+'\n')
        elif player1Symbol == 'O':
            print('winner tally'+ player1Name+': '+ytally+', '+player2Name+': '+xtally+'\n')
        newGame = int(input('enter 1 to play agaion or 0 to exit the game: '))
        if newGame==1:
            play()
        else:
            print('GAME OVER')
        '''------------------------6---------------------'''
    elif seven==five & five==three:
        if seven=='X':
            xtally=xtally+1
        else:
            ytally= ytally+1
        print('Player'+seven+'wins \n')
        if player1Symbol=='X':
            print('winner tally'+ player1Name+': '+xtally+', '+player2Name+': '+ytally+'\n')
        elif player1Symbol == 'O':
            print('winner tally'+ player1Name+': '+ytally+', '+player2Name+': '+xtally+'\n')
        newGame = int(input('enter 1 to play agaion or 0 to exit the game: '))
        if newGame==1:
            play()
        else:
            print('GAME OVER')
        '''----------------------7-----------------------'''  
    elif four==five & five==six:
        if four=='X':
            xtally=xtally+1
        else:
            ytally= ytally+1
        print('Player'+four+'wins \n')
        if player1Symbol=='X':
            print('winner tally'+ player1Name+': '+xtally+', '+player2Name+': '+ytally+'\n')
        elif player1Symbol == 'O':
            print('winner tally'+ player1Name+': '+ytally+', '+player2Name+': '+xtally+'\n')
        newGame = int(input('enter 1 to play agaion or 0 to exit the game: '))
        if newGame==1:
            play()
        else:
            print('GAME OVER')
        '''---------------------8------------------------''' 
    elif seven==eight & eight==nine:
        if seven=='X':
            xtally=xtally+1
        else:
            ytally= ytally+1
        print('Player'+seven+'wins \n')
        if player1Symbol=='X':
            print('winner tally'+ player1Name+': '+xtally+', '+player2Name+': '+ytally+'\n')
        elif player1Symbol == 'O':
            print('winner tally'+ player1Name+': '+ytally+', '+player2Name+': '+xtally+'\n')
        newGame = int(input('enter 1 to play agaion or 0 to exit the game: '))
        if newGame==1:
            play()
        else:
            print('GAME OVER')
        '''---------------------------------------------'''   
    elif turnCount==9:
        print('NO WINNER')
        if player1Symbol=='X':
            print('winner tally'+ player1Name+': '+xtally+', '+player2Name+': '+ytally+'\n')
        elif player1Symbol == 'O':
            print('winner tally'+ player1Name+': '+ytally+', '+player2Name+': '+xtally+'\n')
        newGame = int(input('enter 1 to play agaion or 0 to exit the game: '))
        if newGame==1:
            play()
        else:
            print('GAME OVER')



def main():
    nameSet()
    playerSet()
    playOrder()
    play()
main()
