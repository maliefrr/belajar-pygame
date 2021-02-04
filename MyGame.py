import pygame,sys

clock = pygame.time.Clock() # agar kita bisa mengatur fps

from pygame.locals import *

pygame.init() # menginisiasi pygame
WINDOW_SIZE = (400,400) # mensetting ukuran layar

screen = pygame.display.set_mode(WINDOW_SIZE,0,32) # mengaplikasikan layar yang akan di tampilkan

pygame.display.set_caption("Game") # menambahkan caption pada program kita

while True: # membuat infinite loop agar program kita selalu berjalan

    for event in pygame.event.get(): # membuat program dapat menerima input 
        if event.type == QUIT : # membuat sesuatu saat kita mengklik tombol X
            pygame.quit() # membuat pygame berhenti
            sys.exit() # membuat program berhenti
    pygame.display.update() # agar saat kita mengubah program tampilan dapat terupdate
    clock.tick(60) # mengatur fps agar maksimal di 60
