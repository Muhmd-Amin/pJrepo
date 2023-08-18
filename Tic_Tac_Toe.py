#declaration 

board = [[ str(j) + str(i) for i in range(3)] for j in range(3)]
player =''

#functions

def pr_func() :   
    '''Function to print the board to the players '''   
    print('\n The Board : ')
    for i in range(3) :
        br = ' '.join(board[i]) 
        print(br)       
#----------------------------------------------------------------------
def win_func() :
    '''Function to check if any player won'''
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)) :
            return True 
    if all(board[i][i] == player for i in range(3) ) or all(board[i][2-i] == player for i in range(3)) :
            return True
    else :
            return False
#----------------------------------------------------------------------
def tie_function():
    '''Function to check if it is a tie situation '''
    return all(board[i][j] in ('x' ,'o') for i in range(3) for j in range(3))

#----------------------------------------------------------------------
def move_func():
    '''Function to put the next move of the player on the board'''
    global player
    global board
    while True :  
        while True :
            try :
                row = int(input('please enter the number of the row (0 , 1 , 2) : ').strip())
                if row not in (0 , 1 , 2) :
                    row = int('l')
                else:
                    break
            except ValueError :
                print('please enter onle number from these numbers (0 , 1 , 2) ')
                continue
        while True :
            try :
                column = int(input('please enter the number of the column (0 , 1 , 2) : ').strip())
                if column  not in (0 , 1 , 2) :
                    row = int('l')
                else:
                    break
            except ValueError :
                print('\nplease enter onle number from these numbers (0 , 1 , 2) ')
                continue
                
        if player == 'x' :
            if board[row][column] not in ('x' , 'o'):   
                    board[row][column] = 'x'
                    break
            else:
                    print('\nthis position is taken try again')
                    continue
        else:
            if board[row][column] not in ('x' , 'o'):   
                    board[row][column] = 'o'
                    break
            else:
                    print('\nthis position is taken try again')
                    continue          
#----------------------------------------------------------------------
print('\nThe Board : (Note -> The value like (01) first number row and second number is column) \n')
while True:
    '''The logic of the game '''
    
    player = input('choose (x or o) : ').strip().lower()   
    if player not in ('x','o'):
        print('please choose (x or o) try again!')
        continue
    else:
        break 

while True :
    if player == 'x' :
        print ('\nX player turn :\n')
    else:
       print ('\nO player turn :\n') 
    
    pr_func()
    move_func()  
    win = win_func()
    tie = tie_function()
    
    if win :
        print(f'The Winner is {player}')
        pr_func()
        break
    elif tie :
         print('unfortionatily it is tie situation!') 
         pr_func()
         break
    else:
        if player == 'o' :
            player = 'x'
        else:
            player = 'o'