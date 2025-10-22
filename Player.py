import pygame
from PhysicsObject import PhysicsObject
from settings import PLAYER_SPEED, SCREEN_HEIGHT, JUMP_STRENGTH


class Player(PhysicsObject):
    def __init__(self, pos, animator, *groups):
        super().__init__(*groups)
        self.animator = animator
        self.image = self.animator.image
        self.rect = self.image.get_rect(center=pos)

    def get_input(self):
        keys = pygame.key.get_pressed()
        self.velocity.x = 0

        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.velocity.x = -PLAYER_SPEED
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.velocity.x = PLAYER_SPEED

        if keys[pygame.K_SPACE] or keys[pygame.K_w]:
            self.jump()

    def jump(self):
        if self.rect.bottom >= SCREEN_HEIGHT:
            self.velocity.y = JUMP_STRENGTH

    def update(self):
        self.get_input()
        self.update_physics()
        self.animator.update()
        self.image = self.animator.image