# Puzzle game made in Pygame v2.0.1
# Made by:-
# Nimish Mathur
# Rushali Tripathy
# Siddharth
# Siddharth Rajagopalan
# Yashika Asrani

# Import packages
import pygame
import random

# Initialize Pygame module
pygame.init()

# Set Screen Icon
icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)

# Set Game Caption
pygame.display.set_caption("Puzzle")

# Set Screen Size
scr_size = (300, 300)
screen = pygame.display.set_mode(scr_size)

# Colors
WHITE = (255, 255, 255)
GREY = (183, 240, 173)
BLACK = (0, 0, 0)
BLUE = (255, 169, 135)

# Text
font = pygame.font.Font(pygame.font.get_default_font(), 20)

# Create a Tile class


class Tile():
    def __init__(self, x, y, val):
        self.loc_x = x
        self.loc_y = y
        self.val = val
        self.box = pygame.Rect(self.loc_x, self.loc_y, 100, 100)


# Create Tile objects
loc = [[0, 0], [100, 0], [200, 0], [0, 100], [100, 100],
       [200, 100], [0, 200], [100, 200], [200, 200]]
random.shuffle(loc)
tiles = []
vals = [1, 2, 3, 4, 5, 6, 7, 8]
for i in range(8):
    t = Tile(loc[i][0], loc[i][1], vals[i])
    tiles.append(t)

# Create empty tile
empty = loc[8]
emp_tile = Tile(empty[0], empty[1], -1)

# # Swap Tiles


def swap():
    temp = i.box
    i.box = emp_tile.box
    emp_tile.box = temp


# Game Loop
run = True
screen.fill(GREY)
print("\n")
while run:
    win = 0
    # Print Tiles
    for i in range(8):
        pygame.draw.rect(screen, BLUE, tiles[i].box)
        val_font = font.render(str(tiles[i].val), True, BLACK)
        screen.blit(val_font, (tiles[i].box.center))
    pygame.draw.rect(screen, GREY, emp_tile.box)

    # Check for events
    for event in pygame.event.get():
        # Quit game
        if event.type == pygame.QUIT:
            run = False
        # On click
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                for i in tiles:
                    if i.box.collidepoint(event.pos):
                        # print(i.box, i.val)
                        if i.box.center[0] == emp_tile.box.center[0] and (i.box.center[1]-emp_tile.box.center[1] == 100 or emp_tile.box.center[1]-i.box.center[1] == 100):
                            if i.box.midtop == emp_tile.box.midbottom:
                                # print("Top swap")
                                swap()
                            elif i.box.midbottom == emp_tile.box.midtop:
                                # print("Bottom swap")
                                swap()
                        elif i.box.center[1] == emp_tile.box.center[1] and (i.box.center[0]-emp_tile.box.center[0] == 100 or emp_tile.box.center[0]-i.box.center[0] == 100):
                            if i.box.left == emp_tile.box.right:
                                # print("Left swap")
                                swap()
                            elif i.box.right == emp_tile.box.left:
                                # print("Right swap")
                                swap()
        pygame.display.flip()