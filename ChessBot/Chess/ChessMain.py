import pygame as p
from Chess import ChessEngine
Width = Height = 512
DIMENSION = 8
SQ_SIZE = Height//DIMENSION
MAX_FPS = 15
IMAGES {}

def LoadImages():
    peices = ['wp', 'wK', 'wN', 'wR','wK','wQ', 'bp', 'bR', 'bK', 'bB', 'bQ', 'bK']
    for peice in peices:
        IMAGES[peice] = p.transfor.scale(p.image.load("images/" + peice + ".png")(SQ_SIZE, SQ_SIZE))
    #acces images in dictionary by something like: IMAGES['wp']
def Main():
    p.init
