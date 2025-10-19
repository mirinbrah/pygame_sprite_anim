import pygame
import sys

class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()

        self.sprites = [pygame.image.load(f'src/enemy/attack/enemy_attack_{i}.png') for i in range(7)]
        self.current_sprite = 0.0
        self.animation_speed = 0.2
        self.image = self.sprites[int(self.current_sprite)]

        self.rect = self.image.get_rect()
        self.rect.topleft = (pos_x, pos_y)
        self.is_animating = False

    def update(self):
        if self.is_animating:
            self.current_sprite += self.animation_speed

            if self.current_sprite >= len(self.sprites):
                self.current_sprite = 0
                self.is_animating = False

            self.image = self.sprites[int(self.current_sprite)]

    def animate(self):
        self.is_animating = True


pygame.init()
clock = pygame.time.Clock()

screen_width = 400
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Sprite Animation')

moving_sprites = pygame.sprite.Group()
player = Player(130, 120)
moving_sprites.add(player) # type: ignore



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            player.animate()

    screen.fill((0,0,0))
    moving_sprites.draw(screen)
    moving_sprites.update()
    pygame.display.flip()
    clock.tick(60)