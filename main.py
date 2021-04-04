import pygame
import sys
from Source.screen import Screen
from Source.player import Player

# Initialize the pygame
pygame.init()
pygame.mouse.set_visible(True)
clock = pygame.time.Clock()

# Title and Icon
pygame.display.set_caption('Test')
icon = pygame.image.load('Images/character/char_moving/1.png')
pygame.display.set_icon(icon)

# Creating first screen and displaying background
first_screen = Screen(1024, 800, 'Images/background.png', [0, 0])
intro_screen = Screen(1024,800, 'Images/magic_spell/magic/S1.png', [0, 0])


# Drawing game window
def drawGameWindow():
    # intro_screen.draw()
    # first_screen.draw_intro()
    first_screen.draw()
    player.draw()
    pygame.display.update()


# Creating player
player = Player('Images/character/char_moving/1.png', 10, first_screen)


def main_loop():
    running = True
    while running:
        # pygame.time.delay(50)

        drawGameWindow()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()


        clock.tick(12)


main_loop()
