import pygame
from Source.vectors import Vector2


class Projectile:
    def __init__(self, screen, velocity):
        self.screen = screen
        self.velocity = velocity
        self.projectile_position = Vector2(0, 0)
        self.movement_direction = Vector2(0, 0)
        self.active = False

        # variables for sprite animations
        self.last_update = 0
        self.current_frame = 0

        # projectile images
        self.animation_left = [
            pygame.transform.flip(pygame.image.load('Images/magic_spell/magic/S1.png'), True, False),
            pygame.transform.flip(pygame.image.load('Images/magic_spell/magic/S2.png'), True, False),
            pygame.transform.flip(pygame.image.load('Images/magic_spell/magic/S3.png'), True, False),
            pygame.transform.flip(pygame.image.load('Images/magic_spell/magic/S4.png'), True, False)
        ]
        self.animation_right = [
            pygame.image.load('Images/magic_spell/magic/S1.png'),
            pygame.image.load('Images/magic_spell/magic/S2.png'),
            pygame.image.load('Images/magic_spell/magic/S3.png'),
            pygame.image.load('Images/magic_spell/magic/S4.png')
        ]
        self.animation_up = [
            pygame.image.load('Images/magic_spell/magic_up/S1.png'),
            pygame.image.load('Images/magic_spell/magic_up/S2.png'),
            pygame.image.load('Images/magic_spell/magic_up/S3.png'),
            pygame.image.load('Images/magic_spell/magic_up/S4.png')
        ]
        self.animation_down = [
            pygame.transform.flip(pygame.image.load('Images/magic_spell/magic_up/S1.png'), False, True),
            pygame.transform.flip(pygame.image.load('Images/magic_spell/magic_up/S2.png'), False, True),
            pygame.transform.flip(pygame.image.load('Images/magic_spell/magic_up/S3.png'), False, True),
            pygame.transform.flip(pygame.image.load('Images/magic_spell/magic_up/S4.png'), False, True)
        ]
        self.projectile_width, self.projectile_height = self.animation_right[0].get_size()

    def position(self):
        # return print(self.projectile_position.x, self.projectile_position.y)
        return print('x  ', self.movement_direction.x, 'y   ', self.movement_direction.y)

    def is_active(self):
        return self.active

    # tu mi zostają zmienne movement.y które decydują, że ciągle kulka leci mi na skos albo ggora dół
    # to musi być powiązane z plraer_movements -> sprawdzić

    # def activate(self, player_movement_direction, player_position):
    #     self.active = True
    #     self.projectile_position.x = player_position.x
    #     self.projectile_position.y = player_position.y
    #     self.movement_direction.x = player_movement_direction.x
    #     self.movement_direction.y = player_movement_direction.y

    def activate(self, player_movement_direction, player_position):
        self.active = True
        self.projectile_position.x = player_position.x
        self.projectile_position.y = player_position.y
        self.movement_direction.x = player_movement_direction.x
        self.movement_direction.y = player_movement_direction.y

    def deactivate(self):
        self.active = False
        self.projectile_position.x = 0
        self.projectile_position.y = 0
        self.movement_direction.x = 0
        self.movement_direction.y = 0
        self.current_frame = 0

    # this method draw projectile on the screen
    def draw(self):
        self.update()

        # print(self.movement_direction.x, self.movement_direction.y)
        # counts milliseconds from start of the game to display proper animation image
        now = pygame.time.get_ticks()
        if now - self.last_update > 150:
            self.last_update = now
            if self.current_frame >= 2:
                self.current_frame = 3
            else:
                self.current_frame = (self.current_frame + 1) % len(self.animation_left)

        # offset variable for proper bullet animation (it cannot start from the center of the player)
        start_position_offset = 20
        if self.active:
            if self.movement_direction.x < 0:
                self.screen.screen_display.blit(self.animation_left[self.current_frame],
                                                (self.projectile_position.x - start_position_offset,
                                                 self.projectile_position.y))
            elif self.movement_direction.x > 0:
                self.screen.screen_display.blit(self.animation_right[self.current_frame],
                                                (self.projectile_position.x + start_position_offset, self.projectile_position.y))
            elif self.movement_direction.y > 0:
                self.screen.screen_display.blit(self.animation_down[self.current_frame],
                                                (self.projectile_position.x, self.projectile_position.y + start_position_offset))
            elif self.movement_direction.y < 0:
                self.screen.screen_display.blit(self.animation_up[self.current_frame],
                                                (self.projectile_position.x, self.projectile_position.y - start_position_offset))

    # TODO
    # zrobić do końca animacje w każde strony i na skos

    # this method updates projectile_position with its direction and velocity
    def update(self):
        self.projectile_position.x += self.movement_direction.x * self.velocity
        self.projectile_position.y += self.movement_direction.y * self.velocity

        if self.projectile_position.x > self.screen.screen_width or self.projectile_position.x < 0:
            self.deactivate()

        if self.projectile_position.y > self.screen.screen_height or self.projectile_position.y < 0 - self.projectile_height:
            self.deactivate()
