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

#fonts
font = pygame.font.SysFont('Times New Roman', 26)
red = (255, 0, 0)
green = (0, 255, 0)

#load images
# background image
background_img = pygame.image.load('assets/background.png').convert_alpha()
# health panel
panel_img = pygame.image.load('assets/panel.png').convert_alpha()

#drawing text
def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, x, y)
#function for background drawing
def draw_bg():
    screen.blit(background_img, (0, 0))

def draw_panel():
    screen.blit(panel_img, (0, screen_height - bottom_panel))
    #show player stats
    draw_text()

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
        self.animation_list = []
        self.frame_index = 0
        self.action = 0 #0:idle, 1:attack, 2:hurt, 3:dead
        self.update_time = pygame.time.get_ticks()

        #load idle images
        temp_list = []
        for i in range(8):
            img = pygame.image.load(f'assets/sprites/{self.name}/idle/{i}.png')
            img = pygame.transform.scale(img, (img.get_width() * 2.5, img.get_height() * 2.5))
            temp_list.append(img)
        self.animation_list.append(temp_list)

        # load attack images
        temp_list = []
        for i in range(8):
            img = pygame.image.load(f'assets/sprites/{self.name}/attack/{i}.png')
            img = pygame.transform.scale(img, (img.get_width() * 2.5, img.get_height() * 2.5))
            temp_list.append(img)
        self.animation_list.append(temp_list)

        self.img = self.animation_list[self.action][self.frame_index]
        self.rect = self.img.get_rect()
        self.rect.center = (x, y)

    def update(self):
        animation_cooldown = 100

        self.img = self.animation_list[self.action][self.frame_index]

        if pygame.time.get_ticks() - self.update_time > animation_cooldown:
            self.update_time = pygame.time.get_ticks()
            self.frame_index += 1

        if self.frame_index >= len(self.animation_list[self.action]):
            self.frame_index = 0

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
    white_mage.update()
    white_mage.draw()
    black_mage.update()
    black_mage.draw()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()