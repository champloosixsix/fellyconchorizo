from tkinter import scrolledtext
import pygame, random, shelve, sys

#init pygame
pygame.init()

#create surface
WINDOW_WIDTH = 700
WINDOW_HEIGHT = 500
surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Felly Con Chorizo!")
icon = pygame.image.load('assets/icon.png') 
pygame.display.set_icon(icon)

#load in music
pygame.mixer.music.load('assets/music.wav')
sound_eat = pygame.mixer.Sound('assets/eat.wav')
sound_eat.set_volume(.5)

def setGame():
    global FPS, VELOCITY, tacosAte, RED, GREEN, YELLOW, WHITE, BLACK
    global timer, dt
    global dragon_left, dragon_left_rect, dragon_right, dragon_right_rect, felly_face, felly_face_rect, taco, taco_rect, spacebar, spacebar_rect
    global d, highScore

    #set fps and clock
    FPS = 60

    #set game values
    VELOCITY = 5
    tacosAte = 0

    #define colors
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    YELLOW = (255, 255, 0)
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)

    #make timer
    timer = 30
    dt = 0

    #load images
    dragon_left = pygame.image.load("assets/dragon_left.png")
    dragon_left_rect = dragon_left.get_rect()
    dragon_left_rect.topright = (WINDOW_WIDTH, 0)

    dragon_right = pygame.image.load("assets/dragon_right.png")
    dragon_right_rect = dragon_right.get_rect()
    dragon_right_rect.topleft = (0, 0)

    felly_face = pygame.image.load("assets/fellyface.png")
    felly_face_rect = felly_face.get_rect()
    felly_face_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2)

    taco = pygame.image.load("assets/tacos.png")
    taco_rect = taco.get_rect()
    taco_rect.center = (WINDOW_WIDTH//2+150, WINDOW_HEIGHT//2)

    spacebar = pygame.image.load("assets/spacebar.png")
    spacebar_rect = spacebar.get_rect()
    spacebar_rect.center = (350, 265)

    #read high score
    import shelve
    d = shelve.open('highScore.txt')
    highScore = d['highScore']  # the score is read from disk
    d.close()

def startingScreen():
    #load starting screen text
    surface.blit(dragon_left, dragon_left_rect)
    surface.blit(dragon_right, dragon_right_rect)
    pygame.draw.line(surface, GREEN, (0,70), (WINDOW_WIDTH,70), 5)
    pygame.draw.line(surface, YELLOW, (0,73), (WINDOW_WIDTH,73), 3)
    pygame.draw.line(surface, WHITE, (0,75), (WINDOW_WIDTH,75), 2)
    name_font = pygame.font.Font("assets/AttackGraffiti.ttf", 50)
    name_text = name_font.render("Felly Con Chorizo!", True, RED)
    name_text_rect = name_text.get_rect()
    name_text_rect.center = (WINDOW_WIDTH//2, 35)
    toplay1_text = name_font.render("Press", True, RED)
    toplay1_text_rect = toplay1_text.get_rect()
    toplay1_text_rect.center = (WINDOW_WIDTH//2-10, 190)
    toplay2_text = name_font.render("To Play!", True, RED)
    toplay2_text_rect = toplay2_text.get_rect()
    toplay2_text_rect.center = (WINDOW_WIDTH//2, 340)
    surface.blit(toplay1_text, toplay1_text_rect)
    surface.blit(toplay2_text, toplay2_text_rect)
    surface.blit(name_text, name_text_rect)
    surface.blit(spacebar, spacebar_rect)
    custom_font = pygame.font.Font("assets/AttackGraffiti.ttf", 32)
    high_score = custom_font.render("High Score: " + str(highScore), True, GREEN)
    high_score_rect = high_score.get_rect()
    high_score_rect.center = (WINDOW_WIDTH//2,425)
    surface.blit(high_score, high_score_rect)
    pygame.display.update()

    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    done = True
        
def gameOver():
    #load game over text
    pygame.mixer.music.stop()
    custom_font2 = pygame.font.Font("assets/AttackGraffiti.ttf", 50)
    game_over = custom_font2.render("Game Over!", True, RED)
    game_over_rect = game_over.get_rect()
    game_over_rect.center = (WINDOW_WIDTH//2,WINDOW_HEIGHT//2)

    custom_font3 = pygame.font.SysFont('Consolas', 25)
    game_over2 = custom_font3.render("Your score: " + str(tacosAte), True, RED)
    game_over2_rect = game_over2.get_rect()
    game_over2_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2 + 50)

    #write high score
    d = shelve.open('highScore.txt')
    x = d['highScore']
    if tacosAte > x:
        d['highScore'] = tacosAte
        x = tacosAte          
        d.close()
    else:

        pass

    #blit game over text
    surface.blit(game_over, game_over_rect)
    surface.blit(game_over2, game_over2_rect)
    surface.blit(dragon_left, dragon_left_rect)
    surface.blit(dragon_right, dragon_right_rect)
    surface.blit(score, score_rect)
    surface.blit(time_font2, time_font2_rect)
    high_score = custom_font.render("High Score: " + str(x), True, GREEN)
    high_score_rect = high_score.get_rect()
    high_score_rect.center = (WINDOW_WIDTH//2,400)
    surface.blit(high_score, high_score_rect)
    spacebar2 = pygame.image.load("assets/spacebar.png")
    spacebar_rect2 = spacebar2.get_rect()
    spacebar_rect2.center = (300, 150)
    custom_font3 = pygame.font.Font("assets/AttackGraffiti.ttf", 25)
    toplay3_text = custom_font3.render("Press", True, GREEN)
    toplay3_text_rect = toplay3_text.get_rect()
    toplay3_text_rect.center = (200, 150)
    toplay4_text = custom_font3.render("To Play Again!", True, GREEN)
    toplay4_text_rect = toplay4_text.get_rect()
    toplay4_text_rect.center = (460, 150)
    surface.blit(toplay3_text, toplay3_text_rect)
    surface.blit(toplay4_text, toplay4_text_rect)
    surface.blit(spacebar2, spacebar_rect2)
    pygame.display.flip()   
    done = False
    while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        done == True
                        surface.fill(BLACK) 
                        setGame()
                        main() 

def main():
    #main game loop
    global score 
    global timer
    global dt
    global score_rect
    global time_font
    global time_font2
    global time_font2_rect
    global tacosAte
    global custom_font
    setGame()
    startingScreen()
    pygame.mixer.music.play(-1, 0.0)
    running = True
    while running:
        clock = pygame.time.Clock()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            
        timer -= dt
        if timer <= 0:
            break
        
        time_font = pygame.font.Font("assets/AttackGraffiti.ttf", 40)
        time_font2 = time_font.render(str(round(timer, 2)), True, RED)
        time_font2_rect = time_font2.get_rect()
        time_font2_rect.topleft = (500,13)
        dt = clock.tick(FPS) / 1000

        #list all keys being pressed
        keys = pygame.key.get_pressed()

        #move felly contiuously
        if keys[pygame.K_LEFT] and felly_face_rect.left > 0 or keys[pygame.K_a] and felly_face_rect.left > 0:
            felly_face_rect.x -= VELOCITY
        if keys[pygame.K_RIGHT] and felly_face_rect.right > 0 or keys[pygame.K_d] and felly_face_rect.right < WINDOW_WIDTH:
            felly_face_rect.x += VELOCITY
        if keys[pygame.K_UP] and felly_face_rect.top > 0 or keys[pygame.K_w] and felly_face_rect.top > 0:
            felly_face_rect.y -= VELOCITY
        if keys[pygame.K_DOWN] and felly_face_rect.bottom > 0 or keys[pygame.K_s] and felly_face_rect.bottom < WINDOW_HEIGHT:
            felly_face_rect.y += VELOCITY

        #check for collision 
        if felly_face_rect.colliderect(taco_rect):
            taco_rect.x = random.randint(0, WINDOW_WIDTH-75)
            taco_rect.y = random.randint(76, WINDOW_HEIGHT-75)
            tacosAte += 1
            sound_eat.play()
            
        #load text
        custom_font = pygame.font.Font("assets/AttackGraffiti.ttf", 32)
        score = custom_font.render("Tacos Eaten: " + str(tacosAte), True, GREEN)
        score_rect = score.get_rect()
        score_rect.topleft = (80,20)
            

        #blit images to surface
        surface.blit(dragon_left, dragon_left_rect)
        surface.blit(dragon_right, dragon_right_rect)
        surface.blit(felly_face, felly_face_rect)
        surface.blit(taco, taco_rect)

        #blit text to surface
        surface.blit(score, score_rect)
        surface.blit(time_font2, time_font2_rect)
        
        #update display
        pygame.display.update()
        surface.fill(BLACK)


        #line(surface, color, starting point, ending point, thickness)
        pygame.draw.line(surface, GREEN, (0,70), (WINDOW_WIDTH,70), 5)
        pygame.draw.line(surface, YELLOW, (0,73), (WINDOW_WIDTH,73), 3)
        pygame.draw.line(surface, WHITE, (0,75), (WINDOW_WIDTH,75), 2)
    
    gameOver()

main()





