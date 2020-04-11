'''*************************************************************************
NAME: Snakes game
DISCRIPTION: A Medium python project that create a basic Snake game.
CREATED BY: Thejus S
DATE OF CREATION: 11 Apr 2020
MODIFIED: -
*************************************************************************'''
import random
import os
import pygame
pygame.init()
pygame.mixer.init()

screen_width = 900
screen_height = 600
wn = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("The Snakes") # Game title
pygame.display.update() # Update game title

# Background
welimg = pygame.image.load("dist/welcome.jpg")
welimg = pygame.transform.scale(welimg,(screen_width,screen_height)).convert_alpha()
overimg = pygame.image.load("dist/gameover.jpg")
overimg = pygame.transform.scale(overimg,(screen_width,screen_height)).convert_alpha()
bgimg = pygame.image.load("dist/main.png")
bgimg = pygame.transform.scale(bgimg,(screen_width,screen_height)).convert_alpha()

clock = pygame.time.Clock()
f= pygame.font.SysFont(None,50)
# ------------------------Colors---------------------------#
white = (255,255,255)
red = (255,0,0)
black = (0,0,0)
grey = (167,163,163)
yellow = (255,255,0)
# ---------------------------------------------------------#
food_x = random.randint(45,(screen_width/2)) # Food position x
food_y = random.randint(45,(screen_height/2)) # food position y
##-- Print stuff on screen --##
def text_screen(text,color,x,y):
    # Renders the text onto screen with defined font 'f'
    screen_text = f.render(text,True,color)
    # displays the text on window at positions x,y
    wn.blit(screen_text,[x,y])

# A function to draw the snake
def plot_snake(wn,color,snk_list,snake_size):
    for x,y in snk_list:
        pygame.draw.rect(wn, color,[x, y, snake_size, snake_size])

def welcome():
    pygame.mixer.music.load("dist/back.mp3")
    pygame.mixer.music.play()
    exit_game = False
    while not exit_game:
        wn.fill(white)
        wn.blit(welimg,(0,0))
        #text_screen("Welcome To Snakes",black,285,250)
        #text_screen("Press space to continue",black,250,290)
        for event in pygame.event.get():
            # Close the loop if close button clicked
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pygame.mixer.music.load("dist/eat.mp3")
                    pygame.mixer.music.play()
                    gameloop()
        pygame.display.update() #Update with changes in window
        clock.tick(30) #Determines the overall game speed
    pygame.quit()
    quit()

# ----------------- game loop --------------------------------#
def gameloop():
    #------------- Game specific variables --------------------- #
    exit_game = False  # Main game loop condition
    game_over = False  # Game over condition
    snake_x = 45  # initial position of snake
    snake_y = 55  # initial position of snake
    global food_x
    global food_y
    snake_size = 20  # size of the squre snake
    food_size = 12 # Size of snake food
    fps = 30
    vel = 4 # Speed of snake movement
    velocity_x = 0 # speed of automatic movement in x
    velocity_y = 0 # speed of automatic movement in y
    score = 0 # Initial score

    # If highscore file doesnot exist
    if (not os.path.exists("dist/score.txt")):
        with open("dist/score.txt","w") as f: #Opening in write mode creates the file
            f.write("0")
    # opens the file with highscores and takes last highscore
    with open("dist/score.txt","r") as f:
        highscore = int(f.read())

    snk_list = [ ]
    snk_length = 1 # Initial length of the snake / minimum length
    #-----------------------------------------------------------#
    while not exit_game:
        if game_over==True:
            # Rewrite the highscore to newer highscore as game closes
            with open("dist/score.txt","w") as f:
                f.write(str(highscore))

            wn.fill(white)
            wn.blit(overimg,(0,0))
            text_screen("Score "+str(score),grey,370,375)

            for event in pygame.event.get():
                # Close the loop if close button clicked
                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        welcome()
        else:
            # Loop to get the key press events
            for event in pygame.event.get():
                # Close the loop if close button clicked
                if event.type == pygame.QUIT:
                    exit_game = True
                #If a key is pressed
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        if (velocity_x == 0):
                            velocity_x += vel
                            velocity_y = 0
                        else:
                            continue
                    if event.key == pygame.K_DOWN:
                        if(velocity_y ==0):
                            velocity_y += vel
                            velocity_x = 0
                        else:
                            continue
                    if event.key == pygame.K_LEFT:
                        if (velocity_x == 0 ):
                            velocity_x -= vel
                            velocity_y = 0
                        else:
                            continue
                    if event.key == pygame.K_UP:
                        if (velocity_y == 0):
                            velocity_y -= vel
                            velocity_x = 0
                        else:
                            continue


            snake_x += velocity_x
            snake_y += velocity_y

            # food eating condition
            if (abs(snake_x - food_x)<8 and abs(snake_y - food_y)<8):
                pygame.mixer.music.load("dist/eat.mp3")
                pygame.mixer.music.play()
                score += 10
                food_x = random.randint(10,screen_width/2) #new Food position x
                food_y = random.randint(10,screen_height/2) #new food position y
                snk_length += 5 # Increases the minimum length
                # Resets the highscore value
                if score>highscore:
                    highscore = score

            wn.fill(white) # Set window color to white
            wn.blit(bgimg,(0,0))
            # Adding new head to the snake
            head = [ ]
            head.append(snake_x)
            head.append(snake_y)
            # New head value will be coninously added to snk_list
            snk_list.append(head)

            # Check wether the length of snake is greater than minimum length
            if len(snk_list)>snk_length:
                del snk_list[0]

            # Game over on wall collapse
            if snake_x<0 or snake_x>screen_width or snake_y<0 or snake_y>screen_height:
                game_over = True
                pygame.mixer.music.load("dist/gameover.mp3")
                pygame.mixer.music.play()

            # Game over if snake hits body
            # if new head coordinate is already present in snk_list
            if head in snk_list[:-1]:
                game_over = True
                pygame.mixer.music.load("dist/gameover.mp3")
                pygame.mixer.music.play()

            text_screen("Score: "+str(score)+" | Highscore:  "+str(highscore),white,5,5)
            # Food for the snake
            pygame.draw.rect(wn, red,[food_x, food_y, snake_size, snake_size])
            #pygame.draw.circle(wn, red,(food_x, food_y),food_size)
            # Head of the snake as rectangle
            plot_snake(wn,yellow,snk_list,snake_size)
            #pygame.draw.rect(wn, black,[snake_x, snake_y, snake_size, snake_size])
        pygame.display.update() #Update with changes in window
        clock.tick(fps) #Determines the overall game speed
    # -------------------------------------------------------------#

    pygame.quit()
    quit()

welcome()
