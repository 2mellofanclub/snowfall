import shutil, time
from random import randint, choice


COLCOUNT, LINECOUNT = shutil.get_terminal_size()
SCREEN = []
FLAKES = []
WIND = {"turns":0, "strength":0}
for y in range(LINECOUNT):
    SCREEN.append([])
    for x in range(COLCOUNT):
        SCREEN[y].append(" ")



def reset_screen():
    for y in range(LINECOUNT):
        for x in range(COLCOUNT):
            SCREEN[y][x] = " "

def print_screen():
    for y in range(LINECOUNT):
        print("".join(SCREEN[y]))

def roll_two_dice(a):
    a = int(a)
    return randint(1,a) + randint(1,a)

def wind():
    if WIND["turns"] > 0:
        WIND["turns"] -= 1
    elif randint(1,15) == 8:
        WIND["turns"] = randint(3,5)
        WIND["strength"] = randint(1,3) * choice([-1, 1])
    else:
        WIND["strength"] = 0


class Flake:
    def __init__(self, startx):
        self.shape = "*"
        if randint(1,20) == 20:
            self.shape = "#"
        self.posx = startx
        self.posy = 0
        self.done = False
    def get_shape(self):
        return self.shape
    def get_x(self):
        return self.posx
    def get_y(self):
        return self.posy
    def jitter(self, wind):
        nextx = self.posx + (choice([-1,1])+wind)
        if nextx < 0:
            nextx = 0
        elif nextx > COLCOUNT-1:
            nextx = COLCOUNT-1
        return nextx
    def update(self):
        if self.done:
            pass
        elif self.posy < LINECOUNT-1:
            nexty = self.posy+1
            nextx = self.jitter(WIND["strength"])
            if SCREEN[nexty][nextx] == " ":
                self.posx = nextx
                self.posy = nexty
            else:
                self.done = True




while True:
    reset_screen()
    wind()
    FLAKES.append(Flake(roll_two_dice(COLCOUNT/2)))
    for flake in FLAKES:
        flake.update()
        SCREEN[flake.get_y()][flake.get_x()] = flake.get_shape()
    print_screen()
    time.sleep(0.8)
