import sys

import pygame

from Player import Player
from animator import Animator
from settings import TITLE, SCREEN_WIDTH, SCREEN_HEIGHT, BLACK, FPS


class Game:

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()
        self.is_running = True
        self.all_sprites = pygame.sprite.Group()

        player_animation_frames = [
            pygame.image.load(f'src/enemy/attack/enemy_attack_{i}.png').convert_alpha()
            for i in range(7)
        ]

        player_animator = Animator(sprites=player_animation_frames, animation_speed=0.2)
        start_pos = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

        self.player = Player(start_pos, player_animator, self.all_sprites)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                self.is_running = False

    def update(self):
        self.all_sprites.update()

    def draw(self):
        self.screen.fill(BLACK)
        self.all_sprites.draw(self.screen)
        pygame.display.flip()

    def run(self):
        while self.is_running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(FPS)

        pygame.quit()
        sys.exit()