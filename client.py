import pygame
import Bullet
from network import Network
from Step import Step

pygame.mixer.init()
pygame.font.init()

width = 1000
height = 700
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Client")


#Path

# Khai báo background
background = pygame.image.load(r'Img\background.png')
background = pygame.transform.scale(background, (width, height))
step1 = Step(150, 400)
step2 = Step(600, 400)
# Khai báo âm thanh
ban_sound = pygame.mixer.Sound(r'Sound\Ban.mp3')
bi_ban_sound = pygame.mixer.Sound(r'Sound\BiBan.mp3')
nhay_sound = pygame.mixer.Sound(r'Sound\Nhay.mp3')
napdan_sound = pygame.mixer.Sound(r'Sound\NapDan.mp3')

def redrawWindow(win, game, p, n):
    win.fill((128, 128, 128))
    if not (game.connected()):
        font = pygame.font.SysFont("comicsans", 80)
        text = font.render("Waiting for Player...", 1, (255, 0, 0), True)
        win.blit(text, (width / 2 - text.get_width() / 2, height / 2 - text.get_height() / 2))

    else:
        win.blit(background, (0, 0))
        win.blit(step1.step, (step1.x, step1.y))
        win.blit(step2.step, (step2.x, step2.y))

        s = "Your HP: " + str(game.players[p].hp)
        font = pygame.font.SysFont("comicsans", 50)
        text = font.render(s, 1, (255, 0, 0), True)
        win.blit(text, (700, 10))

        players_surface = list()
        players_rect = list()

        for i in range(0, len(game.players)):
            if game.players[i].jumping:
                surface = pygame.image.load(str(game.players[i].img['jump']))
                players_surface.append(surface)
            elif game.players[i].gunning:
                surface = pygame.image.load(str(game.players[i].gun_img[game.players[i].index_gun_img]))
                players_surface.append(surface)
            elif game.players[i].hurting:
                surface = pygame.image.load(str(game.players[i].hurt_img[game.players[i].index_hurt_img]))
                players_surface.append(surface)
            else:
                surface = pygame.image.load(str(game.players[i].img[game.players[i].index_img]))
                players_surface.append(surface)
            players_surface[i] = pygame.transform.scale(players_surface[i], (game.players[i].width, game.players[i].height))

            if game.players[i].left:
                players_surface[i] = pygame.transform.flip(players_surface[i], True, False)
            rect = players_surface[i].get_rect()
            players_rect.append(rect)
            players_rect[i].x = game.players[i].x
            players_rect[i].y = game.players[i].y
        for i in range(0, len(game.players)):
            win.blit(players_surface[i], (game.players[i].x, game.players[i].y))
        if p == 0:
            if not game.players[0].va_cham_da and players_rect[0].x + 60.5 >= 150 and players_rect[0].x < 276.3 and players_rect[0].y < 304:
                print("va cham da")
                n.send("va_cham_da")
            elif game.players[0].va_cham_da and (players_rect[0].x + 60.5 < 150 or players_rect[0].x >= 276.3 ):
                print("het va cham da")
                n.send("het_va_cham_da")
        if p == 1:
            if not game.players[1].va_cham_da and players_rect[1].x + 60.5 >= 600 and players_rect[1].x < 726.3 and players_rect[1].y < 304:
                print("va cham da")
                n.send("va_cham_da")
            elif game.players[1].va_cham_da and (
                    players_rect[1].x + 60.5 < 600 or players_rect[1].x >= 726.3):
                print("het va cham da")
                n.send("het_va_cham_da")

        drawBullet(game.players, players_rect, p, n)

    pygame.display.update()


def drawBullet(players, players_rect, p, n):
    for player in players:
        index_player = players.index(player)
        for bullet in player.bullets:
            bullet_surface = pygame.image.load(Bullet.Bullet.getImg())
            bullet_surface = pygame.transform.scale(bullet_surface, (bullet.width, bullet.height))
            if bullet.left:
                bullet_surface = pygame.transform.flip(bullet_surface, True, False)
            bullet_rect = bullet_surface.get_rect()
            bullet_rect.x, bullet_rect.y = bullet.x, bullet.y
            win.blit(bullet_surface, (bullet.x, bullet.y))
            print("Toa do dan la: ", bullet.x, bullet.y)
            for player_rect in players_rect:
                if bullet_rect.colliderect(player_rect):
                    index_rect = players_rect.index(player_rect)
                    if index_rect != index_player and p == index_rect:
                        n.send("bi_ban_boi_dan_" + str(bullet.id))
                        bi_ban_sound.play()


def main():
    run = True
    clock = pygame.time.Clock()
    n = Network()

    player = int(n.getP())
    print("You are player", player)

    while run:
        clock.tick(30)
        try:
            # print("Chuan bi game = n.send('get')")
            game = n.send("get")
            # print("Da game = n.send('get') xong")
        except:
            print("Couldn't get game")
            break
        if game.playerWin != -1:
            font = pygame.font.SysFont("comicsans", 60)
            win_text = font.render("You Win", 1, (0, 0, 0))
            lose_text = font.render("You Lose", 1, (0, 0, 0))
            for i in range(0, len(game.players)):
                if game.playerWin == player:
                    win.blit(win_text, (100, 350))
                else:
                    win.blit(lose_text, (100, 350))
            pygame.display.update()
            print("Da update -----------")
            pygame.time.delay(4000)
            return
        action = ""
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            action = "left"
        elif keys[pygame.K_RIGHT]:
            action = "right"

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    action = "un_left"
                elif event.key == pygame.K_RIGHT:
                    action = "un_right"
                elif event.key == pygame.K_UP:
                    action = "un_jump"
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    if keys[pygame.K_LEFT]:
                        action = "left_jump"
                        nhay_sound.play()
                        print("nhay sang trai")

                    elif keys[pygame.K_RIGHT]:
                        action = "right_jump"
                        nhay_sound.play()
                        print("nhay sang phai")
                    else:
                        action = "jump"
                        nhay_sound.play()
                if event.key == pygame.K_s:
                    action = "shoot"
                    current_player = game.players[player]
                    if len(current_player.bullets) < 2:
                        ban_sound.play()
                    else:
                        napdan_sound.play()
        if action != "" and game.connected():
            n.send(action)
        redrawWindow(win, game, player, n)


def menu_screen():
    run = True
    clock = pygame.time.Clock()
    while run:
        clock.tick(30)
        # Vẽ background
        win.blit(background, (0, 0))
        win.blit(step1.step, (step1.x, step1.y))
        win.blit(step2.step, (step2.x, step2.y))

        font = pygame.font.SysFont("comicsans", 60)
        text = font.render("Click to Play!", 1, (255, 0, 0))
        win.blit(text, (100, 200))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                run = False

    main()


while True:
    menu_screen()
