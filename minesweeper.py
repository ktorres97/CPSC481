'''
Hey gang, go down to line 395, thats where my changes take place
'''

import random
import pygame
import time
pygame.init()

RED = (255,0,0)
ORANGE = (255,127,0)
YELLOW = (255,255,0)
WHITE = (255,255,255)
GREY = (127,127,127)
BLACK = (0,0,0)
BLUE = (76,76,255)
GREEN = (0,255,0)

size = (500,600)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Minesweeper")

done = False
startMode = True
guessMode = True

clock = pygame.time.Clock()

font = pygame.font.Font(None,20)

mouse_state = 0
mouse_x = 0
mouse_y = 0

cColumns = 0
cRows = 0
cMines = 0

gameState = -1

class Button():
    def __init__(self):
        self.textBoxes = {}

    #----Clicked In----
    def clickedIn(self,x,y,width,height):
        global mouse_state, mouse_x, mouse_y
        if mouse_state == 1 and mouse_x >= x and mouse_x <= (x + width) and mouse_y >= y and mouse_y <= (y + height):
            return True

    #----Clicked Out----
    def clickedOut(self,x,y,width,height):
        global mouse_state, mouse_x, mouse_y
        if mouse_state == 1 and mouse_x < x or mouse_state == 1 and mouse_x > (x + width) or mouse_state == 1 and mouse_y < y or mouse_state == 1 and mouse_y > (y + height):
            return True

    #----Hovering----
    def hovering(self,x,y,width,height):
        global mouse_state, mouse_x, mouse_y
        if mouse_state == 0 and mouse_x >= x and mouse_x <= (x + width) and mouse_y >= y and mouse_y <= (y + height):
            return True

    #----Click Button----
    def clickButton(self,x,y,width,height,normalColor,hoverColor,textFont,text,textColor,stateHolding = False,stateVariable = 0,state = 1):
        if not self.clickedIn(x,y,width,height) and not self.hovering(x,y,width,height):
            pygame.draw.rect(screen,normalColor,(x,y,width,height))
        elif self.hovering(x,y,width,height):
            pygame.draw.rect(screen,hoverColor,(x,y,width,height))
        if stateHolding == True and stateVariable == state:
            pygame.draw.rect(screen,hoverColor,(x,y,width,height))
        buttonText = textFont.render(text,True,textColor)
        buttonText_x = buttonText.get_rect().width
        buttonText_y = buttonText.get_rect().height
        screen.blit(buttonText,(((x + (width / 2)) - (buttonText_x / 2)),((y + (height / 2)) - (buttonText_y / 2))))
        if self.clickedIn(x,y,width,height):
            return True

button = Button()

def infoBar():
    global gameState
    pygame.draw.rect(screen,GREY,(0,0,500,100))
    pygame.draw.line(screen,BLACK,(0,100),(500,100),4)

    if gameState == 0:
        text = font.render("MINES: " + str(game.nummines),True,BLACK)
        text_x = text.get_rect().width
        text_y = text.get_rect().height
        screen.blit(text,((150 - (text_x / 2)),(50 - (text_y / 2))))
        text = font.render("FLAGS: " + str(game.numflaged),True,BLACK)
        text_x = text.get_rect().width
        text_y = text.get_rect().height
        screen.blit(text,((350 - (text_x / 2)),(50 - (text_y / 2))))
    elif gameState == 1:      #win
        text = font.render("YOU  WIN",True,BLACK)
        text_x = text.get_rect().width
        text_y = text.get_rect().height
        screen.blit(text,((150 - (text_x / 2)),(50 - (text_y / 2))))
    elif gameState == 2:    #loose
        text = font.render("YOU  LOSE",True,BLACK)
        text_x = text.get_rect().width
        text_y = text.get_rect().height
        screen.blit(text,((150 - (text_x / 2)),(50 - (text_y / 2))))

    if gameState == 1 or gameState == 2:
        if button.clickButton(325,25,150,50,RED,ORANGE,font,"RESET",BLACK):
            gameState = -1
            game.reset(0,0,0)

def menu():
    global gameState
    screen.fill(GREY)
    text = font.render("MINE",True,BLACK)
    text_x = text.get_rect().width
    text_y = text.get_rect().height
    screen.blit(text,((250 - (text_x / 2)),(100 - (text_y / 2))))
    text = font.render("SWEEPER",True,BLACK)
    text_x = text.get_rect().width
    text_y = text.get_rect().height
    screen.blit(text,((250 - (text_x / 2)),(150 - (text_y / 2))))
    if button.clickButton(200,250,100,50,RED,ORANGE,font,"EASY",BLACK):
        game.reset(5,5,5)
        gameState = 0
    if button.clickButton(200,310,100,50,RED,ORANGE,font,"MEDIUM",BLACK):
        game.reset(10,10,15)
        gameState = 0
    if button.clickButton(200,370,100,50,RED,ORANGE,font,"HARD",BLACK):
        game.reset(15,15,30)
        gameState = 0
    if button.clickButton(200,430,100,50,RED,ORANGE,font,"CUSTOM",BLACK):
        gameState = -2

def custom():
    global cColumns, cRows, cMines, gameState
    text = font.render("COLUMNS: " + str(cColumns),True,BLACK)
    text_x = text.get_rect().width
    text_y = text.get_rect().height
    screen.blit(text,((225 - (text_x / 2)),(180 - (text_y / 2))))
    if button.clickButton(300,160,20,20,RED,ORANGE,font," /\ ",BLACK):
        if cColumns < 20:
            cColumns += 1
    if button.clickButton(300,180,20,20,RED,ORANGE,font," \/ ",BLACK):
        if cColumns > 0:
            cColumns -= 1
    text = font.render("ROWS: " + str(cRows),True,BLACK)
    text_x = text.get_rect().width
    text_y = text.get_rect().height
    screen.blit(text,((230 - (text_x / 2)),(260 - (text_y / 2))))
    if button.clickButton(300,240,20,20,RED,ORANGE,font," /\ ",BLACK):
        if cRows < 20:
            cRows += 1
    if button.clickButton(300,260,20,20,RED,ORANGE,font," \/ ",BLACK):
        if cRows > 0:
            cRows -= 1
    text = font.render("MINES: " + str(cMines),True,BLACK)
    text_x = text.get_rect().width
    text_y = text.get_rect().height
    screen.blit(text,((230 - (text_x / 2)),(340 - (text_y / 2))))
    if button.clickButton(300,320,20,20,RED,ORANGE,font," /\ ",BLACK):
        if cMines < 50 and cMines < (cColumns * cRows):
            cMines += 1
    if button.clickButton(300,340,20,20,RED,ORANGE,font," \/ ",BLACK):
        if cMines > 0:
            cMines -= 1
    if button.clickButton(200,390,100,60,RED,ORANGE,font,"START",BLACK):
        #game.reset(cColumns,cRows,cMines)
        game.reset(10,10,5)
        gameState = 0


class Tile():
    def __init__(self,x,y,columns,rows):
        self.columns = columns
        self.rows = rows
        self.x = (x * (size[0] / self.columns))
        self.y = (y * ((size[1] - 100) / self.rows)) + 100
        self.mine = False
        self.neighbors = 0
        self.visible = False
        self.flag = False
        self.unknown = True

    def update(self):
        global gameState
        if gameState == 0:
            if mouse_state == 1 and mouse_x >= self.x and mouse_x <= (self.x + (size[0] / self.columns)) and mouse_y >= self.y and mouse_y <= (self.y + ((size[1] - 100) / self.rows)):
                self.visible = True
                self.flag = False
            if mouse_state == 3 and mouse_x >= self.x and mouse_x <= (self.x + (size[0] / self.columns)) and mouse_y >= self.y and mouse_y <= (self.y + ((size[1] - 100) / self.rows)):
                if self.flag == False:
                    self.flag = True
                elif self.flag == True:
                    self.flag = False
            if self.visible == True and self.mine == True:
                gameState = 2


    def show(self):
        if self.flag == True:
            pygame.draw.rect(screen,YELLOW,(self.x,self.y,(size[0] / self.columns),((size[1] - 100) / self.rows)))
        if self.visible == True:
            if self.mine == False:
                pygame.draw.rect(screen,GREY,(self.x,self.y,(size[0] / self.columns),((size[1] - 100) / self.rows)))
                if self.neighbors > 0:
                    text = font.render(str(self.neighbors),True,BLACK)
                    text_x = text.get_rect().width
                    text_y = text.get_rect().height
                    screen.blit(text,((self.x + ((size[0] / self.columns) / 2) - (text_x / 2)),(self.y + (((size[1] - 100) / self.rows) / 2) - (text_y / 2))))

            elif self.mine == True:
                pygame.draw.rect(screen,RED,(self.x,self.y,(size[0] / self.columns),((size[1] - 100) / self.rows)))

        pygame.draw.rect(screen,BLACK,(self.x,self.y,(size[0] / self.columns),((size[1] - 100) / self.rows)),2)

    #Fixes the render issue for traversing though the revealed points
    def showAI(self):
        if self.flag == True:
            pygame.draw.rect(screen,YELLOW,(self.x,self.y,(size[0] / self.columns),((size[1] - 100) / self.rows)))
        if self.visible == True:
            if self.mine == True:
                pygame.draw.rect(screen,RED,(self.x,self.y,(size[0] / self.columns),((size[1] - 100) / self.rows)))

        pygame.draw.rect(screen,BLACK,(self.x,self.y,(size[0] / self.columns),((size[1] - 100) / self.rows)),2)


class Game():
    def __init__(self,columns,rows,mines):
        self.columns = columns
        self.rows = rows
        self.nummines = mines
        self.board = []
        self.mines = []
        self.minenum = len(self.mines)
        self.neighbnum = 0
        self.numflaged = 0
        self.numvis = 0
        self.foundmines = 0
        self.proboard = []

        #creating board
        for y in range(self.rows):
            self.board.append([])
            for x in range(self.columns):
                self.board[y].append(Tile(x,y,self.columns,self.rows))

        #placing mines
        while self.minenum < self.nummines:
            self.mineloc = [random.randrange(self.columns),random.randrange(self.rows)]
            if self.board[self.mineloc[1]][self.mineloc[0]].mine == False:
                self.mines.append(self.mineloc)
                self.board[self.mineloc[1]][self.mineloc[0]].mine = True
            self.minenum = len(self.mines)

        #neighbors
        for y in range(self.rows):
            for x in range(self.columns):
                self.neighbnum = 0
                if y > 0 and x > 0:
                    if self.board[y-1][x-1].mine == True:
                        self.neighbnum += 1
                if y > 0:
                    if self.board[y-1][x].mine == True:
                        self.neighbnum += 1
                if y > 0 and x < (self.columns - 1):
                    if self.board[y-1][x+1].mine == True:
                        self.neighbnum += 1
                if x > 0:
                    if self.board[y][x-1].mine == True:
                        self.neighbnum += 1
                if x < (self.columns - 1):
                    if self.board[y][x+1].mine == True:
                        self.neighbnum += 1
                if x > 0 and y < (self.rows - 1):
                    if self.board[y+1][x-1].mine == True:
                        self.neighbnum += 1
                if y < (self.rows - 1):
                    if self.board[y+1][x].mine == True:
                        self.neighbnum += 1
                if x < (self.columns - 1) and y < (self.rows - 1):
                    if self.board[y+1][x+1].mine == True:
                        self.neighbnum += 1
                self.board[y][x].neighbors = self.neighbnum

    def update(self):
        global gameState
        self.numflaged = 0
        self.numvis = 0
        self.foundmines = 0
        for y in range(self.rows):
            for x in range(self.columns):
                self.board[y][x].update()
                if self.board[y][x].neighbors == 0 and self.board[y][x].visible == True:
                    if y > 0 and x > 0:
                        self.board[y-1][x-1].visible = True
                    if y > 0:
                        self.board[y-1][x].visible = True
                    if y > 0 and x < (self.columns - 1):
                        self.board[y-1][x+1].visible = True
                    if x > 0:
                        self.board[y][x-1].visible = True
                    if x < (self.columns - 1):
                        self.board[y][x+1].visible = True
                    if x > 0 and y < (self.rows - 1):
                        self.board[y+1][x-1].visible = True
                    if y < (self.rows - 1):
                        self.board[y+1][x].visible = True
                    if x < (self.columns - 1) and y < (self.rows - 1):
                        self.board[y+1][x+1].visible = True
                if self.board[y][x].flag == True:
                    self.numflaged += 1
                if self.board[y][x].visible == True:
                    self.numvis += 1
        for mine in self.mines:
            if self.board[mine[1]][mine[0]].flag == True:
                self.foundmines += 1
        if self.numflaged == self.nummines and self.foundmines == self.nummines and self.numvis == ((self.columns * self.rows) - self.nummines):
            gameState = 1
        if gameState == 1 or gameState == 2:
            for y in range(self.rows):
                for x in range(self.columns):
                    self.board[y][x].visible = True


    def render(self):
        for y in range(self.rows):
            for x in range(self.columns):
                self.board[y][x].show()
    #Fixes the render issue for traversing though the revealed points
    def renderAI(self, x, y):
        self.board[y][x].showAI()

    def reset(self,columns,rows,mines):
        if columns != 0 and rows != 0 and mines != 0:
            self.columns = columns
            self.rows = rows
            self.nummines = mines
        self.board = []
        self.mines = []
        self.minenum = len(self.mines)
        self.neighbnum = 0
        self.numflaged = 0
        self.numvis = 0
        self.foundmines = 0

        #creating board
        for y in range(self.rows):
            self.board.append([])
            for x in range(self.columns):
                self.board[y].append(Tile(x,y,self.columns,self.rows))

        #placing mines
        while self.minenum < self.nummines:
            self.mineloc = [random.randrange(self.columns),random.randrange(self.rows)]
            if self.board[self.mineloc[1]][self.mineloc[0]].mine == False:
                self.mines.append(self.mineloc)
                self.board[self.mineloc[1]][self.mineloc[0]].mine = True
            self.minenum = len(self.mines)

        #neighbors
        for y in range(self.rows):
            for x in range(self.columns):
                self.neighbnum = 0
                if y > 0 and x > 0:
                    if self.board[y-1][x-1].mine == True:
                        self.neighbnum += 1
                if y > 0:
                    if self.board[y-1][x].mine == True:
                        self.neighbnum += 1
                if y > 0 and x < (self.columns - 1):
                    if self.board[y-1][x+1].mine == True:
                        self.neighbnum += 1
                if x > 0:
                    if self.board[y][x-1].mine == True:
                        self.neighbnum += 1
                if x < (self.columns - 1):
                    if self.board[y][x+1].mine == True:
                        self.neighbnum += 1
                if x > 0 and y < (self.rows - 1):
                    if self.board[y+1][x-1].mine == True:
                        self.neighbnum += 1
                if y < (self.rows - 1):
                    if self.board[y+1][x].mine == True:
                        self.neighbnum += 1
                if x < (self.columns - 1) and y < (self.rows - 1):
                    if self.board[y+1][x+1].mine == True:
                        self.neighbnum += 1
                self.board[y][x].neighbors = self.neighbnum

    #This function returns the coordinates of the unrevealed neighbors
    #of a given coordinate on the grid
    def getNumOfHiddenNeigbors(self, x, y):
        result = []
        if(x > 0):
            if self.board[x-1][y].visible != True:
                coords = tuple([x-1,y])
                result.append(coords)
        if(y > 0):
            if(self.board[x][y-1].visible != True):
                coords = tuple([x,y-1])
                result.append(coords)
        if(x < self.rows - 1):
            if(self.board[x+1][y].visible != True):
                coords = tuple([x+1,y])
                result.append(coords)
        if(y < self.columns - 1):
            if(self.board[x][y+1].visible != True):
                coords = tuple([x,y+1])
                result.append(coords)
        if(x < self.rows - 1 and y < self.columns - 1):
            if(self.board[x+1][y+1].visible != True):
                coords = tuple([x+1,y+1])
                result.append(coords)
        if(x > 0 and y > 0):
            if(self.board[x-1][y-1].visible != True):
                coords = tuple([x-1,y-1])
                result.append(coords)
        if(x < self.rows - 1 and y > 0):
            if(self.board[x+1][y-1].visible != True):
                coords = tuple([x+1,y-1])
                result.append(coords)
        if(x > 0 and y < self.columns - 1):
            if(self.board[x-1][y+1].visible != True):
                coords = tuple([x-1,y+1])
                result.append(coords)
        return result

    #this function returns an array of flags that have been placed
    #I dont think I actually used this function
    def getArrayOfFlags(self, coords):
        flags = []
        for coord in coords:
            x = coord[0]
            y = coord[1]
            if self.board[x][y].flag == True:
                flags.append(coord)
        return flags

    def getNumOfFlags(self, neighbs):

        count = 0
        for neighb in neighbs:
            x = neighb[0]
            y = neighb[1]
            if self.board[x][y].flag == True:
                count += 1
        return count

    #This function checks to see if a point on the grid has been satisfied
    def isSatisfied(self, x, y):

            neighbs = self.getNumOfHiddenNeigbors(x,y)
            flagCount = self.getNumOfFlags(neighbs)
            if(len(neighbs) == flagCount):
                return True
            return False

    #returns an array of all of the revealed points on the grid
    def getAllRevealed(self):
        revealed = []
        x = 0
        y = 0
        while x < self.rows:
            while y < self.columns:
                if self.board[x][y].visible == True and self.isSatisfied(x,y) == False:
                    coord = tuple([x,y])
                    revealed.append(coord)
                y += 1
            x += 1
            y = 0
        return revealed

    #returns an array of all unrevealed points on the graph
    def getAllUnrevealed(self):
        unrevealed = []
        x = 0
        y = 0
        while x < self.rows:
            while y < self.columns:
                if self.board[x][y].visible == False:
                    coord = tuple([x,y])
                    unrevealed.append(coord)
                y += 1
            x += 1
            y = 0
        return unrevealed

    #flags the neighbors
    def flagNeighbors(self, coords):
        for coord in coords:
            x = coord[0]
            y = coord[1]
            self.board[x][y].flag = True
            infoBar()
            self.update()

    #This function reveals the neighbors that are 100% forsure not mines
    def revealNeigborsWithouFlags(self, neighbors):
        for neigb in neighbors:
            x = neigb[0]
            y = neigb[1]
            xval = game.board[x][y].x
            yval = game.board[x][y].y
            time.sleep(.2)
            if self.board[x][y].flag == False:
                pygame.draw.rect(screen,GREEN,(xval,yval,(size[0] / game.columns),((size[1] - 100) / game.rows)))
                pygame.draw.rect(screen, BLACK, [xval,yval,(size[0] / game.columns),((size[1] - 100) / game.rows)], 3)
                infoBar()
                game.update()
                game.renderAI(x,y)
                pygame.display.flip()
                time.sleep(.2)
                self.board[x][y].visible = True
                infoBar()
                self.update()
                self.renderAI(x,y)
                pygame.display.flip()
                time.sleep(.5)

    #Identify tiles around the targeted tile
    def checkSurrounding(self, x, y):
        surrounding = []
        if(x>0 and self.board[x-1][y].visible!=True and self.board[x-1][y].flagged!=True):
            surrounding.add(self.board[x-1][y])
        if(x<self.rows-1 and self.board[x+1][y].visible!=True and self.board[x+1][y].flagged!=True):
            surrounding.add(self.board[x+1][y])
        if(x>0 and y>0 and self.board[x-1][y-1].visible!=True and self.board[x-1][y-1].flagged!=True):
            surrounding.add(self.board[x-1][y-1])
        if(x<self.rows-1 and y>0 and self.board[x+1][y-1].visible!=True and self.board[x+1][y-1].flagged!=True):
            surrounding.add(self.board[x+1][y-1])
        if(x>0 and y<self.columns-1 and self.board[x-1][y+1].visible!=True and self.board[x-1][y+1].flagged!=True):
            surrounding.add(self.board[x-1][y+1])
        if(x<self.rows-1 and y<self.columns-1 and self.board[x+1][y+1].visible!=True and self.board[x+1][y+1].flagged!=True):
            surrounding.add(self.board[x+1][y+1])
        if(y>0 and self.board[x][y-1].visible!=True and self.board[x][y-1].flagged!=True):
            surrounding.add(self.board[x][y-1])
        if(y<self.columns-1 and self.board[x][y+1].visible!=True and self.board[x][y+1].flagged!=True):
            surrounding.add(self.board[x][y+1])
        return surrounding

    #Add new group of tiles to groups
    def join(self, newGroup, x, y):
        newGroup.add(self.board[x][y])
        for i in range(self.rows):
            for j in range(self.colums):
                if self.board[i][j].visible and self.board[i][j].flagged!=True and self.board[i][j] not in newGroup:
                    for k in range(8-self.board[i][j].neighbors):
                        surroundingGiven = checkSurrounding(x,y)
                        surroundingNew = checkSurrounding(i,j)
                        if surroundingNew[k] in surroundingGiven:
                            join(newGroup, i,j)

    #Solve the group of tiles
    def solveGroup(self, group):
        hiding = []
        for i in range(len(group)):
            pass


    #Assign probability of being a mine for all hidden spaces
    def calcProbabilities(self):
        unknownAmount = 0
        for x in range(self.rows):
            for y in range(self.columns):
                #Look at surrounding tiles
                if self.board[x][y].visible is True:
                    tileUnknown = True
                    self.board[x][y].unknown = True
                    if x>0 and self.board[x-1][y].visible: tileUnknown=False
                    if x<self.rows-1 and self.board[x+1][y].visible: tileUnknown=False
                    if x>0 and y>0 and self.board[x-1][y-1].visible: tileUnknown=False
                    if x<self.rows-1 and j>0 and self.board[x+1][y-1].visible: tileUnknown=False
                    if x>0 and j<self.columns-1 and self.board[x-1][y+1].visible: tileUnknown=False
                    if x<self.rows-1 and j<self.columns-1 and self.board[x+1][y+1].visible: tileUnknown=False
                    if j<self.colums-1 and self.board[x][y+1].visible: tileUnknown=False
                    if j>0 and self.board[x][j-1].visible: tileUnknown=False
                    if tileUnknown is True:
                        self.board[x][y].unknown = False
                        unknownAmount+=1

        #Group areas together so we can identify relationships
        groups = []
        for x in range(self.rows):
            for y in range(self.columns):
                if self.board[x][y].visible and self.board[x][y].flagged!=True and self.board[x][y].neighbors!=8:
                    owned = False
                    for z in range(group):
                        if self.board[x][y] in group[z]:
                            owned = True
                            break
                    if owned!=True:
                        newGroup = []
                        join(newGroup, x, y)
                        group.add(newGroup)


        #See possible positions of mines

        #Combine all sections' solutions

        #Find probability of each cell being a mine



    #Return probabily board
    def getProboard(self):
        return self.proboard

    def getRows(self):
        return self.rows

    def getColumns(self):
        return self.columns

    def remainingMines(self):
        return self.minenum


game = Game(5,5,5)
#def mineAi(game):

#This is the function you guys need to impliment. At the moment all it does is pick a random unrevealed point on the graph
#and if that point is not revealed then it will reveal it. You guys need to make it calculate the odds of
#each unrevealed point on the graph and pick the one that is LEAST likely to be a mine.
def guessMode(game):
    if game.remainingMines() > 50:
        #pick random
        pass
    else:
        game.calcProbabilities()
        proboard = game.getProboard()
        rows = game.getRows()
        columns = game.getColumns()
        min = 1
        x_coor = 0
        y_coor = 0
        for x in range(rows):
            for y in range(columns):
                if (proboard[x][y].flagged is False and proboard[x][y] is True and
                    proboard[x][y].probability < min):
                    min = proboard[x][y].probability
                    x_coor = x
                    y_coor = y
        #choose tile at xy
        self.board[x][y].visible = True



#traverses through the revealed points on the grid
def traverseThoughRevealed(game, coords):
    for coord in coords:
        x = coord[0]
        y = coord[1]
        xval = game.board[x][y].x
        yval = game.board[x][y].y

        #gets neighbors
        neighbs = game.getNumOfHiddenNeigbors(x,y)
        #draws blue rectangle with black border indicating where the AI is looking
        pygame.draw.rect(screen,BLUE,(xval,yval,(size[0] / game.columns),((size[1] - 100) / game.rows)))
        pygame.draw.rect(screen, BLACK, [xval,yval,(size[0] / game.columns),((size[1] - 100) / game.rows)], 3)
        if(game.board[x][y].neighbors > 0):
            #if the point on the graph has neighbors write the number over the Blue rectangle
            text = font.render(str(game.board[x][y].neighbors),True,BLACK)
            text_x = text.get_rect().width
            text_y = text.get_rect().height
            screen.blit(text,((game.board[x][y].x + ((size[0] / game.columns) / 2) - (text_x / 2)),(game.board[x][y].y + (((size[1] - 100) / game.rows) / 2) - (text_y / 2))))
        #these next 4 lines update everything
        infoBar()
        game.update()
        game.renderAI(x,y)
        pygame.display.flip()

        #if there are neighbors that havent been revealed the AI lookss at the,
        if len(neighbs) > 0:
            drawNeighbors(game,neighbs)
            infoBar()
            game.update()
            game.renderAI(x,y)
            pygame.display.flip()

            #when we know forsure to flag neighbors
            if(len(neighbs) == game.board[x][y].neighbors):
                game.flagNeighbors(neighbs)

            #get array of flags
            flags = game.getArrayOfFlags(neighbs)
            #if there are a sufficient number of flags reveal all other points
            if(len(flags) == game.board[x][y].neighbors):
               game.revealNeigborsWithouFlags(neighbs)

            time.sleep(.5)
        time.sleep(.05)
        game.render()
        pygame.display.flip()

#draws out the orange outline indicating the neighbors that the AI is looking at
def drawNeighbors(game, coords):
    for coord in coords:
        x = coord[0]
        y = coord[1]
        xval = game.board[x][y].x
        yval = game.board[x][y].y
        pygame.draw.rect(screen, ORANGE, [xval,yval,(size[0] / game.columns),((size[1] - 100) / game.rows)], 3)

def shouldEnterGuessMode(game, revOne, revTwo):

    if(len(revOne) != len(revTwo)):
        return False

    n = len(revTwo)
    for i in range(0,n-1):

        xOne = revOne[i][0]
        yOne = revOne[i][1]
        xTwo = revTwo[i][0]
        yTwo = revTwo[i][1]
        neighbsOne = game.getNumOfHiddenNeigbors(xOne,yOne)
        neighbsTwo = game.getNumOfHiddenNeigbors(xTwo,yTwo)

        if(len(neighbsOne) != len(neighbsTwo)):
            return False

        if game.getNumOfFlags(neighbsOne) != game.getNumOfFlags(neighbsTwo):
            return False

    return True


while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_state = event.button
            pygame.mouse.set_pos(mouse_x,mouse_y + 1)
        else:
            mouse_state = 0

    mouse_x = pygame.mouse.get_pos()[0]
    mouse_y = pygame.mouse.get_pos()[1]

    screen.fill(WHITE)

    if gameState == -1:
        menu()

    elif gameState == -2:
        custom()

    elif gameState >= 0 and gameState <= 2:

        infoBar()
        game.update()
        game.render()
        pygame.display.flip()
        if(gameState == 1 or gameState == 2):
            #startmode basically looks for an initial point to reveal, right now i just do the most middle point
            infoBar()
            game.update()
            game.render()
            pygame.display.flip()

        else:
            if(startMode):
                guessMode(game)
                startMode = False
                infoBar()
                game.update()
                game.render()
                pygame.display.flip()
                if(gameState != 2 and gameState != 1):
                    newRev = game.getAllRevealed()
                    traverseThoughRevealed(game,newRev)
            else:
                infoBar()
                game.update()
                game.render()
                pygame.display.flip()
                #get all revealed points and traverse through them
                oldRev = newRev
                newRev = game.getAllRevealed()

                if(shouldEnterGuessMode(game,oldRev,newRev)):
                    guessMode(game)
                else:
                    traverseThoughRevealed(game,newRev)



    pygame.display.flip()

    clock.tick(60)

pygame.quit()
