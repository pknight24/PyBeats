
import pygame, sys, os
import time
from pygame.locals import *
from pynput.keyboard import Key, Controller

keyboard = Controller()

cwd = os.getcwd()
pygame.mixer.pre_init(44100, -16, 1, 512)
pygame.init()
DISPLAYSURF = pygame.display.set_mode((200, 200))
pygame.display.set_caption("PyBeats")
red = pygame.Color(255, 0, 0)
blue = pygame.Color(0, 0, 255)
green = pygame.Color(0, 255, 0)
white = pygame.Color(255, 255, 255)
gray = pygame.Color(128, 128, 128)
maroon = pygame.Color(128, 0, 0)

def getsound(folder):
    for f in os.listdir(folder):
        if f.endswith(".wav") or f.endswith(".WAV"):
            print(f)
            return f

s1 = getsound("sounds/pad1sound/")
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
loopsounds = []
looptimes = []
def loopPlayback(x):
    for n in range(4):
        beep.play()
        time.sleep(1)
    for n in range(x):
        for s in range(len(loopsounds)):
            time.sleep(abs(looptimes[s]))
            keyboard.type(loopsounds[s])
        time.sleep(endTime)
    looping = 0


DISPLAYSURF.fill(white)
while(looping == 0):
        
    pygame.draw.circle(DISPLAYSURF, gray,(100, 100), 25, 0 )
    if recording == True:
        pygame.draw.circle(DISPLAYSURF, maroon,(100, 100), 10, 0 )

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                pad1sound.play()
                if recording == True:
                    loopsounds.append('q')
                    looptimes.append(startTime - time.time())
                    startTime = time.time()
            if event.key == pygame.K_w:
                pad2sound.play()
                if recording == True:
                    loopsounds.append('w')
                    looptimes.append(startTime - time.time())
                    startTime = time.time()
            if event.key == pygame.K_e:
                pad3sound.play()
                if recording == True:
                    loopsounds.append('e')
                    looptimes.append(startTime - time.time())
                    startTime = time.time()
            if event.key == pygame.K_r:
                pad4sound.play()
                if recording == True:
                    loopsounds.append('r')
                    looptimes.append(startTime - time.time())
                    startTime = time.time()
            if event.key == pygame.K_u:
                stopsound()
                pad5sound.play()
                if recording == True:
                    loopsounds.append('u')
                    looptimes.append(startTime - time.time())
                    startTime = time.time() 
            if event.key == pygame.K_i:
                stopsound()
                pad6sound.play()
                if recording == True:
                    loopsounds.append('i')
                    looptimes.append(startTime - time.time())
                    startTime = time.time()
            if event.key == pygame.K_o:
                stopsound()
                pad7sound.play()
                if recording == True:
                    loopsounds.append('o')
                    looptimes.append(startTime - time.time())
                    startTime = time.time()
            if event.key == pygame.K_p:
                stopsound()
                pad8sound.play()
                if recording == True:
                    loopsounds.append('p')
                    looptimes.append(startTime - time.time())
                    startTime = time.time()
            if event.key == pygame.K_a:
                pad9sound.play()
                pygame.draw.rect(DISPLAYSURF, blue, pad9)
                if recording == True:
                    loopsounds.append('a')
                    looptimes.append(startTime - time.time())
                    startTime = time.time()
            if event.key == pygame.K_s:
                pad10sound.play()
                if recording == True:
                    loopsounds.append('s')
                    looptimes.append(startTime = time.time())
                    startTime = time.time()
            if event.key == pygame.K_d:
                pad11sound.play()
                if recording == True:
                    loopsounds.append('d')
                    looptimes.append(startTime = time.time())
            if event.key == pygame.K_f:
                pad12sound.play()
                if recording == True:
                    loopsounds.append('f')
                    looptimes.append(startTime - time.time())
                    startTime = time.time()
            if event.key == pygame.K_j:
                stopsound()
                pad13sound.play()
                if recording == True:
                    loopsounds.append('j')
                    looptimes.append(startTime - time.time())
                    startTime = time.time()
            if event.key == pygame.K_k:
                stopsound()
                pad14sound.play()
                if recording == True:
                    loopsounds.append('k')
                    looptimes.append(startTime - time.time())
                    startTime = time.time()
            if event.key == pygame.K_l:
                stopsound()
                pad15sound.play()
                if recording == True:
                    loopsounds.append('l')
                    looptimes.append(startTime - time.time())
                    startTime = time.time()
            if event.key == pygame.K_SEMICOLON:
                stopsound()
                pad16sound.play()
                if recording == True:
                    loopsounds.append(';')
                    looptimes.append(startTime - time.time())
                    startTime = time.time()
            if event.key == pygame.K_SPACE:
                if recording == False:
                    recording = True
                    startTime = time.time()
                else:
                    endTime = time.time() - startTime
                    recording = False
            if event.key == pygame.K_1:
                looping = 1
                loopPlayback(2)
            if event.key == pygame.K_2:
                looping = 1
                loopPlayback(4)
            if event.key == pygame.K_3:
                looping = 1
                loopPlayback(8)
            if event.key == pygame.K_4:
                looping = 1
                loopPlayback(16)
            if event.key == pygame.K_5:
                looping = 1
                loopPlayback(32)
            if event.key == pygame.K_6:
                looping = 1
                loopPlayback(64)
            if event.key == pygame.K_PERIOD:
                del loopsounds[:]
                del looptimes[:]
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
