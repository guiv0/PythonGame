#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame

from code.const import WINDOW_WIDTH, ENTITY_SPEED
from code.entity import Entity


class Enemy(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.surf = pygame.image.load(f'asset/{name}.png')
        self.surf = pygame.transform.scale(self.surf, (88, 48))
        self.rect = self.surf.get_rect(midleft=position)

    def move(self, ):
        self.rect.centerx -= ENTITY_SPEED[self.name]
        if self.rect.right <= 0:
            self.rect.left = WINDOW_WIDTH
