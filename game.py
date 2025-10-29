import pygame
import sys
from settings import *
from player import Player  # Убедитесь, что импортируете исправленный Player
from animator import Animator


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()
        self.is_running = True

        self.all_sprites = pygame.sprite.Group()

        animations = {}
        animation_data = {
            'idle': 10,
            'run': 16,
            'attack': 7,
        }

        for anim_name, frame_count in animation_data.items():
            frames = []
            for i in range(frame_count):
                path = f'src/player/{anim_name}/player_{anim_name}_{i}.png'
                image = pygame.image.load(path).convert_alpha()
                frames.append(image)

            animations[anim_name] = frames

        player_animator = Animator(animations, initial_state='idle', animation_speed=0.2)
        start_pos = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
        self.player = Player(start_pos, player_animator, PLAYER_SCALE, self.all_sprites)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                self.is_running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_k:
                    self.player.attack()

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