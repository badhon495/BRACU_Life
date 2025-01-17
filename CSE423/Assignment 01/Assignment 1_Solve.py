#TASK 1
'''
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random

bg_clr = [0, 0, 0, 0]
rain_bend = 0.0
raindrops_arr = []

def raindrop(x1, y1):
    glColor3f(0.0, 0.0, .6)
    glLineWidth(2)
    glBegin(GL_LINES)
    glVertex2f(x1, y1)
    glVertex2f(x1, y1 - 14)  # lomba bristi
    glEnd()

def init_rain():
    for i in range(500):
        x = random.uniform(0, 500)
        y = random.uniform(0, 500)
        raindrops_arr.append((x, y))

def rain():
    global rain_bend
    for i in range(len(raindrops_arr)):
        update_x, update_y = raindrops_arr[i]
        update_x += rain_bend
        update_y -= 1 #rain going down
        
        #out of screen
        if update_y < 0:
            update_x, update_y = random.uniform(0, 500), random.uniform(0, 500)
        
        raindrops_arr[i] = (update_x, update_y)

def draw_house():
    glColor3f(0, 3.6, 0.0)
    glPointSize(5)
    glLineWidth(3)
    
    # roof
    glBegin(GL_TRIANGLES)
    glVertex2f(400, 250)
    glVertex2f(100, 250)
    glVertex2f(250, 325)
    glEnd()

    # body
    glBegin(GL_LINES)
    glVertex2f(380, 250)
    glVertex2f(380, 100)
    glVertex2f(120, 250)
    glVertex2f(120, 100)
    glVertex2f(120, 100)
    glVertex2f(380, 100)
    glEnd()

    # door
    glLineWidth(2)
    glBegin(GL_LINES)
    glVertex2f(350, 200)
    glVertex2f(350, 100)
    glVertex2f(300, 200)
    glVertex2f(300, 100)
    glVertex2f(300, 200)
    glVertex2f(350, 200)
    glEnd()

    # window
    glLineWidth(2)
    glBegin(GL_LINES)
    glVertex2f(150, 175)
    glVertex2f(150, 225)
    glVertex2f(200, 175)
    glVertex2f(200, 225)
    glVertex2f(150, 175)
    glVertex2f(200, 175)
    glVertex2f(200, 225)
    glVertex2f(150, 225)
    glVertex2f(175, 175)
    glVertex2f(175, 225)
    glVertex2f(150, 200)
    glVertex2f(200, 200)
    glEnd()

    # lock
    glPointSize(5)
    glBegin(GL_POINTS)
    glVertex2f(315, 150)
    glEnd()

def specialKeyListener(key, x, y):
    global rain_bend, bg_clr
    if key == GLUT_KEY_RIGHT:
        rain_bend += 0.5
        print("Rain Going Right")
    if key == GLUT_KEY_LEFT:
        rain_bend -= 0.5
        print("Rain Going Left")
    if key == GLUT_KEY_UP:
        for i in range(len(bg_clr)):
            bg_clr[i] -= 0.1
        print("Mental Peace")
    if key == GLUT_KEY_DOWN:
        for i in range(len(bg_clr)):
            bg_clr[i] += 0.1
        print("you psycho")

    glutPostRedisplay()

def animation():
    rain()
    glutPostRedisplay()

def iterate():
    glViewport(0, 0, 500, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

def showScreen():
    glClearColor(*bg_clr)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    draw_house()
    
    # Draw raindrops first
    for k in raindrops_arr:
        raindrop(k[0], k[1])
 
    glutSwapBuffers()

glutInit()
init_rain()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(500, 500)
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"Bristi")
glutDisplayFunc(showScreen)
glutIdleFunc(animation)
glutSpecialFunc(specialKeyListener)

glutMainLoop()
'''



#TASK 2
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random
import time

window_width = 500
window_height = 500
speed = 1
is_frozen = False
is_blinking = True
last_blink = time.time()
points = [] # List to store the points


def renderPoint(x, y, color):
    glPointSize(5)
    glBegin(GL_POINTS)
    glColor3f(color[0], color[1], color[2])
    glVertex2f(x, y)
    glEnd()


def generateRandomPoints(x, y):
    global points, speed
    color = [random.random(), random.random(), random.random()]
    direction_x, direction_y = random.choice([-1, 1]), random.choice([-1, 1])
    points.append({'x': x, 'y': y, 'color': color, 'speed': speed,
                  'dx': direction_x, 'dy': direction_y, 'blink': False})


def mouseClick(button, state, x, y):
    global points
    if button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
        for point in points:
            point['blink'] = not point['blink']
    elif button == GLUT_RIGHT_BUTTON and state == GLUT_DOWN:
        x, y = x, window_height - y
        generateRandomPoints(x, y)


def specialKeyListener(key, x, y):
    global points, speed, is_frozen
    if key == GLUT_KEY_UP:
        speed += 0.5
        print("I am speed")
    elif key == GLUT_KEY_DOWN and speed > 0.4:
        print("Getting old")
        speed -= 0.5
    for point in points:
        point['speed'] = speed


def KeyboardListener(key, x, y):
    global is_frozen
    if key == b' ':
        is_frozen = not is_frozen


def animate():
    global points, window_width, window_height, is_frozen
    if not is_frozen:
        for point in points:
            point['x'] += point['dx'] * point['speed']
            point['y'] += point['dy'] * point['speed']
            if point['x'] >= window_width or point['x'] <= 0:
                point['dx'] *= -1
            if point['y'] >= window_height or point['y'] <= 0:
                point['dy'] *= -1
    glutPostRedisplay()


def display():
    global points, is_blinking, last_blink
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glViewport(0, 0, window_width, window_height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, window_width, 0.0, window_height, 0.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    current_time = time.time()
    if current_time - last_blink >= 0.35:
        is_blinking = not is_blinking
        last_blink = current_time

    for point in points:
        if point['blink'] and is_blinking:
            renderPoint(point['x'], point['y'], [0, 0, 0])
        else:
            renderPoint(point['x'], point['y'], point['color'])
    glutSwapBuffers()


glutInit()
glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE)
glutInitWindowSize(window_width, window_height)
glutInitWindowPosition(0, 0)
glutCreateWindow(b"The Amazing Box")
glutDisplayFunc(display)
glutIdleFunc(animate)
glutSpecialFunc(specialKeyListener)
glutMouseFunc(mouseClick)
glutKeyboardFunc(KeyboardListener)
glutMainLoop()