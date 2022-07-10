import random
import pygame

# activate the pygame library .
# initiate pygame and give permission
# to use pygame's functionality.
pygame.init()

# define the RGB value
# for white colour
black = (0, 0, 0)

# assigning values to X and Y variable
X = 800
Y = 800

# create the display surface object
# of specific dimension..e(X, Y).
display_surface = pygame.display.set_mode((X, Y))

# set the pygame window name
pygame.display.set_caption('Image')

# create a surface object, image is drawn on it.
# "E:\C64\Telengard\box_cover.jpg"
# image = pygame.image.load(r'C:\Users\user\Pictures\geek.jpg')
image = pygame.image.load(r'E:\C64\Telengard\box_cover.jpg')
# infinite loop


'''    # completely fill the surface object
    # with colour
    display_surface.fill(black)

    # copying the image surface object
    # to the display surface object at
    # (0, 0) coordinate.
    display_surface.blit(image, (0, 0))

    # iterate over the list of Event objects
    # that was returned by pygame.event.get() method.
    for event in pygame.event.get():

        # if event object type is QUIT
        # then quitting the pygame
        # and program both.
        if event.type == pygame.QUIT:
            # deactivates the pygame library
            pygame.quit()

            # quit the program.
            quit()

        # Draws the surface object to the screen.
        pygame.display.update()'''
running = True
while running:
    display_surface.fill(black)

    # copying the image surface object
    # to the display surface object at
    # (0, 0) coordinate.
    display_surface.blit(image, (0, 0))
    for event in pygame.event.get():
        pygame.display.update()
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
            print("escape pressed")
            # pygame.quit()
            running = False
print("Welcome to Telengard")