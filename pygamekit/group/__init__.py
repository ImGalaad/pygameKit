import pygame

class Group:
    def __init__(self):
        self.items = []
    
    def add(self, item):
        self.items.append(item)

    def remove(self, item):
        self.items.remove(item)

    def update(self):
        for item in self.items:
            try:
                item.update()
            except:
                pass

    def draw(self, surface):
        for item in self.items:
            try:
                item.draw(surface)
            except:
                pass