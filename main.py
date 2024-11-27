import pygame
import random

pygame.init()

clock = pygame.time.Clock()
fps = 60

# game window
bottom_panel = 150
screen_width = 600
screen_height = 400 + bottom_panel

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Battle')

#game variables
current_mage = 1
total_mage = 2
action_cooldown = 0
action_wait_time = 90
attack = False
potion = False
clicked = False
game_over = 0

#fonts
font = pygame.font.SysFont('Monospace', 20)
ko_font = pygame.font.SysFont('Monospace', 50)
red = (255, 0, 0)
green = (0, 255, 0)
white = (255,255,255)
light_blue = (0, 175, 199)

# restart text
restart_text = 'RESTART'
restart_font = font
restart_x, restart_y = 250, 125
restart_color = green if game_over == 1 else red
# Define a rect for restart
restart_img = restart_font.render(restart_text, True, restart_color)
restart_rect = restart_img.get_rect(topleft=(restart_x, restart_y))

#load images
# background image
background_img = pygame.image.load('assets/background.png').convert_alpha()
# health panel
panel_img = pygame.image.load('assets/panel.png').convert_alpha()
#fireball cursor
fireball_img = pygame.image.load('assets/Fireball.png').convert_alpha()
# potion image
healspell_img = pygame.image.load('assets/healspell.png').convert_alpha()


#drawing text
def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))
#function for background drawing
def draw_bg():
    screen.blit(background_img, (0, 0))

def draw_panel():
    screen.blit(panel_img, (0, screen_height - bottom_panel))
    #show player stats
    draw_text(f'{white_mage.name} HP: {white_mage.hp}', font, white, 355, 410)
    draw_text(f'Heals left: {white_mage.heals}', font, white, 375, 475)
    draw_text(f'{black_mage.name} HP: {black_mage.hp}', font, light_blue, 55, 410)

# player class
class Mage():
    def __init__(self, x, y, name, max_hp, magic, heals):
        self.name = name
        self.max_hp = max_hp
        self.hp = max_hp
        self.magic = magic
        self.start_heals = heals
        self.heals = heals
        self.alive = True
        self.animation_list = []
        self.frame_index = 0
        self.action = 0 #0:idle, 1:attack, 2: heal, 3:hurt, 4:dead
        self.update_time = pygame.time.get_ticks()

        #load idle images
        temp_list = []
        for i in range(1):
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

        # load heal images
        temp_list = []
        for i in range(8):
            img = pygame.image.load(f'assets/sprites/{self.name}/heal/{i}.png')
            img = pygame.transform.scale(img, (img.get_width() * 2.5, img.get_height() * 2.5))
            temp_list.append(img)
        self.animation_list.append(temp_list)

        # load hurt images
        temp_list = []
        for i in range(6):
            img = pygame.image.load(f'assets/sprites/{self.name}/hurt/{i}.png')
            img = pygame.transform.scale(img, (img.get_width() * 2.5, img.get_height() * 2.5))
            temp_list.append(img)
        self.animation_list.append(temp_list)

        # load death image
        temp_list = []
        for i in range(1):
            img = pygame.image.load(f'assets/sprites/{self.name}/dead/{i}.png')
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
            if self.hp < 1:
                self.dead()
            elif (self.hp / self.max_hp) < 0.5:
                self.hurt()
            else:
                self.idle()

    def idle(self):
        self.action = 0
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()

    def attack(self, target):
        #deal damage
        rand = random.randint(-5, 5)
        damage = self.magic + rand
        target.hp -= damage
        # hurt animation
        target.hurt()
        #check if dead
        if target.hp < 1:
            target.hp = 0
            target.alive = False
            target.dead()

        # animation
        self.action = 1
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()


    def heal(self):
        #heal amount
        rand = random.randint(-5, 5)
        heal = self.magic + rand
        if self.heals <= 0:
            return
        else:
            self.hp += heal
            self.heals -= 1
        #check if more than health bar
        if self.hp > self.max_hp:
            self.hp = self.max_hp
        # animation
        self.action = 2
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()


    def hurt(self):
        self.action = 3
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()


    def dead(self):
        self.action = 4
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()


    def reset(self):
        self.alive = True
        self.heals = self.start_heals
        self.hp = self.max_hp
        self.frame_index = 0
        self.action = 0
        self.update_time = pygame.time.get_ticks()


    def draw(self):
        screen.blit(self.img, self.rect)



class HealthBar():
    def __init__(self, x, y, hp, max_hp):
        self.x = x
        self.y = y
        self.hp = hp
        self.max_hp = max_hp

    def draw(self, hp):
        #update with new health
        self.hp = hp
        ratio = self.hp / self.max_hp
        pygame.draw.rect(screen, red, (self.x, self.y, 150, 20))
        pygame.draw.rect(screen, green, (self.x, self.y, 150 * ratio, 20))



white_mage = Mage(450, 325, 'White Mage', 30, 10, 3)
black_mage = Mage(150, 325, 'Black Mage', 35, 10, 1)

white_mage_health_bar = HealthBar(375, screen_height - bottom_panel + 40, white_mage.hp, white_mage.max_hp)
black_mage_health_bar = HealthBar(75, screen_height - bottom_panel + 40, black_mage.hp, black_mage.max_hp)

def wait_for_click():
    print("Click anywhere to start")  # Prompt the user
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # Allow the user to quit while waiting
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:  # Start the game on mouse click
                waiting = False

    # Wait for the user to click before starting
wait_for_click()

run = True
while run:

    clock.tick(fps)

    # draw images
    draw_bg()
    draw_panel()
    white_mage_health_bar.draw(white_mage.hp)
    black_mage_health_bar.draw(black_mage.hp)

    white_mage.update()
    white_mage.draw()
    black_mage.update()
    black_mage.draw()

    #control plater actions
    # reset actions
    attack = False
    heal = False
    # mouse visible
    pygame.mouse.set_visible(True)
    pos = pygame.mouse.get_pos()

    #attack
    if black_mage.rect.collidepoint(pos):
        #hide mouse
        pygame.mouse.set_visible(False)
        #show fireball
        screen.blit(fireball_img, pos)
        if clicked == True:
            attack = True

    #heal
    if white_mage.rect.collidepoint(pos):
        #hide mouse
        pygame.mouse.set_visible(False)
        #show fireball
        screen.blit(healspell_img, pos)
        if clicked == True:
            heal = True

    if game_over == 0:
        # player action
        if white_mage.alive == True:
            if current_mage == 1:
                action_cooldown += 1
                if action_cooldown >= action_wait_time:
                    #attack
                    if attack == True:
                        white_mage.attack(black_mage)
                        current_mage += 1
                        action_cooldown = 0
                    #heal
                    if heal == True:
                        white_mage.heal()
                        current_mage += 1
                        action_cooldown = 0
        else:
            game_over = -1

        # boss action
        if black_mage.alive == True:
            if current_mage == 2:
                action_cooldown += 1
                if action_cooldown >= action_wait_time:
                    #check if need to heal otherwise attack
                    if (black_mage.hp / black_mage.max_hp) < 0.5 and black_mage.heals > 0:
                        black_mage.heal()
                        current_mage += 1
                        action_cooldown = 0
                    else:
                        # attack
                        black_mage.attack(white_mage)
                        current_mage += 1
                        action_cooldown = 0
        else:
            game_over = 1

    if game_over != 0:
        if game_over == 1:
            draw_text('VICTORY!', ko_font, green, 175, 75)
        if game_over == -1:
            draw_text('DEFEAT', ko_font, red, 205, 75)

        # Render restart text and display it
        restart_surface = restart_font.render(restart_text, True, (255, 255, 0) if restart_rect.collidepoint(pos) else restart_color)
        screen.blit(restart_surface, restart_rect.topleft)

        # Check if clicked on restart
        if restart_rect.collidepoint(pos) and clicked:
            game_over = 0
            white_mage.reset()
            black_mage.reset()
            current_mage = 1
            action_cooldown = 0

    # reset current mage
    if current_mage > total_mage:
        current_mage = 1

    #clicked event logic
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            clicked = True
        else:
            clicked = False

    pygame.display.update()

pygame.quit()
