from pygame import font
from pygame.sprite import Sprite


class Label(Sprite):
    def __init__(
        self,
        text: str = "Hello World",
        font_name: str = None,
        font_size: int = 30,
        x: int = 0,
        y: int = 0,
        color: tuple = (255, 255, 255),
        anchor_x: str = "left",
        anchor_y: str = "top",
    ):
        super().__init__()
        self.text = text
        self.font = font.Font(font_name, font_size)
        self.color = color
        self.anchor_x = anchor_x
        self.anchor_y = anchor_y
        self.update_image()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update_image(self):
        self.image = self.font.render(self.text, True, self.color)

    def draw(self, surf):
        if self.anchor_x == "left":
            x = self.rect.x
        elif self.anchor_x == "center":
            x = self.rect.centerx
        elif self.anchor_x == "right":
            x = self.rect.right

        if self.anchor_y == "top":
            y = self.rect.y
        elif self.anchor_y == "center":
            y = self.rect.centery
        elif self.anchor_y == "bottom":
            y = self.rect.bottom

        surf.screen.blit(self.image, (x, y))