import pygame
import random


pygame.mixer.init()
pygame.init()


#colors
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)

screen_width = 900
screen_height = 500

#creating window
gameWindow = pygame.display.set_mode((screen_width, screen_height))
#background image
bgimg = pygame.image.load("F:\hp\Desktop\snake.jpg")
bgimg = pygame.transform.scale(bgimg, (screen_width, screen_height)).convert_alpha()

bgimg1 = pygame.image.load("F:\hp\Desktop\gameover.jpg")
bgimg1 = pygame.transform.scale(bgimg1, (screen_width, screen_height)).convert_alpha()

bgimg2 = pygame.image.load("F:\hp\Desktop\snake1.jpg")
bgimg2 = pygame.transform.scale(bgimg2, (screen_width, screen_height)).convert_alpha()


pygame.display.set_caption("Snake With Prince")
pygame.display.update()

clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 55)


def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text, [x, y])


def plot_snake(gameWindow, color, snk_list, snake_size):
    for x, y in snk_list:
        pygame.draw.rect(gameWindow, color, [x, y, snake_size, snake_size])


def welcome():
    exit_game =  False
    while not exit_game:
        gameWindow.fill((233, 220, 229))
        gameWindow.blit(bgimg2, (0, 0))
        text_screen("Welcome To Snakes", black, 260, 250)
        text_screen("Press Space Bar To Play", black, 232, 290)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    gameloop()


        pygame.display.update()
        clock.tick(60)
# Game Loop


def gameloop():
    # GAME SPECIFIC VARIABLE
    exit_game = False
    game_over = False
    snake_x = 45
    snake_y = 55
    velocity_x = 0
    velocity_y = 0
    score = 0
    init_velocity = 5
    food_x = random.randint(20, screen_width / 2)
    food_y = random.randint(20, screen_height / 2)
    snake_size = 15
    fps = 70
    snk_list = []
    snk_length = 1
    with open("hiscore.txt", "r") as f:
        hiscore = f.read()

    while not exit_game:
        if game_over:
            with open("hiscore.txt", "w") as f:
                f.write(str(hiscore))
            gameWindow.fill(white)
            gameWindow.blit(bgimg1, (0, 0))
            text_screen("Press Enter To Continue", red, 50, 20)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        welcome()


        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x = init_velocity
                        velocity_y = 0

                    if event.key == pygame.K_LEFT:
                        velocity_x = -init_velocity
                        velocity_y = 0

                    if event.key == pygame.K_UP:
                        velocity_y = - init_velocity
                        velocity_x = 0

                    if event.key == pygame.K_DOWN:
                        velocity_y = init_velocity
                        velocity_x = 0

            snake_x = snake_x + velocity_x
            snake_y = snake_y + velocity_y

            if abs(snake_x - food_x)<6 and abs(snake_y - food_y)<6:
                score += 10
                food_x = random.randint(0, screen_width)
                food_y = random.randint(0, screen_height)
                snk_length +=5
                if score>int(hiscore):
                    hiscore = score
            gameWindow.fill(white)
            gameWindow.blit(bgimg, (0, 0))
            text_screen("Score :" + str(score) + "  Hi_Score: "+str(hiscore), red, 5, 5)
            pygame.draw.rect(gameWindow, red, [food_x, food_y, snake_size, snake_size])

            head = []
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)

            if len(snk_list)>snk_length:
                del snk_list[0]

            if head in snk_list[:-1]:
                game_over = True


            if snake_x<0 or snake_x>screen_width or snake_y<0 or snake_y>screen_height:
                game_over = True
                print(game_over)






           # pygame.draw.rect(gameWindow, black, [snake_x, snake_y, snake_size, snake_size ])
            plot_snake(gameWindow, black, snk_list, snake_size)
        pygame.display.update()
        clock.tick(fps)

    pygame.QUIT()
    quit()


welcome()
gameloop()