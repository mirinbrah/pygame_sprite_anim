import pygame


class Animator:
    def __init__(self, animations, initial_state='idle', animation_speed=0.2):
        self.animations = animations
        self.animation_speed = animation_speed
        self.current_animation_name = initial_state
        self.current_sprite_index = 0.0
        self.image = self.animations[self.current_animation_name][0]
        self.just_finished = False

    def set_animation(self, name):
        if self.current_animation_name == name:
            return

        if name in self.animations:
            self.current_animation_name = name
            self.current_sprite_index = 0.0
        else:
            print(f"Внимание: Анимация '{name}' не найдена!")

    def is_animation_finished(self):
        return self.just_finished

    def update(self):
        self.just_finished = False
        current_frames = self.animations[self.current_animation_name]

        if len(current_frames) > 1:
            self.current_sprite_index += self.animation_speed
            if self.current_sprite_index >= len(current_frames):
                self.current_sprite_index = 0
                self.just_finished = True

            self.image = current_frames[int(self.current_sprite_index)]