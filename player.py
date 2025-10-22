import pygame
from physics import PhysicsObject
from settings import PLAYER_SPEED, JUMP_STRENGTH


class Player(PhysicsObject):
    def __init__(self, pos, animator, *groups):
        super().__init__(*groups)
        self.animator = animator
        self.image = self.animator.image
        self.rect = self.image.get_rect(center=pos)
        self.direction = 1  # 1 - вправо, -1 - влево
        self.is_attacking = False

    def get_input(self):
        if self.is_attacking:
            return

        keys = pygame.key.get_pressed()
        self.velocity.x = 0

        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.velocity.x = -PLAYER_SPEED
            self.direction = -1
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.velocity.x = PLAYER_SPEED
            self.direction = 1

        if keys[pygame.K_SPACE] or keys[pygame.K_w]:
            self.jump()

    def jump(self):
        if self.is_on_ground:
            self.velocity.y = JUMP_STRENGTH

    def attack(self):
        if not self.is_attacking:
            self.is_attacking = True
            self.animator.set_animation('attack')

    def set_animation_state(self):
        if self.is_attacking:
            return

        if not self.is_on_ground:
            # Need jump animation
            self.animator.set_animation('idle')
        elif self.velocity.x != 0:
            self.animator.set_animation('run')
        else:
            self.animator.set_animation('idle')

    def update(self):
        self.get_input()
        self.update_physics()
        self.set_animation_state()

        self.animator.update()
        if self.is_attacking and self.animator.is_animation_finished():
            self.is_attacking = False

        self.image = self.animator.image
        if self.direction == -1:
            self.image = pygame.transform.flip(self.image, True, False)