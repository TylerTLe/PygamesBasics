import pygame
from sys import exit

def display_score():
    current_time = int(pygame.time.get_ticks() / 1000) - start_time
    score_surface = test_font.render(f'Score:{current_time}', False, (64,64,64))
    score_rect = score_surface.get_rect(center = (400,50))
    screen.blit(score_surface,score_rect)

pygame.init() 
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()
test_font = pygame.font.Font('font/Pixeltype.ttf',50)
game_active = True
start_time = 0

sky = pygame.image.load('graphics/Sky.png').convert()
ground = pygame.image.load('graphics/Ground.png').convert()

# score_surface = test_font.render('Score:', False, (64,64,64))
# score_rect = score_surface.get_rect(center = (400,50))

snail_surface = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
snail_hitbox = snail_surface.get_rect(bottomright = (600,300))

player_surface = pygame.image.load('graphics/player/player_walk_1.png').convert_alpha()
player_hitbox = player_surface.get_rect(midbottom = (80,300))
player_gravity = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if game_active:
            if event.type == pygame.MOUSEBUTTONDOWN and player_hitbox.bottom >=300:
                    if player_hitbox.collidepoint(event.pos):
                        player_gravity = -20
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player_hitbox.bottom >=300:
                    player_gravity = -20
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                snail_hitbox.left = 800
                start_time = int(pygame.time.get_ticks() / 1000)

# Game screen and mechanics
    if game_active:
        # Background
        screen.blit(sky,(0,0))
        screen.blit(ground,(0,300))
        display_score()

        # Snail
        snail_hitbox.x -= 4
        if snail_hitbox.right <= 0: snail_hitbox.left = 800
        screen.blit(snail_surface,snail_hitbox)

        # Player
        player_gravity += 1
        player_hitbox.y += player_gravity
        if player_hitbox.bottom >= 300: player_hitbox.bottom = 300
        screen.blit(player_surface,player_hitbox)

        # Collision
        if snail_hitbox.colliderect(player_hitbox):
            game_active = False

# Start screen
    else:
        screen.fill('Blue')
 
    pygame.display.update()
    clock.tick(60)

