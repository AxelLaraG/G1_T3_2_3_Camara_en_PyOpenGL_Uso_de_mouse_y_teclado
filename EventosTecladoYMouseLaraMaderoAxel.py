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


# Loop principal
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        handle_mouse_events(event)

    # Manejo de eventos de teclado
    keys = pygame.key.get_pressed()
    if keys[K_PLUS]:
        glTranslatef(0.0, 0.0, 0.1)  # Zoom in
    if keys[K_MINUS]:
        glTranslatef(0.0, 0.0, -0.1)  # Zoom out

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    # Dibuja un cubo
    glBegin(GL_QUADS)  # Usamos GL_QUADS en lugar de GL_TRIANGLES para definir las caras del cubo
    # Cara frontal
    glColor3f(0, 0, 1)
    glVertex3f(-1, -1, -1)
    glVertex3f(1, -1, -1)
    glVertex3f(1, 1, -1)
    glVertex3f(-1, 1, -1)
    # Cara posterior
    glColor3f(1, 0, 0)
    glVertex3f(-1, -1, 1)
    glVertex3f(1, -1, 1)
    glVertex3f(1, 1, 1)
    glVertex3f(-1, 1, 1)
    # Cara superior
    glColor3f(0, 1, 0)
    glVertex3f(-1, 1, -1)
    glVertex3f(1, 1, -1)
    glVertex3f(1, 1, 1)
    glVertex3f(-1, 1, 1)
    # Cara inferior
    glColor3f(1, 1, 0)
    glVertex3f(-1, -1, -1)
    glVertex3f(1, -1, -1)
    glVertex3f(1, -1, 1)
    glVertex3f(-1, -1, 1)
    # Cara izquierda
    glColor3f(1, 0.5, 0)
    glVertex3f(-1, -1, -1)
    glVertex3f(-1, 1, -1)
    glVertex3f(-1, 1, 1)
    glVertex3f(-1, -1, 1)
    # Cara derecha
    glColor3f(0.5, 0, 0.5)
    glVertex3f(1, -1, -1)
    glVertex3f(1, 1, -1)
    glVertex3f(1, 1, 1)
    glVertex3f(1, -1, 1)
    glEnd()
    pygame.display.flip()
    pygame.time.wait(10)
