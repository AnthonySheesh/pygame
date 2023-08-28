import pygame
from pygame.locals import *
import random
import os

# Iniciar Pygame
pygame.init()
dis = pygame.display.Info()
width, height = dis.current_w, dis.current_h
screen = pygame.display.set_mode((width, height))

pygame.display.set_caption("Space")
pos_x = (width//2)
pos_y = (height//1.5)
# Definir los colores
black = pygame.Color("black")
light_grey = pygame.Color("lightgrey")
white = pygame.Color("white")

import math

class Bala():
    def __init__(self, velocidad, pos_x, pos_y, id_bala):
        self.id = id_bala
        self.rect = pygame.Rect(pos_x, pos_y, 50, 50)
        self.bala = pygame.draw.rect(screen, white, (pos_x-25, pos_y-25, 50, 50))
        self.velocidad = velocidad
        
        # Definir el ángulo de rotación inicial
        self.angulo = 0
    def rectget(self):
    	return self.bala
    def update(self):
        # Mover la bala hacia arriba
        self.bala.y -= self.velocidad
        
        # Actualizar el ángulo de rotación de la bala
        self.angulo += 1
        self.bala = pygame.draw.rect(screen, white, (self.bala.x, self.bala.y-25, 50, 50))
        self.rect = pygame.Rect(self.bala.x, self.bala.y, 50, 50)
        
        # Verificar si la bala ha alcanzado una cierta posición
        if self.bala.y <= 0:
            bala = balas.pop(0)
            pass
class Enemy():
    def __init__(self, pos_x, pos_y):
        self.time = pygame.time.get_ticks()
        poses = True
        while poses:
        	self.position_x = random.randint(0, width-70)
        	self.position_y = random.randint(0, height-70)
        	if (pos_x - self.position_x) < -100 or (self.position_x - pos_x) < 100:
        		if (pos_y - self.position_y) < -100 or (self.position_y - pos_y) < 100:
        			poses = False
        self.rect = pygame.Rect(self.position_x, self.position_y, 70,70)
        self.enemy = pygame.draw.rect(screen, (200,0,200), (self.position_x, self.position_y, 70, 70))
    def rectget(self):
    	return self.rect
    def impact(self, enemy_id):
    	enemy.pop(enemy_id)
    def update(self):
        if (pygame.time.get_ticks() - self.time) >= 1500:
        	enemy.pop(0)
        	for x in [0,90,180,270]:
        		balase.append(BalaE(2, self.position_x, self.position_y, x))
        else:
        	self.bala = pygame.draw.rect(screen, (200,0,200), (self.position_x, self.position_y, 70, 70))
class Rayo():
    def __init__(self, pos_x, pos_y):
        self.time = pygame.time.get_ticks()
        poses = True
        while poses:
        	self.position_x = random.randint(0, width-70)
        	self.position_y = random.randint(0, height-70)
        	if (pos_x - self.position_x) < -100 or (self.position_x - pos_x) < 100:
        		if (pos_y - self.position_y) < -100 or (self.position_y - pos_y) < 100:
        			poses = False
        self.rect = pygame.Rect(self.position_x, self.position_y, 70,70)
        self.enemy = pygame.draw.rect(screen, (100,0,100), (0, self.position_y, width, 100))
    def rectget(self):
    	return self.rect
    def impact(self):
    	rayo.pop(0)
    def update(self):
        if (pygame.time.get_ticks() - self.time) >= 200:
        	rayo.pop(0)
        	space = width//10
        	dspace = 0
        	current = 0
        	spacelist = []
        	while current <= space:
        		dspace += space
        		spacelist.append(dspace)
        		current += 1
        	for x in spacelist:
        		balase.append(BalaE(2, x, self.position_y, 180))
        else:
        	self.bala = pygame.draw.rect(screen, (100,0,100), (0, self.position_y, width, 100))
class BalaE():
    def __init__(self, velocidad, pos_x, pos_y, angle):
        self.rect = pygame.Rect(pos_x, pos_y, 20, 20)
        self.position_x = pos_x
        self.position_y = pos_y
        self.bala = pygame.draw.circle(screen, (200,0,200), (self.position_x, self.position_y),20)
        self.velocidad = velocidad
        self.angle = angle
    def rectget(self):
    	return self.bala
    def update(self):
        # Mover la bala hacia arriba
        if self.angle == 0:
        	self.position_x+= 0 * self.velocidad
        	self.position_y += -2 * self.velocidad
        elif self.angle == 90:
        	self.position_x += 2 * self.velocidad
        	self.position_y += 0 * self.velocidad
        elif self.angle == 180:
        	self.position_x += 0 * self.velocidad
        	self.position_y += 2 * self.velocidad
        elif self.angle == 270:
        	self.position_x += -2 * self.velocidad
        	self.position_y += 0 * self.velocidad
        # Actualizar el ángulo de rotación de la bala
        self.bala = pygame.draw.circle(screen, (200,0,200), (self.position_x, self.position_y),20)
        self.rect = pygame.Rect(self.bala.x, self.bala.y, 20, 20)
        
        # Verificar si la bala ha alcanzado una cierta posición
        if self.position_y <= 0 or self.position_x <= 0 or self.position_y >= height or self.position_x >= width:
            bala = balase.pop(0)
            pass
class Mira():
    def __init__(self, pos_x, pos_y):
        self.time = pygame.time.get_ticks()
        self.bala = pygame.draw.rect(screen, white, (pos_x, pos_y-50, 5, 5))
        self.velocidad_x = 0
        self.velocidad_y = 2
        
    def update(self):
        # Mover la bala hacia arriba
        self.bala.y += self.velocidad_y
        self.bala.x += self.velocidad_x
        self.bala = pygame.draw.rect(screen, (200,0,0), (self.bala.x, self.bala.y-50, 5, 5))
        
        
        # Verificar si la bala ha alcanzado una cierta posición
        if (pygame.time.get_ticks() - self.time) >= 500:
            bala = particles.pop(0)
            pass
# Variables de control
running = True
score1 = 0
score2 = 0
balas = []
balase = []
particles = []
enemy = []
time = 0
level = 0
rayo = []
player_kill = False
cooltime = 0
powerball = 1000
name_game = pygame.font.Font(None, 70).render("Space - ®TechDev", True, (250,250,250))
text_height = name_game.get_height()
score = 0
# Iniciar el bucle principal del juego
while running:
    # Manejar eventos de teclado
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
    # Limpiar la pantalla y dibujar las paletas
    screen.fill(black)
    screen.blit(name_game,(50,(height-(text_height*5))))
    screen.blit(pygame.font.Font(None, 70).render("SCORE: "+str(score), True, (250,250,250)),(50,50))
    if player_kill:
    	render = pygame.font.Font(None, 200).render("GAME OVER",True, (250,250,250))
    	height_r = render.get_height()
    	width_r = render.get_width()
    	screen.blit(render,((width-width_r)//2,((height-height_r)//2)))
    	if (pygame.time.get_ticks() - cooltime) >= 1500:
    		player_kill = False
    		score = 0
    w_pos, h_pos = pygame.mouse.get_pos()
    if w_pos == 0 and h_pos == 0:
    	touch = pygame.draw.circle(screen, light_grey, (-100, -100),30)
    	None
    else:
    	pos_x = w_pos
    	pos_y = h_pos-300
    	touch = pygame.draw.circle(screen, light_grey, (w_pos, h_pos+35),30)
    	touch_rect = pygame.Rect(w_pos, h_pos,20,20)
    	particle = Mira(w_pos, h_pos)
    	particles.append(particle)
    	for particle in particles:
    		particle.update()
    player = pygame.draw.polygon(screen, white, [(pos_x-70,pos_y+170),(pos_x+0,pos_y+0),(pos_x+70,pos_y+170),(pos_x+0,pos_y+100)])
    current = pygame.time.get_ticks()
    powerball = 1000
    if (current - time) >= powerball:
    	id_bala = len(balas)
    	cargando_disparo = Bala(5, pos_x, pos_y, id_bala)
    	disparando = balas.append(cargando_disparo)
    	time = current
    for bala in balas:
    		bala.update()
    for bala in balase:
    		bala.update()
    if random.randint(0,10000) < 400:
    	preparando = Enemy(pos_x, pos_y)
    	desplegando = enemy.append(preparando)
    for e in enemy:
    		e.update()
    #VERIFICAR COLISIONES
    enemy_id = 0
    for e in enemy:
    	if touch.colliderect(e.rectget()):
    		e.impact(enemy_id)
    		score += 1
    		break
    	enemy_id += 1
    enemy_id = 0
    for e in enemy:
    	for b in balas:
    		if b.rect.colliderect(e.rectget()):
    			e.impact(enemy_id)
    			score += 2
    			break
    	enemy_id += 1
    for b in balase:
    	if player.colliderect(b.rectget()):
    			player_kill = True
    			cooltime = pygame.time.get_ticks()
    			break
    for r in rayo:
    	r.update()
    if (score - level) >= 10:
    	addrayo = Rayo(pos_x, pos_y)
    	rayo.append(addrayo)
    	level = score
    # Actualizar la ventana
    pygame.time.Clock().tick(60)
    pygame.display.update()

# Salir del juego
pygame.quit()