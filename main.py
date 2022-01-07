import pygame

# Python Files
from settings_screen import *
from game_screen import *
from menu_screen import *
from workshop_screen import *
from data import *

pygame.init()

surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Space Blasters")

enemy_pattern_v = EnemyWave1(200, 0, 2)
enemy_pattern_rt = EnemyWave2(700, 0, 3)
enemy_pattern_lt = EnemyWave3(0, 0, 3)
enemy_pattern_plus = EnemyWave4(400, -200, 5, 5)

FPS = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    if SCREEN == "menu":
        surface.blit(bg_img, (0, 0))
        SCREEN = LoadMenuScreen(surface, SCREEN)

    elif SCREEN == "game":
        if player_01.hp > 0:
            surface.fill((0, 0, 32))
            LoadGameScreen(surface)
            speed = player_01.Movement(speed)
            text = font.render(f"Score: {SCORE}", True, (255, 255, 255))
            surface.blit(text, (500, 10))

            if player_01.Shoot() == True and (time.time() - bullet_delay) > reload_time:
                LIST_BULLET = ShootBullets(LIST_BULLET)
                bullet_delay = time.time()

            temp_bullet_counter = 0
            for bullet in LIST_BULLET:
                delete = False
                bullet.Display(surface)
                delete = bullet.Move(delete)

                if delete == True:
                    del(bullet)
                    LIST_BULLET.pop(temp_bullet_counter)
                temp_bullet_counter += 1

            temp_bullet_counter = 0
            for bullet in LIST_ENEMY_BULLET:
                delete = False
                bullet.Display(surface)
                delete = bullet.Move(delete)

                if bullet.rect.colliderect(player_01.rect):
                    delete = True
                    player_01.hp -= 10

                if delete == True:
                    del(bullet)
                    LIST_ENEMY_BULLET.pop(temp_bullet_counter)
                temp_bullet_counter += 1

            temp_enemy_counter = 0
            for enemy in enemy_pattern_v:
                enemy.Draw(surface)
                enemy.Move("arrow")
                if enemy.rect.colliderect(player_01.rect):
                    player_01.hp -= 10
                    enemy.hp = 0
                delay = 100
                if time.time() - enemy_pattern_v_trigger > 0.9 and random.randint(0, delay) >= delay - 1:
                    LIST_ENEMY_BULLET = EnemyShootBullets(
                        LIST_ENEMY_BULLET, enemy, -15)
                    enemy_pattern_v_trigger = time.time()
                for bullet in LIST_BULLET:
                    if bullet.show == True:
                        if bullet.rect.colliderect(enemy.rect):
                            enemy.hp -= bullet.damage
                            bullet.show = False
                if enemy.hp <= 0:
                    SCORE += 5
                    del(enemy)
                    enemy_pattern_v.pop(temp_enemy_counter)
                elif enemy.rect.y > 600 or enemy.rect.colliderect(player_01.rect):
                    del(enemy)
                    enemy_pattern_v.pop(temp_enemy_counter)
                temp_enemy_counter += 1

            if len(enemy_pattern_v) <= 0:
                x = random.randint(100, 400)
                enemy_pattern_v = EnemyWave1(x, 0, 2)

            temp_enemy_counter = 0
            for enemy in enemy_pattern_rt:
                enemy.Draw(surface)
                enemy.Move("right_tilt")
                if enemy.rect.colliderect(player_01.rect):
                    player_01.hp -= 10
                    enemy.hp = 0
                for bullet in LIST_BULLET:
                    if bullet.show == True:
                        if bullet.rect.colliderect(enemy.rect):
                            enemy.hp -= bullet.damage + 50
                            bullet.show = False
                if enemy.hp <= 0:
                    SCORE += 5
                    del(enemy)
                    enemy_pattern_rt.pop(temp_enemy_counter)
                elif enemy.rect.y > 600:
                    del(enemy)
                    enemy_pattern_rt.pop(temp_enemy_counter)
                temp_enemy_counter += 1

            if len(enemy_pattern_rt) <= 0:
                y = random.randint(0, 350)
                enemy_pattern_rt = EnemyWave2(700, y, 3)

            temp_enemy_counter = 0
            for enemy in enemy_pattern_lt:
                enemy.Draw(surface)
                enemy.Move("left_tilt")
                if enemy.rect.colliderect(player_01.rect):
                    player_01.hp -= 10
                    enemy.hp = 0
                for bullet in LIST_BULLET:
                    if bullet.show == True:
                        if bullet.rect.colliderect(enemy.rect):
                            enemy.hp -= bullet.damage + 50
                            bullet.show = False
                if enemy.hp <= 0:
                    SCORE += 5
                    del(enemy)
                    enemy_pattern_lt.pop(temp_enemy_counter)
                elif enemy.rect.y > 800:
                    del(enemy)
                    enemy_pattern_lt.pop(temp_enemy_counter)
                temp_enemy_counter += 1

            if len(enemy_pattern_lt) <= 0:
                y = random.randint(0, 350)
                enemy_pattern_lt = EnemyWave3(0, y, 3)

            temp_enemy_counter = 0
            for enemy in enemy_pattern_plus:
                enemy.Draw(surface)
                enemy.Move("plus")
                if enemy.rect.colliderect(player_01.rect):
                    player_01.hp -= 10
                    enemy.hp = 0
                delay = 100
                if time.time() - enemy_pattern_v_trigger > 0.9 and random.randint(0, delay) >= delay - 1:
                    LIST_ENEMY_BULLET = EnemyShootBullets(
                        LIST_ENEMY_BULLET, enemy, -15)
                    enemy_pattern_v_trigger = time.time()
                for bullet in LIST_BULLET:
                    if bullet.show == True:
                        if bullet.rect.colliderect(enemy.rect):
                            enemy.hp -= bullet.damage
                            bullet.show = False
                if enemy.hp <= 0:
                    SCORE += 5
                    del(enemy)
                    enemy_pattern_plus.pop(temp_enemy_counter)
                elif enemy.rect.y > 600 or enemy.rect.colliderect(player_01.rect):
                    del(enemy)
                    enemy_pattern_plus.pop(temp_enemy_counter)
                temp_enemy_counter += 1

            if len(enemy_pattern_plus) <= 0:
                x = random.randint(400, 500)
                enemy_pattern_plus = EnemyWave4(x, -200, 5, 5)
        else:
            health_reduce += 1
            player_01.hp = 100/health_reduce
            SCREEN = "menu"

    elif SCREEN == "workshop":
        LoadWorkshopScreen(surface)
        speed, SCORE, reload_time, SCREEN = ButtonClick(
            speed, SCORE, reload_time, SCREEN)
        text = font.render(f"Score: {SCORE}", True, (255, 255, 255))
        surface.blit(text, (525, 10))

    elif SCREEN == "settings":
        LoadSettingsScreen(surface)
        SCREEN = BackButton(SCREEN)

    elif SCREEN == "quit":
        pygame.quit()
        quit()

    FPS.tick(60)
    pygame.display.update()
