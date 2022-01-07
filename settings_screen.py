import pygame
from pygame import mixer

# Importing Variables
from data import *

# Sounds
mixer.music.load("Assets/Music/Synthwave.wav")
mixer.music.play(loops=-1)


class Text:
    def __init__(self, text, x, y, size):
        self.font = font
        self.text = self.font.render(text, True, (255, 255, 255))
        self.text = resize_img(self.text, size)
        self.text_rect = self.text.get_rect(center=(x, y))

    def Display(self, win):
        win.blit(self.text, self.text_rect)

# Texts


title = Text("Settings", 180, 50, 200)
on = Text("On", 400, 50, 100)
off = Text("Off", 600, 50, 100)
music_text = Text("Music:", 100, 250, 110)


def Buttons(win):
    win.blit(music_on, music_on_rect)
    win.blit(music_off, music_off_rect)


def BackButton(x):
    if back_btn_rect.collidepoint(pygame.mouse.get_pos()):
        mouse_pressed = pygame.mouse.get_pressed()
        if mouse_pressed[0] == 1:
            x = "menu"

    return x


def Click():
    if music_on_rect.collidepoint(pygame.mouse.get_pos()):
        mouse_pressed = pygame.mouse.get_pressed()
        if mouse_pressed[0] == 1:
            mixer.music.unpause()
    if music_off_rect.collidepoint(pygame.mouse.get_pos()):
        mouse_pressed = pygame.mouse.get_pressed()
        if mouse_pressed[0] == 1:
            mixer.music.pause()


def LoadSettingsScreen(win):
    win.blit(bg_img_settings, (0, 0))
    title.Display(win)
    music_text.Display(win)
    on.Display(win)
    off.Display(win)
    Buttons(win)
    win.blit(back_btn, back_btn_rect)
    Click()
