
 
# Import a library of functions called 'pygame'
import pygame


def board(): 
# Define some colors
    pygame.init()
    pygame.font.init()
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    BLUE = (0, 0, 255)
    GREEN = (0, 255, 0)
    RED = (255, 0, 0)

    WIDTH = 40
    HEIGHT = 40
    MARGIN = 1
  
    grid = []
    for row in range(10):
        grid.append([])
        for column in range(10):
            grid[row].append(0)

    
    WINDOW_SIZE = [530,450]
    
   
    screen = pygame.display.set_mode(WINDOW_SIZE)
    screen.fill(BLACK)
    loop = True
    while(loop):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type ==pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                column = pos[0]//(WIDTH+MARGIN)
                row = pos[1]//(HEIGHT+MARGIN)
                grid[row][column]= not grid[row][column]
                if row>0:
                    grid[row-1][column]= not grid[row-1][column] 
                if row<9:
                    grid[row+1][column]=not grid[row+1][column]
                if column>0:
                    grid[row][column-1]= not grid[row][column-1]
                if column<9:
                    grid[row][column+1]= not grid[row][column+1]

                



        
        for row in range(10):
            for column in range(10):
                color = WHITE if not grid[row][column] else BLACK
                pygame.draw.rect(screen,color,[(MARGIN+WIDTH)*column+MARGIN,
                (MARGIN+HEIGHT)*row+MARGIN,WIDTH,HEIGHT])
               

                    
                    
                


        
        


       
        
        
            

        pygame.display.flip()


board()


 

