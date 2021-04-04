from Source.vectors import Vector2
from Source.player_movements import *
from Source.player_events_movements import *
from Source.player_projectile_pool import ProjectilePool


class Player:
    def __init__(self, player_image, velocity, screen):
        # Player image and sprites
        self.player_image = pygame.image.load(player_image)
        self.player_image_width, self.player_image_height = self.player_image.get_size()
        self.walkLeft = [
            pygame.image.load('Images/character/char_moving/1.PNG'),
            pygame.image.load('Images/character/char_moving/2.PNG'),
            pygame.image.load('Images/character/char_moving/1.PNG'),
            pygame.image.load('Images/character/char_moving/3.PNG')
        ]
        self.walkRight = [
            pygame.transform.flip(pygame.image.load('Images/character/char_moving/1.PNG'), True, False),
            pygame.transform.flip(pygame.image.load('Images/character/char_moving/2.PNG'), True, False),
            pygame.transform.flip(pygame.image.load('Images/character/char_moving/1.PNG'), True, False),
            pygame.transform.flip(pygame.image.load('Images/character/char_moving/3.PNG'), True, False)
        ]
        self.walkUp = [
            pygame.image.load('Images/character/char_moving_down/1.PNG'),
            pygame.image.load('Images/character/char_moving_down/2.PNG'),
            pygame.image.load('Images/character/char_moving_down/1.PNG'),
            pygame.image.load('Images/character/char_moving_down/3.PNG')
        ]
        self.walkDown = [
            pygame.image.load('Images/character/char_moving_up/1.PNG'),
            pygame.image.load('Images/character/char_moving_up/2.PNG'),
            pygame.image.load('Images/character/char_moving_up/1.PNG'),
            pygame.image.load('Images/character/char_moving_up/3.PNG')
        ]

        # Screen
        self.screen = screen

        # Player movement
        self.player_position = Vector2(self.screen.screen_width / 2 - self.player_image_width / 2,
                                       self.screen.screen_height - self.player_image_height)
        self.velocity = velocity
        self.movement_direction = Vector2(0, 0)
        self.standing = True

        # Variables for proper FPS displaying animation
        self.current_frame = 0
        self.last_update = 0

        # Variables for proper jumping animation and physics
        self.is_jump = False
        self.jump_count = 7

        # Create Player projectile pool with and define constant pool capacity (int parameter)
        self.projectile_pool = ProjectilePool(2, self.screen)

    def player_projectile_pool_initialize(self):
        self.projectile_pool.initiate()

    def update(self):
        # self.projectile_pool.show_all()
        self.projectile_pool.animate()

        # counts milliseconds from start of the game to display proper animation image
        now = pygame.time.get_ticks()
        if now - self.last_update > 50:
            self.last_update = now
            self.current_frame = (self.current_frame + 1) % len(self.walkLeft)

        # methods which update player position and direction
        self.not_events_movements()

    def events_movements(self, events):
        # events = pygame.event.get() -> ta zmienna jako glówna określona jest w main.py w main.py uruchamiam tę
        # funkcję aby móc zczytać eventy wyłącznie od danego gracza, w main.py mogę nadpisać dodatkowo event i
        # osiągnąć dodatkowy output
        for event in events:
            key_z(event, self)
            pressed_quit(event)

    def not_events_movements(self):
        keys = pygame.key.get_pressed()

        left_right(keys, self)

        if not self.is_jump:
            is_jump(keys, self)
            key_up_down(keys, self)
        else:
            jump(self)

        key_not(keys, self)

    def draw_player(self):
        print(self.movement_direction.x, self.movement_direction.y)
        self.update()

        # conditions where different images of the player are picked to animate

        # TODO
        #     zmieni¢ warunki aby prawidłowo wyswietlały sie animacje

        if not self.standing:
            if self.movement_direction.x < 0:
                self.screen.screen_display.blit(self.walkLeft[self.current_frame],
                                                (self.player_position.x, self.player_position.y))

            elif self.movement_direction.x > 0:
                self.screen.screen_display.blit(self.walkRight[self.current_frame],
                                                (self.player_position.x, self.player_position.y))

            elif self.movement_direction.y < 0:
                self.screen.screen_display.blit(self.walkUp[self.current_frame],
                                                (self.player_position.x, self.player_position.y))

            elif self.movement_direction.y > 0:
                self.screen.screen_display.blit(self.walkDown[self.current_frame],
                                                (self.player_position.x, self.player_position.y))

        else:
            if self.movement_direction.x < 0:
                self.screen.screen_display.blit(self.walkLeft[0], (self.player_position.x, self.player_position.y))
            elif self.movement_direction.x > 0:
                self.screen.screen_display.blit(self.walkRight[0], (self.player_position.x, self.player_position.y))
            elif self.movement_direction.y > 0:
                self.screen.screen_display.blit(self.walkDown[0], (self.player_position.x, self.player_position.y))
            elif self.movement_direction.y < 0:
                self.screen.screen_display.blit(self.walkUp[0], (self.player_position.x, self.player_position.y))
            else:
                self.screen.screen_display.blit(self.walkDown[0], (self.player_position.x, self.player_position.y))


# Test class - checking if works with example inheritance (for enemy or the second player character)
# class Enemy(Player):
#     def __init__(self,player_image, velocity, screen):
#         super().__init__(player_image, velocity, screen)
#
#     def not_events_movements(self):
#         keys = pygame.key.get_pressed()
#
#         # left_right(keys, self)
#         left_right_test(keys, self)
#
#         if not self.is_jump:
#             is_jump(keys, self)
#             key_up_down(keys, self)
#         else:
#             jump(self)
#
#         key_not(keys, self)
#
#     def events_movements(self):
#         events = pygame.event.get()
#
#         for event in events:
#             key_z_test(event, self)
#             pressed_quit(event)
