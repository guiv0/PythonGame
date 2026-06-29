#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame

from code.EnemyShot import EnemyShot
from code.const import ENTITY_SPEED, ENTITY_SHOT_DELAY
from code.entity import Entity


class Enemy(Entity):

    def __init__(self, name, position):
        super().__init__(name, position)

        self.shot_delay = ENTITY_SHOT_DELAY[self.name]

        self.frame_width = 100
        self.frame_height = 100

        self.animation_speed = 5
        self.animation_timer = 0
        self.current_frame = 0

        self.state = "fly"

        animation_config = {
            "Enemy1": {
                "fly": 11,
                "attack": 11,
                "hurt": 3,
                "death": 4
            },

            "Enemy2": {
                "fly": 8,
                "attack": 8,
                "hurt": 4,
                "death": 4
            }
        }

        config = animation_config[name]

        self.animations = {
            state: self.load_sheet(
                f"{name}_{state}",
                frames
            )
            for state, frames in config.items()
        }

        self.surf = self.animations[self.state][0]
        self.rect = self.surf.get_rect(midleft=position)

    def load_sheet(self, file, frame_count):

        sheet = pygame.image.load(
            f"asset/{file}.png"
        ).convert_alpha()

        frame_width = sheet.get_width() // frame_count
        frame_height = sheet.get_height()

        frames = []

        for i in range(frame_count):
            frame = pygame.Surface(
                (frame_width, frame_height),
                pygame.SRCALPHA
            )

            frame.blit(
                sheet,
                (0, 0),
                (
                    i * frame_width,
                    0,
                    frame_width,
                    frame_height
                )
            )

            frame = pygame.transform.scale(
                frame,
                (88, 48)
            )
            frame = pygame.transform.flip(
                frame,
                True,
                False
            )

            frames.append(frame)

        return frames

    def set_state(self, state):

        if state != self.state:
            self.state = state
            self.current_frame = 0

    def animate(self):

        frames = self.animations[self.state]

        self.animation_timer += 1

        if self.animation_timer >= self.animation_speed:

            self.animation_timer = 0
            self.current_frame += 1

            if self.current_frame >= len(frames):

                if self.state == "death":
                    self.health = 0
                    return

                self.current_frame = 0

                if self.state in ["attack", "hurt"]:
                    self.state = "fly"
                    frames = self.animations["fly"]

        self.surf = frames[self.current_frame]

    def move(self):

        if self.state != "death":
            self.rect.centerx -= ENTITY_SPEED[self.name]

        self.animate()

    def shoot(self):

        self.shot_delay -= 1

        if self.shot_delay <= 0:
            self.shot_delay = ENTITY_SHOT_DELAY[self.name]

            self.set_state("attack")

            return EnemyShot(
                name=f"{self.name}Shot",
                position=(
                    self.rect.centerx,
                    self.rect.centery
                )
            )

        return None
