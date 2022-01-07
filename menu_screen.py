import pygame

# Importing all the Variables
from data import *


class Button:
    def __init__(self, text, x=0, y=0):
        self.x = x
        self.y = y
        self.font = font
        self.img_01 = img_blue
        self.img_02 = img_yellow
        self.text = self.font.render(text, True, (0, 0, 0))
        self.text_rect = self.text.get_rect(center=(0, 0))
        self.rect = self.img_01.get_rect(center=(self.x, self.y))

    def Display(self, win):
        self.text_rect.x = self.rect.x + self.rect.w/2 - self.text_rect.w/2
        self.text_rect.y = self.rect.y + self.rect.h/2 - self.text_rect.h/2

        if self.rect.collidepoint(pygame.mouse.get_pos()):
            win.blit(self.img_02, self.rect)
        else:
            win.blit(self.img_01, self.rect)

        win.blit(self.text, self.text_rect)


def MenuButtonClick(SCREEN):
    if btn_start.rect.collidepoint(pygame.mouse.get_pos()):
        mouse_pressed = pygame.mouse.get_pressed()
        if mouse_pressed[0] == 1:
            SCREEN = 'game'
    if btn_workshop.rect.collidepoint(pygame.mouse.get_pos()):
        mouse_pressed = pygame.mouse.get_pressed()
        if mouse_pressed[0] == 1:
            SCREEN = 'workshop'
    if btn_settings.rect.collidepoint(pygame.mouse.get_pos()):
        mouse_pressed = pygame.mouse.get_pressed()
        if mouse_pressed[0] == 1:
            SCREEN = 'settings'
    if btn_exit.rect.collidepoint(pygame.mouse.get_pos()):
        mouse_pressed = pygame.mouse.get_pressed()
        if mouse_pressed[0] == 1:
            SCREEN = 'quit'

    return SCREEN


def DisplayButtons(win):
    global btn_list

    for btn in btn_list:
        btn.Display(win)


def DisplayTitle(win):
    win.blit(main_title, (115, -165))


def LoadMenuScreen(win, SCREEN):
    global bg_list, btn_list

    DisplayButtons(win)
    DisplayTitle(win)

    SCREEN = MenuButtonClick(SCREEN)

    return SCREEN


btn_start = Button('Play', 250, 300)
btn_workshop = Button('Workshop', 250, 380)
btn_settings = Button('Settings', 470, 300)
btn_exit = Button('Quit', 470, 380)

btn_list = [btn_start, btn_workshop, btn_settings, btn_exit]
