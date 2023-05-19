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
text_surface = test_font.render('My game', False, 'Black')

snail_surface = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
snail_x = 600
snail_hitbox = snail_surface.get_rect(bottomright = (600,300))


player_surface = pygame.image.load('graphics/player/player_walk_1.png').convert_alpha()
player_hitbox = player_surface.get_rect(midbottom = (80,300))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEMOTION:
            if player_hitbox.collidepoint(event.pos): print('collision')

    screen.blit(sky,(0,0))
    screen.blit(ground,(0,300))
    screen.blit(text_surface,(300,50))

    snail_hitbox.x -= 4
    if snail_hitbox.right <= 0: snail_hitbox.left = 800
    screen.blit(snail_surface,snail_hitbox)
    screen.blit(player_surface,player_hitbox)
    
    # if player_hitbox.collidedict(snail_hitbox):
    #     player_hitbox.collidepoint()

    # mouse_pos = pygame.mouse.get_pos()
    # if player_hitbox.collidepoint((mouse_pos)):
    #     pygame.mouse.get_pressed()
        

    pygame.display.update()
    clock.tick(60)

