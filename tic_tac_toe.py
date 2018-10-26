from itertools import permutations
import sys
import random
import os
import time


def win(data):
    win_comb = [ (1,2,3), (1,4,7), (1,5,9), (2,5,8), (3,6,9), (3,5,7),(4,5,6), (7,8,9) ]
    player_comb = list(permutations(sorted(data),3))


    for comb in win_comb:
        if comb in player_comb :
            return True
    else :
        return False


def print_board(msg):
    clr_scr()
    print(msg)
    print("\n\nYour Current Board is : \n")
    
    for var in board :
        print("\t\t\t","-"*19)
        print("\t\t\t","|     |     |     |")
        print("\t\t\t",f"|  {var[0]}  |  {var[1]}  |  {var[2]}  |")
        print("\t\t\t","|     |     |     |")

    print("\t\t\t","-"*19)
    print("\n\n")




def choice(player):
    
    possible_choices = [ '1','2','3','4','5','6','7','8','9' ]
    print("\n\nLeft Positions : ",*total_pos)
    ch = input(f"\n\n{player} pos : ")
    if ch in possible_choices :
        ch = int(ch)
        if ch in covered_pos : 
            print_board("")
            print("\n\nThat Position is Already Choosen Please Select Another Position \n\n")
            return choice(player)
        else :
            covered_pos.append(ch)
            total_pos.remove(ch)
            return ch

    else :
        print_board("")
        print("\n\nInvalid Choice please Select only 1-9 positions \nTry Again\n\n")
        return choice(player)

def play_game(p_list):
    c = 1
    ch1 = choice(p_list[1][0])
    p_list[1][2].append(ch1)
    pos_ch1 = pos.get(ch1)
    board[pos_ch1[0]][pos_ch1[1]] = p_list[1][1]
    print_board(f'\n\nAfter move {c} the board is ')
    if win(p_list[1][2]) :
        print(f"\n\nPlayer {p_list[0][0]} has won the Game\n\n")
        return True
    c = c + 1
    
    k = 1 
    while k <= 4 :
        ch1 = choice(p_list[0][0])
        p_list[0][2].append(ch1)
        pos_ch1 = pos.get(ch1)
        board[pos_ch1[0]][pos_ch1[1]] = p_list[0][1]
        print_board(f'\n\nAfter move {c} the board is ')
        if win(p_list[0][2]) :
            print(f"\n\nPlayer {p_list[0][0]} has won the Game\n\n")
            break
        c = c + 1
        ch1 = choice(p_list[1][0])
        p_list[1][2].append(ch1)
        pos_ch1 = pos.get(ch1)
        board[pos_ch1[0]][pos_ch1[1]] = p_list[1][1]
        print_board(f'\n\nAfter move {c} the board is ')
        if win(p_list[1][2]) :
            print(f"\n\nPlayer {p_list[1][0]} has won the Game\n\n")
            break
        c = c + 1
        k = k + 1
       

    else :
        print(f"\n\nwoooo...Match is Tie Between {p_list[0][0]} and {p_list[1][0]}\n\n")


def clr_scr():
    
    os.system('cls')
    print('\n\n\n')

if __name__ == "__main__" : 
    
    clr_scr()
    print("\n\nWelcome to Tic Tac Toe Game\n\n") 
    pos = { 1:(0,0), 2:(0,1), 3:(0,2), 4:(1,0), 5:(1,1), 6:(1,2), 7:(2,0),8:(2,1),9:(2,2) }
    

    board = [ [ 1, 2, 3 ], [ 4, 5, 6 ], [ 7, 8, 9 ] ]
    print_board('\t\tHere are the key Positions to select your move')
    
    input("\n\nPress Enter key to Continue Game ")
    
    board = [ [ ' ', ' ', ' ' ], [ ' ', ' ', ' ' ], [ ' ', ' ', ' '] ]
    print_board('\t\tafter initial Move the board is ')
    
    player1 = input("\n\nEnter Player one name : ")
    player2 = input("\n\nEnter player two name : ")

    time.sleep(2)
    clr_scr()
    print("\n\nSymbols --> X and 0 ")
    print("\n\nChoosing The Symobls for each Player")
    symbol = [ 'X', '0']
    random.shuffle(symbol)
    print(f'\n\n{player1} symbol is - {symbol[0]}')
    print(f'\n\n{player2} symbol is - {symbol[1]}')

    p_list = ( ( player1, symbol[0],[] ),( player2, symbol[1],[] ) )
   
    total_pos = [ 1, 2, 3, 4, 5, 6, 7, 8, 9 ]
    covered_pos = [] 

    input("\nPress Any key to Start Game ".center(300))
    print_board('Initial Status of Board')

    play_game(p_list)

