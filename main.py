#!/usr/bin/env python
from x_o_design import design_final

'''
The main aim of this file is:
1)to take in the name and symbol(i.e. X or O) for each player using OOP
2)next step is to take in entries of the game-board from the players one after another by using 
  dictionary called matrix_choices
3)from the fifth entry, along with taking entries from players,conditions of the game are also checked 
   (i.e. checking if horizontal,vertical and diagonal entries are of same symbol or not)
4)if any such conditions are satisfied, the winner is declared. Else,game is declared as: draw. 

Note:1)Player1 will have first turn followed by player 2
     2)I formatted these two files by myselves as on using the formatting tool, i was gettin syntax errors
     3)please make sure that the input format is slightly differing for VS code and other IDEs
     4)if u r using VScode, pls do give name of players and symbols in single quotes 
       and the keys for the dictionary as integers.
'''


design_object=design_final()

available_symbols=['X','O']

#dictionary to allow the players to fill entries
#when asked, please enter an entry from 1-9 as keys for the corresponding coordinate values
matrix_choices={1:[0,0],2:[0,1],3:[0,2],4:[1,0],5:[1,1],6:[1,2],7:[2,0],8:[2,1],9:[2,2]}

#function to perform all the activities with the two objects
def gaming(player_1,player_2):
    tictactoe_matrix=[[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
    #2D matrix in which each sublist corresponds to the row of the game-board

    #this function is to check the entries along the column or vertically
    #entry1,entry2,entry3 correspond to the rows of the game-board after each entry
    def checking_1(entry1,entry2,entry3):
        i=0
        while i<3:
            if entry1[i]==entry2[i] and entry2[i]==entry3[i] and entry2[i]!=' ':
                return 1
            i+=1
    
    #this function is to check the entries along the row or horizontally
    def checking_2(entry1,entry2,entry3):
        if entry1[0]==entry1[1] and entry1[0]==entry1[2] and entry1[0]!=' ':
            return 1
        
        elif entry2[0]==entry2[1] and entry2[0]==entry2[2] and entry2[0]!=' ':
            return 1
            
        elif entry3[0]==entry3[1] and entry3[0]==entry3[2] and entry3[0]!=' ':
            return 1
    
    #this function is to check the entries along the diagonals or crosswards
    def checking_3(entry1,entry2,entry3):
        if entry1[0]==entry2[1] and entry1[0]==entry3[2] and entry1[0]!=' ':
            return 1
        
        elif entry1[2]==entry2[1] and entry1[2]==entry3[0] and entry1[2]!=' ':
            return 1
    
    count=1
    #variable to measure the entry number i.e. to measure the number of cells filled after each entry
    #after each entry is made,corresponding coordinates will be deleted from the matrix_choices dictionary

    while count<10:
        if count<5:
            print(matrix_choices)

            #variable to store the key of the matrix_choices dictionary given by the user
            loc=int(input(player_1.name+"!!Please enter any location from the choices available: "))

            #variable to store the coordinates given in the matrix_choices dictionary
            coord=matrix_choices[loc]

            #filling the elements in the tictactoe_matrix with the corresponding symbol
            tictactoe_matrix[coord[0]][coord[1]]=player_1.symbol

            
            del matrix_choices[loc]
            
            #deleting the coordinates stored in previous entry for filling the coordinates for next entry
            del(coord[0])
            del(coord[0])

            #status of game-board is printed after every entry
            print("")
            print("Players!!The current board status is: ")
            print("")
            design_object.designer_final(tictactoe_matrix)
            
            count=count+1
            print("")
            print(matrix_choices)
            loc=int(input(player_2.name+"!!Please enter any location from the choices available: "))
            coord=matrix_choices[loc]
            tictactoe_matrix[coord[0]][coord[1]]=player_2.symbol
            del matrix_choices[loc]
            del(coord[0])
            del(coord[0])
            print("")
            print("Players!!The current board status is: ")
            print("")
            design_object.designer_final(tictactoe_matrix)
        

        #after 5 cells are filled,conditions will be checked each time

        #for checking conditions for player 1 entries 
        elif count>=5 and count%2==1:
            print("")
            print(matrix_choices)
            loc=int(input(player_1.name+"!!Please enter any location from the choices available: "))
            coord=matrix_choices[loc]
            tictactoe_matrix[coord[0]][coord[1]]=player_1.symbol
            del matrix_choices[loc]
            del(coord[0])
            del(coord[0])
            print("")
            print("Players!!The current board status is: ")
            print("")
            design_object.designer_final(tictactoe_matrix)
            if checking_1(tictactoe_matrix[0],tictactoe_matrix[1],tictactoe_matrix[2]) or checking_2(tictactoe_matrix[0],tictactoe_matrix[1],tictactoe_matrix[2]) or checking_3(tictactoe_matrix[0],tictactoe_matrix[1],tictactoe_matrix[2]):
                print("\tYayy!!Player 1 is the winner!!"),
                print("KUDOS")
                print("\n\t\tGAME OVER")
                exit()
        
        #for checking conditions for player 2 entries  
        else:
            print("")
            print(matrix_choices)
            loc=int(input(player_2.name+"!!Please enter any location from the choices available: "))
            coord=matrix_choices[loc]
            tictactoe_matrix[coord[0]][coord[1]]=player_2.symbol
            del matrix_choices[loc]
            del(coord[0])
            del(coord[0])
            print("")
            print("Players!!The current board status is: ")
            print("")
            design_object.designer_final(tictactoe_matrix)
            if checking_1(tictactoe_matrix[0],tictactoe_matrix[1],tictactoe_matrix[2]) or checking_2(tictactoe_matrix[0],tictactoe_matrix[1],tictactoe_matrix[2]) or checking_3(tictactoe_matrix[0],tictactoe_matrix[1],tictactoe_matrix[2]):
                print("\tYayy!!Player 2 is the winner!!"),
                print("CONGO")
                print("\n\t\tGAME OVER")
                exit()
        count+=1
    print("\tWHOAH!!Its a draw!!")
    print("\n\t\tGAME OVER")
    exit()

            

class gamer:
    name=" "
    symbol=' '

#following few steps involve making of an object for each player for name and symbol
player1=gamer()
player1.name=input("Enter the name of Player 1: ")
player1.symbol=input(player1.name+" Pls enter either X or O: ")
available_symbols.remove(player1.symbol)

print("")

player2=gamer()
player2.name=input("Enter the name of Player 2: ")
player2.symbol=available_symbols[0]
#the symbol for the second player is automatically declared by removing the symbol selected by the first player from the symbols list

#the initial empty game-board is being displayed
print("")
print("Here's the Tic-Tac-Toe table: ")
design_object.designer_final([[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']])
print("")

print("")
gaming(player1,player2)
print("")



