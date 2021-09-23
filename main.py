from Boid import Boid
import numpy as np
import pygame

pygame.init()

screen = pygame.display.set_mode([500,500])

running = True

boids = Boid(np.array([[250], [250]], float), np.array([[0.01], [0.01]], float))

def eventChecker():
    
    global running

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

def update():
    boids.update()

def draw():
    screen.fill(0)
    boids.draw(screen)

def main():

    while(running):
        eventChecker()
        update()
        draw()
        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()