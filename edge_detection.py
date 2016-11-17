# Imports
import pygame
import math

# Initialize game engine
pygame.init()


# Window
width = 800
height = 600
SIZE = (width, height)
TITLE = "Edge Detection"
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption(TITLE)


# Timer
clock = pygame.time.Clock()
refresh_rate = 60


# Colors
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

    
# Make a block
block =  [375, 275, 50, 50]

block_vx = 0
block_vy = 0

block_speed = 5


# Select test case
'''
1 = stop on edge
2 = wrap around
'''
case = 1


# Game loop
done = False

while not done:
    # Event processing (React to key presses, mouse clicks, etc.)
    ''' for now, we'll just check to see if the X is clicked '''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    state = pygame.key.get_pressed()

    up = state[pygame.K_w]
    down = state[pygame.K_s]
    left = state[pygame.K_a]
    right = state[pygame.K_d]

    if up:
        block_v_y = -block_speed
    elif down:
        block_v_y = block_speed
    else:
        block_v_y = 0
        
    if left:
        block_v_x = -block_speed
    elif right:
        block_v_x = block_speed
    else:
        block_v_x = 0

        
    # Game logic (Check for collisions, update points, etc.)
    ''' move the block '''
    block[0] += block_v_x
    block[1] += block_v_y

    ''' get block edges (makes collision resolution easier to read) '''
    top = block[1]
    bottom = block[1] + block[3]
    left = block[0]
    right = block[0] + block[2]
    
    if case == 1:
        ''' if the block is moved out of the window, nudge it back on. '''
        if top < 0:
            block[1] = 0
        elif bottom > height:
            block[1] = height - block[3]
        elif left < 0:
            block[0] = 0
        elif right > width:
            block[0] = width - block[2]
    
    elif case == 2:
        ''' if the block is moved completely off of the window, reposition it on the other side '''
        pass


    
    # Drawing code (Describe the picture. It isn't actually drawn yet.)
    screen.fill(BLACK)

    pygame.draw.rect(screen, WHITE, block)


    # Update screen (Actually draw the picture in the window.)
    pygame.display.flip()


    # Limit refresh rate of game loop 
    clock.tick(refresh_rate)


# Close window and quit
pygame.quit()
