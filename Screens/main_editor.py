import pygame
from Source.settings import *

editor_screen = pygame.display.set_mode((SCREEN_WIDTH + SIDE_MARGIN, SCREEN_HEIGHT + LOWER_MARGIN))
pygame.display.set_caption('Editor screen')


# abstract class for generating all screens
class Screen:
    def __init__(self, screen_width, screen_height, background_image, background_location):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.images = dict()
        self.screen_display = pygame.display.set_mode((self.screen_width, self.screen_height), pygame.RESIZABLE)

    def load_images(self):
        pass        


    # Drawing screen with background. If user changes widht/height of the screen on the computer
    # pygame.display.get_window_size() will return tuple with new screen width/height
    def draw(self):
        self.screen_width, self.screen_height = pygame.display.get_window_size()
        self.screen_display.blit(self.background_image, self.background_location)
        # pygame.draw.rect(self.screen_display, (0, 0, 0), (200, 150, 100, 50))
        # pygame.draw.rect(self.screen_display, (0, 0, 0), (500, 350, 100, 50))


class Sample:
   def __init__(self):
        self.data = list()

   def build(self,name):
        self.data.append(name)

   def build1(self,loc):
        self.data[-1].append(loc)     #Use negative index to append.


s = Sample()
a1 = ["mohan,ps","gandhi,as"]
for a in a1:
    split_values = a.split(",")
    s.build([split_values[0]])
    s.build1(split_values[1])

print(s.data)

#
# intro = True
#
# while intro:
#     for event in pygame.event.get():
#         print(event)
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             quit()