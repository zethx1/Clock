import pygame
import sys
import math
from datetime import datetime

pygame.init()

#Display
screen = pygame.display.set_mode((900, 800))
pygame.display.set_caption("Mouse Clock")

#Images
background = pygame.image.load("main-clock.png").convert_alpha()
minute_hand = pygame.image.load("right-hand.png").convert_alpha()
second_hand = pygame.image.load("left-hand.png").convert_alpha()

#Rotation function
def blit_rotate_center(surf, image, topleft, angle):
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center=image.get_rect(topleft=topleft).center)
    surf.blit(rotated_image, new_rect.topleft)

#Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #Current time
    now = datetime.now()
    minutes = now.minute
    seconds = now.second

    #Angle calculation
    minute_angle = - (minutes * 6)  # 360 degrees / 60 minutes = 6 degrees per minute
    second_angle = - (seconds * 6)  # 360 degrees / 60 seconds = 6 degrees per second

    # Clear screen and blit background
    screen.fill((255, 255, 255))
    screen.blit(background, (0, 0))

    # Blit rotated hands in center
    blit_rotate_center(screen, minute_hand, (200, 330), minute_angle)
    blit_rotate_center(screen, second_hand, (135, 350), second_angle)

    # Update the display
    pygame.display.flip()

    #frame rate 60
    pygame.time.Clock().tick(60)

pygame.quit()
sys.exit()

