import pygame
from pygame import mixer
import time

pygame.init()

# Size


def resize_img(img, ratio):
    w = img.get_width()
    h = img.get_height()
    new_W = int(w * ratio/100)
    new_H = int(h * ratio/100)
    img = pygame.transform.scale(img, (new_W, new_H))

    return img


# Variables
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500
SCREEN = "menu"
LIST_BULLET = []
bullet_delay = time.time()
shoot = False
bg_list = []
ENEMY_LIST = []
total_enemies = 3
enemy_x = 150
reload_time = 0.5
pattern = "arrow"
enemy_pattern_v = []
SCORE = 0
enemy_pattern_v_trigger = 0
LIST_ENEMY_BULLET = []
enemy_pattern_rt = []
fg = (255, 255, 255)
health_reduce = 0
enemy_pattern_plus = []
speed = 5

# Images
bg_img = pygame.image.load("Assets/Game Background/menu_bg2.png")

bg_img_settings = pygame.image.load("Assets/Game Background/settings_bg.jpeg")
bg_img_settings = pygame.transform.scale(bg_img_settings, (SCREEN_WIDTH, SCREEN_HEIGHT))

space_bg = pygame.image.load("Assets/Game Background/game_bg.gif")
space_bg = pygame.transform.scale(space_bg, (SCREEN_WIDTH, SCREEN_WIDTH))

workshop_bg = pygame.image.load("Assets/Game Background/workshop_bg.png")

main_title = pygame.image.load("Assets/Title.png")

img_blue = pygame.image.load("Assets/Buttons/Img/main_button.png")
img_yellow = pygame.image.load("Assets/Buttons/Img/hover_button.png")
img_yellow = pygame.transform.scale(img_yellow, (395, 395))

font = pygame.font.Font("Assets/Font/kenvector_future.ttf", 22)

player_spaceship = pygame.image.load("Assets/battleship.png")
player_spaceship = resize_img(player_spaceship, 11)

enemy_spaceship = pygame.image.load("Assets/enemy_00.png")
enemy_spaceship = resize_img(enemy_spaceship, 505)

img_bullet = pygame.image.load("Assets/bullet_00.png")
img_bullet = resize_img(img_bullet, 550)

music_on = pygame.image.load("Assets/Buttons/Img/Music_On_Button.png")
music_on = resize_img(music_on, 60)
music_on_rect = music_on.get_rect(center=(400, 250))
music_off = pygame.image.load("Assets/Buttons/Img/Music_Off_Button.png")
music_off = resize_img(music_off, 60)
music_off_rect = music_off.get_rect(center=(600, 250))

back_btn = pygame.image.load("Assets/Buttons/Img/Movement Buttons.png")
back_btn = resize_img(back_btn, 70)
back_btn_rect = back_btn.get_rect(center=(100, 470))

font = font
text = font.render(f"Score: {SCORE}", True, (255, 255, 255))
text = resize_img(text, 50)

game_over = pygame.image.load("Assets/Game Background/game_over_bg.png")
game_over = pygame.transform.scale(game_over, (SCREEN_WIDTH, SCREEN_HEIGHT))
