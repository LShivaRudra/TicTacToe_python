# /usr/bin/env python

'''
XX      XX
  XX  XX
    XX
  XX  XX
XX      XX
          
'''
'''
   OOOO   
 OO    OO
OO      OO
 OO    OO
   OOOO
'''

'''The main aim of this file is:
    1)to take in the 2D array i.e. tictactoe_matrix(from main.py) which has row matrices of the game-board.
    2)to extract each row of the tictactoe_matrix one iteration after another naming it each time as "mat"
    3)now each element of the list i.e. mat is stored in a,b and c respectively
    4)a dictionary named allotment_dictionary is created so as to check the elements in a,b and c and allot the required pattern to each row 
       which on iteration forms the complete table for each entry of a player and prints the game-board status in each step 
    5)another key idea is to print the rows by printing each line of the patterns one by one leading to the formation of the complete row.'''


#The following are the string lists each of which has rows of the above shown X and O patterns
pattern_X=["XX      XX", "  XX  XX  ", "    XX    ", "  XX  XX  ", "XX      XX"]

pattern_O=["   OOOO   ", " OO    OO ", "OO      OO", " OO    OO ", "   OOOO   "]

#pattern_space is created so as to fill the cell in the game-board where X or O are not filled
pattern_space=["          ", "          ", "          ", "          ", "          "]


class design_final:
    #the following function takes in the 2D list having the elements of the game-board in the required manner
    def designer_final(self,tictactoe_matrix):

        allotment_dictionary={'X':pattern_X,'O':pattern_O,' ':pattern_space}
        for z in range(0,24,1):
            print("-"),
        print("")
        for x in range(0,3,1):
            mat=tictactoe_matrix[x]
            a=mat[0]
            b=mat[1]
            c=mat[2]

            '''The following three steps form the most important part- extracting the elements in each cell of the game-board and using them as the keys 
                for the allotment_dictionary so as to figure out the pattern '''
            d=allotment_dictionary[a]
            e=allotment_dictionary[b]
            f=allotment_dictionary[c]

            #printing the vertical lines in the game-board along with each row of the tictactoe_matrix
            for y in range(0,5,1):
                print(" | "),
                print(d[y]),
                print(" | "),
                print(e[y]),
                print(" | "),
                print(f[y]),
                print(" | ")
            
            #printing the horizontal lines of the game-board
            for z in range(0,24,1):
                print("-"),
            print("")

        for m in range(0,45,1):
            print("xo"),   
        print("")
        print("")

