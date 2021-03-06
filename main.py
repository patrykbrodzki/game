from Source.screen import first_screen
from Source.player import Player
from Source.player_events_movements import *

# Initialize the pygame
pygame.init()
pygame.mouse.set_visible(True)
clock = pygame.time.Clock()

# Title and Icon
pygame.display.set_caption('test_game')

icon = pygame.image.load('Images/character/char_moving/1.PNG')
pygame.display.set_icon(icon)


# Creating player
player = Player('Images/character/char_moving/1.PNG', 5, first_screen, 5)
# Creating player projectile pool
player.player_projectile_pool_initialize()


def draw_line():
    pygame.draw.line(first_screen.screen_display, (0, 0, 0), (0, 0),
                     (player.player_position.x, player.player_position.y), width=1)


# Drawing game window
def drawGameWindow():
    first_screen.draw()

    player.draw_player()
    draw_line()

    pygame.display.update()
    # print('x  ', player.movement_direction.x, 'y  ', player.movement_direction.y)
def main_loop():
    running = True

    while running:
        clock.tick(12)

        drawGameWindow()

        events = pygame.event.get()
        for event in events:
            player.events_movements(events)
            pressed_quit(event)
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_z:
                    # print('Z pressed') -> mam event z playera ale mogę dodatkowo nadpisać czymkolwiek w main loop
                    pass


if __name__ == "__main__":
    main_loop()
