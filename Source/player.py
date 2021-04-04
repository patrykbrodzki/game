import pygame
import sys
from Source.projectile import Projectile


class Player:
    def __init__(self, player_image, velocity, screen):
        self.player_image = pygame.image.load(player_image)
        self.player_image_width, self.player_image_height = self.player_image.get_size()
        self.velocity = velocity
        self.screen = screen
        self.start_position_x = self.screen.screen_width / 2 - self.player_image_width / 2
        self.start_position_y = self.screen.screen_height - self.player_image_height
        self.is_jump = False
        self.jump_count = 10
        self.standing = True
        self.left = False
        self.right = False
        self.up = False
        self.down = False
        self.walk_count = 0
        self.walkLeft = [
            pygame.image.load('Images/character/char_moving/1.PNG'), pygame.image.load('Images/character/char_moving/2.PNG'),
            pygame.image.load('Images/character/char_moving/1.PNG'), pygame.image.load('Images/character/char_moving/3.PNG')
        ]
        self.walkRight = [
            pygame.transform.flip(pygame.image.load('Images/character/char_moving/1.PNG'), True, False),
            pygame.transform.flip(pygame.image.load('Images/character/char_moving/2.PNG'), True, False),
            pygame.transform.flip(pygame.image.load('Images/character/char_moving/1.PNG'), True, False),
            pygame.transform.flip(pygame.image.load('Images/character/char_moving/3.PNG'), True, False)
        ]
        self.walkUp = [
            pygame.image.load('Images/character/char_moving_down/1.PNG'), pygame.image.load('Images/character/char_moving_down/2.PNG'),
            pygame.image.load('Images/character/char_moving_down/1.PNG'), pygame.image.load('Images/character/char_moving_down/3.PNG')
        ]
        self.walkDown = [
            pygame.image.load('Images/character/char_moving_up/1.PNG'), pygame.image.load('Images/character/char_moving_up/2.PNG'),
            pygame.image.load('Images/character/char_moving_up/1.PNG'), pygame.image.load('Images/character/char_moving_up/3.PNG')
        ]
        self.magic_bullets = []
        self.magic_left = False
        self.magic_right = False
        self.magic_up = False
        self.magic_down = False

        self.a = self.start_position_x
        self.b = self.start_position_y

    def draw(self):
        # print(self.start_position_x, self.a)
        # print(self.start_position_y, self.b)
        self.events_movements()
        self.not_events_movements()
        # drawing bullet
        for magic_bullet in self.magic_bullets:
            print(magic_bullet)

            if magic_bullet.magic_right and self.screen.screen_width > magic_bullet.position_x > 0:
                magic_bullet.position_x += magic_bullet.facing_x * magic_bullet.velocity
                magic_bullet.draw_right()
                if magic_bullet.magic_up:
                    magic_bullet.position_y += magic_bullet.facing_y * magic_bullet.velocity
                    if magic_bullet.position_y < 0 - magic_bullet.projectile_width:
                        self.magic_bullets.pop(self.magic_bullets.index(magic_bullet))
                elif magic_bullet.magic_down:
                    magic_bullet.position_y += magic_bullet.facing_y * magic_bullet.velocity
                    if magic_bullet.position_y < 0 - magic_bullet.projectile_width:
                        self.magic_bullets.pop(self.magic_bullets.index(magic_bullet))
            elif magic_bullet.magic_left and self.screen.screen_width > magic_bullet.position_x > 0 - magic_bullet.projectile_width:
                magic_bullet.position_x += magic_bullet.facing_x * magic_bullet.velocity
                magic_bullet.draw_left()
                if magic_bullet.magic_up:
                    magic_bullet.position_y += magic_bullet.facing_y * magic_bullet.velocity
                    if magic_bullet.position_y < 0 - magic_bullet.projectile_width:
                        self.magic_bullets.pop(self.magic_bullets.index(magic_bullet))
                elif magic_bullet.magic_down:
                    magic_bullet.position_y += magic_bullet.facing_y * magic_bullet.velocity
                    if magic_bullet.position_y < 0 - magic_bullet.projectile_width:
                        self.magic_bullets.pop(self.magic_bullets.index(magic_bullet))

            elif magic_bullet.magic_down and self.screen.screen_height > magic_bullet.position_y > 0:
                if not magic_bullet.magic_right or magic_bullet.magic_left:
                    magic_bullet.draw_down()
                    magic_bullet.position_y += magic_bullet.facing_y * magic_bullet.velocity
                else:
                    self.magic_bullets.pop(self.magic_bullets.index(magic_bullet))

            elif magic_bullet.magic_up and self.screen.screen_height > magic_bullet.position_y > 0:
                if not magic_bullet.magic_right or magic_bullet.magic_left:
                    magic_bullet.draw_up()
                    magic_bullet.position_y += magic_bullet.facing_y * magic_bullet.velocity
                else:
                    self.magic_bullets.pop(self.magic_bullets.index(magic_bullet))

            else:
                self.magic_bullets.pop(self.magic_bullets.index(magic_bullet))

    def events_movements(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_z:
                    facing_x = 0
                    facing_y = 0
                    start_position_x = 0
                    start_position_y = 0
                    if self.magic_left:
                        facing_x = -2
                        start_position_x = self.start_position_x - self.player_image_width / 2
                        start_position_y = self.start_position_y
                    if self.magic_right:
                        facing_x = 2
                        start_position_x = self.start_position_x + self.player_image_width / 2
                        start_position_y = self.start_position_y
                    if self.magic_up:
                        facing_y = -2
                        start_position_y = self.start_position_y - self.player_image_height / 1.5
                        start_position_x = self.start_position_x
                    if self.magic_down:
                        facing_y = 2
                        start_position_y = self.start_position_y + self.player_image_height / 2
                        start_position_x = self.start_position_x

                    # if len(self.bullets) < 10 and facing_x != 0 and facing_y != 0:
                    if len(self.magic_bullets) < 5:
                        self.magic_bullets.append(Projectile(10, self.screen, start_position_x, start_position_y,
                                                             facing_x, facing_y, self.magic_left, self.magic_right, self.magic_up,
                                                             self.magic_down))

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_z:
                    self.magic_left = False
                    self.magic_right = False
                    self.magic_up = False
                    self.magic_down = False


            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    def not_events_movements(self):
        keys = pygame.key.get_pressed()
        # print(self.walk_count)

        # Below methods are for displaying stripes #
        if self.walk_count + 1 >= 12:
            self.walk_count = 0

        if not self.standing:
            if self.left:
                self.screen.screen_display.blit(self.walkLeft[self.walk_count // 3],
                                                (self.start_position_x, self.start_position_y))
                self.walk_count += 1
            elif self.right:
                self.screen.screen_display.blit(self.walkRight[self.walk_count // 3],
                                                (self.start_position_x, self.start_position_y))
                self.walk_count += 1
            elif self.up:
                self.screen.screen_display.blit(self.walkUp[self.walk_count // 3],
                                                (self.start_position_x, self.start_position_y))
                self.walk_count += 1
            else:
                self.screen.screen_display.blit(self.walkDown[self.walk_count // 3],
                                                (self.start_position_x, self.start_position_y))
                self.walk_count += 1
        else:
            if self.left:
                self.screen.screen_display.blit(self.walkLeft[0], (self.start_position_x, self.start_position_y))
                self.magic_left = True
            elif self.right:
                self.screen.screen_display.blit(self.walkRight[0], (self.start_position_x, self.start_position_y))
                self.magic_right = True
            elif self.up:
                self.screen.screen_display.blit(self.walkUp[0], (self.start_position_x, self.start_position_y))
                self.magic_up = True
            elif self.down:
                self.screen.screen_display.blit(self.walkDown[0], (self.start_position_x, self.start_position_y))
                self.magic_down = True
            else:
                self.screen.screen_display.blit(pygame.image.load('Images/character/char_moving_up/1.PNG'),
                                                (self.start_position_x, self.start_position_y))
        # Above methods are for displaying stripes with movements#

        # Below methods are movement methods with additional parameters which allow to display stripes #
        if keys[pygame.K_LEFT]:
            if self.start_position_x > 0 - self.velocity:
                self.start_position_x -= self.velocity
                self.left = True
                self.right = False
                self.up = False
                self.down = False
                self.standing = False
                self.magic_left = True
                self.magic_right = False
        if keys[pygame.K_RIGHT]:
            if self.start_position_x < self.screen.screen_width - self.player_image_width + self.velocity:
                self.start_position_x += self.velocity
                self.right = True
                self.left = False
                self.up = False
                self.down = False
                self.standing = False
                self.magic_left = False
                self.magic_right = True

        if not self.is_jump:
            if keys[pygame.K_DOWN]:
                if self.start_position_y < self.screen.screen_height - self.player_image_height:
                    self.start_position_y += self.velocity
                    self.right = False
                    self.left = False
                    self.up = False
                    self.down = True
                    self.standing = False
                    self.magic_down = True
                    self.magic_up = False
            if keys[pygame.K_UP]:
                if self.start_position_y > 0:
                    self.start_position_y -= self.velocity
                    self.right = False
                    self.left = False
                    self.up = True
                    self.down = False
                    self.standing = False
                    self.magic_down = False
                    self.magic_up = True
            if keys[pygame.K_SPACE]:
                self.is_jump = True
                # right = False
                # left = False
                # walkCount = 0
        else:
            if self.jump_count >= -10:
                neg = 1
                if self.jump_count < 0:
                    neg = -1
                self.start_position_y -= (self.jump_count ** 2) * 0.25 * neg
                self.jump_count -= 1
            else:
                self.is_jump = False
                self.jump_count = 10

        if not keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT] and not keys[pygame.K_UP] and not keys[pygame.K_DOWN]:
            self.walk_count = 0
            self.standing = True


# Test class - checking if works with example inheritance
# class Enemy(Player):
#     def __init__(self,player_image, velocity, screen):
#         super().__init__(player_image, velocity, screen)
#
#         self.start_position_x = 500
#         self.start_position_y = 400
#         self.is_jump = False
#         self.jump_count = 10
#         self.standing = True
#         self.left = False
#         self.right = False
#         self.up = False
#         self.down = False
#         self.walk_count = 0
#         self.walkLeft = [pygame.image.load('Images/char_moving/1.png'), pygame.image.load('Images/char_moving/2.png'),
#                          pygame.image.load('Images/char_moving/1.png'), pygame.image.load('Images/char_moving/3.png')]
#         self.walkRight = [pygame.transform.flip(pygame.image.load('Images/char_moving/1.png'), True, False),
#                           pygame.transform.flip(pygame.image.load('Images/char_moving/2.png'), True, False),
#                           pygame.transform.flip(pygame.image.load('Images/char_moving/1.png'), True, False),
#                           pygame.transform.flip(pygame.image.load('Images/char_moving/3.png'), True, False)]
#         self.walkUp = [pygame.image.load('Images/char_moving_down/1.png'),
#                        pygame.image.load('Images/char_moving_down/2.png'),
#                        pygame.image.load('Images/char_moving_down/1.png'),
#                        pygame.image.load('Images/char_moving_down/3.png')]
#         self.walkDown = [pygame.image.load('Images/char_moving_up/1.png'),
#                          pygame.image.load('Images/char_moving_up/2.png'),
#                          pygame.image.load('Images/char_moving_up/1.png'),
#                          pygame.image.load('Images/char_moving_up/3.png')]
