import pygame
import sys


# THOSE ARE PLAYER ONLY EVENT METHODS
def key_z(event, self):
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_z:
            self.projectile_pool.fire(self.movement_direction, self.player_position)


def pressed_quit(event):
    if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
