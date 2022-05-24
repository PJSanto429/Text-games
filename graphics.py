#adds grahics to the game
import pygame

pygame.init() #this will show up as an error, but the code actually works. idk why

#colors:
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("bruh")

carryOn = True
 
clock = pygame.time.Clock()

while carryOn:
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            carryOn = False
 
     # --- Game logic should go here
     #self.image = pygame.image.load('image.png').convert_alpha() #use this type of thing to set the background image and anything in the room

    screen.fill(WHITE)
    #The you can draw different shapes and lines or add text to your background stage.
    #pygame.draw.rect(screen, RED, [55, 200, 100, 70],0)
    #pygame.draw.line(screen, GREEN, [0, 0], [100, 100], 5)
    #pygame.draw.ellipse(screen, BLACK, [20,20,250,100], 2)
 
 
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
    
    # --- Limit to 60 frames per second
    clock.tick(60)
 
#Once we have exited the main program loop we can stop the game engine:
pygame.quit()