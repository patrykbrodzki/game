import pygame
from Source.settings import *

# editor_screen = pygame.display.set_mode((SCREEN_WIDTH + SIDE_MARGIN, SCREEN_HEIGHT + LOWER_MARGIN))
# pygame.display.set_caption('Editor screen')


# abstract class for generating all screens
class Screen:
    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.images = list()
        self.screen_display = pygame.display.set_mode((self.screen_width, self.screen_height), pygame.RESIZABLE)

    def add_images(self, file, position_x, position_y):
        self.images.append({"source": file, "position_x": position_x, "position_y": position_y})


    # Drawing screen with background. If user changes widht/height of the screen on the computer
    # pygame.display.get_window_size() will return tuple with new screen width/height
    def draw(self):
        self.screen_width, self.screen_height = pygame.display.get_window_size()

        for image in test_screen.images:
            self.screen_display.blit(pygame.image.load(image.get('source')), (image.get('position_x'), image.get('position_y')))


test_screen = Screen(SCREEN_WIDTH, SCREEN_HEIGHT)

test_screen.add_images('Images/Background/sky_solid_color.png', 0, 0)
test_screen.add_images('Images/Background/clouds.png', 0, 0)
test_screen.add_images('Images/Background/mountain_depth_z_1.png', 0, 150)
test_screen.add_images('Images/Background/mountain_depth_z_2.png', 0, 200)
