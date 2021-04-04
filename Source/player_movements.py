import pygame


# THOSE ARE PLAYER MOVEMENT METHODS
def left_right(keys, self):
    if keys[pygame.K_LEFT] and self.player_position.x > 0 - self.velocity:
        self.movement_direction.x = - 1
        self.movement_direction.y = 0
        self.player_position.x += self.movement_direction.x * self.velocity

    elif keys[pygame.K_RIGHT] and self.player_position.x < self.screen.screen_width - self.player_image_width + self.velocity:
        self.movement_direction.x = 1
        self.movement_direction.y = 0
        self.player_position.x += self.movement_direction.x * self.velocity


def key_up_down(keys, self):
    if keys[pygame.K_DOWN] and self.player_position.y < self.screen.screen_height - self.player_image_height:
        self.movement_direction.y = 1
        self.movement_direction.x = 0
        self.player_position.y += self.movement_direction.y * self.velocity

    elif keys[pygame.K_UP] and self.player_position.y > 0:
        self.movement_direction.y = - 1
        self.movement_direction.x = 0
        self.player_position.y += self.movement_direction.y * self.velocity


def key_not(keys, self):
    if not keys[pygame.K_DOWN] and not keys[pygame.K_UP] and not keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT]:
        self.standing = True
    else:
        self.standing = False


# This function set is_jump variable to know if player is already jumping or not. You can't jump while you are jumping.
def is_jump(keys, self):
    if keys[pygame.K_SPACE]:
        self.is_jump = True


def jump(self):
    if self.jump_count >= - 7:
        neg = 1
        if self.jump_count < 0:
            neg = -1
        self.player_position.y -= (self.jump_count ** 2) * 0.25 * neg
        self.jump_count -= 1
    else:
        self.jump_count = 7
        self.is_jump = False

# back up function - if that in events stopped working
# def fire(keys, self):
#     if keys[pygame.K_z]:
#         self.projectile_pool.fire()


# test function for the second player character
# def left_right_test(keys, self):
#
#     if keys[pygame.K_a] and self.player_position.x > 0 - self.velocity:
#         self.standing = False
#         self.movement_direction.x = - 1
#         self.player_position.x += self.movement_direction.x * self.velocity
#
#     elif keys[pygame.K_d] and self.player_position.x < self.screen.screen_width - self.player_image_width + self.velocity:
#         self.standing = False
#         self.movement_direction.x = 1
#         self.player_position.x += self.movement_direction.x * self.velocity
