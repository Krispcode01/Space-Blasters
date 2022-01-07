import pygame

# Importing all the Variables
from data import *
from menu_screen import *


class Text:
    def __init__(self, text, x, y, size):
        self.font = font
        self.text = self.font.render(text, True, (255, 255, 255))
        self.text = resize_img(self.text, size)
        self.text_rect = self.text.get_rect(center=(x, y))

    def Display(self, win):
        win.blit(self.text, self.text_rect)


# Texts
title = Text("Workshop", 350, 50, 200)
speed_txt = Text("Player Speed + :", 150, 190, 110)
speed_cost = Text("(50 Points)", 150, 210, 80)
reload_txt = Text("Reload Speed - :", 150, 290, 110)
reload_cost = Text("(100 Points)", 150, 310, 80)

# Buttons
btn_speed_yes = Button('Purchase', 450, 200)
btn_bullet_reload = Button('Purchase', 450, 300)
btn_back = Button('Back', 120, 470)


def ButtonClick(speed, SCORE, reload_time, SCREEN):
    if btn_speed_yes.rect.collidepoint(pygame.mouse.get_pos()):
        mouse_pressed = pygame.mouse.get_pressed()
        if SCORE >= 50 and speed < 10:
            if mouse_pressed[0] == 1:
                speed = 10
                SCORE -= 50

    if btn_bullet_reload.rect.collidepoint(pygame.mouse.get_pos()):
        mouse_pressed = pygame.mouse.get_pressed()
        if SCORE >= 100 and reload_time > 0.15:
            if mouse_pressed[0] == 1:
                reload_time = 0.15
                SCORE -= 100

    if btn_back.rect.collidepoint(pygame.mouse.get_pos()):
        mouse_pressed = pygame.mouse.get_pressed()
        if mouse_pressed[0] == 1:
            SCREEN = "menu"

    return speed, SCORE, reload_time, SCREEN


def LoadWorkshopScreen(win):
    win.blit(workshop_bg, (0, 0))
    title.Display(win)
    speed_txt.Display(win)
    speed_cost.Display(win)
    reload_txt.Display(win)
    reload_cost.Display(win)
    btn_speed_yes.Display(win)
    btn_bullet_reload.Display(win)
    btn_back.Display(win)
