import pygame
from animator import Animator  # <-- Импортируем новый класс


class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()

        attack_sprites = [pygame.image.load(f'src/enemy/attack/enemy_attack_{i}.png') for i in range(7)]

        self.animator = Animator(attack_sprites, animation_speed=0.2)
        self.image = self.animator.image

        self.rect = self.image.get_rect()
        self.rect.topleft = (pos_x, pos_y)

    def update(self):
        self.animator.update()
        self.image = self.animator.image  # Обновляем свою картинку из аниматора

    def attack(self):
        self.animator.start_animation()