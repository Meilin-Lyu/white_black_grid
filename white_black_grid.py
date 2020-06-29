
# Import a library of functions called 'pygame'
import pygame
import random


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
smileImg = pygame.image.load('win_face.jpg')
smileImg = pygame.transform.scale(smileImg,(300,300))

WINDOW_SIZE = [920,450]
 
screen = pygame.display.set_mode(WINDOW_SIZE)


   



   


def auto():
    grid2 =[]
    for row in range(10):
        grid2.append([])
        for column in range(10):
            grid2[row].append(False)
    time = 2
    for i in range(0,time):
        column2 = random.randint(0,9)
        row2 = random.randint(0,9)
        grid2 = reColor(grid2,column2,row2)
               
    return grid2
    
    
def reColor(grid,column,row):
    grid[row][column]= not grid[row][column]
    if row>0:
        grid[row-1][column]= not grid[row-1][column] 
    if row<9:
        grid[row+1][column]=not grid[row+1][column]
    if column>0:
        grid[row][column-1]= not grid[row][column-1]
    if column<9:
        grid[row][column+1]= not grid[row][column+1]
    return grid
                

        

# game board for white back grid

def board(): 

   
   
    
    # setting grid
    grid = []
    
    

    for row in range(10):
        grid.append([])
        for column in range(10):
            grid[row].append(False)
    
     
    
    loop = True
    touch = False
    reset = False
    screen.fill(BLACK)
    pygame.draw.rect(screen, RED,(440,300,50,40))
    grid2 = auto()
    for row2 in range(10):
                    for column2 in range(10):

                        color = WHITE if not grid2[row2][column2] else BLACK
                        pygame.draw.rect(screen,color,[(MARGIN+WIDTH)*column2+MARGIN+510,
                        (MARGIN+HEIGHT)*row2+MARGIN,WIDTH,HEIGHT])
                        pygame.draw.rect(screen,(255,255,255),[(MARGIN+WIDTH)*column2+MARGIN,
                        (MARGIN+HEIGHT)*row2+MARGIN,WIDTH,HEIGHT])
                       
    while(loop):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type ==pygame.MOUSEBUTTONDOWN:

                

            
                pos = pygame.mouse.get_pos()
                
                


                print(pos)
                if((pos[0]<=394) and (pos[1]<=401)):
                

                    
                    column = pos[0]//(WIDTH+MARGIN)
                    row = pos[1]//(HEIGHT+MARGIN)
               
                    grid = reColor(grid,column,row)
              
                if(grid==grid2):
                    screen.fill(BLACK)
                    screen.blit(smileImg,(500,0))
                
                


                
                for row in range(10):
                    for column in range(10):
                        color = WHITE if not grid[row][column] else BLACK
                        pygame.draw.rect(screen,color,[(MARGIN+WIDTH)*column+MARGIN,
                        (MARGIN+HEIGHT)*row+MARGIN,WIDTH,HEIGHT])
                
                        if(((pos[0]<=488)and(pos[0]>=440)) and ((pos[1]>=299)and(pos[1]<=338))):
                            grid[row][column]= False
                            pygame.draw.rect(screen,(255,255,255),[(MARGIN+WIDTH)*column+MARGIN,
                            (MARGIN+HEIGHT)*row+MARGIN,WIDTH,HEIGHT])
                            
              

        pygame.display.flip()


board()


 

