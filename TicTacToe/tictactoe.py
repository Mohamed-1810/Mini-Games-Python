
def printBoard(board):
    # print()
    # print("|   |   |   |")
    print(" "+board[1]+" | "+board[2]+" | "+board[3]+" ")
    # print("|   |   |   |")
    print("----------")
    # print("|   |   |   |")
    print(" "+board[4]+" | "+board[5]+" | "+board[6]+" ")
    # print("|   |   |   |")
    print("-----------")
    # print("|   |   |   |")
    print(" "+board[7]+" | "+board[8]+" | "+board[9]+" ")
    # print("|   |   |   |")
    # print("----------")
    print()

def isboardFull(board):
    if board.count(' ')>1:
        return False 
    else:
        return True  

def isWinner(b,l):
    return ((b[1] == l and b[2] == l and b[3] == l) or
    (b[4] == l and b[5] == l and b[6] == l) or
    (b[7] == l and b[8] == l and b[9] == l) or
    (b[1] == l and b[4] == l and b[7] == l) or
    (b[2] == l and b[5] == l and b[8] == l) or
    (b[3] == l and b[6] == l and b[9] == l) or
    (b[1] == l and b[5] == l and b[9] == l) or
    (b[3] == l and b[5] == l and b[7] == l)) 
 
def spaceisFree(m):
    if board[m]==' ':
        return True 
    else:
        return False

def insert(letter,pos):
    board[pos]=letter 

def playerMove(p):
    if p.lower()=='one':
        run=True 
        while run:
            move=input("Please select a position to Enter the X between 1 to 9: ")
            try:
                move=int(move)
                if move>0 and move<10:
                    if spaceisFree(move):
                        run=False 
                        insert('X',move)
                    else:
                        print("Please Enter a Position, that's not Occupied")
                else:
                    print("Please Enter a number between 1 and 9")
            except:
                print("Please type a Integer")
    else:
        run=True 
        while run:
            move=input("Player 1 Enter between 1 to 9 for Positon 'X': ")
            try:
                move=int(move)
                if move>0 and move<10:
                    if spaceisFree(move):
                        run=False 
                        insert('X',move)
                    else:
                        print("Player1 :Please Enter a Position, that's not Occupied")
                else:
                    print("Player1 :Please Enter a number between 1 and 9")
            except:
                print("Player11 :Please type a Integer")

def player1Move():
    run=True 
    while run:
        move=input("Player 2 Enter between 1 to 9 for Positon 'O':")
        try:
            move=int(move)
            if move>0 and move<10:
                if spaceisFree(move):
                    run=False 
                    insert('O',move)
                else:
                    print("Player2 :Please Enter a Position, that's not Occupied")
            else:
                print("Player2 :Please Enter a number between 1 and 9")
        except:
            print("Player2 :Please type a Integer")




def computerMove():
    possibleMoves=[x for x,letter in enumerate(board) if letter==' ' and x!=0]
    move=0

    for let in ['O','X']:
        for i in possibleMoves:
            bcopy=board[:]
            bcopy[i]=let 
            if isWinner(bcopy,let):
                move=i 
                return move 
    cornersOpen=[]
    for i in possibleMoves:
        if i in [1,3,7,9]:
            cornersOpen.append(i) 

    if len(cornersOpen)>0:
        move =selectRandom(cornersOpen)
        return move       

    if 5 in possibleMoves:
        return 5 
    
    edgesOpen = []
    for i in possibleMoves:
        if i in [2,4,6,8]:
            edgesOpen.append(i)

    if len(edgesOpen)>0:
        move =selectRandom(edgesOpen)
        return move 

def selectRandom(li):
    import random
    ln=len(li)
    r=random.randrange(0,ln)
    return li[r]


def main():
    Player=input("Enter 'One' for One Player OR 'Two' for Two Player:")
    if Player.lower()=='one':
        print("Welcome to the game!")
        printBoard(board)
        while not(isboardFull(board)):
            if not(isWinner(board,'O')):
                playerMove(Player)
                printBoard(board)
            else:
                print("Sorry You LOOSE") 
                break 
            
            if not(isWinner(board,'X')):
                move=computerMove()
                if isboardFull(board):
                    break
                else:
                    print(move)
                    insert('O',move)
                    print("Computer Placed an O on Positon ",move,':')
                    printBoard(board)
            else:
                print("You Win the Game!")
                break
        if isboardFull(board):
            print()
            print("Tie Game!")
    elif Player.lower()=='two':
        print("Welcome to the Game:")
        print("Player1:'X' \n Player:'O'")
        printBoard(board)
        while not(isboardFull(board)):
            if not(isWinner(board,'O')):
                playerMove(Player)
                printBoard(board)
            else:
                print("Player 2 WON") 
                break 

            if not(isWinner(board,'X')):
                player1Move()
                printBoard(board)
            else:
                print("Player 1 WON")
                break
    else:
        print("Please Enter 'One' or 'Two'")
        
while True:
    x=input("Press 'Y' to Start the Game: ")
        # x=input("Do you want to Play again? (y/n): ")
    if x.lower()=='y':
        board=[' ' for i in range(10)]
        print('------------------')
        main()
    else:
        break
