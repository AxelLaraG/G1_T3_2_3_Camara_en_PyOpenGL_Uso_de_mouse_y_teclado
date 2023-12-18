import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

# Inicializa Pygame
pygame.init()

# Configura la ventana Pygame
display = (800, 600)
pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
pygame.display.set_caption("Manipulación de Perspectiva 3D")

# Configura la perspectiva OpenGL
gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
glTranslatef(0.0, 0.0, -5)

# Variables para el control del mouse
rotating = False
prev_mouse_x = 0
prev_mouse_y = 0
rotation_speed = 0.5

# Variables para el control del teclado
key_states = {
    K_LEFT: False,
    K_RIGHT: False,
    K_UP: False,
    K_DOWN: False,
    K_PLUS: False,
    K_MINUS: False,
}


# Función para manejar los eventos del mouse
def handle_mouse_events(event):
    global rotating, prev_mouse_x, prev_mouse_y

    if event.type == pygame.MOUSEBUTTONDOWN:
        if event.button == 1:  # Botón izquierdo del mouse
            rotating = True
            prev_mouse_x, prev_mouse_y = event.pos
    elif event.type == pygame.MOUSEBUTTONUP:
        if event.button == 1:
            rotating = False
    elif event.type == pygame.MOUSEMOTION and rotating:
        delta_x = event.pos[0] - prev_mouse_x
        delta_y = event.pos[1] - prev_mouse_y
        prev_mouse_x, prev_mouse_y = event.pos
        glRotatef(delta_x * rotation_speed, 0, 1, 0)
        glRotatef(delta_y * rotation_speed, 1, 0, 0)


# Función para manejar los eventos del teclado
def handle_keyboard_events():
    global key_states

    for event in pygame.event.get():
        if event.type == KEYDOWN:
            key_states[event.key] = True
        elif event.type == KEYUP:
            key_states[event.key] = False
        elif event.type == pygame.QUIT:
            pygame.quit()
            quit()


# Loop principal
while True:
    handle_keyboard_events()

    if key_states[K_LEFT]:
        glRotatef(1, 0, -1, 0)
    if key_states[K_RIGHT]:
        glRotatef(1, 0, 1, 0)
    if key_states[K_UP]:
        glRotatef(1, -1, 0, 0)
    if key_states[K_DOWN]:
        glRotatef(1, 1, 0, 0)
    if key_states[K_PLUS]:
        glTranslatef(0.0, 0.0, 0.1)
    if key_states[K_MINUS]:
        glTranslatef(0.0, 0.0, -0.1)

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glBegin(GL_TRIANGLES)
    glVertex3f(-1, -1, -2)
    glVertex3f(0, 1, -2)
    glVertex3f(1, -1, -2)
    glEnd()
    pygame.display.flip()
    pygame.time.wait(10)
