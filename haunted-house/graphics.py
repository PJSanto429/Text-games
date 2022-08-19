import sys
import pygame
from textInput import text_input
from typeEffect import *

pygame.init()
pygame.font.init()

#my_font = pygame.font.SysFont('Comic Sans MS', 30)
#textBackground = ('')
#test_font = pygame.font.Font('freesansbold.ttf', 32)
#score_surf = test_font.render('Joe mama?!?!?!?', False, (64,64,64))
#score_rect = score_surf.get_rect(center = (400, 50))

#text/font
#font = pygame.font.Font('freesansbold.ttf', 32)
#text = font.render('Wow so cool', False, (0, 0, 0))
#textRect = text.get_rect()

def graphicsInit():
    #colors:
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    GREY = (71, 80, 82)

    size = (600, 600)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("bruh")
    
    clock = pygame.time.Clock()

    userText = ''
    baseFont = pygame.font.Font(None, 32)
    input_rect = pygame.Rect(15, 550, 1, 32)
    color_active = pygame.Color('lightskyblue3')
    color_passive = pygame.Color('chartreuse4')
    color = color_passive

    if len(allText) == 0:
        text = baseFont.render('', True, BLACK, RED)
    else:
        text = baseFont.render(allText[-1], True, BLACK, RED)
    textRect = text.get_rect(center = (300, 300))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    userText = userText[:-1]
                elif event.key == pygame.K_RETURN:
                    if userText.lower() in ['quit', 'quit()', 'exit', 'exit()']:
                        pygame.quit()
                        sys.exit()
                    else:
                        text_input(userText, 'first', 'dev', True)
                        userText = ''
                else:
                    userText += event.unicode
        
        screen.fill(WHITE)
        pygame.display.set_caption('Text Game')
        
        if len(allText) == 0:
            text = baseFont.render('', True, BLACK, WHITE)
        else:
            text = baseFont.render(' '.join(allText[-1]), True, BLACK, WHITE)
        textRect = text.get_rect(center = (300, 300))
        
        screen.blit(text, textRect)
        
        pygame.draw.rect(screen, color, input_rect)
        text_surface = baseFont.render(userText, True, WHITE)
        screen.blit(text_surface, (input_rect.x + 5, input_rect.y + 5))
        input_rect.w = max(100, text_surface.get_width() + 10)
    
        pygame.display.flip()
        if inputText:
            setInputText(' '.join(allText[-1]))
        clock.tick(60)