from turtle import width
import pygame
import os
import cv2

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):
        command = 'cls'
    os.system(command)

pygame.init()
clearConsole()

cam = cv2.VideoCapture(0)
cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
cascade_side = cv2.CascadeClassifier("haarcascade_profileface.xml")

cam_width = cv2.CAP_PROP_FRAME_WIDTH
cam_height = cv2.CAP_PROP_FRAME_HEIGHT

pygame_size = width, height = cam_width *2 , cam_height

pygame_screen = pygame.display.set_mode(pygame_size)

def cvimage_to_pygame(image):
    return pygame.image.frombuffer(im.tostring(), im.shape[1::-1],
                                   "RGB")

while True:
    _, im = cam.read()
    im_grey = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    faces = cascade.detectMultiScale(im_grey)
    side = cascade_side.detectMultiScale(im_grey)
    for x,y, width, height in faces:
        cv2.rectangle(im, (x, y), (x + width, y + height), color=(255,0,0), thickness=4)
        cv2.rectangle(im_grey, (x,y), (x + width, y+ height), color=(0,255,0), thickness=4)
    