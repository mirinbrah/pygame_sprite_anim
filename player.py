import pygame
from physics import PhysicsObject  # <-- Наследуемся отсюда
from animator import Animator
from settings import PLAYER_SPEED, JUMP_STRENGTH


class Player(PhysicsObject):  # <-- Наследуемся от PhysicsObject
    def __init__(self, pos_x, pos_y, *groups):  # <-- Добавили *groups
        # Передаем группы спрайтов родительскому классу! Это ключевой момент.
        super().__init__(*groups)

        # Загружаем спрайты как и раньше
        attack_sprites = [pygame.image.load(f'src/enemy/attack/enemy_attack_{i}.png') for i in range(7)]
        self.animator = Animator(attack_sprites, animation_speed=0.2)

        # Обновляем image и rect, которые были созданы в PhysicsObject
        self.image = self.animator.image
        self.rect = self.image.get_rect(topleft=(pos_x, pos_y))

    def get_input(self):
        self.velocity.x = 0
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.velocity.x = -PLAYER_SPEED
        if keys[pygame.K_d]:
            self.velocity.x = PLAYER_SPEED
        if keys[pygame.K_SPACE] or keys[pygame.K_w]:
            self.jump()

    def jump(self):
        if self.is_on_ground:
            self.velocity.y = JUMP_STRENGTH

    def attack(self):
        self.animator.start_animation()

    def update(self):
        self.get_input()  # <-- Получаем ввод
        self.update_physics()  # <-- Применяем физику из родителя

        # Обновляем анимацию
        self.animator.update()
        # Важно: обновляем свой image из аниматора ПОСЛЕ всех расчетов
        old_center = self.rect.center
        self.image = self.animator.image
        self.rect = self.image.get_rect(center=old_center)  # Центрируем, чтобы не дергался