import pygame
import constants as const
import random

pygame.init()

gameDisplay = pygame.display.set_mode((const.SCREEN_WIDTH, const.SCREEN_HEIGHT))
pygame.display.set_caption("Ribicija")

clock = pygame.time.Clock()

mreza_w = 100
mreza_h = 133
floor_h = 40

class Mreza:
	mreza_w = 100
	mreza_h = 133
	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.xspeed = 0
		self.yspeed = 0
		self.mreza_slika = pygame.image.load("mreza_small.png")
	def drwa_mreza(self):
		gameDisplay.blit(self.mreza_slika, (self.x, self.y))
		self.y += self.yspeed
		self.x += self.xspeed
		#Mreza walls Collision
		if self.y + mreza_h >= 560: 
			self.y = 560 - mreza_h	
			#print(slef.y)
		if self.y <= floor_h:
			self.y = floor_h
		if self.x <= 1:
			self.x = 1
		elif self.x + mreza_w >= const.SCREEN_WIDTH:
		 	self.x = const.SCREEN_WIDTH - mreza_w	
		



	def mreza_movement(self):
		global mreza_h, floor_h
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_UP:
				self.yspeed = -3
			elif event.key == pygame.K_DOWN:
				self.yspeed = 3
			elif event.key == pygame.K_LEFT:
				self.xspeed = -3
			elif event.key == pygame.K_RIGHT:
				self.xspeed = 3
		if event.type == pygame.KEYUP:
			if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
				self.yspeed = 0
			if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
				self.xspeed = 0

class Riba:
	floor_h = 40
	riba_w = 50
	riba_h = 23
	def __init__(self, x, y, speed):
		self.speed = speed
		self.x = x
		self.y = y
		self.riba_slika = pygame.image.load("riba.png")
		self.y = random.randrange(40, const.SCREEN_HEIGHT-80)
	def draw_fish(self):
		global mreza_w, score
		gameDisplay.blit(self.riba_slika, (self.x, self.y))
		self.x -= self.speed
		if self.x <  0 :
			self.x = const.SCREEN_WIDTH + 10
			self.y = random.randrange(40, const.SCREEN_HEIGHT-40-floor_h)
		#if mreza_x + mreza_w == self.x and mreza_y - 80 <= self.y and self.y >= mreza_y:
		if mreza_x + mreza_w - 40 >= self.x and mreza_x + mreza_w <= self.x + Riba.riba_w and self.y >= mreza_y and self.y <= mreza_y + 50 :
			self.x = random.randrange(1000, 1500) 
			score += 1
			


def floor(x, y, w, h, color):
	pygame.draw.rect(gameDisplay, color, [x, y, w, h])



floor1_pos = 1
floor_h = 40

mreza = Mreza(200, 300)

drugaRiba = Riba(random.randrange(1000, 1500), 200, random.randrange(1, 5))
prvaRiba = Riba(random.randrange(1000, 1500), 200, random.randrange(1, 5))
trecaRiba = Riba(random.randrange(1000, 1500), 200, 1)
cetvrtaRiba = Riba(random.randrange(1000, 1500), 200, 3)
petaRiba = Riba(random.randrange(1000, 1500), 200, random.randrange(1, 5))
sestaRiba = Riba(random.randrange(1000, 1500), 200, 4)

score = 0

font = pygame.font.SysFont("comicsansms", 22)
text = font.render("Score 0"   , True, (255, 255, 255))
game_exit = 0
while not game_exit:

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				game_exit = True
			mreza.mreza_movement()


		gameDisplay.fill(const.SPLAVA)
	
		floor(floor1_pos, 0, 1000, floor_h, const.EMR)
		floor(floor1_pos, 560, 1000, floor_h, const.EMR)
		
		mreza.drwa_mreza()
		mreza_x = mreza.x
		mreza_y = mreza.y
		drugaRiba.draw_fish()
		prvaRiba.draw_fish()
		trecaRiba.draw_fish()
		cetvrtaRiba.draw_fish()
		petaRiba.draw_fish()
		sestaRiba.draw_fish()
		text = font.render("Score " +str(score)  , True, (255, 255, 255))
		gameDisplay.blit(text, ( 450, 5))

		pygame.display.update()
		clock.tick(105)