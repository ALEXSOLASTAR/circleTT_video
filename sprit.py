import pygame

class MyCircleSprite(pygame.sprite.Sprite):
    def __init__(self, color, x, y, radius, speed, direction, m):
        super().__init__()
        self.m = m
        self.x = x
        self.y = y
        self.image = pygame.Surface((radius * 2, radius * 2), pygame.SRCALPHA)
        pygame.draw.circle(self.image, color, (radius, radius), radius)
        self.rect = self.image.get_rect(center=(self.x, self.y))
        self.speed = speed
        self.direction = direction

    def update(self, left_border, width):
        if self.direction == "rith":
            self.x += self.speed
            self.rect = self.image.get_rect(center=(self.x, self.y))
            if self.rect.x + self.rect.width >= width:
                self.direction = "left"
                self.m.play()
        elif self.direction == "left":
            self.x -= self.speed
            self.rect = self.image.get_rect(center=(self.x, self.y))
            if self.rect.x <= left_border:
                self.direction = "rith"
                self.m.play()
