import pygame
from Wolf import load_image


class Health(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.health = 3
        self.image = load_image('health/fullhealth.png')
        self.rectangle = self.image.get_rect(center=(500, 70))
        self.gameover = False

    def update(self):
        if self.health == 3:
            self.image = load_image('health/fullhealth.png')
        elif self.health == 2:
            self.image = load_image('health/-1.png')
        elif self.health == 1:
            self.image = load_image('health/-2.png')
        else:
            self.image = load_image("health/gameover.png")
            self.gameover = True


class Misses(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.missfile = load_image('health/miss.png')
        self.missvisible = 0
        self.center = None
        self.rect = (-1000, -1000)
        if pos == 1:
            self.center = (281, 228 + 83)
            self.rect = self.missfile.get_rect(center=self.center)
        elif pos == 2:
            self.center = (294, 228)
            self.rect = self.missfile.get_rect(center=self.center)
        elif pos == 3:
            self.center = (710, 228)
            self.rect = self.missfile.get_rect(center=self.center)
        elif pos == 4:
            self.center = (716, 315)
            self.rect = self.missfile.get_rect(center=self.center)

    def update(self):
        if self.missvisible == 35:
            self.rect = (-1000, -1000)
            self.missvisible = 0
        else:
            self.missvisible += 1
