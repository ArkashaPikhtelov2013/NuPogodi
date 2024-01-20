import pygame
import sys
import os


def load_image(name, colorkey=None):
    fullname = 'data1/' + name
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image


class Wolf(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.r = True
        self.armup = False
        self.image = load_image('player/right.png')
        self.armimage = load_image('arm/right_down.png')
        self.wx = None
        self.army = None
        self.pos = 4

    def update(self):
        if self.r:
            self.image = load_image('player/right.png')
            self.wx = 584
            self.armx = self.wx + 80
            if not self.armup:
                self.armimage = load_image('arm/right_down.png')
                self.army = 300
            elif self.armup:
                self.armimage = load_image('arm/right_up.png')
                self.army = 240
            self.armrect = self.armimage.get_rect(center=(self.armx, self.army))
        if not self.r:
            self.image = load_image('player/left.png')
            self.wx = 414
            self.armx = self.wx - 80
            if not self.armup:
                self.armimage = load_image('arm/left_down.png')
                self.army = 300
            elif self.armup:
                self.armimage = load_image('arm/left_up.png')
                self.army = 240
            self.armrect = self.armimage.get_rect(center=(self.armx, self.army))
        self.rectangle = self.image.get_rect(center=(self.wx, 300))
