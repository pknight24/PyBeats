import pygame, sys, os
import time
from pygame.locals import *

cwd = os.getcwd()
pygame.mixer.pre_init(44100, -16, 1, 512)
pygame.init()
DISPLAYSURF = pygame.display.set_mode((1110, 600))
pygame.display.set_caption("PyBeats")
red = pygame.Color(255, 0, 0)
blue = pygame.Color(0, 0, 255)
green = pygame.Color(0, 255, 0)
white = pygame.Color(255, 255, 255)
gray = pygame.Color(128, 128, 128)
maroon = pygame.Color(128, 0, 0)
pad1 = pygame.Rect(10, 20, 100, 100)
pad2 = pygame.Rect(150, 20, 100, 100)
pad3 = pygame.Rect(300, 20, 100, 100)
pad4 = pygame.Rect(440, 20, 100, 100)
pad5 = pygame.Rect(580, 20, 100, 100)
pad6 = pygame.Rect(720, 20, 100, 100)
pad7 = pygame.Rect(860, 20, 100, 100)
pad8 = pygame.Rect(1000, 20, 100, 100)
pad9 = pygame.Rect(10, 140, 100, 100)
pad10 = pygame.Rect(150, 140, 100, 100)
pad11 = pygame.Rect(300, 140, 100, 100)
pad12 = pygame.Rect(440, 140, 100, 100)
pad13 = pygame.Rect(580, 140, 100, 100)
pad14 = pygame.Rect(720, 140, 100, 100)
pad15 = pygame.Rect(860, 140, 100, 100)
pad16 = pygame.Rect(1000, 140, 100, 100)

def getsound(folder):
    for f in os.listdir(folder):
        if f.endswith(".wav") or f.endswith(".WAV"):
            print(f)
            return f

s1 = str(getsound("sounds/pad1sound/"))
s2 = getsound("sounds/pad2sound/")
s3 = getsound("sounds/pad3sound/")
s4 = getsound("sounds/pad4sound/")
s5 = getsound("sounds/pad5sound/")
s6 = getsound("sounds/pad6sound/")
s7 = getsound("sounds/pad7sound/")
s8 = getsound("sounds/pad8sound/")
s9 = getsound("sounds/pad9sound/")
s10 = getsound("sounds/pad10sound/")
s11 = getsound("sounds/pad11sound/")
s12 = getsound("sounds/pad12sound/")
s13 = getsound("sounds/pad13sound/")
s14 = getsound("sounds/pad14sound/")
s15 = getsound("sounds/pad15sound/")
s16 = getsound("sounds/pad16sound/")
pad1sound = pygame.mixer.Sound(os.path.join(cwd, "sounds/pad1sound/"+s1))
pad2sound = pygame.mixer.Sound(os.path.join(cwd, "sounds/pad2sound/"+s2))
pad3sound = pygame.mixer.Sound(os.path.join(cwd, "sounds/pad3sound/"+s3))
pad4sound = pygame.mixer.Sound(os.path.join(cwd, "sounds/pad4sound/"+s4))
pad5sound = pygame.mixer.Sound(os.path.join(cwd, "sounds/pad5sound/"+s5))
pad6sound = pygame.mixer.Sound(os.path.join(cwd, "sounds/pad6sound/"+s6))
pad7sound = pygame.mixer.Sound(os.path.join(cwd, "sounds/pad7sound/"+s7))
pad8sound = pygame.mixer.Sound(os.path.join(cwd, "sounds/pad8sound/"+s8))
pad9sound = pygame.mixer.Sound(os.path.join(cwd, "sounds/pad9sound/"+s9))
pad10sound = pygame.mixer.Sound(os.path.join(cwd, "sounds/pad10sound/"+s10))
pad11sound = pygame.mixer.Sound(os.path.join(cwd, "sounds/pad11sound/"+s11))
pad12sound = pygame.mixer.Sound(os.path.join(cwd, "sounds/pad12sound/"+s12))
pad13sound = pygame.mixer.Sound(os.path.join(cwd, "sounds/pad13sound/"+s13))
pad14sound = pygame.mixer.Sound(os.path.join(cwd, "sounds/pad14sound/"+s14))
pad15sound = pygame.mixer.Sound(os.path.join(cwd, "sounds/pad15sound/"+s15))
pad16sound = pygame.mixer.Sound(os.path.join(cwd, "sounds/pad16sound/"+s16))


def stopsound():
    pad5sound.stop()
    pad6sound.stop()
    pad7sound.stop()
    pad8sound.stop()
    pad13sound.stop()
    pad14sound.stop()
    pad15sound.stop()
    pad16sound.stop()


class Loop:
    def __init__(self, sequence, timing, loopNum):
        self.seq = sequence
        self.t = timing
        self.x = loopNum
    def playback(seq, t, x):
        for n in range(4):
            beep.play()
            time.sleep(1)
        

DISPLAYSURF.fill(white)
while(True):
    pygame.draw.rect(DISPLAYSURF, green, pad1)
    pygame.draw.rect(DISPLAYSURF, green, pad2)
    pygame.draw.rect(DISPLAYSURF, green, pad3)
    pygame.draw.rect(DISPLAYSURF, green, pad4)
    pygame.draw.rect(DISPLAYSURF, red, pad5)
    pygame.draw.rect(DISPLAYSURF, red, pad6)
    pygame.draw.rect(DISPLAYSURF, red, pad7)
    pygame.draw.rect(DISPLAYSURF, red, pad8)
    pygame.draw.rect(DISPLAYSURF, green, pad9)
    pygame.draw.rect(DISPLAYSURF, green, pad10)
    pygame.draw.rect(DISPLAYSURF, green, pad11)
    pygame.draw.rect(DISPLAYSURF, green, pad12)
    pygame.draw.rect(DISPLAYSURF, red, pad13)
    pygame.draw.rect(DISPLAYSURF, red, pad14)
    pygame.draw.rect(DISPLAYSURF, red, pad15)
    pygame.draw.rect(DISPLAYSURF, red, pad16)       
   

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                pad1sound.play()
                pygame.draw.rect(DISPLAYSURF, blue, pad1)
            if event.key == pygame.K_w:
                pad2sound.play()
                pygame.draw.rect(DISPLAYSURF, blue, pad2)
               

            if event.key == pygame.K_e:
                pad3sound.play()
                pygame.draw.rect(DISPLAYSURF, blue, pad3)
                
            if event.key == pygame.K_r:
                pad4sound.play()
                pygame.draw.rect(DISPLAYSURF, blue, pad4)
                
            if event.key == pygame.K_u:
                stopsound()
                pad5sound.play()
                pygame.draw.rect(DISPLAYSURF, blue, pad5)
               
            if event.key == pygame.K_i:
                stopsound()
                pad6sound.play()
                pygame.draw.rect(DISPLAYSURF, blue, pad6)
                
            if event.key == pygame.K_o:
                stopsound()
                pad7sound.play()
                pygame.draw.rect(DISPLAYSURF, blue, pad7)
               
            if event.key == pygame.K_p:
                stopsound()
                pad8sound.play()
                pygame.draw.rect(DISPLAYSURF, blue, pad8)
                
            if event.key == pygame.K_a:
                pad9sound.play()
                pygame.draw.rect(DISPLAYSURF, blue, pad9)
                
            if event.key == pygame.K_s:
                pad10sound.play()
                pygame.draw.rect(DISPLAYSURF, blue, pad10)
                
            if event.key == pygame.K_d:
                pad11sound.play()
                pygame.draw.rect(DISPLAYSURF, blue, pad11)
                
            if event.key == pygame.K_f:
                pad12sound.play()
                pygame.draw.rect(DISPLAYSURF, blue, pad12)
                
            if event.key == pygame.K_j:
                stopsound()
                pad13sound.play()
                pygame.draw.rect(DISPLAYSURF, blue, pad13)
                
            if event.key == pygame.K_k:
                stopsound()
                pad14sound.play()
                pygame.draw.rect(DISPLAYSURF, blue, pad14)
                
            if event.key == pygame.K_l:
                stopsound()
                pad15sound.play()
                pygame.draw.rect(DISPLAYSURF, blue, pad15)
                
            if event.key == pygame.K_SEMICOLON:
                stopsound()
                pad16sound.play()
                pygame.draw.rect(DISPLAYSURF, blue, pad16)
                
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
