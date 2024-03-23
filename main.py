# Import the pygame module
import pygame
import sys
import random
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

def fps_counter(screen, system_font):
    fps = str(int(clock.get_fps()))
    fps_text = system_font.render(fps, 1, pygame.Color("BLUE"))
    screen.blit(fps_text, (0, 0))  # Adjust the position as needed

def getSystemFont():
    font_name = "Arial"
    system_font_size = 18
    system_font = pygame.font.SysFont(font_name, system_font_size)
    return system_font
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
            #if its 1 in matrix, set the associated node as an unpenetrable obstackle:
            if matrix[x + y * MATRIX_WIDTH] ==1:
                node.setAsObstackle()
            worldRectsList.append(node)

    print("number of elements in worldRectsList: ", len(worldRectsList))
    return worldRectsList

def determineNeighboursOfAllNodes(worldRectsList, MATRIX_HEIGHT, MATRIX_WIDTH):
    for i in range(len(worldRectsList)):
        worldRectsList[i].determineNeighboursOfNode(worldRectsList, MATRIX_HEIGHT, MATRIX_WIDTH)

def calculateHeuristics(p1, p2):
    #euclidean distance - distance between current node and the end:
    #dist = math.sqrt(  math.pow((p2.x/100 - p1.x/100), 2)
                     #+ math.pow((p2.y/100 - p1.y/100), 2)  )

    #Manhatan distance: the distance between two points measured along axes at right angles. In a plane with p1 at (x1, y1) and p2 at (x2, y2), it is |x1 - x2| + |y1 - y2|. Lm distance:
    dist = abs(p1.x/100 - p2.x/100) + abs(p1.y/100 - p2.y/100)
    print(dist)
    return dist

def drawMatrix(screen, matrix, MATRIX_HEIGHT, MATRIX_WIDTH, FIELD_SIZE, worldRectsList):
    BLUE = (0,0,255)
    RED = (255,0,0)
    WHITE = (255,255,255)
    BLACK = (0,0,0)
    for y in range(MATRIX_HEIGHT):
        for x in range(MATRIX_WIDTH):
            if matrix[x + y * MATRIX_WIDTH] == 0:
                worldRectsList[x + y * MATRIX_WIDTH].draw(screen, FIELD_SIZE, WHITE)
            elif matrix[x + y * MATRIX_WIDTH] == 1:
                worldRectsList[x + y * MATRIX_WIDTH].draw(screen, FIELD_SIZE, BLACK)

def drawStartAndGoalNodes(screen, FIELD_SIZE, worldRectsList, startNode, goalNode):
    PINK = (255,150,200)
    for i in range(len(worldRectsList)):
        if worldRectsList[i] == startNode or worldRectsList[i] == goalNode:
            worldRectsList[i].draw(screen, FIELD_SIZE, PINK)
def drawNodesToBeEvaluated(screen, MATRIX_HEIGHT, MATRIX_WIDTH, FIELD_SIZE, worldRectsList, nodesToBeEvaluated):
    #draw the nodes from nodesToBeEvaluated list:
    YELLOW = (255,255,0)
    for i in range(len(nodesToBeEvaluated)):
        nodesToBeEvaluated[i].draw(screen, FIELD_SIZE, YELLOW)

def drawNodesEvaluated(screen, MATRIX_HEIGHT, MATRIX_WIDTH, FIELD_SIZE, worldRectsList, nodesEvaluated):
    #draw the nodes from nodesEvaluated list:
    RED = (255,0,0)
    for i in range(len(nodesEvaluated)):
        nodesEvaluated[i].draw(screen, FIELD_SIZE, RED)


def drawPath(screen,  FIELD_SIZE, pathList):
    #print("path length: ", len(pathList))
    #draw the nodes from nodesEvaluated list:
    GREEN = (0, 228, 0)
    for i in range(len(pathList)):
        pathList[i].draw(screen, FIELD_SIZE, GREEN)

def estimateActualPath(currentNode):
    if currentNode == 0:
        print("currentNode ==0!")
        return
    tempNode = currentNode
    pathList.append(tempNode)
    # this while loop condition goes all the way back to the startNode:
    while tempNode.getPrevious() != None:
        pathList.append(tempNode.getPrevious())
        # if previous mode was found, check now its own previous node by setting it do "tempNode" which existence is the while loop condition:
        tempNode = tempNode.getPrevious()

def pathFinding(nodesToBeEvaluated, nodesEvaluated, goalNode, MATRIX_HEIGHT, MATRIX_WIDTH, pathList):
    #print("id1 is: ", id(endNode))
    lowestFNodeIndex = 0
    currentNode = 0
    if len(nodesToBeEvaluated) >0:
        for i in range(len(nodesToBeEvaluated)):
            #if there is a node better suiting the easest path - go there setting it as current:
            if nodesToBeEvaluated[i].getF() < nodesToBeEvaluated[lowestFNodeIndex].getF():
                lowestFNodeIndex = i
                currentNode = nodesToBeEvaluated[lowestFNodeIndex]
    else:
        print("Goal unreachable!!!")
        return currentNode
    # current node is the node in the nodesToBeEvaluated list having the LOWEST fScore:
    currentNode = nodesToBeEvaluated[lowestFNodeIndex]

    if currentNode == goalNode:
        estimateActualPath(currentNode)
        print("We reached the goal!")

        # we must return currentNode, cause in the main loop there
        return currentNode

    nodesToBeEvaluated.remove(currentNode)
    #nodesEvaluated consist of currents (red), but not all corrents create the path:
    nodesEvaluated.append(currentNode)
    #check every single neighbour of the current node for g value:
    neighboursOfCurrent = currentNode.getNeighbourList()
    for i in range(len(neighboursOfCurrent)):
        print("nr neighbours: ", len(neighboursOfCurrent))
        neighbour = neighboursOfCurrent[i]
        #check if a neighbour was already evaluated (meaning is present in nodesEvaluated):
        if (neighbour not in nodesEvaluated) and (neighbour.checkIfObstackle() == False) :
            #and if it was not evaluated, get its g and add 1 to it, as every neighbour of current node will have higher g (current.g + 1):
            tempG = currentNode.getG() +1 + calculateHeuristics(neighbour, goalNode)
            #check, if the neighbour with a lower tempG was already found in nodesToBeEvaluated (meaning there is a better way to get there):
            if neighbour in nodesToBeEvaluated:
                #so if the neighbour was already evaluated and its g is smaller than tempG, set its g to tempG:
                if neighbour.getG() > tempG:
                    neighbour.setG(tempG)
            #and if the neighbour is not in nodesToBeEvaluated, set its g to the current's g +1 (currentNode.getG() +1):
            else:
                neighbour.setG(tempG)
                nodesToBeEvaluated.append(neighbour)
            #setting heuristics (educated guess how long will it take to get to the end) for the neighbour:
            neighbour.setH(calculateHeuristics(neighbour, goalNode))
            neighbour.setF( neighbour.getG() + neighbour.getH() )
            #get the previous node (where it came from), for finding the best path:
            #so we seek for the best neighbour, and set current node as the predecesor of the neighbour
            neighbour.setPrevious(currentNode)

    return currentNode

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
'''  
#Create matrix
matrix = [0,1,0,0,0,0,0,0,
          0,1,0,0,0,0,0,0,
          0,0,0,0,0,0,0,0,
          1,1,1,1,1,1,1,0,
          0,0,0,0,0,0,1,0,
          0,0,0,0,0,0,1,0]

MATRIX_HEIGHT = 6
MATRIX_WIDTH = 8
FIELD_SIZE = 30
'''
MATRIX_HEIGHT = 20
MATRIX_WIDTH = 20
FIELD_SIZE = 30
matrix = [0] * MATRIX_HEIGHT * MATRIX_WIDTH


#make random obstackles
for _ in range(150):
    x = random.randint(1, MATRIX_WIDTH-1)
    y = random.randint(1, MATRIX_HEIGHT-1)
    matrix[x + y * MATRIX_WIDTH] = 1

worldRectsList = associateMatrixToDrawableRects(matrix, MATRIX_HEIGHT, MATRIX_WIDTH, FIELD_SIZE)

#make every mode in the matrix (worldRectsList) know its neighbours (fill neighbours list in every node)
determineNeighboursOfAllNodes(worldRectsList, MATRIX_HEIGHT, MATRIX_WIDTH)

nodesToBeEvaluated = [] #open set - when this list gets empty and the goal is not reacher, the search must be stopped | it starts with initial node
nodesEvaluated = [] #close set is empty at the beginning
pathList = []

startNode = worldRectsList[0 + 0 * MATRIX_WIDTH]
#goalNode = worldRectsList[7 + 5 * MATRIX_WIDTH]
goalNode = worldRectsList[(MATRIX_WIDTH-1) + (MATRIX_HEIGHT-1)* MATRIX_WIDTH]
#make sure the start and the goal nodes are not obstackles, otherwise they d never be checked and this goal wouldnt be reached:
startNode.setAsObstackle(False)
goalNode.setAsObstackle(False)
#add starting node to nodesToBeEvaluated:
nodesToBeEvaluated.append(startNode)



system_font = getSystemFont()
#test
#test  = worldRectsList[7 + 0 * MATRIX_WIDTH]
#nodesEvaluated.append(test)


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

    currentNode = pathFinding(nodesToBeEvaluated, nodesEvaluated, goalNode, MATRIX_HEIGHT, MATRIX_WIDTH, pathList)
    # draw A* algorithm at work:
    estimateActualPath(currentNode)

    #draw nodes on the screen according to the natrix:
    drawMatrix(screen, matrix, MATRIX_HEIGHT, MATRIX_WIDTH, FIELD_SIZE, worldRectsList)

    # draw the nodes from nodesEvaluated list:
    drawNodesEvaluated(screen, MATRIX_HEIGHT, MATRIX_WIDTH, FIELD_SIZE, worldRectsList, nodesEvaluated) #RED

    #draw the nodes from nodesToBeEvaluated list:
    drawNodesToBeEvaluated(screen, MATRIX_HEIGHT, MATRIX_WIDTH, FIELD_SIZE, worldRectsList, nodesToBeEvaluated)  #YELLOW

    drawStartAndGoalNodes(screen, FIELD_SIZE, worldRectsList, startNode, goalNode)

    drawPath(screen, FIELD_SIZE, pathList)
    pathList.clear()

    #drawObjects(listOfObjectsToDraw)
    #drawControlableObject(player)
    fps_counter(screen, system_font)
    # Update the display
    pygame.display.update()
    # Control the frame rate
    clock.tick(60)

# Quit pygame
pygame.quit()
