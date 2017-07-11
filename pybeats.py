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
#loads all of the sounds into the correct pad
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
beep = pygame.mixer.Sound(os.path.join(cwd, "sounds/beep.WAV"))

def playsound(key):
    if key == 'q':
        pad1sound.play()
        pygame.draw.rect(DISPLAYSURF, blue, pad1)
    if key == 'w':
        pad2sound.play()
        pygame.draw.rect(DISPLAYSURF, blue, pad2)
    if key == 'e':
        pad3sound.play()
        pygame.draw.rect(DISPLAYSURF, blue, pad3)
    if key == 'r':
        pad4sound.play()
        pygame.draw.rect(DISPLAYSURF, blue, pad4)
    if key == 'u':
        stopsound()
        pad5sound.play()
        pygame.draw.rect(DISPLAYSURF, blue, pad5)
    if key == 'i':
        stopsound()
        pad6sound.play()
        pygame.draw.rect(DISPLAYSURF, blue, pad6)
    if key == 'o':
        stopsound()
        pad7sound.play()
        pygame.draw.rect(DISPLAYSURF, blue, pad7)
    if key == 'p':
        stopsound()
        pad8sound.play()
        pygame.draw.rect(DISPLAYSURF, blue, pad8)
    if key == 'a':
        pad9sound.play()
        pygame.draw.rect(DISPLAYSURF, blue, pad9)
    if key == 's':
        pad10sound.play()
        pygame.draw.rect(DISPLAYSURF, blue, pad10)
    if key == 'd':
        pad11sound.play()
        pygame.draw.rect(DISPLAYSURF, blue, pad11)
    if key == 'f':
        pad12sound.play()
        pygame.draw.rect(DISPLAYSURF, blue, pad12)
    if key == 'j':
        stopsound()
        pad13sound.play()
        pygame.draw.rect(DISPLAYSURF, blue, pad13)
    if key == 'k':
        stopsound()
        pad14sound.play()
        pygame.draw.rect(DISPLAYSURF, blue, pad14)
    if key == 'l':
        stopsound()
        pad15sound.play()
        pygame.draw.rect(DISPLAYSURF, blue, pad15)
    if key == ';':
        stopsound()
        pad16sound.play()
        pygame.draw.rect(DISPLAYSURF, blue, pad16)
                

def stopsound():
    pad5sound.stop()
    pad6sound.stop()
    pad7sound.stop()
    pad8sound.stop()
    pad13sound.stop()
    pad14sound.stop()
    pad15sound.stop()
    pad16sound.stop()

looping = 0
recording = False

class Loop:
    def __init__(self):
        self.seq = []
        self.t = []
        self.endTime = 0
    def playback(self, loopNum):
        for n in range(4):
            beep.play()
            time.sleep(1)
        for n in range(loopNum):
            for n in range(len(self.seq)):
                time.sleep(abs(self.t[n]))
                playsound(self.seq[n])
            time.sleep(self.endTime)
        

        

DISPLAYSURF.fill(white)
while(looping == 0):
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
    pygame.draw.circle(DISPLAYSURF, gray, (35, 550), 25, 0)
    if recording:
        pygame.draw.circle(DISPLAYSURF, maroon, (35, 550), 10, 0)
   

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                playsound('q')
                if recording == True:
                    loo.seq.append('q')
                    loo.t.append(startTime - time.time())
                    startTime = time.time()
            if event.key == pygame.K_w:
                playsound('w')
                if recording == True:
                    loo.seq.append('w')
                    loo.t.append(startTime - time.time())
                    startTime = time.time()
            if event.key == pygame.K_e:
                playsound('e')
                if recording == True:
                    loo.seq.append('e')
                    loo.t.append(startTime - time.time())
                    startTime = time.time()
            if event.key == pygame.K_r:
                playsound('r')
                if recording == True:
                    loo.seq.append('r')
                    loo.t.append(startTime - time.time())
                    startTime = time.time()
            if event.key == pygame.K_u:
                playsound('u')
                if recording == True:
                    loo.seq.append('u')
                    loo.t.append(startTime - time.time())
                    startTime = time.time() 
            if event.key == pygame.K_i:
                playsound('i')
                if recording == True:
                    loo.seq.append('i')
                    loo.t.append(startTime - time.time())
                    startTime = time.time()
            if event.key == pygame.K_o:
                playsound('o')
                if recording == True:
                    loo.seq.append('o')
                    loo.t.append(startTime - time.time())
                    startTime = time.time()
            if event.key == pygame.K_p:
                playsound('p')
                if recording == True:
                    loo.seq.append('p')
                    loo.t.append(startTime - time.time())
                    startTime = time.time()
            if event.key == pygame.K_a:
                playsound('a')
                pygame.draw.rect(DISPLAYSURF, blue, pad9)
                if recording == True:
                    loo.seq.append('a')
                    loo.t.append(startTime - time.time())
                    startTime = time.time()
            if event.key == pygame.K_s:
                playsound('s')
                if recording == True:
                    loo.seq.append('s')
                    loo.t.append(startTime - time.time())
                    startTime = time.time()
            if event.key == pygame.K_d:
                playsound('d')
                if recording == True:
                    loo.seq.append('d')
                    loo.t.append(startTime - time.time())
            if event.key == pygame.K_f:
                playsound('f')
                if recording == True:
                    loo.seq.append('f')
                    loo.t.append(startTime - time.time())
                    startTime = time.time()
            if event.key == pygame.K_j:
                playsound('j')
                if recording == True:
                    loo.seq.append('j')
                    loo.t.append(startTime - time.time())
                    startTime = time.time()
            if event.key == pygame.K_k:
                playsound('k')
                if recording == True:
                    loo.seq.append('k')
                    loo.t.append(startTime - time.time())
                    startTime = time.time()
            if event.key == pygame.K_l:
                playsound('l')
                if recording == True:
                    loo.seq.append('l')
                    loo.t.append(startTime - time.time())
                    startTime = time.time()
            if event.key == pygame.K_SEMICOLON:
                playsound(';')
                if recording == True:
                    loo.seq.append(';')
                    loo.t.append(startTime - time.time())
                    startTime = time.time()
            if event.key == pygame.K_SPACE:
                if recording == False:
                    loo = Loop()
                    recording = True
                    startTime = time.time()
                else:
                    loo.endTime = time.time() - startTime
                    recording = False
            if event.key == pygame.K_1:
                looping = 1
                loo.playback(2)
            if event.key == pygame.K_2:
                looping = 1
                loo.playback(4)
            if event.key == pygame.K_3:
                looping = 1
                loo.playback(8)
            if event.key == pygame.K_4:
                looping = 1
                loo.playback(16)
            if event.key == pygame.K_5:
                looping = 1
                loo.playback(32)
            if event.key == pygame.K_6:
                looping = 1
                loo.playback(64)
            if event.key == pygame.K_PERIOD:
                del loo.seq[:]
                del loo.t[:]
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()




