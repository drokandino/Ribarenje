import pygame
import constants as const
import random

pygame.init()

#Creating gameSurface
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
		self.mreza_slika = pygame.image.load("mreza_small.png") #Loading mreza image 
	def drwa_mreza(self):
		gameDisplay.blit(self.mreza_slika, (self.x, self.y)) #Loading mreza image into the surface
		self.y += self.yspeed #Mreza movement
		self.x += self.xspeed
		#Mreza walls Collision
		if self.y + 65 >= 560: 
			self.y = 490	
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
	speed_min = 1
	speed_max = 3
	counter = True
	k = 0
	def __init__(self):
		self.speed = random.randrange(Riba.speed_min, Riba.speed_max)
		self.x = random.randrange(1000, 1500)
		self.y = random.randrange(40, const.SCREEN_HEIGHT-80)
		self.riba_slika = pygame.image.load("riba.png")
	def draw_fish(self):
		global mreza_w, score
		gameDisplay.blit(self.riba_slika, (self.x, self.y))
		self.x -= self.speed
		if self.x <  0 :
			self.speed = random.randrange(Riba.speed_min, Riba.speed_max)
			self.y = random.randrange(40, const.SCREEN_HEIGHT-40-floor_h)
			self.x = random.randrange(1000, 1500)
		#Speeding up the fishes as the score increases
		if score > 15*Riba.k and score < 30 * Riba.k:
			Riba.counter = True
		if score % 15 == 0 and score > 1 and Riba.counter == True: 
			Riba.speed_min += 1
			Riba.speed_max += 1
			Riba.counter = False
			Riba.k += 1
		
		#Mreza and Fish collision 
		if mreza_x + mreza_w - 40 >= self.x and mreza_x + mreza_w <= self.x + Riba.riba_w and self.y >= mreza_y and self.y <= mreza_y + 50 :
			self.x = random.randrange(1000, 1500) 
			score += 1
			self.y = random.randrange(40, const.SCREEN_HEIGHT-40-floor_h)
			self.speed = random.randrange(Riba.speed_min, Riba.speed_max)
			


def floor(x, y, w, h, color):
	pygame.draw.rect(gameDisplay, color, [x, y, w, h])



floor1_pos = 1
floor_h = 40

mreza = Mreza(200, 300)

drugaRiba = Riba()
prvaRiba = Riba()
trecaRiba = Riba()
cetvrtaRiba = Riba()

score = 0

#Text stuff
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
		print (prvaRiba.speed_max)
		print(prvaRiba.counter)

		text = font.render("Score " +str(score)  , True, (255, 255, 255))
		gameDisplay.blit(text, ( 450, 5))

		pygame.display.update()
		clock.tick(80)