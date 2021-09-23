import numpy as np
import pygame

class Boid:
    def __init__(self, pos:np.ndarray, vel:np.ndarray, ffactor:float = 0.1) -> None:
        self.pos = pos
        self.vel = vel
        self.acc = np.zeros((2,1), float)

        self.ffactor = ffactor

    def getPos(self) -> np.ndarray:
        return self.pos

    def applyForce(self, f:np.ndarray) -> None:
        np.add(self.acc, f, self.acc)

    def update(self):
        self.acc = np.multiply(self.acc, self.ffactor)
        self.vel = np.add(self.vel, self.acc)
        self.pos = np.add(self.pos, self.vel)
        self.acc = np.multiply(self.acc, 0)

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), (self.pos[0][0], self.pos[1][0]), 10)