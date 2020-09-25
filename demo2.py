import pygame
import random

pygame.init()

screen = pygame.display.set_mode((700,600))
pygame.display.set_caption('Keo Bua Bao')  

GREY = (150,150,150)
WHITE = (255,255,255)
BLACK = (0,0,0)

RESULT=0
AI = 0

font = pygame.font.SysFont('sans',50)

player = ''

text_1 = font.render('KEO', True, BLACK)
text_2 = font.render('BUA', True, BLACK)
text_3 = font.render('BAO', True, BLACK)

text_4 = font.render('WIN', True, BLACK)
text_5 = font.render('LOSE', True, BLACK)
text_6 = font.render('DRAW', True, BLACK)

text_7 = font.render('AI: ', True, BLACK)

image1 = pygame.image.load(r'C:\Users\boybe\OneDrive\Máy tính\code\python\paperrockscissor\scissor1.png') 
image1 = pygame.transform.scale(image1, ( 80 , 80 ))
image2 = pygame.image.load(r'C:\Users\boybe\OneDrive\Máy tính\code\python\paperrockscissor\rock1.png') 
image2 = pygame.transform.scale(image2, ( 80 , 80 ))
image3 = pygame.image.load(r'C:\Users\boybe\OneDrive\Máy tính\code\python\paperrockscissor\paper1.png') 
image3 = pygame.transform.scale(image3, ( 80 , 80 ))

image4 = pygame.image.load(r'C:\Users\boybe\OneDrive\Máy tính\code\python\paperrockscissor\scissor.png') 
image4 = pygame.transform.scale(image4, ( 80 , 80 ))
image5 = pygame.image.load(r'C:\Users\boybe\OneDrive\Máy tính\code\python\paperrockscissor\rock.png') 
image5 = pygame.transform.scale(image5, ( 80 , 80 ))
image6 = pygame.image.load(r'C:\Users\boybe\OneDrive\Máy tính\code\python\paperrockscissor\paper.png') 
image6 = pygame.transform.scale(image6, ( 80 , 80 ))

running = True


while running:
        screen.fill(GREY)
         
        pygame.draw.rect(screen, WHITE, (100,500,100,50))
        pygame.draw.rect(screen, WHITE, (300,500,100,50))
        pygame.draw.rect(screen, WHITE, (500,500,100,50))
        
        pygame.draw.rect(screen, WHITE, (250,50,200,50))
        
        pygame.draw.rect(screen, WHITE, (285,280,125,50))
        
        screen.blit(text_1, (105,500))
        screen.blit(text_2, (305,500))
        screen.blit(text_3, (505,500))  
                
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
               
                mouse_x, mouse_y = pygame.mouse.get_pos()
                
                if mouse_x>100 and mouse_x<200 and mouse_y>500 and mouse_y<550 :
                    AI = random.randint(1, 3)
                    player = 'KEO'
                    print('player: ', player) 
                    if AI==1:
                        print('AI: KEO')
                        print('DRAW')
                        RESULT=3 
                        
                    elif AI==2:
                        
                        print('AI: BUA')
                        print('LOSE')
                        RESULT=2
                          
                    elif AI==3:
                        print('AI: BAO')
                        print('WIN')   
                        RESULT=1
                        
                             
                if mouse_x>300 and mouse_x<400 and mouse_y>500 and mouse_y<550 :
                    AI = random.randint(1, 3)
                    player = 'BUA'
                    print('player: ', player) 
                    if AI==1:
                        print('AI: KEO')
                        print('WIN')
                        RESULT=1   
                    elif AI==2:
                        print('AI: BUA')
                        print('DRAW')
                        RESULT=3     
                    elif AI==3:
                        print('AI: BAO')
                        print('LOSE')
                        RESULT=2
                                  
                if mouse_x>500 and mouse_x<600 and mouse_y>500 and mouse_y<550 :
                    AI = random.randint(1, 3)
                    player = 'BAO'  
                    print('player: ', player) 
                    if AI==1:
                        print('AI: KEO')
                        print('LOSE')
                        RESULT=2      
                    elif AI==2:
                        print('AI: BUA')
                        print('WIN')
                        RESULT=1   
                    elif AI==3:
                        print('AI: BAO')
                        print('DRAW')  
                        RESULT=3   
        
        screen.blit(text_7, (260,45))
        if AI == 1: 
            screen.blit(text_1, (340,45))
            screen.blit(image1, (310, 125))
        elif AI == 2: 
            screen.blit(text_2, (340,45))
            screen.blit(image2, (310, 125))
        elif AI == 3: 
            screen.blit(text_3, (340,45))  
            screen.blit(image3, (310, 125))  
            
        if player == 'KEO': 
            screen.blit(image4, (310, 400))
        elif player == 'BUA': 
            screen.blit(image5, (310, 400))
        elif player == 'BAO': 
            screen.blit(image6, (310, 400))     
                       
        if RESULT==1:   
            screen.blit(text_4, (305,277))      
        elif RESULT==2:
            screen.blit(text_5, (293,277))  
        elif RESULT==3:
            screen.blit(text_6, (285,277))          
                              
        pygame.display.flip()
        
pygame.quit()        