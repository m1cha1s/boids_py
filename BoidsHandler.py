from Boid import Boid
import numpy as np
from random import random as rnd
import pygame

class BoidsHandler:
    def __init__(self, boid_cnt:int, screen:pygame.Surface) -> None:
        
        self.boids = []
        self.screen = screen

        for _ in range(boid_cnt):
            self.boids.append(Boid(np.array([[rnd()*500], [rnd()*500]], float), np.array([[(rnd()*2)-1, (rnd()*2)-1]], float)))

    def handleBoids(self):
        for boid in range(len(self.boids)):
            self.boids[boid].update()
            self.boids[boid].draw(self.screen)