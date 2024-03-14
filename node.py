import pygame

class Node(pygame.Rect):
    def __init__(self, x, y, width, height):
        #This node's cost of the path f(n)=g(n)+h(n)
        self.f = 0
        #the path cost from the start node to the current node - accumulated cost of the path taken so far
        # - distance traveled from the start node to the current node.
        self.g = 0
        #h - cost from the current node to the goal node.
        self.h = 0

        #calling the parent class constructor (pygame.Rect)
        super().__init__(x, y, width, height)

    def draw(self, screen, color):
        # Draw the rectangle on the screen using the specified color
        pygame.draw.rect(screen, color, self)