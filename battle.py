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
background_img = pygame.image.load('assets/background.png').convert_alpha()
# health panel
panel_img = pygame.image.load('assets/panel.png').convert_alpha()

#function for background drawing
def draw_bg():
    screen.blit(background_img, (0, 0))

def draw_panel():
    screen.blit(panel_img, (0, screen_height - bottom_panel))

# player class
class Mage():
    def __init__(self, x, y, name, max_hp, strength, potions):
        self.name = name
        self.max_hp = max_hp
        self.hp = max_hp
        self.strength = strength
        self.start_potions = potions
        self.potions = potions
        self.alive = True
        img = pygame.image.load(f'assets/sprites/{self.name}/idle/idle.png')
        self.img = pygame.transform.scale(img, (img.get_width() * 2.5, img.get_height() * 2.5))
        self.rect = self.img.get_rect()
        self.rect.center = (x, y)

    def draw(self):
        screen.blit(self.img, self.rect)

white_mage = Mage(450, 325, 'player', 30, 10, 3)
black_mage = Mage(150, 325, 'boss', 40, 10, 1)

run = True
while run:

    clock.tick(fps)

    # draw images
    draw_bg()
    draw_panel()
    white_mage.draw()
    black_mage.draw()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()