import pygame
from sys import exit

# This is needed for all pygames
pygame.init() 
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('Blade Runner')
clock = pygame.time.Clock()
test_font = pygame.font.Font('font/Pixeltype.ttf',50)

sky = pygame.image.load('graphics/Sky.png').convert()
ground = pygame.image.load('graphics/Ground.png').convert()

score_surface = test_font.render('Score:', False, (64,64,64))
score_rect = score_surface.get_rect(center = (400,50))

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
        if event.type == pygame.MOUSEBUTTONDOWN and player_hitbox.bottom >=300:
                if player_hitbox.collidepoint(event.pos):
                    player_gravity = -20
              
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and player_hitbox.bottom >=300:
                player_gravity = -20

    # Background
    screen.blit(sky,(0,0))
    screen.blit(ground,(0,300))
    pygame.draw.rect(screen,'#c0e8ec', score_rect, )
    pygame.draw.rect(screen,'#c0e8ec', score_rect, 10)
    screen.blit(score_surface,score_rect)

    # Snail
    snail_hitbox.x -= 4
    if snail_hitbox.right <= 0: snail_hitbox.left = 800
    screen.blit(snail_surface,snail_hitbox)

    # Player
    player_gravity += 1
    player_hitbox.y += player_gravity
    if player_hitbox.bottom >= 300: player_hitbox.bottom = 300
    screen.blit(player_surface,player_hitbox)

    pygame.display.update()
    clock.tick(60)

