import random
import numpy as np
import matplotlib.pyplot as plt
from typing import List

class Board(object):
    
    """
    Board class - Create board with given start and end position.
                  Validate the input values of the board.
                  Input values:
                    - start value
                    - end value
                    - snake list
                    - ladder list
    
    Parameter:
    ----------
    
    snakes  : List of list of integers.
    ladders : List of list of integers.
    start   : Integer.
    end     : Integer.
    
    Method:
    -------
    
    init() : Initialize the parameters.
             
             Input verification.

             Given cases are sample only:
                
                - Board input verification:
                    example : Game start value is grater than or equals to end value 
                    then print invalid board with reason.

                - Snake input verification:
                    example : Snake head value is less than snake tail then print invalid snake with reason.  
                
                - Ladder input verification:
                    example : Ladder top is less than ladder base then print invalid ladder with reason.
                    
                - Snake ladder cross verification:
                    example : Same position - snake tail and ladder base (or) ladder top and snake head then
                    print invalid combination of ladder and snake with reason.
                        
        Return:
        -------
        
            Return : None 
    
    """
    
    def __init__(self,
                 snakes:List[List[int]],
                 ladders:List[List[int]],
                 start:int=1,
                 end:int=100
                 ) -> None:
        
        #Initialize the values:
        
        # Board start value is start
        # Board end value is end
        # Board total length is number of cells in that board.
        # example: start is 0 and end is 100 then total cell value is 101.
        # Board snake list : snakes
        # Board ladder list : ladders
        
        # work space 
        
        
        # Board Input Verification
        
        # Write a code that statement:
        
        # Starting value is grater than or equal to end then print Invalid board.
        
        # work space 
        
        
        # Board length is less than 2 then print Invalid board
        
        # work space
        
        
        # Snake Input Verification
        # Consider a board : [1,2,3,...,100]
        # Consider a example snake list is : [[4,10],[20,-2],[-2,65]]
        # From the snake list we need to verify each snake head and tail is valid.
        # Note: [5,1] - 5 is head of the snake, 1 is tail of the snake.
        # If I take the first list from this example snake list - [4,10]
        # 4 is snake head and tail is 10. If I bite 4 then I will go to 10.
        # This is not a snake behaviour. So the list like this are Invalid.
        # If you have Invalid list then print - Invalid list along with that list.
        
        # Chances of getting invalid snake list:
        # snake head is less than or equal to snake tail
        # snake head is less than start value or grater than end value
        # snake tail is less than start value or grater than end value
        
        
        # work space 
        
             
        # Ladder Input Verification
        # Like snake list, ladder list - [2,20] : 2 is ladder base and 20 is the top
        
        # If you have Invalid list then print - Invalid list along with that list.
        
        # Chances of getting invalid ladder list:
        # ladder top is less than or equal to ladder base
        # ladder top is less than start value or grater than end value
        # ladder base is less than start value or grater than end value
        
        # work space
             
        # Snake Ladder Cross Verification
        # Chances of getting invalid combination of snake and ladder
        # Ladder top position is same as snake head
        # Snake head position is same as ladder base
        
        # work space
        
        
class Die():
    
    """
    Die class - Control die
    This class help us to generate a random value for each player
    
    """
        
    def roll_die(self):
        
        """ 
        Randomly generate die value with respect to given range.

        Returns:
            int : die value between the given range.
        """
        
        # Given range is 1 to 6. Then return any random integer between the interval.
        # Example: call a roll_die() -> any interger between 1 to 6
         
        
class Game(Board,Die):
    """
    Game class - main class. it's controll entire game.
                 Inherits from Board and Die classes.
    Args:
        Board (Class): Board of the game
        Die (Class): Die of the game 
    
    Method:
    -------
    init():
    
        Parameter:
        ----------
    
        snakes      : List of list of integers.
        ladders     : List of list of integers.
        start       : Integer.
        end         : Integer.
        num_player  : Integer.
        
    Return:
    ------
        Return : none
    
    """
    
    def __init__(self,
                 snakes:List[List[int]],
                 ladders:List[List[int]],
                 start:int=1,
                 end:int=100,
                 num_players:int=2
                 ) -> None:
    
        
        super().__init__(snakes, 
                         ladders,
                         start, 
                         end)
        
        super(Die,self).__init__()
        
        #Initialize the variables
        # Number of players is num_players
        # Player positions is list of each player position. example [0,0]
        # Hint : player position = [start] * number of players
        # Each player's die value is list of die values. example [2,5]
        # Hint : number die throws = [0] * number of players
        # Winner is which player first reach end position.
        # example: [100,67] -> Then player 1 is winner.
        # Initialize winner.
          
        
    def play_game(self):
        
        """
        Play game method take self as a parameter. This method uses the appropriate value
        for finding the each players die value and their position. Each round the die is roll.
        Each player roll a die. After complete the everyone rolled a die. The next round will be start.
        For each player's current position check snake/ladder is there then move your position
        to that one. Which player reach the end, then game is over. That player won the game.
        Parameter : self
        
        Returns:
            list[int,int]: list[number of rounds play, winning player] 
        """
        
        # calculate each round
        # Start a game
        # Example: 
        # 2 player ready to start their game
        # players position is [0,0]
        # First time the die is rolled for first player
        # Then add a die value to that player's postion index
        # Then check on that position there's any snake or ladder
        # If there's no snake or ladder player is stayed that accumulated value
        # If snake or ladder is exist then change the position of the player
        # After completing first player process move to next players
        # After completing all of them then the first round is over
        # if any player reach the end then return that round they are going and which player is won
        # The game is end
        
        # work space
        
        
if __name__ == "__main__":
    
    random.seed(1234)
    snakes=[[17,7],
            [54,34],
            [62,19],
            [64,60],
            [87,24],
            [93,72],
            [96,76],
            [99,78]]
    ladders=[[4,14],
             [9,31],
             [20,36],
             [28,84],
             [40,59],
             [51,67],
             [63,81],
             [71,91]]
    
    our_game=Game(snakes,ladders,1,100,2)
    our_game.play_game()
    