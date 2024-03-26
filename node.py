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
        #node's all neighbours:
        self.neighbours = []
        #this node's predecessor in path:
        self.previous = None
        #is the node an unpenetrable obstacle?:
        self.obstacle = False
        # Manhatan distance: the distance between two points measured along axes at right angles. In a plane with p1 at (x1, y1) and p2 at (x2, y2), it is |x1 - x2| + |y1 - y2|. Lm distance:
        self.dist = 1000
        #calling the parent class constructor (pygame.Rect)
        super().__init__(x, y, width, height)
    def setAsObstackle(self, val = True):
        self.obstacle = val
    def checkIfObstackle(self):
        return self.obstacle
    def getF(self):
        return self.f
    def setF(self, val):
        self.f = val
    def getG(self):
        return self.g
    def setG(self, val):
        self.g = val
    def getH(self):
        return self.h
    def setH(self, val):
        self.h = val
    def getDist(self):
        return self.dist
    def setDist(self, val):
        self.dist = val
    def getPrevious(self):
        return self.previous
    def setPrevious(self, val):
        self.previous = val
    def getNeighbourList(self):
        return self.neighbours
    def draw(self, screen, FIELD_SIZE, color):
        grid_thickness = 1
        # Draw the rectangle on the screen using the specified color
        pygame.draw.rect(screen, color, pygame.Rect(self.x, self.y,FIELD_SIZE-grid_thickness,
                                                                   FIELD_SIZE-grid_thickness))


    def determineNeighboursOfNode(self, worldRectsList, MATRIX_HEIGHT, MATRIX_WIDTH):
        x = int(self.x/self.size[0]) #100
        y = int(self.y/self.size[0])
        if x - 1 >= 0:
            left = worldRectsList[(x - 1) + y * MATRIX_WIDTH]
            self.neighbours.append(left)
        if x + 1 < MATRIX_WIDTH:
            right = worldRectsList[(x + 1) + y * MATRIX_WIDTH]
            self.neighbours.append(right)
        if y - 1 >= 0 :
            up = worldRectsList[x + (y - 1) * MATRIX_WIDTH]  # (y-1) must be in braces !!!
            self.neighbours.append(up)
        if y + 1 < MATRIX_HEIGHT:
            down = worldRectsList[x + (y + 1) * MATRIX_WIDTH]
            self.neighbours.append(down)