import struct  # import library struct
import pygame  # import library pygame
import serial  # import library serial

pygame.init()  # initiate pygame

win = pygame.display.set_mode((700, 700))  # open a pygame window

ser = serial.Serial('COM3', 9600)

z = 90  # initial position for left servo
w = 35  # initial position for crane
D = 0.1

run = True
while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    mouse = pygame.mouse.get_pos()  # get mouse position (x;y)

    # convert mouse position (x,y) to degree
    x = int(pygame.mouse.get_pos()[0] * 179 / 699)  # middle servo move
    y = int(pygame.mouse.get_pos()[1] * 179 / 699)  # right servo move

    keys = pygame.key.get_pressed()

    # left servo move
    if keys[pygame.K_KP2 or pygame.K_DOWN]:
        z -= D
    if keys[pygame.K_KP8]:
        z += D
    # set limit
    if z < 0:
        z = 0
    if z > 180:
        z = 180

    # crane servo
    if keys[pygame.K_KP4]:
        w -= D
    if keys[pygame.K_KP6]:
        w += D
    # set limit
    if w < 0:
        w = 0
    if w > 180:
        w = 180

    ser.write(struct.pack('>BBBB', x, y, z, w))  # send the moves to arduino
    print(x, y, z, w)  # print angles
