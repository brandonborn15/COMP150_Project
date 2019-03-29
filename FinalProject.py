import random
'''-----------------------GLOBAL VARIABLES-----------------------'''
one='1'
two='2'
three='3'
four='4'
five='5'
six='6'
seven= '7'
eight='8'
nine= '9' 
choice = ' '
player1Name= ' '
player2Name= ' '
player1Symbol= ' '
player2Symbol= ' '
player1T= 0
player2T= 0
doubles=['empty']
compMoves = [1,2,3,4,5,6,7,8,9]
xtally=0
ytally=0
xtally = int(xtally)
ytally = int(ytally)
turnCount=0
'''-------------------------CODE METHODS-------------------------'''

def nameSet():
    global player1Name
    global player2Name
    player1Name = str(input("Please, enter Player 1's name: "))
    print(' ')
    player2Name= str(input("Please, enter Player 2's name: "))
    print(' ')

def playerSet():
    global player1Symbol
    global player2Symbol
    global player1Name
    global player2Name
    player1Symbol = str(input(player1Name + ", choose a symbol to play with, \"x\" or \"o\"? \n : "))
    if player1Symbol == 'x' or player1Symbol== 'X':
        player1Symbol='X'
        player2Symbol='O'
    else:
        player1Symbol='O'
        player2Symbol='X'
    print(player1Name+' plays as '+player1Symbol)
    print(player2Name+' plays as '+player2Symbol)

def playOrder():
    global player1Name
    global player1T
    global player2T
    answer = str(input(player1Name+' Do you wish to move first? Yes or No:  '))
    if answer == 'yes' or answer == 'Yes' or answer == 'YES':
        player1T = 0
        player2T = 1
    else:
        player1T = 1
        player2T = 0

def draw():
    global one
    global two
    global three
    global four
    global five
    global six 
    global seven
    global eight
    global nine
   
    print('\n'+'   |  '+one +'  |  '+two+'  |  '+three+'  |  ' + '\n'+ '   ___________________'+'\n'+'   |  '+four+'  |  '+five+'  |  '+six+'  |' + '\n'+ '   ___________________'+'\n'+'   |  '+seven+'  |  '+eight+'  |  '+nine+'  | \n')
  
def clearBoard():
    global doubles
    global one
    global two
    global three
    global four
    global five
    global six 
    global seven
    global eight
    global nine
    global turnCount
    global compMoves
    doubles[:]=[]
    compMoves = [1,2,3,4,5,6,7,8,9]
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
    turnCount=0
    clearBoard()
    draw()
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
    global one
    global two
    global three
    global four
    global five
    global six 
    global seven
    global eight
    global nine
    global turnCount
    global player1Symbol
    global player2Symbol
    global player1Name
    global player2Name
    global doubles
    turnCount= turnCount+1
    retryCount=0
    choice= int(input(player1Name+", enter the number that corresponds to the cell: "))
    
    if 1==choice and 1 not in doubles:
            doubles.insert(0,choice)
            one = player1Symbol
            draw()

    elif 2==choice and 2 not in doubles:
            doubles.insert(0,choice)
            two = (player1Symbol)
            draw()

    elif 3==choice and 3 not in doubles:
            doubles.insert(0,choice)
            three = (player1Symbol)
            draw()

    elif 4==choice and 4 not in doubles:
            doubles.insert(0,choice)
            four = (player1Symbol)
            draw()

    elif 5==choice and 5 not in doubles:
            doubles.insert(0,choice)
            five = (player1Symbol)
            draw()

    elif 6==choice and 6 not in doubles:
            doubles.insert(0,choice)
            six = (player1Symbol)
            draw()

    elif 7==choice and 7 not in doubles:
            doubles.insert(0,choice)
            seven = (player1Symbol)
            draw()

    elif 8==choice and 8 not in doubles:
            doubles.insert(0,choice)
            eight = (player1Symbol)
            draw()

    elif 9==choice and 9 not in doubles:
            doubles.insert(0,choice)
            nine = (player1Symbol)
            draw()
    elif choice in doubles:
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
    global one
    global two
    global three
    global four
    global five
    global six 
    global seven
    global eight
    global nine
    global turnCount
    global player1Symbol
    global player2Symbol
    global player1Name
    global player2Name
    global doubles
    turnCount=turnCount+1
    retryCount=0
    choice= int(input(player2Name+", enter the number that corresponds to the cell: "))
    
    if 1==choice and 1 not in doubles:
        doubles.insert(0,choice)
        one = str(player2Symbol) 
        draw()

    elif 2==choice and 2 not in doubles:
        doubles.insert(0,choice)
        two = str(player2Symbol) 
        draw()

    elif 3==choice and 3 not in doubles:
        doubles.insert(0,choice)
        three = str(player2Symbol) 
        draw()

    elif 4==choice and 4 not in doubles:
        doubles.insert(0,choice)
        four = str(player2Symbol) 
        draw()

    elif 5==choice and 5 not in doubles:
        doubles.insert(0,choice)
        five = str(player2Symbol) 
        draw()

    elif 6==choice and 6 not in doubles:
        doubles.insert(0,choice)
        six = str(player2Symbol) 
        draw()

    elif 7==choice and 7 not in doubles:
        doubles.insert(0,choice)
        seven = str(player2Symbol) 
        draw()

    elif 8==choice and 8 not in doubles:
        doubles.insert(0,choice)
        eight = str(player2Symbol) 
        draw()

    elif 9==choice and 9 not in doubles:
        doubles.insert(0,choice)
        nine = str(player2Symbol) 
        draw()
    elif choice in doubles:
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
    global one
    global two
    global three
    global four
    global five
    global six 
    global seven
    global eight
    global nine
    global xtally
    global ytally
    global player1Symbol
    global player2Symbol
    global player1Name
    global player2Name
    xtally = int(xtally)
    ytally = int(ytally)
    '''----------------------1-----------------------'''
    if one is two and two is three:
        if one=='X':
            xtally=xtally+1
        else:
            ytally= ytally+1
        print('Player '+one+' wins \n')
        if player1Symbol=='X':
            xtally = str(xtally)
            ytally = str(ytally)
            print('Winner Tally \n'+ player1Name+': '+xtally+'\n'+player2Name+': '+ytally+'\n')
        elif player1Symbol == 'O':
            xtally = str(xtally)
            ytally = str(ytally)
            print('Winner Tally \n'+ player1Name+': '+ytally+'\n'+player2Name+': '+xtally+'\n')
        newGame = int(input('Enter 1 to play agaion or 0 to exit the game: '))
        if newGame==1:
            clearBoard()
            play()
        else:
            print('GAME OVER \n')
            raise SystemExit
        '''----------------------2-----------------------'''
    elif one is four and four is seven:
        if one=='X':
            xtally=xtally+1
        else:
            ytally= ytally+1
        print('Player '+ one +'  wins \n')
        if player1Symbol=='X':
            xtally = str(xtally)
            ytally = str(ytally)
            print('Winner Tally \n'+ player1Name+': '+xtally+'\n'+player2Name+': '+ytally+'\n')
        elif player1Symbol == 'O':
            xtally = str(xtally)
            ytally = str(ytally)
            print('Winner Tally \n'+ player1Name+': '+ytally+'\n'+player2Name+': '+xtally+'\n')
        newGame = int(input('Enter 1 to play agaion or 0 to exit the game: '))
        if newGame==1:
            clearBoard()
            play()
        else:
            print('GAME OVER \n')
            raise SystemExit
        '''-----------------------3----------------------'''
    elif one is five and five is nine:
        if one=='X':
            xtally=xtally+1
        else:
            ytally= ytally+1
        print('Player '+one+' wins \n')
        if player1Symbol=='X':
            xtally = str(xtally)
            ytally = str(ytally)
            print('Winner Tally \n'+ player1Name+': '+xtally+'\n'+player2Name+': '+ytally+'\n')
        elif player1Symbol == 'O':
            xtally = str(xtally)
            ytally = str(ytally)
            print('Winner Tally \n'+ player1Name+': '+ytally+'\n'+player2Name+': '+xtally+'\n')
        newGame = int(input('Enter 1 to play agaion or 0 to exit the game: '))
        if newGame==1:
            clearBoard()
            play()
        else:
            print('GAME OVER \n')
            raise SystemExit
        '''------------------------4---------------------'''  
    elif two is five and five is eight:
        if two=='X':
            xtally=xtally+1
        else:
            ytally= ytally+1
        print('Player '+two+' wins \n')
        if player1Symbol=='X':
            xtally = str(xtally)
            ytally = str(ytally)
            print('Winner Tally \n'+ player1Name+': '+xtally+'\n'+player2Name+': '+ytally+'\n')
        elif player1Symbol == 'O':
            xtally = str(xtally)
            ytally = str(ytally)
            print('Winner Tally \n'+ player1Name+': '+ytally+'\n'+player2Name+': '+xtally+'\n')
        newGame = int(input('Enter 1 to play agaion or 0 to exit the game: '))
        if newGame==1:
            clearBoard()
            play()
        else:
            print('GAME OVER \n')
            raise SystemExit
        '''-----------------------5----------------------'''
    elif three is six and six is nine:
        if three=='X':
            xtally=xtally+1
        else:
            ytally= ytally+1
        print('Player '+three+' wins \n')
        if player1Symbol=='X':
            xtally = str(xtally)
            ytally = str(ytally)
            print('Winner Tally \n'+ player1Name+': '+xtally+'\n'+player2Name+': '+ytally+'\n')
        elif player1Symbol == 'O':
            xtally = str(xtally)
            ytally = str(ytally)
            print('Winner Tally \n'+ player1Name+': '+ytally+'\n'+player2Name+': '+xtally+'\n')
        newGame = int(input('Enter 1to play agaion or 0 to exit the game: '))
        if newGame==1:
            clearBoard()
            play()
        else:
            print('GAME OVER \n')
            raise SystemExit
        '''------------------------6---------------------'''
    elif seven is five and five is three:
        if seven=='X':
            xtally=xtally+1
        else:
            ytally= ytally+1
        print('Player '+seven+' wins \n')
        if player1Symbol=='X':
            xtally = str(xtally)
            ytally = str(ytally)
            print('Winner Tally \n'+ player1Name+': '+xtally+'\n'+player2Name+': '+ytally+'\n')
        elif player1Symbol == 'O':
            xtally = str(xtally)
            ytally = str(ytally)
            print('Winner Tally \n'+ player1Name+': '+ytally+'\n'+player2Name+': '+xtally+'\n')
        newGame = int(input('Enter 1to play agaion or 0 to exit the game: '))
        if newGame==1:
            clearBoard()
            play()
        else:
            print('GAME OVER \n')
            raise SystemExit
        '''----------------------7-----------------------'''  
    elif four is five and five is six:
        if four=='X':
            xtally=xtally+1
        else:
            ytally= ytally+1
        print('Player '+four+' wins \n')
        if player1Symbol=='X':
            xtally = str(xtally)
            ytally = str(ytally)
            print('Winner Tally \n'+ player1Name+': '+xtally+'\n'+player2Name+': '+ytally+'\n')
        elif player1Symbol == 'O':
            xtally = str(xtally)
            ytally = str(ytally)
            print('Winner Tally \n'+ player1Name+': '+ytally+'\n'+player2Name+': '+xtally+'\n')
        newGame = int(input('Enter 1to play agaion or 0 to exit the game: '))
        if newGame==1:
            clearBoard()
            play()
        else:
            print('GAME OVER \n')
            raise SystemExit
        '''---------------------8------------------------''' 
    elif seven is eight and eight is nine:
        if seven=='X':
            xtally=xtally+1
        else:
            ytally= ytally+1
        print('Player '+seven+' wins \n')
        if player1Symbol=='X':
            xtally = str(xtally)
            ytally = str(ytally)
            print('Winner Tally \n'+ player1Name+': '+xtally+'\n'+player2Name+': '+ytally+'\n')
        elif player1Symbol == 'O':
            xtally = str(xtally)
            ytally = str(ytally)
            print('Winner Tally \n'+ player1Name+': '+ytally+'\n'+player2Name+': '+xtally+'\n')
        newGame = int(input('Enter 1to play agaion or 0 to exit the game: '))
        if newGame==1:
            clearBoard()
            play()
        else:
            print('GAME OVER \n')
            raise SystemExit
        '''---------------------------------------------'''   
    elif turnCount==9:
        print('NO WINNER \n')
        if player1Symbol=='X':
            xtally = str(xtally)
            ytally = str(ytally)
            print('Winner Tally \n'+ player1Name+': '+xtally+'\n'+player2Name+': '+ytally+'\n')
        elif player1Symbol == 'O':
            xtally = str(xtally)
            ytally = str(ytally)
            print('Winner Tally \n'+ player1Name+': '+ytally+'\n'+player2Name+': '+xtally+'\n')
        newGame = int(input('Enter 1to play agaion or 0 to exit the game: '))
        if newGame==1:
            clearBoard()
            play()
        else:
            print('GAME OVER \n')
            raise SystemExit

def main():
    GameOverride = str(input("Solo or Multiplayer?\n:  "))
    if GameOverride=='multiplayer' or GameOverride == 'Multiplayer':
        nameSet()
        playerSet()
        playOrder()
        play()
    elif(GameOverride == 'solo' or GameOverride=='Solo'):
        soloNameSet()
        soloSet()
        soloOrder()
        soloPlay()
'''----------------------COMPUTER MODE @ RANDOM-----------------------'''
def soloNameSet():
    global player1Name
    player1Name = str(input("Please, enter your username: "))
    print(' ')

def soloSet():
    global player1Name
    global player1Symbol
    global player2Symbol
    player1Symbol = str(input(player1Name+ ", choose a symbol to play with, \"x\" or \"o\"? \n : "))
    if player1Symbol == 'x' or player1Symbol== 'X':
        player1Symbol='X'
        player2Symbol='O'
    else:
        player1Symbol='O'
        player2Symbol='X'
    print(player1Name+' plays as '+player1Symbol)
    print('Comp plays as '+player2Symbol)

def soloOrder():
    global player1Name
    global player1T
    global player2T
    answer = str(input(player1Name+' Do you wish to move first? Yes or No:  '))
    if answer == 'yes' or answer == 'Yes' or answer == 'YES':
        player1T = 0
        player2T = 1
    else:
        player1T = 1
        player2T = 0

def soloPlayer():
    global one
    global two
    global three
    global four
    global five
    global six 
    global seven
    global eight
    global nine
    global turnCount
    global player1Symbol
    global player2Symbol
    global player1Name
    global doubles
    global compMoves
    turnCount= turnCount+1
    retryCount=0
    choice= int(input(player1Name+", enter the number that corresponds to the cell: "))
    
    if 1==choice and 1 not in doubles:
            doubles.insert(0,choice)
            compMoves.remove(1)
            one = player1Symbol
            draw()

    elif 2==choice and 2 not in doubles:
            doubles.insert(0,choice)
            compMoves.remove(2)
            two = (player1Symbol)
            draw()

    elif 3==choice and 3 not in doubles:
            doubles.insert(0,choice)
            compMoves.remove(3)
            three = (player1Symbol)
            draw()

    elif 4==choice and 4 not in doubles:
            doubles.insert(0,choice)
            compMoves.remove(4)
            four = (player1Symbol)
            draw()

    elif 5==choice and 5 not in doubles:
            doubles.insert(0,choice)
            compMoves.remove(5)
            five = (player1Symbol)
            draw()

    elif 6==choice and 6 not in doubles:
            doubles.insert(0,choice)
            compMoves.remove(6)
            six = (player1Symbol)
            draw()

    elif 7==choice and 7 not in doubles:
            doubles.insert(0,choice)
            compMoves.remove(7)
            seven = (player1Symbol)
            draw()

    elif 8==choice and 8 not in doubles:
            doubles.insert(0,choice)
            compMoves.remove(8)
            eight = (player1Symbol)
            draw()

    elif 9==choice and 9 not in doubles:
            doubles.insert(0,choice)
            compMoves.remove(9)
            nine = (player1Symbol)
            draw()
    elif choice in doubles:
        print('INVALID INPUT \n Try again please: ')
        retryCount=retryCount+1
        if retryCount==3:
            print('Max amount of retrys has been reached ' + player2Name +' your turn')
            turnCount=turnCount-1
            comp()
        else:
            player1()
    retryCount=0

def soloPlay():
    turnCount=0
    clearBoard()
    draw()
    while turnCount<=8:
        if player1T==0:
            player1()
            compCheckWin()
            comp()
            compCheckWin()
        else:
            comp()
            compCheckWin()
            player1()
            compCheckWin()

def comp():
    global one
    global two
    global three
    global four
    global five
    global six 
    global seven
    global eight
    global nine
    global turnCount
    global player2Symbol
    global doubles
    global compMoves
    turnCount= turnCount+1
    choice=0
    choice = random.choice(compMoves)
    
    if 1==choice:
        if 1 not in doubles:
            doubles.insert(0,choice)
            compMoves.remove(1)
            one = player2Symbol
            draw()

    elif 2==choice:
        if 2 not in doubles:
            doubles.insert(0,choice)
            compMoves.remove(2)
            two = (player2Symbol)
            draw()

    elif 3==choice:
        if 3 not in doubles:
            doubles.insert(0,choice)
            compMoves.remove(3)
            three = (player2Symbol)
            draw()

    elif 4==choice:
        if 4 not in doubles:
            doubles.insert(0,choice)
            compMoves.remove(4)
            four = (player2Symbol)
            draw()

    elif 5==choice:
        if 5 not in doubles:
            doubles.insert(0,choice)
            compMoves.remove(5)
            five = (player2Symbol)
            draw()

    elif 6==choice:
        if 6 not in doubles:
            doubles.insert(0,choice)
            compMoves.remove(6)
            six = (player2Symbol)
            draw()

    elif 7==choice:
        if 7 not in doubles:
            doubles.insert(0,choice)
            compMoves.remove(7)
            seven = (player2Symbol)
            draw()

    elif 8==choice:
        if 8 not in doubles:
            doubles.insert(0,choice)
            compMoves.remove(8)
            eight = (player2Symbol)
            draw()

    elif 9==choice:
        if 9 not in doubles:
            doubles.insert(0,choice)
            compMoves.remove(9)
            nine = (player2Symbol)
            draw()
    
def compCheckWin():
    global one
    global two
    global three
    global four
    global five
    global six 
    global seven
    global eight
    global nine
    global xtally
    global ytally
    global player1Symbol
    global player2Symbol
    global player1Name
    xtally = int(xtally)
    ytally = int(ytally)
    '''----------------------1-----------------------'''
    if one is two and two is three:
        if one=='X':
            xtally=xtally+1
        else:
            ytally= ytally+1
        print('Player '+one+' wins \n')
        if player1Symbol=='X':
            xtally = str(xtally)
            ytally = str(ytally)
            print('Winner Tally \n'+ player1Name+': '+xtally+'\nComp: '+ytally+'\n')
        elif player1Symbol == 'O':
            xtally = str(xtally)
            ytally = str(ytally)
            print('Winner Tally \n'+ player1Name+': '+ytally+'\nComp: '+xtally+'\n')
        newGame = int(input('Enter 1to play agaion or 0 to exit the game: '))
        if newGame==1:
            clearBoard()
            soloPlay()
        else:
            print('GAME OVER \n')
            raise SystemExit
        '''----------------------2-----------------------'''
    elif one is four and four is seven:
        if one=='X':
            xtally=xtally+1
        else:
            ytally= ytally+1
        print('Player '+one+' wins \n')
        if player1Symbol=='X':
            xtally = str(xtally)
            ytally = str(ytally)
            print('Winner Tally \n'+ player1Name+': '+xtally+'\nComp: '+ytally+'\n')
        elif player1Symbol == 'O':
            xtally = str(xtally)
            ytally = str(ytally)
            print('Winner Tally \n'+ player1Name+': '+ytally+'\nComp: '+xtally+'\n')
        newGame = int(input('Enter 1to play agaion or 0 to exit the game: '))
        if newGame==1:
            clearBoard()
            soloPlay()
        else:
            print('GAME OVER \n')
            raise SystemExit
        '''-----------------------3----------------------'''
    elif one is five and five is nine:
        if one=='X':
            xtally=xtally+1
        else:
            ytally= ytally+1
        print('Player '+one+' wins \n')
        if player1Symbol=='X':
            xtally = str(xtally)
            ytally = str(ytally)
            print('Winner Tally \n'+ player1Name+': '+xtally+'\nComp: '+ytally+'\n')
        elif player1Symbol == 'O':
            xtally = str(xtally)
            ytally = str(ytally)
            print('Winner Tally \n'+ player1Name+': '+ytally+'\nComp: '+xtally+'\n')
        newGame = int(input('Enter 1to play agaion or 0 to exit the game: '))
        if newGame==1:
            clearBoard()
            soloPlay()
        else:
            print('GAME OVER \n')
            raise SystemExit
        '''------------------------4---------------------'''  
    elif two is five and five is eight:
        if two=='X':
            xtally=xtally+1
        else:
            ytally= ytally+1
        print('Player '+two+' wins \n')
        if player1Symbol=='X':
            xtally = str(xtally)
            ytally = str(ytally)
            print('Winner Tally \n'+ player1Name+': '+xtally+'\nComp: '+ytally+'\n')
        elif player1Symbol == 'O':
            xtally = str(xtally)
            ytally = str(ytally)
            print('Winner Tally \n'+ player1Name+': '+ytally+'\nComp: '+xtally+'\n')
        newGame = int(input('Enter 1to play agaion or 0 to exit the game: '))
        if newGame==1:
            clearBoard()
            soloPlay()
        else:
            print('GAME OVER \n')
            raise SystemExit
        '''-----------------------5----------------------'''
    elif three is six and six is nine:
        if three=='X':
            xtally=xtally+1
        else:
            ytally= ytally+1
        print('Player '+three+' wins \n')
        if player1Symbol=='X':
            xtally = str(xtally)
            ytally = str(ytally)
            print('Winner Tally \n'+ player1Name+': '+xtally+'\nComp: '+ytally+'\n')
        elif player1Symbol == 'O':
            xtally = str(xtally)
            ytally = str(ytally)
            print('Winner Tally \n'+ player1Name+': '+ytally+'\nComp: '+xtally+'\n')
        newGame = int(input('Enter 1to play agaion or 0 to exit the game: '))
        if newGame==1:
            clearBoard()
            soloPlay()
        else:
            print('GAME OVER \n')
            raise SystemExit
        '''------------------------6---------------------'''
    elif seven is five and five is three:
        if seven=='X':
            xtally=xtally+1
        else:
            ytally= ytally+1
        print('Player '+seven+' wins \n')
        if player1Symbol=='X':
            xtally = str(xtally)
            ytally = str(ytally)
            print('Winner Tally \n'+ player1Name+': '+xtally+'\nComp: '+ytally+'\n')
        elif player1Symbol == 'O':
            xtally = str(xtally)
            ytally = str(ytally)
            print('Winner Tally \n'+ player1Name+': '+ytally+'\nComp: '+xtally+'\n')
        newGame = int(input('Enter 1to play agaion or 0 to exit the game: '))
        if newGame==1:
            clearBoard()
            soloPlay()
        else:
            print('GAME OVER \n')
            raise SystemExit
        '''----------------------7-----------------------'''  
    elif four is five and five is six:
        if four=='X':
            xtally=xtally+1
        else:
            ytally= ytally+1
        print('Player '+four+' wins \n')
        if player1Symbol=='X':
            xtally = str(xtally)
            ytally = str(ytally)
            print('Winner Tally \n'+ player1Name+': '+xtally+'\nComp: '+ytally+'\n')
        elif player1Symbol == 'O':
            xtally = str(xtally)
            ytally = str(ytally)
            print('Winner Tally \n'+ player1Name+': '+ytally+'\nComp: '+xtally+'\n')
        newGame = int(input('Enter 1to play agaion or 0 to exit the game: '))
        if newGame==1:
            clearBoard()
            soloPlay()
        else:
            print('GAME OVER \n')
            raise SystemExit
        '''---------------------8------------------------''' 
    elif seven is eight and eight is nine:
        if seven=='X':
            xtally=xtally+1
        else:
            ytally= ytally+1
        print('Player '+seven+' wins \n')
        if player1Symbol=='X':
            xtally = str(xtally)
            ytally = str(ytally)
            print('Winner Tally \n'+ player1Name+': '+xtally+'\nComp: '+ytally+'\n')
        elif player1Symbol == 'O':
            xtally = str(xtally)
            ytally = str(ytally)
            print('Winner Tally \n'+ player1Name+': '+ytally+'\nComp: '+xtally+'\n')
        newGame = int(input('Enter 1to play agaion or 0 to exit the game: '))
        if newGame==1:
            clearBoard()
            soloPlay()
        else:
            print('GAME OVER \n')
            raise SystemExit
        '''---------------------------------------------'''   
    elif turnCount==9:
        print('NO WINNER \n')
        if player1Symbol=='X':
            xtally = str(xtally)
            ytally = str(ytally)
            print('Winner Tally \n'+ player1Name+': '+xtally+'\nComp: '+ytally+'\n')
        elif player1Symbol == 'O':
            xtally = str(xtally)
            ytally = str(ytally)
            print('Winner Tally \n'+ player1Name+': '+ytally+'\nComp: '+xtally+'\n')
        newGame = int(input('Enter 1to play agaion or 0 to exit the game: '))
        if newGame==1:
            clearBoard()
            soloPlay()
        else:
            print('GAME OVER \n')
            raise SystemExit
main()
