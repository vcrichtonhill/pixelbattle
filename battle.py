import pygame

pygame.init()

clock = pygame.time.Clock()
fps = 60

# game window
bottom_panel = 150
screen_width = 600
screen_height = 400 + bottom_panel

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Battle')

#load images
# background image
background_img = pygame.image.load('assets/sprites/background.png').convert_alpha()
# health panel
panel_img = pygame.image.load('assets/sprites/panel.png').convert_alpha()

#function for background drawing
def draw_bg():
    screen.blit(background_img, (0, 0))

def draw_panel():
    screen.blit(panel_img, (0, screen_height - bottom_panel))
run = True
while run:

    clock.tick(fps)

    # draw images
    draw_bg()
    draw_panel()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()