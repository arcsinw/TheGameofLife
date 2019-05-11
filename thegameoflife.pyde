grid_rows = 30
grid_cols = 40
cell_size = 20
fps = 30

isStart = False

# upon left is center point
# horizontal x
# vertical y
# grid[i][j] i is col, j is row

def setup():
    frameRate(fps)
    size(grid_cols * cell_size, grid_rows * cell_size)
    global grid_rows, grid_cols, grid
    grid = makeGrid()
    for i in xrange(grid_cols):
        for j in xrange(grid_rows):
            grid[i][j] = Cell(20*i, 20*j, 20, 20, False)
    
def draw():
    global grid_rows, grid_cols, grid, isStart
    background(0)
    
    for i in xrange(grid_cols):
        for j in xrange(grid_rows):
            #grid[i][j].oscillate()
            grid[i][j].display()
    
    if (isStart == True):
        evolve()
    
def makeGrid():
    global grid_rows, grid_cols
    grid = []
    for i in xrange(grid_cols):
        grid.append([])
        for j in xrange(grid_rows):
            grid[i].append(0)
    return grid

def mouseClicked():
    global grid_rows, grid_cols, grid
    
    x = mouseX / 20
    y = mouseY / 20
    if (x > grid_rows - 1):
        x = grid_rows - 1
    if x < 0:
        x = 0
        
    if (y > grid_cols - 1):
        y = grid_cols - 1
    if y < 0:
        y = 0
        
    if (mouseButton == LEFT):
        grid[x][y].setAlive()
    if (mouseButton == RIGHT):
        grid[x][y].setDead()
    
    print(getNeighborAlive(x,y))
    
def mouseDragged():
    global grid_rows, grid_cols, grid
    
    x = mouseX / 20
    y = mouseY / 20
    if (x > grid_rows - 1):
        x = grid_rows - 1
    if x < 0:
        x = 0
        
    if (y > grid_cols - 1):
        y = grid_cols - 1
    if y < 0:
        y = 0
    
    if (mouseButton == LEFT):
        grid[x][y].setAlive()
    if (mouseButton == RIGHT):
        grid[x][y].setDead()
    
def keyPressed():
    global isStart
    if (key == 'c'):
        clear()    
    
    # step
    if (key == 's'):
        evolve()
    
    # run/stop 
    if (key == ' '):
        if (isStart == True):
            isStart = False
        else: 
            isStart = True
    
# make all cells dead
def clear():
    for i in xrange(grid_cols):
        for j in xrange(grid_rows):
            grid[i][j].setDead()

def evolve():
    global grid
    new_grid = makeGrid()
    for i in xrange(grid_cols):
        for j in xrange(grid_rows):
            new_grid[i][j] = Cell(20*i, 20*j, 20, 20, False)
            
    for i in xrange(grid_cols):
        for j in xrange(grid_rows):
            if (grid[i][j].isAlive()):
                neightbor_alive_count = getNeighborAlive(i, j)
                if (2 == neightbor_alive_count or neightbor_alive_count == 3):
                    new_grid[i][j].setAlive()
                else:
                    new_grid[i][j].setDead()
            else:
                neightbor_alive_count = getNeighborAlive(i, j)
                if (neightbor_alive_count == 3):
                    new_grid[i][j].setAlive()

    grid = new_grid
    
# get alive neightbor's count of cell(x, y)
def getNeighborAlive(x, y):
    global grid_rows, grid_cols, grid
    count = 0
    
    for i in range(x-1, x+2):
        for j in range(y-1, y+2):
            if ((i < 0) or (j < 0) or 
                (i >= grid_cols - 1) or 
                    (j >= grid_rows - 1) or 
                        (i == x and j == y)) :
                continue
            else:
                if (grid[i][j].isAlive()):
                    count = count + 1

    return count

class Cell():
    # A cell object knows about its location in the grid 
    # it also knows of its size with the variables x,y,w,h.
    def __init__(self, tempX, tempY, tempW, tempH, alive):
        self.x = tempX
        self.y = tempY
        self.w = tempW
        self.h = tempH
        self.alive = alive
    
    def isAlive(self):
        return self.alive
    
    def setAlive(self):
        self.alive = True
    
    def setDead(self):
        self.alive = False
    
    def setState(self):
        if(self.alive == True):
            self.alive = False
        else:
            self.alive = True
     
    def display(self):
        stroke(200)
        fill(255)
        
        if (self.alive == True):
            fill(0)    

        rect(self.x,self.y,self.w,self.h)
