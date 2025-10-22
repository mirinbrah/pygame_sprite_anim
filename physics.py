import pygame
from settings import GRAVITY, SCREEN_HEIGHT, SCREEN_WIDTH


class PhysicsObject(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)
        self.image = None
        self.rect = None
        self.velocity = pygame.math.Vector2(0, 0)
        self.gravity = GRAVITY
        self.is_on_ground = False

    def apply_gravity(self):
        self.velocity.y += self.gravity

    def update_physics(self):
        if self.rect is None:
            raise NotImplementedError("Дочерний класс должен определить self.rect")

        self.apply_gravity()
        self.rect.x += self.velocity.x

        self.is_on_ground = False
        self.rect.y += self.velocity.y

        if self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT
            self.velocity.y = 0
            self.is_on_ground = True

        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH