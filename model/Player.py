import pygame


class Player:
    def __init__(self, x, y, sprite):
        self.x = x
        self.y = y
        self.sprite = pygame.image.load(sprite)
        self.sprite = pygame.transform.scale(self.sprite, (50, 50))

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def render(self, screen):
        screen.blit(self.sprite, (self.x, self.y))
