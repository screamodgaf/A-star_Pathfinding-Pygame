# Import the pygame module
import pygame
import sys
from node import Node


def createControlableObject():
    # Create a rectangle object
    rect = pygame.Rect(100, 300, 100, 50)
    return rect

def checkKeyEvents(player):
    # Get the state of the keyboard keys
    keys = pygame.key.get_pressed()
    # Check if the left arrow key is pressed
    if keys[pygame.K_LEFT]:
        # Move the rectangle to the left
        player.move_ip(-5, 0)
    # Check if the right arrow key is pressed
    if keys[pygame.K_RIGHT]:
        # Move the rectangle to the right
        player.move_ip(5, 0)
    # Check if the up arrow key is pressed
    if keys[pygame.K_UP]:
        # Move the rectangle up
        player.move_ip(0, -5)
    # Check if the down arrow key is pressed
    if keys[pygame.K_DOWN]:
        # Move the rectangle down
        player.move_ip(0, 5)

def createObjectsToDraw():

    rect = pygame.Rect(600, 300, 100, 50)
    listOfObjectsToDraw = []
    listOfObjectsToDraw.append(rect)
    return listOfObjectsToDraw

def drawObjects(listOfObjectsToDraw):
    for rect in listOfObjectsToDraw:
        pygame.draw.rect(screen, (255,10,10), rect)

def drawControlableObject(player):
    pygame.draw.rect(screen, (255,10,10), player)

def associateMatrixToDrawableRects(matrix, MATRIX_HEIGHT, MATRIX_WIDTH, FIELD_SIZE):
    worldRectsList = []

    for y in range(MATRIX_HEIGHT):
        for x in range(MATRIX_WIDTH):
            node = Node(x * FIELD_SIZE, y * FIELD_SIZE, FIELD_SIZE, FIELD_SIZE) #instead: rect = pygame.Rect(posX, posY, FIELD_SIZE, FIELD_SIZE)
            worldRectsList.append(node)

    print("number of elements in worldRectsList: ", len(worldRectsList))
    return worldRectsList

def drawMatrix(screen, matrix, MATRIX_HEIGHT, MATRIX_WIDTH, worldRectsList):
    BLUE = (0,0,255)
    RED = (255,0,0)
    YELLOW = (255,255,0)

    for y in range(MATRIX_HEIGHT):
        for x in range(MATRIX_WIDTH):
            if matrix[x + y * MATRIX_WIDTH] == 0:
                worldRectsList[x + y * MATRIX_WIDTH].draw(screen, BLUE)
            elif matrix[x + y * MATRIX_WIDTH] == 1:
                worldRectsList[x + y * MATRIX_WIDTH].draw(screen, RED)

    worldRectsList[(MATRIX_WIDTH-1) + (MATRIX_HEIGHT-1) * MATRIX_WIDTH].draw(screen, YELLOW)
 
# Initialize pygame
pygame.init()
# Create a display surface
screen = pygame.display.set_mode((800, 600))
# Set the caption of the window
pygame.display.set_caption("Game")
# Create a clock object
clock = pygame.time.Clock()

#Create objects to draw:
listOfObjectsToDraw = createObjectsToDraw()
#create human controlled object with keyboard:
player = createControlableObject()

# Create a color object
color = pygame.Color(255, 0, 0)

#Create matrix
matrix = [1,1,1,1,1,1,1,1,
          1,0,0,0,0,0,0,1,
          1,0,1,0,1,0,0,1,
          1,0,1,1,1,0,0,1,
          1,0,0,0,0,0,0,1,
          1,1,1,1,1,1,1,1]

MATRIX_HEIGHT = 6
MATRIX_WIDTH = 8
FIELD_SIZE = 100

worldRectsList = associateMatrixToDrawableRects(matrix, MATRIX_HEIGHT, MATRIX_WIDTH, FIELD_SIZE)

nodesToBeEvaluated = [] #open set - when this list gets empty and the goal is not reacher, the search must be stopped | it starts with initial node
nodesEvaluated = [] #close set is empty at the beginning
startNode = worldRectsList[0 + 0 * MATRIX_WIDTH]
endNode = worldRectsList[0 + 0 * MATRIX_WIDTH]


# Create a variable for the game loop
running = True

# Start the game loop
while running:
    # Handle the events
    for event in pygame.event.get():
        # Check if the user clicked the close button
        if event.type == pygame.QUIT:
            # Exit the loop
            running = False
            sys.exit()
    checkKeyEvents(player)
    # Fill the screen with black
    screen.fill((0, 0, 0))

    #draw your objects on the screen:
    drawMatrix(screen, matrix, MATRIX_HEIGHT, MATRIX_WIDTH, worldRectsList)
    #drawObjects(listOfObjectsToDraw)
    #drawControlableObject(player)


    # Update the display
    pygame.display.update()
    # Control the frame rate
    clock.tick(60)

# Quit pygame
pygame.quit()
