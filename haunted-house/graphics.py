#adds grahics to the game #DOESNT WORK YET...
import pygame

pygame.init() #this will show up as an error, but the code actually works. idk why

#colors:
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
GREY = (71, 80, 82)

size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("bruh")

carryOn = True
 
clock = pygame.time.Clock()

pygame.font.init()
my_font = pygame.font.SysFont('Comic Sans MS', 30)

textBackground = ('')

test_font = pygame.font.Font('freesansbold.ttf', 32)
score_surf = test_font.render('Joe mama?!?!?!?', False, (64,64,64))
score_rect = score_surf.get_rect(center = (400, 50))

#text/font
font = pygame.font.Font('freesansbold.ttf', 32)
text = font.render('Wow so cool', False, (0, 0, 0))
#textRect = text.get_rect()

while carryOn:
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            carryOn = False
 
    # --- Game logic should go here
    
    pygame.display.set_caption('Text Game')
    #textRect.center = (100, 50)

    #use this type of thing to set the background image and anything in the room
    kitchen1 = pygame.image.load('assets/kitchen1.png').convert_alpha()
    kitchen1 = pygame.transform.scale(kitchen1, (size))

    largeGoldKey = pygame.image.load('assets/large gold key.png').convert_alpha()
    largeGoldKey = pygame.transform.scale(largeGoldKey, (100, 50))

    screen.fill(WHITE)
    screen.blit(kitchen1, (0, 0))
    screen.blit(largeGoldKey, (50,50))

    #text
    screen.blit(score_surf, score_rect)
    #screen.blit(text, (0, 0))

    #The you can draw different shapes and lines or add text to your background stage.
    pygame.draw.rect(screen, GREY, [55, 200, 100, 70], 0)
 
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
    
    # --- Limit to 60 frames per second
    clock.tick(60)
 
#Once we have exited the main program loop we can stop the game engine:
pygame.quit()