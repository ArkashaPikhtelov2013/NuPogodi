import pygame
from Wolf import load_image


class Eggs(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.coords = []
        self.image = load_image('eggs.png')
        self.pos = pos
        self.rectangle = 0
        self.rimage = None

        if self.pos == 2:
            self.centers = [(204, 176),
                            (221, 187),
                            (232, 193),
                            (245, 199),
                            (258, 208),
                            (269, 216),
                            (281, 220),
                            (294, 228),
                            (0, 0)]
        elif self.pos == 3:
            self.centers = [(800, 175),
                            (788, 185),
                            (776, 195),
                            (764, 200),
                            (752, 205),
                            (740, 210),
                            (728, 215),
                            (710, 228),
                            (0, 0)]
        elif self.pos == 1:
            self.centers = [(204, 176 + 90),
                            (215, 187 + 90),
                            (226, 193 + 90),
                            (237, 199 + 90),
                            (248, 208 + 90),
                            (259, 216 + 87),
                            (270, 220 + 85),
                            (281, 228 + 83),
                            (0, 0)]
        elif self.pos == 4:
            self.centers = [(800, 270),
                            (788, 275),
                            (776, 283),
                            (764, 295),
                            (752, 298),
                            (740, 302),
                            (728, 308),
                            (716, 315),
                            (0, 0)]

    def update(self, ci):
        x, y = self.centers[ci - 1][0], self.centers[ci - 1][-1]
        if self.pos == 1 or self.pos == 2:
            self.rimage = pygame.transform.rotate(self.image, 315 * ci)
        else:
            self.rimage = pygame.transform.rotate(self.image, 45 * ci)
        self.rectangle = self.rimage.get_rect(center=(x, y))
