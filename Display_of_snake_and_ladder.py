import tkinter as tk
from tkinter import *
from PIL import ImageTk,Image
import random

def player_buttons():
    
    #Botton create

    global dice_img
    
    global b1,b2
    
    # Player 1

    b1.place(x=1000,y=300)

    # Player 2

    b2.place(x=1000,y=500)

    # Dice 

    dice = Image.open('D:\Hope\Phase 2 python projects\Snake and Ladder Game\dice.png')

    re_dice = dice.resize((100,100))

    dice_img = ImageTk.PhotoImage(re_dice)

    d_button = tk.Button(root,image=dice_img,height=100,width=100)

    d_button.place(x = 1100, y = 700)

    # Exit button 

    b3 = tk.Button(root,activebackground='red',bg='black',height=3,width=20,fg='white',text='End the game',font=('Cursive',14,'bold'),command=root.destroy)

    b3.place(x=1000,y=100)
    
def reset_coins():
    
    global player_1,player_2,pos1,pos2
    
    player_1.place(x=0,y=700)
    
    player_2.place(x=0,y=750)
    
    pos1 = 0 
    pos2 = 0
    
def dice_create():
    
    global dice_list 
    
    names = ['Ff1.png','Ff2.png','Ff3.png','Ff4.png','Ff5.png','Ff6.png']
    
    for di in names:
        
        dice = Image.open("D:\Hope\Phase 2 python projects\Snake and Ladder Game"+"\\"+di)

        re_dice = dice.resize((100,100))

        dice_img = ImageTk.PhotoImage(re_dice)
        
        dice_list.append(dice_img)
        
def roll_dice():
    
    global dice_list
    global turn
    global pos1,pos2
    global snake,ladder
    
    die_value = random.randint(1,6)
    
    d_button = tk.Button(root,image=dice_list[die_value-1],height=100,width=100)

    d_button.place(x = 1100, y = 700)
    
    if (turn == 1):
        if ((pos1+die_value) <= 100):
            
            if((snake.get(pos1+die_value) != None)):
                
                pos1 = snake[pos1+die_value] 
            
            elif((ladder.get(pos1+die_value) != None)):
                
                pos1 = ladder[pos1+die_value] 
            
            else:
                pos1 += die_value
                
        move_coins(turn,pos1)
        turn = 2
        b1.configure(state='disabled')
        b2.configure(state='normal')
    
    else: 
        
        if ((pos2+die_value) <= 100): 
            
            if((snake.get(pos2+die_value) != None)):
                
                pos2 = snake[pos2+die_value] 
            
            elif((ladder.get(pos2+die_value) != None)):
                
                pos2 = ladder[pos2+die_value] 
            else:
                pos2 += die_value  
            
        move_coins(turn,pos2)
        turn = 1 
        b2.configure(state='disabled')
        b1.configure(state='normal')
        
    is_winner()

def is_winner():
    
    global pos1,pos2,b1,b2
    print(pos1)
    print(pos2)
    if (pos1 == 100):
        
        msg = "Player 1 is the Winner"
        
        d_box = tk.Label(root,text=msg,bg='red',height=2,width=20,font=('Cursive',20,'bold'))
        
        d_box.place(x=200,y=100)
        
        reset_coins()
        b1.configure(state='disabled')
        b2.configure(state='disabled')
    
    elif(pos2 == 100):
        
        msg = "Player 2 is the Winner"
        
        d_box = tk.Label(root,text=msg,bg='red',height=2,width=20,font=('Cursive',20,'bold'))
        
        d_box.place(x=200,y=100)
        
        reset_coins()
        b1.configure(state='disabled')
        b2.configure(state='disabled')
    
def move_coins(turn,die_value):
    
    global player_1,player_2,index
    
    x_co = index[die_value][0]
    y_co = index[die_value][1]
    
    if(turn == 1):
        player_1.place(x=x_co,y=y_co)
    
    else:
        player_2.place(x=x_co,y=y_co)

def get_index():
    
    global index
    
    board_arrangement = [100,99,98,97,96,95,94,93,92,91,81,82,83,84,85,86,87,88,89,90,80,79,78,77,76,75,74,73,72,71,61,62,63,64,65,66,67,68,69,70,60,59,58,57,56,55,54,53,52,51,41,42,43,44,45,46,47,48,49,50,40,39,38,37,36,35,34,33,32,31,21,22,23,24,25,26,27,28,29,30,20,19,18,17,16,15,14,13,12,11,1,2,3,4,5,6,7,8,9,10]

    vertical_shift = 70
    horizontal_shift = 70
    
    i = 0
    y = 4
    x = 8
     
    for f_row in range(1,11):
        
        x = 8
        
        for f_col in range(1,11):
                 
            index[board_arrangement[i]] = (x,y)
            
            x += horizontal_shift
            
            i += 1
        
        y += vertical_shift  
           
    
root = tk.Tk()

root.geometry("1200x800")

root.title("Snake and ladder game")

F1 = tk.Frame(root,width=1200,height=800,relief='raised')

F1.place(x=0,y=0)

#set image

img1 = Image.open('D:\Hope\Phase 2 python projects\Snake and Ladder Game\snake_ladder.png')

resized_img = img1.resize((700,700),Image.ANTIALIAS)

img1a = ImageTk.PhotoImage(resized_img)

#img1a = ImageTk.PhotoImage(img1)

Lab = tk.Label(F1,image=img1a)

Lab.place(x=0,y=0)


# create player 1 coin

player_1 = tk.Canvas(root,width=40,height=40)

player_1.create_oval(10,10,40,40,fill='orange')



# create player 2 coin

player_2 = tk.Canvas(root,width=40,height=40)

player_2.create_oval(10,10,40,40,fill='pink')

# player 1 button 

b1 = tk.Button(root,activebackground='yellow',bg='orange',height=3,width=20,fg='black',text='Dharshini',font=('Cursive',14,'bold'),command=roll_dice)

# player 2 button 

b2 = tk.Button(root,activebackground='yellow',bg='pink',height=3,width=20,fg='black',text='Bharkavi',font=('Cursive',14,'bold'),command=roll_dice)


# initial position 
pos1 = None
pos2 = None

# snake dict

snake = {43:17,50:5,56:8,73:15,84:58,87:49,98:40}

# ladder dict 

ladder = {2:23,6:45,20:59,52:72,57:96,71:92}

# reset coins
reset_coins()

# Getting x and y co-ordinates of a coin

index = {}
get_index()
print(index)
# upload dice

dice_list = []
dice_create()

# set all buttons
player_buttons()

#whose turn is first default player 1

turn = 1 

root.mainloop()