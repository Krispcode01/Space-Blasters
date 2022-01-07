import pygame
import random

# Importing all the Variables
from data import *


class PLAYER:
    def __init__(self, x, y, img):
        self.img = img
        self.rect = self.img.get_rect(center=(x, y))
        self.hp = 100
        self.hp_max = 100

    def Movement(self, speed):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= speed

        elif keys[pygame.K_RIGHT]:
            self.rect.x += speed

        if keys[pygame.K_UP]:
            self.rect.y -= speed

        elif keys[pygame.K_DOWN]:
            self.rect.y += speed

        if self.rect.y < 200:
            self.rect.y = 200

        if self.rect.y > 415:
            self.rect.y = 415

        if self.rect.x > 900:
            self.rect.x = 900

        if self.rect.x < 25:
            self.rect.x = 25

        return speed

    def Shoot(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_SPACE]:
            return True

        return False

    def Display(self, win):
        win.blit(self.img, self.rect)

    def Draw_Hp(self, win):
        x = 10
        y = 10

        HP_bar_width_max = 150
        HP_bar_height = 17

        ratio = self.hp / self.hp_max

        color_HP = [0, 255, 0]
        color_bg = (50, 50, 50)

        healthBar_width = HP_bar_width_max * ratio

        health_rec = pygame.Rect(x, y, healthBar_width, HP_bar_height)
        health_bound = pygame.Rect(x, y, HP_bar_width_max, HP_bar_height)

        pygame.draw.rect(win, color_bg, health_bound)
        pygame.draw.rect(win, color_HP, health_rec)
        pygame.draw.rect(win, (0, 0, 0), health_bound, 2)


class BULLET:
    def __init__(self, img, x, y, speed):
        self.speed_y = speed
        self.damage = 50
        self.img = img
        self.rect = self.img.get_rect(center=(x, y))
        self.show = True

    def Move(self, delete):
        self.rect.y -= self.speed_y

        if self.rect.y < 0:
            delete = True

        return delete

    def Display(self, win):
        if self.show == True:
            win.blit(self.img, self.rect)


class Enemies():
    def __init__(self, x, y):
        self.enemy = enemy_spaceship
        self.rect = self.enemy.get_rect(center=(x, y))
        self.hp = 100
        self.hp_max = 100
        self.show = True
        self.speed = 1
        self.bullet = img_bullet
        self.bullet_rect = self.bullet.get_rect(center=(x, y))
        self.bullet_show = True

    def Draw(self, win):
        if self.show == True:
            self.hp_w = int(self.rect.w * self.hp/self.hp_max)
            pygame.draw.rect(win, (255, 0, 0), pygame.Rect(
                self.rect.x, self.rect.y - 10, self.hp_w, 3))
            win.blit(self.enemy, self.rect)

    def Move(self, pattern):
        if pattern == "arrow":
            self.rect.y += self.speed + 1

        elif pattern == "right_tilt":
            self.rect.y += self.speed + 5
            self.rect.x -= self.speed + 5

        elif pattern == "left_tilt":
            self.rect.y += self.speed + 5
            self.rect.x += self.speed + 5

        elif pattern == "plus":
            self.rect.y += self.speed + 1


def EnemyWave1(x, y, total_enemies):
    x_space = 40
    y_space = 40
    enemy_list = []
    for i in range(total_enemies + 1):
        if i == 0:
            enemy = Enemies(x - (x_space * i), y - (y_space * i))
            enemy_list.append(enemy)
        else:
            enemy = Enemies(x - (x_space * i), y - (y_space * i))
            enemy_list.append(enemy)
            enemy = Enemies(x + (x_space * i), y - (y_space * i))
            enemy_list.append(enemy)

    return enemy_list


def EnemyWave2(x, y, total_enemies):
    x_space = 40
    y_space = 40
    enemy_list = []
    for i in range(total_enemies + 1):
        enemy = Enemies(x + (x_space * i), y - (y_space * i))
        enemy_list.append(enemy)

    return enemy_list


def EnemyWave3(x, y, total_enemies):
    x_space = 40
    y_space = 40
    enemy_list = []
    for i in range(total_enemies + 1):
        enemy = Enemies(x - (x_space * i), y - (y_space * i))
        enemy_list.append(enemy)

    return enemy_list


def EnemyWave4(x, y, total_enemies_y, total_enemies_x):
    x_space = 50
    y_space = 50
    enemy_list = []
    for i in range(total_enemies_y):
        enemy = Enemies(x + (x_space * 2), y + (y_space * i))
        enemy_list.append(enemy)

    for i in range(total_enemies_x):
        enemy = Enemies(x + (x_space * i), y + (y_space * 2))
        enemy_list.append(enemy)

    return enemy_list


def CreateBg():
    bg_size = SCREEN_WIDTH
    w = int(SCREEN_WIDTH / bg_size)
    h = int(SCREEN_WIDTH / bg_size)

    for i in range(w+1):
        for j in range(h + 1):
            x = i * bg_size
            y = j * bg_size
            rect = space_bg.get_rect(topleft=(x, y))
            bg_list.append(rect)


CreateBg()


def DisplayBg(win):
    for bg in bg_list:
        bg.y += 5
        if bg.top >= SCREEN_HEIGHT:
            bg.bottom = 0

        win.blit(space_bg, bg)


def ShootBullets(LIST_BULLET):
    # create bullet middle of the player
    bullet = BULLET(img_bullet, player_01.rect.x +
                    int(player_01.rect.w/2 - 1), player_01.rect.y, 17)
    LIST_BULLET.append(bullet)

    return LIST_BULLET


def EnemyShootBullets(LIST_ENEMY_BULLET, enemy, speed):
    # create bullet middle of the player
    bullet = BULLET(img_bullet, enemy.rect.x +
                    int(enemy.rect.w/2 - 1), enemy.rect.y, speed)
    LIST_ENEMY_BULLET.append(bullet)

    return LIST_ENEMY_BULLET


player_01 = PLAYER(200, 500, player_spaceship)


def LoadGameScreen(win):
    DisplayBg(win)
    player_01.Display(win)
    player_01.Draw_Hp(win)
    for enemy in ENEMY_LIST:
        enemy.DisplayEnemy(win)
        enemy.Move()
