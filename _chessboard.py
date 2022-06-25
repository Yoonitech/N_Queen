#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pygame
import numpy
from pygame.locals import *

pygame.init()




def CREATE_CHESSBOARD(window_width, window_height, surface, AR, queenImg):

    rect_width = window_width/len(AR)
    rect_height = window_height/len(AR)
    x = y = 0
    color = None
    white = (255, 255, 255)
    black = (0, 0, 0)
    def queen(x, y):
        surface.blit(queenImg, (x, y))

    def create_horizontal_rects(x, y, color, color2):
        for i in range(len(AR)):
            rects = pygame.Rect(x, y, rect_width, rect_height)
            if i % 2 == 0:
                pygame.draw.rect(surface, color, rects)
                x += rect_width
            else:
                pygame.draw.rect(surface, color2, rects)
                x += rect_width

    x = 0

    for i in range(len(AR)):
        if i % 2 == 0:
            create_horizontal_rects(x, y, white, black)
            y += rect_height
        if i % 2 == 1:
            create_horizontal_rects(x, y, black, white)
            y += rect_width

    queenImg = pygame.transform.scale(queenImg,(int(rect_width), int(rect_height))) 
    for i in range(len(AR)):
        x = i*rect_width
        y = AR[i]*rect_height
        queen(x, y)
        

# In[ ]:




