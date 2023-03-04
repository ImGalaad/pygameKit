import pygame


class Circle:
    def __init__(self, x: int, y: int, radius: int, color, centered: bool = True):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.centered = centered

    def draw(self, surface):
        x = self.x
        y = self.y
        if self.centered:
            x -= self.radius
            y -= self.radius
        pygame.draw.circle(surface, self.color, (x, y), self.radius)
