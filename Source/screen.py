import pygame


class Screen:
    def __init__(self, screen_width, screen_height, background_image, background_location):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.background_image = pygame.image.load(background_image)
        self.background_location = background_location
        self.screen_display = pygame.display.set_mode((self.screen_width, self.screen_height), pygame.RESIZABLE)

    def draw_intro(self):

        intro = True

        while intro:
            for event in pygame.event.get():
                print(event)
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_z:
                        intro = False
                        self.draw()


            # self.screen_display.fill(255,255,255)
            # largeText = pygame.font.Font('freesansbold.ttf', 115)
            # TextSurf, TextRect = text_objects("A bit Racey", largeText)
            # TextRect.center = ((self.screen_width / 2), (self.screen_height / 2))
            # self.screen_display.blit(TextSurf, TextRect)
            self.screen_display.blit(self.background_image, self.background_location)

    # Drawing screen with background. If user changes widht/height of the screen on the computer
    # pygame.display.get_window_size() will return tuple with new screen width/height
    def draw(self):
        self.screen_display.blit(self.background_image, self.background_location)
        self.screen_width, self.screen_height = pygame.display.get_window_size()
        # pygame.draw.rect(self.screen_display, (0, 0, 0), (200, 150, 100, 50))
        # pygame.draw.rect(self.screen_display, (0, 0, 0), (500, 350, 100, 50))

