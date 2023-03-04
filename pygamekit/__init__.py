# coding: ascii
# pygame tools
# Copyright (C) 2023 Galaad
import pygame

pygame.init()

__version__ = "0.1.0"

from .core import *
from .text import Label

print("""
pygamekit {}
Our library built around Pygame offers additional help to developers who want to make the most of this platform.""".format(__version__))