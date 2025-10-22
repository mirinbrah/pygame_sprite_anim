class Animator:
    def __init__(self, sprites, animation_speed=0.2):
        self.sprites = sprites
        self.animation_speed = animation_speed
        self.current_sprite_index = 0.0
        self.image = self.sprites[0]

    def update(self):
        if not self.sprites:
            return

        self.current_sprite_index += self.animation_speed

        if self.current_sprite_index >= len(self.sprites):
            self.current_sprite_index = 0

        self.image = self.sprites[int(self.current_sprite_index)]