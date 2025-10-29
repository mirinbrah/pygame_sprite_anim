import pygame
from physics import PhysicsObject
from settings import PLAYER_SPEED, JUMP_STRENGTH, PLAYER_SCALE
from animator import Animator


class Player(PhysicsObject):
    def __init__(self, pos, scale , *groups):
        super().__init__(*groups)

        self.animations = self._load_animations()
        self.animator = Animator(self.animations, initial_state='idle', animation_speed=0.2)
        self.scale = scale
        self.direction = 1  # 1 - вправо, -1 - влево
        self.is_attacking = False
        self.image = pygame.Surface((0, 0))
        self.rect = self.image.get_rect(center=pos)
        self._update_graphics()

    @staticmethod
    def _load_animations():
        animations = {}
        animation_data = {
            'idle': 10,
            'run': 16,
            'attack': 7,
        }

        base_path = 'src/player/'

        for anim_name, frame_count in animation_data.items():
            frames = []
            for i in range(frame_count):
                path = f'{base_path}{anim_name}/player_{anim_name}_{i}.png'
                try:
                    image = pygame.image.load(path).convert_alpha()
                    frames.append(image)
                except pygame.error as e:
                    print(f"Ошибка загрузки изображения: {path}")
                    print(e)
            animations[anim_name] = frames

        return animations

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
            if 'jump' in self.animator.animations:
                self.animator.set_animation('jump')
            else:
                self.animator.set_animation('idle')  # Запасной вариант
        elif self.velocity.x != 0:
            self.animator.set_animation('run')
        else:
            self.animator.set_animation('idle')

    def _update_graphics(self):
        original_image = self.animator.image

        new_size = (int(original_image.get_width() * self.scale),
                    int(original_image.get_height() * self.scale))
        scaled_image = pygame.transform.scale(original_image, new_size)

        if self.direction == -1:
            self.image = pygame.transform.flip(scaled_image, True, False)
        else:
            self.image = scaled_image

        old_center = self.rect.center
        self.rect = self.image.get_rect(center=old_center)

    def update(self):
        self.get_input()
        self.update_physics()
        self.set_animation_state()

        self.animator.update()
        if self.is_attacking and self.animator.is_animation_finished():
            self.is_attacking = False

        self._update_graphics()