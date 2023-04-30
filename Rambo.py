import pygame
import os

width = 1000
height = 700


class Rambo:
    pygame.init()

    def __init__(self, x, y):
        super().__init__()
        # self.img = {0: os.path.join("Img", "Rambo", "Run", "0.png"),
        #             1: os.path.join("Img", "Rambo", "Run", "1.png"),
        #             2: os.path.join("Img", "Rambo", "Run", "2.png"),
        #             3: os.path.join("Img", "Rambo", "Run", "3.png"),
        #             4: os.path.join("Img", "Rambo", "Run", "4.png"),
        #             5: os.path.join("Img", "Rambo", "Run", "5.png"),
        #             6: os.path.join("Img", "Rambo", "Run", "6.png"),
        #             7: os.path.join("Img", "Rambo", "Run", "7.png"),
        #             8: os.path.join("Img", "Rambo", "Run", "8.png"),
        #             9: os.path.join("Img", "Rambo", "Run", "9.png"),
        #             'jump': os.path.join("Img", "Rambo", "Jump", "jump.png")}
        # self.gun_img = {0: os.path.join("Img", "Rambo", "Shot", "0.png"),
        #                 1: os.path.join("Img", "Rambo", "Shot", "1.png"),
        #                 2: os.path.join("Img", "Rambo", "Shot", "2.png"),
        #                 3: os.path.join("Img", "Rambo", "Shot", "3.png"),
        #                 4: os.path.join("Img", "Rambo", "Shot", "4.png"),
        #                 5: os.path.join("Img", "Rambo", "Shot", "5.png"),
        #                 6: os.path.join("Img", "Rambo", "Shot", "6.png"),
        #                 7: os.path.join("Img", "Rambo", "Shot", "7.png"),
        #                 8: os.path.join("Img", "Rambo", "Shot", "8.png"),
        #                 9: os.path.join("Img", "Rambo", "Shot", "9.png")}
        # self.hurt_img = {0: os.path.join("Img", "Rambo", "Hurt", "0.png"),
        #                  1: os.path.join("Img", "Rambo", "Hurt", "1.png"),
        #                  2: os.path.join("Img", "Rambo", "Hurt", "2.png"),
        #                  3: os.path.join("Img", "Rambo", "Hurt", "3.png"),
        #                  4: os.path.join("Img", "Rambo", "Hurt", "4.png"),
        #                  5: os.path.join("Img", "Rambo", "Hurt", "5.png"),
        #                  6: os.path.join("Img", "Rambo", "Hurt", "6.png"),
        #                  7: os.path.join("Img", "Rambo", "Hurt", "7.png"),
        #                  8: os.path.join("Img", "Rambo", "Hurt", "8.png"),
        #                  9: os.path.join("Img", "Rambo", "Hurt", "9.png")}

        self.img = {0: r'Img\Rambo\Run\0.png',
                    1: r'Img\Rambo\Run\1.png',
                    2: r'Img\Rambo\Run\2.png',
                    3: r'Img\Rambo\Run\3.png',
                    4: r'Img\Rambo\Run\4.png',
                    5: r'Img\Rambo\Run\5.png',
                    6: r'Img\Rambo\Run\6.png',
                    7: r'Img\Rambo\Run\7.png',
                    8: r'Img\Rambo\Run\8.png',
                    9: r'Img\Rambo\Run\9.png',
                    'jump': r'Img\Rambo\Jump\jump.png'}
        self.gun_img = {0: r'Img\Rambo\Shot\0.png',
                        1: r'Img\Rambo\Shot\1.png',
                        2: r'Img\Rambo\Shot\2.png',
                        3: r'Img\Rambo\Shot\3.png',
                        4: r'Img\Rambo\Shot\4.png',
                        5: r'Img\Rambo\Shot\5.png',
                        6: r'Img\Rambo\Shot\6.png',
                        7: r'Img\Rambo\Shot\7.png',
                        8: r'Img\Rambo\Shot\8.png',
                        9: r'Img\Rambo\Shot\9.png'}
        self.hurt_img = {0: r'Img\Rambo\Hurt\0.png',
                         1: r'Img\Rambo\Hurt\1.png',
                         2: r'Img\Rambo\Hurt\2.png',
                         3: r'Img\Rambo\Hurt\3.png',
                         4: r'Img\Rambo\Hurt\4.png',
                         5: r'Img\Rambo\Hurt\5.png',
                         6: r'Img\Rambo\Hurt\6.png',
                         7: r'Img\Rambo\Hurt\7.png',
                         8: r'Img\Rambo\Hurt\8.png',
                         9: r'Img\Rambo\Hurt\9.png'}
        self.index_gun_img = 0
        self.index_img = 0
        self.index_hurt_img = 0
        self.left = False
        self.jumpCount = 10
        self.jump_vel = 3
        self.jumping = False
        self.left_jumping = False
        self.right_jumping = False
        self.x = x
        self.y = y
        self.width = 113.5
        self.height = 98
        self.vel = 5
        self.moving_left = False
        self.moving_right = False
        self.moving_jump = False
        self.bullets = list()
        self.hp = 5
        self.va_cham_da = False
        self.fallCount = 0
        self.fallDone = True
        self.gunning = False
        self.hurting = False

    def update(self, moving_left, moving_right, moving_jump):
        if moving_left and moving_jump:
            self.left_jumping = True
        elif moving_right and moving_jump:
            self.right_jumping = True
        elif moving_left:
            self.left = True
            self.x -= self.vel
            self.index_img -= 1
        elif moving_right:
            self.left = False
            self.x += self.vel
            self.index_img += 1
        elif moving_jump:
            self.jumping = True

        # Đổi index ảnh khi di chuyển
        if self.index_img < 0:
            self.index_img = 9
        if self.index_img > 9:
            self.index_img = 0

        # Giới hạn màn hìhh
        if self.x < self.vel:
            self.x = 0
        if self.x > width - self.width:
            self.x = width - self.width
        if self.y < self.vel:
            self.y = 0
        if self.y > height - self.width - 125:
            self.y = height - self.width - 125

    def jump(self):
        if self.jumpCount >= -10:
            self.y -= (self.jumpCount * abs(self.jumpCount)) * 0.25
            self.jumpCount -= 0.5
        else:
            self.jumping = False
            self.jumpCount = 10

    def fall(self):
        if self.fallCount >= -10:
            self.y -= (self.fallCount * abs(self.fallCount)) * 0.25
            self.fallCount -= 0.5
        else:
            self.fallDone = True
            self.fallCount = 0
        if self.y > height - self.width - 125:
            self.y = height - self.width - 125

    def left_jump(self):
        if self.jumpCount >= -10:
            if self.va_cham_da and self.jumpCount <= 2:
                self.x -= 0
            else:
                self.x -= 3
            self.y -= (self.jumpCount * abs(self.jumpCount)) * 0.25
            self.jumpCount -= 0.5
        else:
            self.left_jumping = False
            self.jumpCount = 10

    def right_jump(self):
        if self.jumpCount >= -10:
            if self.va_cham_da and self.jumpCount <= 2:
                self.x += 0
            else:
                self.x += 3
            self.y -= (self.jumpCount * abs(self.jumpCount)) * 0.25
            self.jumpCount -= 0.5
        else:
            self.right_jumping = False
            self.jumpCount = 10

    def gunning_image(self):
        self.index_gun_img += 1
        if self.index_gun_img > 9:
            self.index_gun_img = 0
            self.gunning = False

    def hurting_image(self):
        self.index_hurt_img += 1
        if self.index_hurt_img > 9:
            self.index_hurt_img = 0
            self.hurting = False

    def reset(self):
        self.index_img = 0
        self.left = False
        self.jumpCount = 10
        self.jump_vel = 3
        self.jumping = False
        self.left_jumping = False
        self.right_jumping = False
        self.width = 113.5
        self.height = 98
        self.vel = 5
        self.moving_left = False
        self.moving_right = False
        self.moving_jump = False
        self.bullets.clear()
        self.hp = 5
