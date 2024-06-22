import os
import pygame

from const import *

class Dragger:

    def __init__(self):
        self.piece = None
        self.dragging = False
        self.mouseX = 0
        self.mouseY = 0
        self.initial_row = 0
        self.initial_col = 0

    def update_blit(self, surface):
        # increase piece size while dragging
        self.piece.set_texture(size=128)
        texture = self.piece.texture

        # img
        img = pygame.image.load(texture)

        # rect 
        img_center = (self.mouseX, self.mouseY)
        self.piece.texture_rect = img.get_rect(center=img_center)
        surface.blit(img, self.piece.texture_rect)

    def update_mouse(self, pos: tuple):
        self.mouseX, self.mouseY = pos

    def save_initial(self, pos):
        self.initial_col = pos[0] // SQSIZE # x
        self.initial_row = pos[1] // SQSIZE # y

    def drag_piece(self, piece):
        self.piece = piece
        self.dragging = True

    def undrag_piece(self):
        self.piece.set_texture(size=80)
        self.piece = None
        self.dragging = False 
        