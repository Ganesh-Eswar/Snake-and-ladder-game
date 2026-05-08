import random

class BoardGrid(object):
    
    def __init__(self,start,end) -> None:
        
        self.start = start
        self.end = end
        #self.total_cells = abs(self.end-self.start)
        self.total_cells = (abs(self.end)+abs(self.start))+1
        
    def board_cell(self):
        
        cell_list = []
        
        for i in range (self.start,self.end+1):
            
            cell_list.append(i)
            
        return cell_list
    
    def board_size(self,board_cell):
        
        cell_list = board_cell
        
        factors = []
        
        for number in range (self.start,self.end+1):
            
            if(number != 0 and self.end % number ==0):
                
                factors.append(number)
                
        if(len(factors) % 2 != 0):
                
            index_m = int(len(factors)/2)
                
            m = factors[index_m]
                
            n = m
            
        if(len(factors) % 2 ==0 ):
            
            index_m = int(len(factors)/2)
            
            m = factors[index_m]
            
            n = factors[index_m - 1]
            
        return [m,n]
    
     
    def board_grid(self,board_size):
        
        size = board_size
        
        grid_format = []
        
        inner_list = []
        
        for i in range(self.start,self.end):
            
            inner_list.append(i)
            
            if(len(inner_list) == size[0]):
                
                grid_format.append(inner_list)
                
                inner_list = []
                
        return grid_format 
    
    def number_of_snakes (self):
        
        no_of_snakes = int((self.total_cells) * 0.1) 
        
        return no_of_snakes
    
    def number_of_ladders (self):
        
        no_of_ladders =  int((self.total_cells) * 0.1)
    
        return no_of_ladders


class Snake(BoardGrid):
    
    def __init__(self, start, end) -> None:
        
        super().__init__(start, end)

        self.board_cell_list = self.board_cell()
        self.board_size_list = self.board_size(self.board_cell_list)
        self.board_grid_list = self.board_grid(self.board_size_list)
        
        self.start = self.board_grid_list[0][0]
        
    def snake_head(self):
        
        snake_head_list = []
        
        for list in self.board_grid_list:
            
            i = random.randint(list[0],list[-1])
            
            snake_head_list.append(i)
            
        return snake_head_list
    
    def snake_head_tail(self):
        
        snake_head_tail_list = []
        
        snake_head = self.snake_head()
        
        for ele in snake_head:
            
            i = random.randint(self.start,ele)
            
            snake_head_tail_list.append([ele,i])
            
        return snake_head_tail_list
    
    def new_grid(self):
        
        s_head_tail = self.snake_head_tail()
        
        board_grid = self.board_grid_list
        
        new_board_grid = []
        
        for sH in s_head_tail:
            
            for ele in board_grid:
                
                if(sH[0] in ele):
                    
                    ele.remove(sH[0])
                    #ele.remove(sH[1])
                    
                    new_board_grid.append(ele)
                    
                    break
        
        return s_head_tail,new_board_grid
    
class Ladder(Snake):
    
    def __init__(self, start, end) -> None:
    
        super().__init__(start, end)
        
        self.b_grid_tuple = self.new_grid()
        
        self.snakes_list = self.b_grid_tuple[0]
        
        self.b_grid = self.b_grid_tuple[1]
        
    def ladder_base(self):
        
        ladder_base_list = []
        
        for list in self.b_grid:
            
            i = random.randint(list[0],list[-1])
            
            ladder_base_list.append(i)
            
        return ladder_base_list
    
    def ladder_base_top(self):
        
        ladder_base_top_list = []
        
        ladder_base = self.ladder_base()
        
        for ele in ladder_base:
            
            i = random.randint(ele,self.end)
            
            ladder_base_top_list.append([ele,i])
            
        return ladder_base_top_list,self.snakes_list
    
class Board(Ladder):
    
    def __init__(self, start, end) -> None:
        super().__init__(start, end)
        
        self.start = start
        
        self.end = end 
        
        self.b_cell = self.board_cell()
        
        self.b_size = self.board_size(self.b_cell)
        
        self.b_grid_list = self.board_grid(self.b_size)

        self.ladders_and_snakes = self.ladder_base_top()
     
        self.ladders = self.ladders_and_snakes[0]
        
        self.snakes = self.ladders_and_snakes[1]
    
    def start_value(self):
        
        return self.start
    
    def end_value(self):
        
        return self.end
    
    def b_cell_value(self):
        
        return self.b_cell
    
    def b_size_value(self):
        
        return self.b_size
    
    def b_grid_value(self):
        
        return self.b_grid_list
    
    def game_snakes(self):
        
        return self.snakes
    
    def game_ladders(self):
        
        return self.ladders
    

class Die():
    
    def __init__(self) -> None:
        
        self.die_start_value = 1
        
        self.die_end_value = 6 
        
    def rolling_die(self):
        
        die_value = random.randint(1,6)
        
        return die_value
    
    
class Game(Board,Die):
    
    def __init__(self, start, end) -> None:
        super().__init__(start, end)
        
        self.start = start
        
        self.end = end 
        
        self.snakes = self.game_snakes()
        
        self.ladders = self.game_ladders()
        
    def game(self):
        
        start_value = self.start 
        
        end_value = self.end 
        
        player_current_position = start_value
         
        snake_head_list = []
        ladder_base_list = []
        
        for list in self.snakes:
            
            snake_head_list.append(list[0])
            
        for li in self.ladders:
            
            ladder_base_list.append(li[0])    
            
        count = 0 
        print('Number of times the die is rolled : ', str(count))
        total_die_rolling_score = 0 
        print('Total die value : ', str(total_die_rolling_score))
        
        while (player_current_position != end_value):
            
            die = Die()
            
            die_throw =  self.rolling_die()
            print('-----------------------> The die is thrown, the value you get is', str(die_throw))
                
            count += 1
            print('Number of times the die is rolled : ', str(count))
            
            total_die_rolling_score += die_throw 
            print('Total die value : ', str(total_die_rolling_score))
           
            player_current_position += die_throw
            
            print('-------------------------> The actual player current position is ', player_current_position)
            
            if(player_current_position > end_value):
                
                print('---------------------------> The sum of your current position and die value is grater than destination')
                  
                player_current_position -= die_throw
                
                print('-----------------------------> Sorry! you still hold on this same place', player_current_position) 
                 
            if( player_current_position in snake_head_list ):
                
                for list in self.snakes:
                    
                    if(player_current_position in list):
                        
                        print('----------------------------> But unfornuately now your position is snake head!')
                        print('----------------------------> So it\'s bite you, See you in new position')
                        player_current_position = list[1]
                        print('----------------------------> After the snack bite your new position is :', player_current_position)
                        
            if(player_current_position in ladder_base_list):
                
                for list in self.ladders:
                    
                    if(player_current_position in list):
                        
                        print('-----------------------> Wow! You\'re so lucky! you get the ladder from this position')
                        print('-----------------------> The ladder will help to up you! See you in new position')
                        player_current_position = list[1]
                        print('-----------------------> Your new position after ladder up is :', player_current_position)
                        
            print("Final current position is", player_current_position)
            
            print("******************************************************************")           
        
        if(player_current_position == end_value):
            
            print('*******************************************************')
            print("Wow! your total move is ", str(count))
            print("*******************************************************")
            print('Your total die value is ', str(total_die_rolling_score))
            print('********************************************************')
            print('Congrats! Game is end! You win')

   
        
if __name__ == '__main__':
            
    # start = 1
    # end = 100   
    # P1 = BoardGrid(start,end)

    # board_cells = P1.board_cell()
    # print(board_cells)
    # b_size = P1.board_size(board_cells)
    # print(b_size)
    # print(P1.board_grid(b_size))
    # print(P1.number_of_snakes())
    # print(P1.number_of_ladders())            
    
    # P2 = Snake(start,end)

    # #print(P2.snake_head())      
    # #print(P2.snake_head_tail())
    # print(P2.new_grid())    
                    
    # P3 = Ladder(start,end)
    # print('******************************************************')
    # print(P3.ladder_base_top())        
            
    # p4 = Board(1,100)       

    # print(p4.b_grid_value())
    # # print(p4.ladder_base_top())
    # print(p4.game_snakes())
    # print(p4.game_ladders())

    # p5 = Die()

    # print(p5.rolling_die())

    print("The game is start ")
    first_game = Game(1,100)

    first_game.game()
