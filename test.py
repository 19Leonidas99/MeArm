import pygame
import serial
import struct
from pynput.mouse import Controller, Listener, Button
import random

ser = serial.Serial('COM7', 9600)

pygame.init()
win = pygame.display.set_mode((1000, 1000))
# Shapes
S_1 = pygame.image.load('C:\Users\Maycon\OneDrive\Desktop\Virtual A\S_1.jpg')
S_2 = pygame.image.load('C:\Users\Maycon\OneDrive\Desktop\Virtual A\S_2.jpg')
S_4 = pygame.image.load('C:\Users\Maycon\OneDrive\Desktop\Virtual A\S_4.jpg')
S_5 = pygame.image.load('C:\Users\Maycon\OneDrive\Desktop\Virtual A\S_5.jpg')
S_6 = pygame.image.load('C:\Users\Maycon\OneDrive\Desktop\Virtual A\S_6.jpg')
ShapesList = [S_5]
Shape = random.choice(ShapesList)

z = 50
w = 90
vel = 0.1

mouse = Controller()


run = True
while run:
    a, b = mouse.position  # get mouse position (a,b)

    x = int(179 * a / 1919)  # x axis rotation (middle servo)
    y = int(179 * b / 1079)  # y axis rotation (right servo)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    win.blit(Shape, (0, 0))
    pygame.display.update()

    keys = pygame.key.get_pressed()

    # z axis rotation (left servo)
    if keys[pygame.K_KP2] or keys[pygame.K_s]:
        z -= vel
    if keys[pygame.K_KP8] or keys[pygame.K_w]:
        z += vel
    # set limit
    if z < 0:
        z = 0
    if z > 180:
        z = 180

    if keys[pygame.K_KP4] or keys[pygame.K_a]:
        w -= vel
    if keys[pygame.K_KP6] or keys[pygame.K_d]:
        w += vel
    # set limit
    if w > 180:
        w = 180
    if w < 0:
        w = 0

    ser.write(struct.pack('>BBBB', x, y, z, w))
    print(x, y, z, w)

pygame.quit()
