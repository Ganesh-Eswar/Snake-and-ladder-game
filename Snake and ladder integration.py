import random
import numpy as np
import matplotlib.pyplot as plt
from typing import List
import tkinter as tk
from tkinter import *
from PIL import ImageTk,Image
import time

class Display(object):
    
    def __init__(self,b_image,dice_initial_img,dice_img_list) -> None:
        
        self.root = tk.Tk()

        self.root.geometry("1200x800")

        self.root.title("Snake and ladder game")

        self.F1 = tk.Frame(self.root,width=1200,height=800,relief='raised')

        self.F1.place(x=0,y=0)

        #set image

        self.dice_ini_img = dice_initial_img
        
        self.dice_list = []
        
        self.dice_img = dice_img_list
        
        self.background_image = Image.open(b_image)

        self.resized_img = self.background_image.resize((700,700),Image.ANTIALIAS)

        self.render_img = ImageTk.PhotoImage(self.resized_img)
  
        self.b_Label = tk.Label(self.F1,image=self.render_img)

        self.b_Label.place(x=0,y=0)


        # create player 1 coin

        self.player_1 = tk.Canvas(self.root,width=40,height=40)

        self.player_1.create_oval(10,10,40,40,fill='orange')

        # create player 2 coin

        self.player_2 = tk.Canvas(self.root,width=40,height=40)

        self.player_2.create_oval(10,10,40,40,fill='pink')

        # player 1 button 

        self.b1 = tk.Button(self.root,activebackground='yellow',bg='orange',height=3,width=20,fg='black',text='Player 1',font=('Cursive',14,'bold'))

        # player 2 button 

        self.b2 = tk.Button(self.root,activebackground='yellow',bg='pink',height=3,width=20,fg='black',text='Player 2',font=('Cursive',14,'bold'))


        # initial position 
        self.pos1 = None
        self.pos2 = None

        # snake dict

        self.snake = {43:17,50:5,56:8,73:15,84:58,87:49,98:40}

        # ladder dict 

        self.ladder = {2:23,6:45,20:59,52:72,57:96,71:92}

    def player_buttons(self):
        
        #Botton create
    
        # Player 1

        self.b1.place(x=1000,y=300)

        # Player 2

        self.b2.place(x=1000,y=400)

        # Dice 

        dice = Image.open(self.dice_ini_img)

        re_dice = dice.resize((100,100))

        dice_img = ImageTk.PhotoImage(re_dice)

        d_button = tk.Button(self.root,image=dice_img,height=80,width=80)

        d_button.place(x = 1100, y = 700)

        # Exit button 

        b3 = tk.Button(self.root,activebackground='red',bg='black',height=3,width=20,fg='white',text='End the game',font=('Cursive',14,'bold'),command=self.root.destroy)

        b3.place(x=1000,y=100)
        
    def reset_coins(self):
        
        self.player_1,self.player_2,self.pos1,self.pos2
    
        self.player_1.place(x=0,y=700)

        self.player_2.place(x=0,y=750)
    
        self.pos1 = 0 
        self.pos2 = 0
    
    def dice_create(self):

        dice_image_list = self.dice_img 
    
        for di in dice_image_list:
        
            dice = Image.open(di)

            re_dice = dice.resize((80,80))

            dice_img = ImageTk.PhotoImage(re_dice)
        
            self.dice_list.append(dice_img)
    
    def get_index(self):
    
        self.index = {}
    
        self.board_arrangement = [100,99,98,97,96,95,94,93,92,91,81,82,83,84,85,86,87,88,89,90,80,79,78,77,76,75,74,73,72,71,61,62,63,64,65,66,67,68,69,70,60,59,58,57,56,55,54,53,52,51,41,42,43,44,45,46,47,48,49,50,40,39,38,37,36,35,34,33,32,31,21,22,23,24,25,26,27,28,29,30,20,19,18,17,16,15,14,13,12,11,1,2,3,4,5,6,7,8,9,10]

        vertical_shift = 70
        horizontal_shift = 70
    
        i = 0
        y = 4
        x = 8
     
        for f_row in range(1,11):
        
            x = 8
        
            for f_col in range(1,11):
                 
                self.index[self.board_arrangement[i]] = (x,y)
            
                x += horizontal_shift
            
                i += 1
        
            y += vertical_shift 
    
    def move_coins(self,player_index,dice_value):
        
        x_co = self.index[dice_value][0]
        y_co = self.index[dice_value][1]
    
        if(player_index == 0):
            self.player_1.place(x=x_co,y=y_co)
    
        else:
            self.player_2.place(x=x_co,y=y_co)
      
     
           
class Board(object):
    
    def __init__(self,
                 snakes:List[List[int]],
                 ladders:List[List[int]],
                 start:int=1,
                 end:int=100
                 ) -> None:
        
        self.start = start
        self.end = end
        self.length = self.end-self.start+1
        
        # Board Input Verification
        if start>=end:
            print(f"Invalid board with start value {start} and end value {end}")
        if(self.length<2):
            print(f"Invalid board with start value {start} and end value {end} and size less than 2")
        
        self.snakes = snakes 
        self.ladders = ladders
    
        
        # Snake Input Verification
        for snake in snakes:
            if(snake[0]<=snake[1]):
                print(f"Invalid snake starting at {snake[0]} and ending at {snake[1]}")
            if(snake[0]<self.start or snake[0]>self.end):
                print(f"Invalid snake starting at {snake[0]} and ending at {snake[1]} outside board boundaries")
            if(snake[1]<self.start or snake[1]>self.end):
                print(f"Invalid snake starting at {snake[0]} and ending at {snake[1]} outside board boundaries")
                
        # Ladder Input Verification
        for ladder in ladders:
            if(ladder[1]<=ladder[0]):
                print(f"Invalid ladder starting at {ladder[0]} and ending at {ladder[1]}")
            if(ladder[0]<self.start or ladder[0]>self.end):
                print(f"Invalid ladder starting at {ladder[0]} and ending at {ladder[1]} outside board boundaries")
            if(ladder[1]<self.start or ladder[1]>self.end):
                print(f"Invalid ladder starting at {ladder[0]} and ending at {ladder[1]} outside board boundaries")
                
        # Snake Ladder Cross Verification
        for ladder in ladders:
            for snake in snakes:
                if(ladder[1]==snake[0]):
                    print(f"Invalid combination of snake {snake[0]}-{snake[1]} and ladder {ladder[0]}-{ladder[1]}")
                
                if(snake[1]==ladder[0]):
                    print(f"Invalid combination of snake {snake[0]}-{snake[1]} and ladder {ladder[0]}-{ladder[1]}")
        
class Die():
    
    def __init__(self) -> None:
        
        self.die_start_value = 1
        self.die_end_value = 6 
        
    def roll_die(self):
        
        die_value = random.randint(1,6)
        
        return die_value
    
    
class Game(Board,Die,Display):
    
    def __init__(self,
                 b_image,
                 dice_initial_img,
                 dice_img_list,
                 snakes:List[List[int]],
                 ladders:List[List[int]],
                 start:int=1,
                 end:int=100,
                 num_players:int=2,
                 ) -> None:
        
        Display.__init__(self,b_image,dice_initial_img,dice_img_list)
        
        Board.__init__(self,snakes, 
                         ladders,
                         start, 
                         end)
        
        Die.__init__(self)
        
        self.num_players = num_players
        self.player_positions = [self.start]*self.num_players
        self.num_die_throws = [0]*self.num_players
        self.winner = None
        self.num_rounds=0
        self.player_positions = [self.start]*self.num_players
        self.num_die_throws = [0]*self.num_players
        # self.winner = None
        Display.player_buttons(self)
        Display.reset_coins(self)
        Display.dice_create(self)
        Display.get_index(self)
        
        self.start_button = tk.Button(self.root,activebackground='yellow',bg='black',height=3,width=20,fg='white',text='Play',font=('Cursive',14,'bold'),command=self.play_game)
        self.start_button.place(x=1000,y=600)
        
        self.root.mainloop()
        
    def play_game(self):
                
        self.num_rounds=self.num_rounds+1
        for player_index in range(self.num_players):
                
            if(player_index == 0):
                # player 1 button 
                self.b1 = tk.Button(self.root,bg='yellow',height=3,width=20,fg='black',text='Player 1',font=('Cursive',14,'bold'))
                
                # player 2 button 

                self.b2 = tk.Button(self.root,bg='black',height=3,width=20,fg='black',text='Player 2',font=('Cursive',14,'bold'))
                  
                    
            else:
                    
                # player 1 button
                
                self.b1 = tk.Button(self.root,bg='black',height=3,width=20,fg='black',text='Player 1',font=('Cursive',14,'bold'))
                    
                # player 2 button 
                
                self.b2 = tk.Button(self.root,bg='yellow',height=3,width=20,fg='black',text='Player 2',font=('Cursive',14,'bold'))
                    
                    
            val=self.roll_die()
            
            if(player_index == 0):   
            
                player1_button = tk.Button(self.root,image=self.dice_list[val-1],height=80,width=80)

                player1_button.place(x = 1000, y = 700)
                
                player1_label = tk.Button(self.root,text='Player 1',height=2,width=10)

                player1_label.place(x = 1000, y = 800)

            
            else:
                
                player2_button = tk.Button(self.root,image=self.dice_list[val-1],height=80,width=80)

                player2_button.place(x = 1200, y = 700)
                
                player2_label = tk.Button(self.root,text='Player 2',height=2,width=10)

                player2_label.place(x = 1200, y = 800)
            
            
            self.num_die_throws[player_index]=self.num_die_throws[player_index]+1
                
            self.player_positions[player_index]=min(self.end,self.player_positions[player_index]+val)
                
            if(self.player_positions[player_index]<=100):
                    
                self.move_coins(player_index,self.player_positions[player_index])
                  
                    
            if(self.player_positions[player_index]==self.end):
                self.winner = player_index+1
                msg = "Player" + " "+str(self.winner)+" is the Winner."
                round_msg = "Total round they played : "+str(self.num_rounds)
                d_box = tk.Label(self.root,text=msg,bg='red',height=2,width=20,font=('Cursive',20,'bold'))
        
                d_box.place(x=150,y=200)
                    
                r_box = tk.Label(self.root,text=round_msg,bg='red',height=2,width=30,font=('Cursive',20,'bold'))
        
                r_box.place(x=80,y=300)
                self.b1.configure(state='disabled')
                self.b2.configure(state='disabled')
                self.start_button.configure(state='disabled')
                
                self.reset_coins()
                   
                #print(self.player_positions)
                #print(f"Player {self.winner} won in {self.num_rounds} number of moves")
                break
                
            for snake in self.snakes:
                if snake[0]==self.player_positions[player_index]:
                    #print(f"Player {player_index+1} got bitten by a snake at {snake[0]}")
                    self.player_positions[player_index]=snake[1]
                    self.move_coins(player_index,self.player_positions[player_index])
                        
                        
            for ladder in self.ladders:
                if ladder[0]==self.player_positions[player_index]:
                    #print(f"Player {player_index+1} got onto a ladder at {ladder[0]}")
                    self.player_positions[player_index]=ladder[1]
                    self.move_coins(player_index,self.player_positions[player_index])
                        
        print(f"Results of round {self.num_rounds}")
        print(self.player_positions)
            
        self.root.mainloop()
        #return [num_rounds,self.winner]
        
if __name__ == "__main__":
    
    background_image = 'D:\Hope\Phase 2 python projects\Snake and Ladder Game\image (2).png'
    
    dice_initial_image = 'D:\Hope\Phase 2 python projects\Snake and Ladder Game\dice.png'
    face1 = 'D:\Hope\Phase 2 python projects\Snake and Ladder Game\Ff1.png'
    face2 = 'D:\Hope\Phase 2 python projects\Snake and Ladder Game\Ff2.png'
    face3 = 'D:\Hope\Phase 2 python projects\Snake and Ladder Game\Ff3.png'
    face4 = 'D:\Hope\Phase 2 python projects\Snake and Ladder Game\Ff4.png'
    face5 = 'D:\Hope\Phase 2 python projects\Snake and Ladder Game\Ff5.png'
    face6 = 'D:\Hope\Phase 2 python projects\Snake and Ladder Game\Ff6.png'
    
    dice_img_face_list = [face1,face2,face3,face4,face5,face6]
    
    #display_sl = Display(background_image,dice_initial_image,dice_img_face_list)
    
    # display_sl.player_buttons()
    
    # display_sl.reset_coins()
    
    # display_sl.dice_create()
    
    # display_sl.get_index()
    
    snakes=[[43,17],
            [50,5],
            [56,8],
            [73,15],
            [84,58],
            [87,49],
            [98,40]]
    
    ladders=[[2,23],
             [6,45],
             [20,59],
             [52,72],
             [57,96],
             [71,92]]
    #b_image,dice_initial_img,dice_img_list
    our_game=Game(b_image = background_image,dice_initial_img = dice_initial_image,dice_img_list = dice_img_face_list,snakes = snakes,ladders = ladders,start = 1,end = 100,num_players = 2)
    
    # our_game.play_game()
    
    # num_games=100
    # winner_list=np.zeros(num_games)
    # winner_rounds=np.zeros(num_games)
    
    # for iind in range(num_games):
    #     [num_rounds,winner]=our_game.play_game()
    #     winner_list[iind]=winner
    #     winner_rounds[iind]=num_rounds
        
    # print(winner_list)
    # print(winner_rounds)