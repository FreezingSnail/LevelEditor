import pygame
import re 

class Sprite_sheet:

    def __init__(self):
        self.tile_x = 0
        self.tile_y = 0
        self.sprite_count = 0
        self.sprites = []
        self.sheet = None

    def strip_from_sheet(self, sheet, start, size, columns=1, rows=1):
        """
        Strips individual frames from a sprite sheet given a start location,
        sprite size, and number of columns and rows.
        """
        frames = []
        print(rows, columns)
        for j in range(rows):
            for i in range(columns):
                print('for', j, i)
                location = (start[0]+size[0]*i, start[1]+size[1]*j)
                img = sheet.subsurface(pygame.Rect(location,size))
                scaled = pygame.transform.scale(img, (42,42))
                frames.append(scaled)

        
        return frames

    def load(self, img, filename):
        height = img.get_height()
        width = img.get_width()
        dimensions = re.search(r'\d+x\d+', filename).group()
        print(dimensions)
        dimensions = dimensions.split('x')
        dimensions = [eval(i) for i in dimensions]
        print(dimensions)
        self.sprites = self.strip_from_sheet(img, [0,0], dimensions, 1, 4) 





