import pygame
from settings import GRAVITY, SCREEN_HEIGHT  # <-- Убедитесь, что settings.py создан


class PhysicsObject(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)
        self.velocity = pygame.math.Vector2(0, 0)
        self.gravity = GRAVITY
        self.is_on_ground = False
        # Добавляем rect и image как заглушки, чтобы избежать ошибок
        # self.image = pygame.Surface((0, 0))
        # self.rect = self.image.get_rect()

    def apply_gravity(self):
        self.velocity.y += self.gravity

    def update_physics(self):

        self.apply_gravity()
        self.rect.x += self.velocity.x

        self.is_on_ground = False
        self.rect.y += self.velocity.y

        if self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT
            self.velocity.y = 0
            self.is_on_ground = True