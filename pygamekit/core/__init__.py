from pygamekit.utilities import format_duration
from functools import wraps
from typing import Callable
import pygame
import time
import sys


class Window:
    def __init__(
        self,
        width: int = 1280,
        height: int = 720,
        title: str = None,
        backgroud: tuple = (0, 0, 0),
    ):
        self.width = width
        self.height = height
        self.title = title or sys.argv[0].split("/")[-1]
        self.backgroud = backgroud

        self.running = True

        self.events = []

        pygame.display.set_caption(self.title)
        self.screen = pygame.display.set_mode((self.width, self.height))

        self.clock = pygame.time.Clock()
        self.tick = 0


    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                self.running = False

    def open(self):
        pygame.display.update()

    def clear(self):
        self.screen.fill(self.backgroud)

    def update(self):
        pygame.display.update()

    def run(self):
        while self.running:
            # print(self.events)
            # self.clear()
            # self.update()
            for event in self.events:
                if event["mono"] <= time.monotonic():
                    event["function"]()
                    self.events.remove(event)
                    self.events.append(
                        {**event, **{"mono": time.monotonic() + event["delay"]}}
                    )
            # self.handle_events()

    def schedule(self, delay: float, func: Callable):
        if isinstance(delay, str):
            delay = format_duration(delay)

        self.events.append(
            {
                "mono": 0,
                "delay": delay,
                "function": func,
            }
        )

    def schedule_every(self, delay: float):
        def decorator(func):
            @wraps(func)
            def wrapper(delay, *args, **kwargs):
                self.schedule(delay, func)

            return wrapper(delay)

        return decorator
