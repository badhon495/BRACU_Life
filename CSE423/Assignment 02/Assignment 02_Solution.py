from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLUT.fonts import GLUT_BITMAP_HELVETICA_18
import random
import time
import math


# Global Game State Variables
W_WIDTH, W_HEIGHT = 500, 800 # Window dimensions
bullet_list = [] # List of active bullets.
bubble_list = [] # List of active bubbles. There will be 3-5 bubbles at any given time.
score = 0 # Player score.
misfires = 0 # Number of misfires. Game ends after 3 misfires.
freeze = False # Game freeze state. When True, game is paused.
gameover = 0 # Game over state. When 3, game is over. To make the game end, set to 3. 
last_frame_time = 0 # Time of last frame for delta time calculation. 
bullet_speed = 300 # Speed of bullets in pixels per second. In the final game, this will be increased as the game progresses.
rocket_x = 0 # X-coordinate of the rocket. The rocket moves left and right to shoot bubbles.


############################################################################################################
# The create_bubble function is designed to generate a new bubble with unique positioning and optional dynamic sizing. This function ensures that the new bubble does not overlap with any existing bubbles in the game.
def create_bubble(existing_bubbles):
    is_dynamic = random.random() < 0.2 # 20% chance of creating a dynamic bubble.
    r = random.randint(20, 25) # Random radius between 20 and 25 for normal bubbles.
    color = [1, 1, 0] # Default color for normal bubbles. Yellow.
    if is_dynamic: # If the bubble is dynamic, set the color to red.
        color = [1, 0, 0]
    while True:
        x = random.randint(-220, 220)  # Bubble generation within the game area.
        y = 300 # Initial y-coordinate of the bubble. All bubbles start at the top of the screen.

        # Check if the new bubble overlaps with any existing bubbles. If not, create the a new dictionary for a bubble and return it.
        if not check_bubble_overlap(x, y, r, existing_bubbles):
            bubble = {
                'x': x, 
                'y': y, 
                'r': r, 
                'color': color,
                'is_dynamic': is_dynamic,
                'dynamic_phase': 0, # Phase for dynamic bubble size oscillation. It calculates the change in radius over time.
                'dynamic_direction': 1 # Direction of dynamic bubble size oscillation. It can have a value of 1 for expanding or -1 for shrinking.
            }
            return bubble
############################################################################################################


# The update_dynamic_bubble function is designed to update the radius of a dynamic bubble based on a sine wave function. This function is called during the game loop to animate the dynamic bubble.
def update_dynamic_bubble(bubble, delta_time):
    """Update the radius of a dynamic bubble."""
    if bubble.get('is_dynamic', False): # Check if the bubble is dynamic. If not, do nothing.
        amplitude = 5 # Maximum radius change for dynamic bubble.
        frequency = 10 # Controls the speed of the dynamic bubble oscillation.
        bubble['dynamic_phase'] += delta_time * frequency * bubble['dynamic_direction'] # Update the phase of the dynamic bubble oscillation. The delta_time represents the time elapsed since the last update, and dynamic_direction indicates whether the bubble is expanding (1) or shrinking (-1).
        radius_change = math.sin(bubble['dynamic_phase']) * amplitude # Calculate the change in radius based on a sine wave function.
        new_radius = bubble['r'] + radius_change # New radius of the bubble.
        new_radius = max(15, min(new_radius, 35)) # Ensure the radius stays within a specific range.
        bubble['r'] = new_radius # Update the bubble radius in the dictionary.

        if abs(radius_change) < 0.1:  # If the absolute value of radius_change is less than 0.1, the dynamic_direction is reversed by multiplying it by -1. This causes the bubble to switch between expanding and shrinking phases.
            bubble['dynamic_direction'] *= -1
############################################################################################################


# The check_bubble_overlap function is designed to check if a new bubble overlaps with any existing bubbles in the game. This function is used to prevent the creation of overlapping bubbles.
def check_bubble_overlap(x, y, r, other_bubbles):
    for other in other_bubbles:
        # Calculate the distance between the centers of the new bubble and the existing bubble using the equation for Euclidean distance.
        distance = ((x - other['x']) ** 2 + (y - other['y']) ** 2) ** 0.5
        # If the distance is less than the sum of the radii of the two bubbles, they overlap. Return True to indicate overlap.
        if other['is_dynamic'] and distance < (r + 37): # otherwise screen stuck
            return True
        elif not other['is_dynamic'] and distance < (r + other['r']):
            return True
    return False
############################################################################################################


# The plot_point function is used to draw a single point on the screen using OpenGL. This function is used for rendering individual pixels.
def plot_point(x, y):
    """Plot a single point using OpenGL."""
    glBegin(GL_POINTS)
    glVertex2f(x, y)
    glEnd()
############################################################################################################

#PURE MIDPOINT LINE DRAWING ALGORITHM

"""Convert coordinates to zone 0 for line drawing algorithm."""
def convert_to_zone0(x, y, zone):
    zone_map = {
        0: (x, y),
        1: (y, x),
        2: (y, -x),
        3: (-x, y),
        4: (-x, -y),
        5: (-y, -x),
        6: (-y, x),
        7: (x, -y)
    }
    return zone_map[zone]

"""Convert coordinates from zone 0 back to original zone."""
def convert_from_zone0(x, y, zone):
    zone_map = {
        0: (x, y),
        1: (y, x),
        2: (-y, x),
        3: (-x, y),
        4: (-x, -y),
        5: (-y, -x),
        6: (y, -x),
        7: (x, -y)
    }
    return zone_map[zone]

"""Midpoint line drawing algorithm."""
def midpoint_line(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    zone = 0
    if abs(dx) > abs(dy):
        if dx >= 0 and dy >= 0:
            zone = 0
        elif dx < 0 and dy >= 0:
            zone = 3
        elif dx < 0 and dy < 0:
            zone = 4
        elif dx >= 0 and dy < 0:
            zone = 7
    else:
        if dx >= 0 and dy >= 0:
            zone = 1
        elif dx < 0 and dy >= 0:
            zone = 2
        elif dx < 0 and dy < 0:
            zone = 5
        elif dx >= 0 and dy < 0:
            zone = 6

    x1, y1 = convert_to_zone0(x1, y1, zone)
    x2, y2 = convert_to_zone0(x2, y2, zone)
    dx = x2 - x1
    dy = y2 - y1
    d = 2 * dy - dx
    incrE = 2 * dy
    incrNE = 2 * (dy - dx)
    x, y = x1, y1
    x0, y0 = convert_from_zone0(x, y, zone)
    plot_point(x0, y0)
    while x < x2:
        if d <= 0:
            d += incrE
            x += 1
        else:
            d += incrNE
            x += 1
            y += 1
        x0, y0 = convert_from_zone0(x, y, zone)
        plot_point(x0, y0)

"""Draw a circle using midpoint circle drawing algorithm."""
def midpointcircle(radius, centerX=0, centerY=0):
    glBegin(GL_POINTS)
    x = 0
    y = radius
    d = 1 - radius
    while y > x:
        glVertex2f(x + centerX, y + centerY)
        glVertex2f(x + centerX, -y + centerY)
        glVertex2f(-x + centerX, y + centerY)
        glVertex2f(-x + centerX, -y + centerY)
        glVertex2f(y + centerX, x + centerY)
        glVertex2f(y + centerX, -x + centerY)
        glVertex2f(-y + centerX, x + centerY)
        glVertex2f(-y + centerX, -x + centerY)
        if d < 0:
            d += 2 * x + 3
        else:
            d += 2 * x - 2 * y + 5
            y -= 1
        x += 1
    glEnd()
############################################################################################################


#Returns the x position of a bubble.
def bubble_x_position(bubble):
    return bubble['x']
############################################################################################################


# The draw_bullet function is used to render all active bullets on the screen. This function draws a small circle for each bullet.
def draw_bullet():
    global bullet_list
    glColor3f(1, 1, 1)
    for bullet in bullet_list:
        midpointcircle(8, bullet[0], bullet[1]) # function to draw a circle with a radius of 8 pixels at the bullet's coordinates (bullet[0] for the x-coordinate and bullet[1] for the y-coordinate).
############################################################################################################


# The draw_bubble function is used to render all active bubbles on the screen. This function draws a circle for each bubble based on its position and radius.
def draw_bubble():
    """Draw all bubbles on screen."""
    global bubble_list
    # Loop through each bubble in the bubble list and draw it on the screen. first, set the color of the bubble using the RGB values stored in the bubble dictionary. Then, call the midpointcircle function to draw a circle with the specified radius and position.
    for bubble in bubble_list:
        glColor3f(bubble['color'][0], bubble['color'][1], bubble['color'][2])
        midpointcircle(bubble['r'], bubble['x'], bubble['y'])
############################################################################################################


# The draw_ui function is used to render the game's user interface elements, such as the rocket, score display, and misfire count. This function draws the rocket, score display, and misfire count on the screen.
def draw_ui():
    global rocket_x, score, misfires, freeze

    # Shooter
    glPointSize(2)
    glColor3f(1, 1, 1)
    
    # Draw the rocket body
    midpoint_line(rocket_x - 10, -345, rocket_x - 10, -315)
    midpoint_line(rocket_x + 10, -345, rocket_x + 10, -315)
    midpoint_line(rocket_x - 10, -315, rocket_x + 10, -315)
    
    # Draw the rocket tip
    midpoint_line(rocket_x - 10, -315, rocket_x, -295)
    midpoint_line(rocket_x + 10, -315, rocket_x, -295)
    
    # Draw the rocket fins
    midpoint_line(rocket_x - 10, -345, rocket_x - 15, -355)
    midpoint_line(rocket_x + 10, -345, rocket_x + 15, -355)
    midpoint_line(rocket_x - 15, -355, rocket_x - 10, -355)
    midpoint_line(rocket_x + 15, -355, rocket_x + 10, -355)
    
    # Draw the rocket fire
    glColor3f(1, 0.5, 0)
    midpoint_line(rocket_x - 5, -355, rocket_x, -375)
    midpoint_line(rocket_x + 5, -355, rocket_x, -375)
    midpoint_line(rocket_x - 5, -355, rocket_x + 5, -355)

    # Draw black box around rocket for collision detection
    glColor3f(0, 0, 0)  
    midpoint_line(rocket_x - 20, -375, rocket_x + 20, -375)  # Bottom line
    midpoint_line(rocket_x - 20, -295, rocket_x + 20, -295)  # Top line
    midpoint_line(rocket_x - 20, -375, rocket_x - 20, -295)  # Left line
    midpoint_line(rocket_x + 20, -375, rocket_x + 20, -295)  # Right line


    # Draw restart button
    glPointSize(4)
    glColor3f(0, 0.8, 1)
    midpoint_line(-208, 350, -160, 350)
    glPointSize(3)
    midpoint_line(-210, 350, -190, 370)
    midpoint_line(-210, 350, -190, 330)

    # Draw quit button
    glPointSize(4)
    glColor3f(0.9, 0, 0)
    midpoint_line(210, 365, 180, 335)
    midpoint_line(210, 335, 180, 365)

    # Draw pause button
    glPointSize(4)
    glColor3f(1, .5, 0)
    if freeze:
        midpoint_line(-15, 370, -15, 330)
        midpoint_line(-15, 370, 15, 350)
        midpoint_line(-15, 330, 15, 350)
    else:
        midpoint_line(-10, 370, -10, 330)
        midpoint_line(10, 370, 10, 330)

    # Draw score and misfires
    glColor3f(1, 1, 1)
    # Score
    glRasterPos2f(-240, -390)
    for ch in f"Score: {score}":
        glutBitmapCharacter(GLUT_BITMAP_HELVETICA_18, ord(ch))
    # Misfires
    glRasterPos2f(140, -390)
    for ch in f"Misfires: {misfires}/3":
        glutBitmapCharacter(GLUT_BITMAP_HELVETICA_18, ord(ch))
    # Missed Bubble
    glRasterPos2f(-80, -390)
    for ch in f"Missed Bubble: {gameover}":
        glutBitmapCharacter(GLUT_BITMAP_HELVETICA_18, ord(ch))

############################################################################################################

# The convert_coordinate function is used to convert screen coordinates to OpenGL coordinates. This function takes the x and y coordinates of a point on the screen and converts them to OpenGL coordinates by adjusting the origin and flipping the y-axis.
def convert_coordinate(x, y):
    """Convert screen coordinates to OpenGL coordinates."""
    a = x - (W_WIDTH / 2)
    b = (W_HEIGHT / 2) - y
    return a, b
############################################################################################################


# The restart_game function is used to reset the game state to its initial conditions. This function resets the game state variables, generates a new set of bubbles, and sets the score and misfire count to zero.
def restart_game():
    global freeze, bubble_list, score, gameover, misfires, bullet_list, rocket_x
    freeze = False
    bubble_list = []
    num_starting_bubbles = random.randint(3, 5)
    for _ in range(num_starting_bubbles):
        new_bubble = create_bubble(bubble_list)
        bubble_list.append(new_bubble)
    bubble_list.sort(key=bubble_x_position)
    score = 0
    gameover = 0
    misfires = 0
    bullet_list = []
    rocket_x = 0
############################################################################################################


# This handles the rocket's movement and bullet firing based on keyboard input. The rocket can move left and right within the game area, and bullets can be fired by pressing the spacebar. The rocket's x-coordinate is updated based on the keyboard input, and bullets are added to the bullet list when the spacebar is pressed.
def keyboardListener(key, _, __):
    """Handle keyboard input."""
    global bullet_list, freeze, gameover, rocket_x
    if key == b' ':
        if not freeze and gameover < 3:
            bullet_list.append([rocket_x, -365])
    elif key == b'a':
        if rocket_x > -230 and not freeze:
            rocket_x -= 20
    elif key == b'd':
        if rocket_x < 230 and not freeze:
            rocket_x += 20
    glutPostRedisplay()

# This function handles mouse input for the game. The mouse input is used to interact with the game's user interface elements, such as the restart button, quit button, and pause button. The mouse coordinates are converted to OpenGL coordinates, and the corresponding actions are triggered based on the location of the mouse click.
def mouseListener(button, state, x, y):
    """Handle mouse input."""
    global freeze, gameover, score, bubble_list, bullet_list, misfires
    if button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
        c_x, c_y = convert_coordinate(x, y)
        if -209 < c_x < -170 and 325 < c_y < 375:
            restart_game()
        elif 170 < c_x < 216 and 330 < c_y < 370:
            print(f'Goodbye! Score: {score}')
            # glutDestroyWindow(wind)
            # if the quit button is not working then uncomment the above line and comment the below line
            glutLeaveMainLoop()
        elif -25 < c_x < 25 and 325 < c_y < 375:
            freeze = not freeze
    glutPostRedisplay()
############################################################################################################

# The animate function is the main game loop that handles the game's animation and logic. This function updates the positions of the bubbles, bullets, and dynamic bubbles, checks for collisions, and updates the game state based on the player's actions. The game loop runs continuously until the game is over or the player quits.
def animate():
    """Main game animation and logic loop."""
    global freeze, bubble_list, gameover, score, bullet_list, misfires, last_frame_time, rocket_x
    
    # The function calculates the time elapsed (delta_time) since the last frame update. This is used to ensure smooth animations and movements.
    current_time = time.time()
    delta_time = current_time - last_frame_time
    last_frame_time = current_time

    # The game logic is executed only if the game is not frozen, the game is not over, and the player has not reached the misfire limit.
    if not freeze and gameover < 3 and misfires < 3:
        
        # The function updates the positions of bullets. If a bullet's y-coordinate is less than 400, it moves the bullet upwards. Otherwise, it increments the misfires counter. The updated bullets are stored in new_bullet.
        new_bullet = []
        for b in bullet_list:
            if b[1] < 400: # it means bullet is still in the game area.
                new_bullet.append([b[0], b[1] + bullet_speed * delta_time])
            else: # it means bullet is out of the game area and didn't hit the bubble
                misfires += 1
        bullet_list = new_bullet

        # The function checks for collisions between bubbles and the rocket. If a bubble's center is within the bounding box of the rocket, the gameover state is set to 3, indicating that the game is over.
        for i in range(len(bubble_list) - 1, -1, -1):
            bubble = bubble_list[i]
            box_left = rocket_x - 20
            box_right = rocket_x + 20
            box_top = -295
            box_bottom = -375
            closest_x = max(box_left, min(bubble['x'], box_right))
            closest_y = max(box_bottom, min(bubble['y'], box_top))
            dx = bubble['x'] - closest_x
            dy = bubble['y'] - closest_y
            distance = math.sqrt(dx**2 + dy**2)
            if distance < bubble['r']:
                gameover = 3
                break


        # The function checks for collisions between bullets and bubbles. If a bullet hits a bubble, the score is incremented based on whether the bubble is dynamic or not. The hit bubble is removed from the bubble list, and a new bubble is created to replace it. The updated score is displayed in the console. The function also updates the positions of dynamic bubbles based on the dynamic bubble logic. The function then updates the positions of all bubbles by moving them downwards. If a bubble reaches the bottom of the screen, the gameover state is incremented. The function also ensures that bubbles do not overlap with each other by checking for collisions between bubbles.
        for i in range(len(bubble_list) - 1, -1, -1): 
            bubble = bubble_list[i]
            if bubble.get('is_dynamic', False):
                update_dynamic_bubble(bubble, delta_time)
            if bubble['y'] > -400:
                new_y = bubble['y'] - (10 + score * 5) * delta_time
                bubble['y'] = new_y
                if check_bubble_overlap(bubble['x'], bubble['y'], bubble['r'], 
                                        [b for b in bubble_list if b != bubble]):
                    bubble['y'] = bubble['y'] + (10 + score * 5) * delta_time 
            else:
                gameover += 1
                bubble_list.pop(i)
                new_bubble = create_bubble(bubble_list)
                bubble_list.append(new_bubble)

        # The function sorts the bubbles based on their x-coordinates using the bubble_x_position function. This ensures that the bubbles are drawn in the correct order.
        bubble_list.sort(key=bubble_x_position)
        
        # The function checks for collisions between bullets and bubbles. If a bullet hits a bubble, the score is incremented based on whether the bubble is dynamic or not. The hit bubble is removed from the bubble list, and a new bubble is created to replace it. The updated score is displayed in the console. The function also updates the positions of dynamic bubbles based on the dynamic bubble logic. The function then updates the positions of all bubbles by moving them downwards. If a bubble reaches the bottom of the screen, the gameover state is incremented. The function also ensures that bubbles do not overlap with each other by checking for collisions between bubbles.
        for i in range(len(bubble_list) - 1, -1, -1):
            bubble = bubble_list[i]
            dx = bubble['x'] - rocket_x
            dy = bubble['y'] - (-345)
            distance = math.sqrt(dx**2 + dy**2)
            if distance < (bubble['r'] + 20):
                gameover = 3
                break  
            for j in range(len(bullet_list) - 1, -1, -1):
                bull = bullet_list[j]
                bullet_dx = bubble['x'] - bull[0]
                bullet_dy = bubble['y'] - bull[1]
                bullet_distance = math.sqrt(bullet_dx**2 + bullet_dy**2)
                if bullet_distance < (bubble['r'] + 8):  
                    if bubble.get('is_dynamic', False):
                        score += 2
                        print(f"Dynamic Bubble Hit! Score: {score}")
                    else:
                        score += 1
                        print(f"Score: {score}")
                    bubble_list.pop(i)
                    bullet_list.pop(j)
                    new_bubble = create_bubble(bubble_list)
                    bubble_list.append(new_bubble)
                    break  

    # The function checks if the game is over or if the player has reached the misfire limit. If either condition is met, the game over message is displayed along with the final score. The freeze variable is set to True to pause the game, and the bubble list is cleared to stop any further animations. Gameover increse by 1 if the bubble reaches the bottom of the screen or it increases by 3 if the rocket hits the bubble.
    if (gameover >= 3 or misfires >= 3) and not freeze:
        print(f"Game Over! Score: {score}")
        freeze = True
        bubble_list = []  
    glutPostRedisplay()
############################################################################################################

#Random baalsaal
def display():
    """Render the game display."""
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glClearColor(0, 0, 0, 0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    draw_ui()
    draw_bullet()
    draw_bubble()
    glutSwapBuffers()

def init():
    """Initialize OpenGL settings."""
    global last_frame_time
    glClearColor(0, 0, 0, 0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-250, 250, -400, 400, -1, 1)
    last_frame_time = time.time()

glutInit()
glutInitWindowSize(W_WIDTH, W_HEIGHT)
glutInitWindowPosition(0, 0)
glutInitDisplayMode(GLUT_DEPTH | GLUT_DOUBLE | GLUT_RGB)
wind = glutCreateWindow(b"Shoot The Circles!")
init()
num_starting_bubbles = random.randint(3, 5)
for _ in range(num_starting_bubbles):
    new_bubble = create_bubble(bubble_list)
    bubble_list.append(new_bubble)
bubble_list.sort(key=bubble_x_position)
glutDisplayFunc(display)
glutIdleFunc(animate)
glutKeyboardFunc(keyboardListener)
glutMouseFunc(mouseListener)
glutMainLoop()