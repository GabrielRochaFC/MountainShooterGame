#!/usr/bin/python
# -*- coding: utf-8 -*-
from code.Const import ENTITY_SPEED, ENTITY_SHOT_DELAY, WIN_HEIGHT
from code.EnemyShot import EnemyShot
from code.Entity import Entity


class Enemy(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.shot_delay = ENTITY_SHOT_DELAY[self.name]

        if self.name == 'Enemy3':
            self.y_direction = -1  # Começa subindo

    def move(self):
        if self.name != 'Enemy3':
            self.rect.centerx -= ENTITY_SPEED[self.name]
        else:
            self.rect.centerx -= ENTITY_SPEED[self.name]

            if self.y_direction == -1:  # Movendo para cima
                self.rect.centery += ENTITY_SPEED[self.name] * self.y_direction
            else:  # Movendo para baixo
                self.rect.centery += ENTITY_SPEED[self.name] * 2 * self.y_direction

            if self.rect.top <= 0:
                self.y_direction = 1  # Muda para descer
            elif self.rect.bottom >= WIN_HEIGHT:
                self.y_direction = -1  # Muda para subir

    def shoot(self):
        self.shot_delay -= 1
        if self.shot_delay == 0:
            self.shot_delay = ENTITY_SHOT_DELAY[self.name]
            return EnemyShot(name=f'{self.name}Shot', position=(self.rect.centerx, self.rect.centery))
