from Boid import Boid
from BoidsHandler import BoidsHandler
import numpy as np
import pygame

pygame.init()

screen = pygame.display.set_mode([500,500])

running = True

boids = BoidsHandler(10, screen)

def eventChecker():
    
    global running

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

def main():

    while(running):
        eventChecker()
        screen.fill(0)
        boids.handleBoids()
        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()