import pygame 
import random
import os

pygame.mixer.init()


pygame.init()

width = 700
height = 500

screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("Snake")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 55)

def text_screen(text,color,x,y):
    screen_text = font.render(text,True,color)
    screen.blit(screen_text,[x,y])

def plot_snake(screen,color,snk_list,size):
    for x,y in snk_list:
        pygame.draw.rect(screen,color,[x,y,size,size])

def window():
    fps = 30
    game = True
    while game:
        screen.fill('yellow')
        text_screen("Welcome to Snakes", 'blue', 180, 190)
        text_screen("Press Space Bar to Play", 'blue', 140, 240)
        back = pygame.image.load("Snake.png")
        scale_bg = pygame.transform.scale(back,(200,100)).convert_alpha()
        screen.blit(scale_bg,(250,280))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False
                pygame.quit()
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pygame.mixer.music.load('bak.mp3')
                    pygame.mixer.music.play()
                    gameloop()
        
        pygame.display.update()
        clock.tick(fps)
        
def gameloop():
    snk_list = []
    snk_length = 1
    game = True
    over = False
    snake_x = 90
    snake_y = 90
    food_x = random.randint(0,680)
    food_y =random.randint(0,480)
    size = 20
    score = 0
    fps = 30
    if (not os.path.exists("highscore.txt")):
        with open("highscore.txt",'w') as f:
            f.write("0")
    with open("highscore.txt",'r') as f:
        higscore = f.read()
    
    vel_x = 10
    vel_y = 0

    while game:
        if over:
            with open("highscore.txt",'w') as f:
                f.write(str(higscore))
            screen.fill('white')
            text_screen("Game over! Press enter to continue",'red',20,195)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game = False
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    window()
        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game = False
                    
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        vel_x = 10
                        vel_y = 0
        
                    if event.key == pygame.K_LEFT:
                        vel_x = -10
                        vel_y = 0
        
                    if event.key == pygame.K_DOWN:
                        vel_x = 0
                        vel_y = 10
        
                    if event.key == pygame.K_UP:
                        vel_x = 0
                        vel_y = -10
            
            snake_x += vel_x
            snake_y += vel_y
            
            if abs(snake_x-food_x)<6 and abs(snake_y-food_y)<10:
                score += 10
                food_x = random.randint(50,680)
                food_y =random.randint(150,480)
                if food_y<80 or food_y>450:
                    food_y =random.randint(150,480)
                snk_length += 4
                if score>int(higscore):
                    higscore = score
            
            screen.fill('green')
            pygame.draw.rect(screen,'blue',[0,0,700,60])
            text_screen("Score : " + str(score), 'red', 10, 10)
            text_screen("Highscore : " + str(higscore), 'red', 420, 10)
            pygame.draw.rect(screen,'red',[food_x,food_y,size,size])
            
            head = []
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)
            
            if len(snk_list)>snk_length:
                del snk_list[0]
                
            if head in snk_list[:-1]:
                over = True
                pygame.mixer.music.load('explosion.mp3')
                pygame.mixer.music.play()
                
            if snake_x<0 or snake_x>width or snake_y<60 or snake_y>height:
                over = True
                pygame.mixer.music.load('explosion.mp3')
                pygame.mixer.music.play()
            
            plot_snake(screen,'black',snk_list,size)
            
        pygame.display.update()
        clock.tick(fps)
    
    pygame.quit()

window()