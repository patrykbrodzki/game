import pygame
from Source.settings import *


class Screen:
    def __init__(self, screen_width, screen_height, background_image, background_location):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.background_image = pygame.image.load(background_image)
        self.background_location = background_location
        self.screen_display = pygame.display.set_mode((self.screen_width, self.screen_height), pygame.RESIZABLE)

    # Drawing screen with background. If user changes widht/height of the screen on the computer
    # pygame.display.get_window_size() will return tuple with new screen width/height
    def draw(self):
        self.screen_width, self.screen_height = pygame.display.get_window_size()
        self.screen_display.blit(self.background_image, self.background_location)
        # pygame.draw.rect(self.screen_display, (0, 0, 0), (200, 150, 100, 50))
        # pygame.draw.rect(self.screen_display, (0, 0, 0), (500, 350, 100, 50))


first_screen = Screen(SCREEN_WIDTH, SCREEN_HEIGHT, 'Images/background.PNG', [0, 0])
