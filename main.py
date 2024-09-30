import pygame, random

pygame.init()

WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 400
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Feed THe Dragon")

FPS = 60
clock = pygame.time.Clock()

# Set game value:  CONSTANT_NAME, value
''' 5 CONSTANTS
PLAYER_STARTING_LIVES, 5
PLAYER_VELOCITY, 10
COIN_STARTING_VELOCITY, 10
COIN_ACCELERATION, 0.5
BUFFER_DISTANCE, 100
'''
PLAYER_STARTING_LIVES = 5
PLAYER_VELOCITY = 10
COIN_STARTING_VELOCITY = 10
COIN_ACCELERATION = 0.5
BUFFER_DISTANCE = 100

# Set Game Variables:  variable_name
''' 3 variables
score, 0
player_lives, PLAYER_STARTING_LIVES
coin_velocity, COIN_STARTING_VELOCITY
'''
score = 0
player_lives = PLAYER_STARTING_LIVES
coin_velocity = COIN_STARTING_VELOCITY

GREEN = (0, 255, 0)
DARK_GREEN = (10, 50, 10)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

font = pygame.font.Font("AttackGraffiti.ttf", 32)

'''
variable names:  score_text, score_rect
render text: "Score: " + str(score)
antialias: True
color: GREEN
background: DARK_GREEN
rect location: top_left = (10, 10)  
'''
score_text = font.render("Score: " + str(score), True, GREEN, DARK_GREEN)
score_rect = score_text.get_rect()
score_rect.topleft = (10, 10)

'''
variable names:  title_text , title_rect 
render text: "Feed the Dragon"
antialias: True
color: GREEN
background: WHITE
rect location: center = WINDOW_WIDTH//2
rect location: y = 10 
'''
title_text = font.render("Feed the Dragon", True, GREEN, WHITE)
title_rect = title_text.get_rect()
title_rect.centerx = WINDOW_WIDTH // 2
title_rect.y = 10

'''
Variable: game_over_text
Rect: game_over_rect
PHRASE: "GAMEOVER"
Antialias: True
Color: GREEN,
Background: DARK_GREED ,
Position: center = (WINDOW_WIDTH //2, WINDOW_HEIGHT //2),
'''
game_over_text = font.render("game_over_text", True, GREEN, DARK_GREEN)
game_over_rect = title_text.get_rect()
game_over_rect.center = WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2
'''
Variable:  continue_text
Rect: continue_rect
PHRASE:  "Press any key to play again"
Antialias: True
Color: GREEN, 
Background: DARK_GREEN,
Position: center = (WINDOW_WIDTH //2, WINDOW_HEIGHT //2 + 32),
'''
continue_text = font.render("continue", True, GREEN, DARK_GREEN)
continue_rect = continue_text.get_rect()
continue_rect.center = WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + 32

'''
variable names:  lives_text, lives_rect
render text: "Lives: " + str(player_lives)
antialias: True
color: GREEN
background: DARK_GREEN
rect location: topright = (WINDOW_WIDTH - 10, 10) 
'''
lives_text = font.render("Lives: " + str(player_lives), True, GREEN, DARK_GREEN)
lives_rect = lives_text.get_rect()
lives_rect.topright = (WINDOW_WIDTH - 10, 10)

coin_sound = pygame.mixer.Sound("coin_sound.wav")
miss_sound = pygame.mixer.Sound("miss_sound.wav")
coin_sound.set_volume(1)
miss_sound.set_volume(0.1)
pygame.mixer.music.load("ftd_background_music.wav")

'''
variable names:  player_image, player_rect
image source : "dragon_right.png"
rect location: left = 32
rect location: centery = WINDOW_HEIGHT // 2
'''
player_image = pygame.image.load("dragon_right.png")
player_rect = title_text.get_rect()
player_rect.centery = WINDOW_HEIGHT // 2
player_rect.left = 32

'''
variable names:  coin_image, coin_rect
image source : coin.png"
rect location: x = WINDOWS_WIDTH + BUFFER_DISTANCE
rect location:  y = random.randint(64, WINDOW_HEIGHT - 32)
'''

coin_image = pygame.image.load("coin.png")
coin_rect = coin_image.get_rect()
coin_rect.x = WINDOW_WIDTH + BUFFER_DISTANCE
coin_rect.y = random.randint(64, WINDOW_HEIGHT - 32)

pygame.mixer.music.play(-1, 0.0)

# The main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and player_rect.top > 64:
        player_rect.y -=  PLAYER_VELOCITY
    if keys[pygame.K_DOWN] and player_rect.bottom < WINDOW_HEIGHT:
        player_rect.y += PLAYER_VELOCITY

    if coin_rect.x < 0:
        player_lives -= 1
        miss_sound.play()
        coin_rect.x = WINDOW_WIDTH + BUFFER_DISTANCE
        coin_rect.y = random.randint(64, WINDOW_HEIGHT - 32)
    else:
        coin_rect.x -= coin_velocity

    if player_rect.colliderect(coin_rect):
        score += 1
        coin_sound.play()
        coin_velocity += COIN_ACCELERATION
        coin_rect.x = WINDOW_WIDTH + BUFFER_DISTANCE
        coin_rect.y = random.randint(64, WINDOW_HEIGHT - 32)


    score_text = font.render("Score:" + str(score), True, GREEN, DARK_GREEN)
    lives_text = font.render("Lives: " + str(player_lives), True, GREEN, DARK_GREEN)

    if player_lives == 0:
        display_surface.blit(game_over_text, game_over_rect)
        display_surface.blit(continue_text, continue_rect)
        pygame.display.update()


        pygame.mixer_music.stop()
        is_paused = True
        while is_paused:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    score =0
                    player_lives = PLAYER_STARTING_LIVES
                    player_rect.y = WINDOW_HEIGHT // 2
                    coin_velocity = COIN_STARTING_VELOCITY
                    pygame.mixer.music.play(-1, 0.0)
                    is_paused = False
                if event.type == pygame.QUIT:
                    is_paused = False
                    running = False

                    # Fill the display
    display_surface.fill(BLACK)

    display_surface.blit(score_text, score_rect)
    display_surface.blit(title_text, title_rect)
    display_surface.blit(lives_text, lives_rect)
    display_surface.blit(coin_image, coin_rect)
    display_surface.blit(player_image, player_rect)
    pygame.draw.line(display_surface, WHITE, (0,64), (WINDOW_WIDTH, 64), 2)


    # Update display and tick the clock
    pygame.display.update()
    clock.tick(FPS)

pygame.quit()