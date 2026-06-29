#!/usr/bin/python
# -*- coding: utf-8 -*-
import random
import sys

import pygame.display
from pygame import Surface, Rect
from pygame.font import Font

from code.EntityMediator import EntityMediator
from code.const import C_L_CREAM, WIN_HEIGHT, MENU_OPTION, EVENT_ENEMY, SPAWN_TIME, C_GREEN, C_CYAN, EVENT_TIMEOUT, \
    TIMEOUT_STEP, TIMEOUT_LEVEL
from code.enemy import Enemy
from code.entity import Entity
from code.entityFactory import EntityFactory
from code.player import Player


class Level:
    def __init__(self, window: Surface, name: str, game_mode: str, player_score: list[int]):
        self.window = window
        self.name = name
        self.game_mode = game_mode
        self.timeout = TIMEOUT_LEVEL
        self.player_score_ref = player_score

        self.entity_list: list[Entity] = []

        bg_name = (self.name + 'Bg').replace(' ', '')
        self.entity_list.extend(EntityFactory.get_entity(bg_name))

        player = EntityFactory.get_entity('Player1')
        player.score = player_score[0]
        self.entity_list.append(player)
        self.text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=14)

        if game_mode in [MENU_OPTION[1]]:
            player2 = EntityFactory.get_entity('Player2')
            player2.score = player_score[1]
            self.entity_list.append(player2)

        pygame.time.set_timer(EVENT_ENEMY, SPAWN_TIME)
        pygame.time.set_timer(EVENT_TIMEOUT, TIMEOUT_STEP)

    def _save_scores(self):
        for ent in self.entity_list:
            if isinstance(ent, Player):
                if ent.name == 'Player1':
                    self.player_score_ref[0] = ent.score
                elif ent.name == 'Player2':
                    self.player_score_ref[1] = ent.score

    def run(self):
        pygame.mixer_music.load(f'./asset/{self.name}.mp3')
        pygame.mixer_music.play(-1)
        clock = pygame.time.Clock()

        while True:
            clock.tick(60)

            self.window.fill((0, 0, 0))
            new_shots = []

            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move()

                if isinstance(ent, (Player, Enemy)):
                    shoot = ent.shoot()
                    if shoot is not None:
                        new_shots.append(shoot)

                if ent.name == 'Player1':
                    self.level_text(f'Player1 - Health: {ent.health} | Score: {ent.score}', C_GREEN, (10, 20))
                if ent.name == 'Player2':
                    self.level_text(f'Player2 - Health: {ent.health} | Score: {ent.score}', C_CYAN, (10, 40))

            self.entity_list.extend(new_shots)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == EVENT_ENEMY:
                    choice = random.choice(('Enemy1', 'Enemy2'))
                    self.entity_list.append(EntityFactory.get_entity(choice))

                if event.type == EVENT_TIMEOUT:
                    self.timeout -= TIMEOUT_STEP
                    if self.timeout <= 0:
                        self._save_scores()  # Salva pontos obtidos ao vencer
                        pygame.time.set_timer(EVENT_ENEMY, 0)  # Limpa o timer ao sair
                        pygame.time.set_timer(EVENT_TIMEOUT, 0)  # Limpa o timer ao sair
                        return True

            found_player = False
            for ent in self.entity_list:
                if isinstance(ent, Player):
                    found_player = True
                    break

            if not found_player:
                self._save_scores()  # Salva pontos acumulados mesmo se morrer
                pygame.time.set_timer(EVENT_ENEMY, 0)  # Limpa o timer ao sair
                pygame.time.set_timer(EVENT_TIMEOUT, 0)  # Limpa o timer ao sair
                return False

            self.level_text(f'{self.name} - Timeout: {self.timeout / 1000 :.1f}s', C_L_CREAM, (10, 5))
            self.level_text(f'FPS: {clock.get_fps():.1f}', C_L_CREAM, (10, WIN_HEIGHT - 35))
            self.level_text(f'Entities: {len(self.entity_list)}', C_L_CREAM, (10, WIN_HEIGHT - 20))

            pygame.display.flip()

            EntityMediator.verify_collision(entity_list=self.entity_list)
            EntityMediator.verify_health(entity_list=self.entity_list)

    def level_text(self, text: str, text_color: tuple, text_pos: tuple):
        text_surf: Surface = self.text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(source=text_surf, dest=text_rect)
