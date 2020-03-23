import pygame
import random

pygame.init()

width = 600
height = 600

screen = pygame.display.set_mode((height,width))

pygame.display.set_caption('Snake')

red = (255,0,0)
white = (255,255,255)
green = (0,155,0)

clock = pygame.time.Clock()

font = pygame.font.SysFont(None , 25 )

def snake(block_size, snakeList):
   for XnY in snakeList:
      pygame.draw.rect(screen, green, (XnY[0], XnY[1], block_size, block_size))
   

def message(msg,color):
   screen_text = font.render(msg, True, color)
   screen.blit(screen_text, (200,200))

def gameloop():
   x_change = width/2
   y_change = height/2

   block_size = 10
   AppleSize = 10

   lead_x_change = 0
   lead_y_change = 0

   snakeList = []
   snakeLength = 1
   
   GameExit = False
   GameOver = False

   randAppleX = random.randrange(0, width - 30, 10)
   randAppleY = random.randrange(0, height - 30, 10)
        
   while not GameExit:

      while GameOver == True:
         screen.fill(white)
         message('GAME OVER , Press P to play again or Q to quit',red)
         pygame.display.update()

         for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
               if event.key == pygame.K_q:
                  GameExit = True
                  GameOver = False 
               if event.key == pygame.K_p:
                  gameloop()

      for event in pygame.event.get():
         if event.type == pygame.QUIT:
            GameExit = True
            
         if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
               lead_x_change = -10
               lead_y_change = 0
            elif event.key == pygame.K_RIGHT:
               lead_x_change = 10
               lead_y_change = 0
            elif event.key == pygame.K_UP:
               lead_y_change = -10
               lead_x_change = 0
            elif event.key == pygame.K_DOWN:
               lead_y_change = 10
               lead_x_change = 0
      
                           
      if x_change >= 600 or x_change < 0 or y_change >= 600 or y_change < 0:
         GameOver = True
               
      x_change += lead_x_change 
      y_change += lead_y_change
             
      screen.fill(white)
      
      
      snakehead = []
      snakehead.append(x_change)
      snakehead.append(y_change)
      snakeList.append(snakehead)

      if len(snakeList) > snakeLength:
         del snakeList[0]
         
      for eachElement in snakeList[:-1]:
         if eachElement == snakehead:
            GameOver = True 

      snake(block_size, snakeList)

      
      pygame.draw.rect(screen, red, [randAppleX, randAppleY, AppleSize, AppleSize])
      clock.tick(30)
      pygame.display.update()

      if x_change == randAppleX and y_change == randAppleY:
         randAppleX = random.randrange(0, width - 30, 10)
         randAppleY = random.randrange(0, height - 30, 10)
         snakeLength += 1 
         
         
   pygame.display.update()
   pygame.quit()
   quit()


gameloop()