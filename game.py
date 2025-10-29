import pygame
import sys
from player import Player
from settings import SCREEN_WIDTH, SCREEN_HEIGHT


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()

        self.all_sprites = pygame.sprite.Group()
        self.player = Player(130, 120, self.all_sprites)


    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    self.player.attack()  # Вызываем метод атаки

            self.all_sprites.update()

            self.screen.fill((0, 0, 0))
            self.all_sprites.draw(self.screen)

            pygame.display.flip()
            self.clock.tick(60)


