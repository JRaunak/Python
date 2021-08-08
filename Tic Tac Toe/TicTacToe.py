import numpy as np
import pygame
from pygame import mouse

pygame.init()
screen = pygame.display.set_mode((606, 606))
pygame.display.set_caption('Tic Tac Toe')
Winning = [
            np.array([[1, 0, 0],
                      [0, 1, 0],
                      [0, 0, 1]]),

            np.array([[0, 0, 1],
                      [0, 1, 0],
                      [1, 0, 0]]),

            np.array([[1, 0, 0],
                      [1, 0, 0],
                      [1, 0, 0]]),

            np.array([[0, 1, 0],
                      [0, 1, 0],
                      [0, 1, 0]]),

            np.array([[0, 0, 1],
                      [0, 0, 1],
                      [0, 0, 1]]),

            np.array([[1, 1, 1],
                      [0, 0, 0],
                      [0, 0, 0]]),

            np.array([[0, 0, 0],
                      [1, 1, 1],
                      [0, 0, 0]]),

            np.array([[0, 0, 0],
                      [0, 0, 0],
                      [1, 1, 1]])
]
#Winning = load(open('Winnings.dat', 'rb'))
AllZero = np.zeros([3, 3])
def Grid():
    pygame.draw.line(screen, (70, 70, 210), (200, 0), (200, 606), 3)
    pygame.draw.line(screen, (70, 70, 210), (403, 0), (403, 606), 3)

    pygame.draw.line(screen, (70, 70, 210), (0, 200), (606, 200), 3)
    pygame.draw.line(screen, (70, 70, 210), (0, 403), (606, 403), 3)


def GetPos():
    return mouse.get_pos()[0]//203, mouse.get_pos()[1]//203


class Symbol():
    def __init__(self):
        self.click = False
        self.x = -250
        self.y = -250
        self.pos = (-2, -2)
        self.size = 90

    def SetPos(self):
        self.pos = mouse.get_pos()[0]//203, mouse.get_pos()[1]//203
        self.x = 203*self.pos[0]+100
        self.y = 203*self.pos[1]+100


class Zero(Symbol):
    sign = 'O'

    def Draw(self):
        pygame.draw.circle(screen, (255, 255, 255), (self.x, self.y), self.size, 8)


class Cross(Symbol):
    sign = 'X'

    def Draw(self):
        x11, y11 = self.x-(self.size-5), self.y-(self.size-5)
        x12, y12 = self.x+(self.size-5), self.y+(self.size-5)
        x21, y21 = self.x+(self.size-5), self.y-(self.size-5)
        x22, y22 = self.x-(self.size-5), self.y+(self.size-5)

        pygame.draw.line(screen, (255, 255, 255), (x11, y11), (x12, y12), 12)
        pygame.draw.line(screen, (255, 255, 255), (x21, y21), (x22, y22), 12)


def Pointer(symbol):
    x = mouse.get_pos()[0]
    y = mouse.get_pos()[1]
    if symbol == 'O':
        pygame.draw.circle(screen, (0, 255, 180), (x, y), 20, 4)
    elif symbol == 'X':
        x11, y11 = x-15, y-15
        x12, y12 = x+15, y+15
        x21, y21 = x+15, y-15
        x22, y22 = x-15, y+15

        pygame.draw.line(screen, (0, 255, 180), (x11, y11), (x12, y12), 7)
        pygame.draw.line(screen, (0, 255, 180), (x21, y21), (x22, y22), 7)


def GridState(List):
    state = AllZero
    for sym in List:
        if sym.click:
            if sym.sign == 'X':
                state[sym.pos] = 1
            elif sym.sign == 'O':
                state[sym.pos] = -1
    return state.T


def Winner(I):
    match = np.array(np.where(I == 1))
    match = np.array([match[:, 0], match[:, -1]])
    yi, xi = tuple(match[0])
    yf, xf = tuple(match[-1])
    Xi, Yi = 100+203*xi, 100+203*yi
    Xf, Yf = 100+203*xf, 100+203*yf
    pygame.draw.line(screen, (0, 255, 180), (Xi, Yi), (Xf, Yf), 20)


OX = [Zero()]
for _ in range(4):
    OX += [Cross(), Zero()]

i = 0
lim = 9
W = AllZero
Moves = []

running = True
while running:
    screen.fill((128, 128, 255))
    Grid()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if i != 9 and GetPos() not in Moves:
                OX[i].click = True
                OX[i].SetPos()
                i += 1
                Moves.append(GetPos())

        elif event.type == pygame.MOUSEBUTTONUP and 5 <= i <= lim:
            if i == 9:
                lim = 0
            for A in Winning:
                if np.all(A*GridState(OX) == A):
                    W = A
                    i = 9
                    break
                elif np.all(A*GridState(OX) == -A):
                    W = A
                    i = 9
                    break

    for o_x in OX:
        o_x.Draw()

    if not np.all(W == AllZero):
        Winner(W)

    try:
        if OX[i].sign == 'X':
            Pointer('X')
        elif OX[i].sign == 'O':
            Pointer('O')
    except:
        pass

    pygame.display.flip()