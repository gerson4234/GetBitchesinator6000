import numpy as np
from cmu_graphics import *

app.url = 'https://i.redd.it/f525g7i750n81.png'
Image(app.url, -20, -150)

num = 5
start = 1
end = 20
def size(num, start, end):
    randSize = []
    for j in range(num):
        randSize.append(np.random.randint(start, end))
    return randSize

b1 = 2
s1 = 0
e1 = 390
def location1(b1, s1, e1):
    rand1 = []
    for j in range(b1):
        rand1.append(np.random.randint(s1, e1))
    return rand1

b2 = 2
s2 = 0
e2 = 390
def location2(b2, s2, e2):
    rand2 = []
    for j in range(b2):
        rand2.append(np.random.randint(s2, e2))
    return rand2

b3 = 2
s3 = 0
e3 = 390
def location3(b3, s3, e3):
    rand3 = []
    for j in range(b3):
        rand3.append(np.random.randint(s3, e3))
    return rand3
b4 = 2
s4 = 0
e4 = 390
def location4(b4, s4, e4):
    rand4 = []
    for j in range(b4):
        rand4.append(np.random.randint(s4, e4))
    return rand4

b5 = 2
s5 = 0
e5 = 390
def location5(b5, s5, e5):
    rand5 = []
    for j in range(b5):
        rand5.append(np.random.randint(s5, e5))
    return rand5

coord1 = location1(b1, s1, e1)
coord2 = location2(b2, s2, e2)
coord3 = location3(b3, s3, e3)
coord4 = location4(b4, s4, e4)
coord5 = location5(b5, s5, e5)
rndmSize = size(num, start, end)

bitch1 = Circle(coord1[0], coord1[1], rndmSize[1], fill = 'black')
bitch2 = Circle(coord2[0], coord2[1], rndmSize[4], fill = 'black')
bitch3 = Circle(coord3[0], coord3[1], rndmSize[2], fill = 'black')
bitch4 = Circle(coord4[0], coord4[1], rndmSize[3], fill = 'black')
bitch5 = Circle(coord5[0], coord5[1], rndmSize[0], fill = 'black')


bitchFinder = Line(400, 0, 0, 0, fill='black', lineWidth=2, opacity=100, visible=False)
counter = Label(0, 300, 300, size = 25, fill = 'yellow')
message = Label("You get no bitches.", 250, 350, size = 20, fill = 'yellow')
def onMousePress(x, y):
    if (x == coord1[0] and y == coord1[1]):
        bitch1.visible = False
        counter.value += 1
    if (x == coord2[0] and y == coord2[1]):
        bitch2.visible = False
        counter.value += 1
    if (x == coord3[0] and y == coord3[1]):
        bitch3.visible = False
        counter.value += 1
    if (x == coord4[0] and y == coord4[1]):
        bitch4.visible = False
        counter.value += 1
    if (x == coord5[0] and y == coord5[1]):
        bitch5.visible = False
        counter.value += 1
    if (counter.value == 1):
        message.value = "You got a bitch, not bitches."
    if (counter.value >= 2):
        message.value = "Nicely done, but you can still get more."
    if (counter.value == 5):
        message.value = "Okay you're done you did it"
    if (counter.value >= 6):
        message.value = "Uh hey I think that's enough bitches..."
    if (counter.value == 8):
        message.value = "Stop"
    if (counter.value > 8):
        message.value = "WTF"
    if (counter.value == 10):
        message.value = "This game is not for you. Leave."
    if (counter.value > 10):
        quit()
    
cmu_graphics.run()