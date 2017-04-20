
# Include pygame which we got from pip 
import pygame

# bring in the math module so we can use absolute value
from math import fabs

# get the random module
from random import randint
# In order to use pygame, we have to run the init method
pygame.init()

screen = {
	"height": 512,
	"width": 480
}

keys = {
	"right": 275,
	"left": 276,
	"up": 273,
	"down": 274
}

keys_down = {
	"right": False,
	"left": False,
	"up": False,
	"down": False
}

hero = {
	"x": 100,
	"y": 100,
	"speed": 10,
	"wins": 0
}

goblin = {
	"x": 400,
	"y": 300,
	"speed": 10
}

monster = {
	"x": 200,
	"y": 150,
	"speed": 10
}

screen_size = (screen["height"], screen ["width"])
pygame_screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Goblin Chase")
background_image = pygame.image.load('images/background.png')
hero_image = pygame.image.load('images/hero.png')
goblin_image = pygame.image.load('images/goblin.png')
monster_image = pygame.image.load('images/monster.png')

# //////////////MAIN GAME LOOP//////////////
game_on = True
while game_on:
	# we are inside the main game loop. I will run as long as the game is True
	# ----EVENTS----
	for event in pygame.event.get():
		# Looping through all events that happened this game loop cycle
		if event.type == pygame.QUIT:
			# the use clicked on the red X to leave the game
			game_on = False 
			# update our boolean, so pygame can escape the loop 
		elif event.type == pygame.KEYDOWN:
			if event.key == keys["up"]: 
				keys_down['up'] = True
			elif event.key == keys["down"]:
				keys_down['down'] = True
			elif event.key == keys["left"]:
				keys_down['left'] = True
			elif event.key == keys["right"]:
				keys_down['right'] = True
		elif event.type == pygame.KEYUP:
			# print "The user let go of a key"
			if event.key == keys["up"]:
				keys_down['up'] = False
			if event.key == keys["down"]:
				keys_down['down'] = False
			if event.key == keys["left"]:
				keys_down['left'] = False
			if event.key == keys["right"]:
				keys_down['right'] = False
	# Update Hero position
	
	if keys_down['up']:
		hero['y'] -= hero['speed']
	elif keys_down['down']:
		hero['y'] += hero['speed']
	if keys_down['left']:
		hero['x'] -= hero['speed']
	elif keys_down['right']:
		hero['x'] += hero['speed']

	# COLLISION DETECTION!!
	distance_between = fabs(hero['x'] - goblin ['x']) + (hero['y'] - goblin ['y'])
	if (distance_between < 32):
		# the hero and goblin are touching
		# generate a random X > 0, X < screen["width"]
		# generate a random Y > 0, Y < screen['height']
		rand_x = randint(0, screen['width'])
		rand_y = randint(0, screen['height'])
		goblin['x'] = rand_x
		goblin['y'] = rand_y
		# update the hero's wins
		hero['wins'] += 1
	# ----RENDER!----
	# blit takes 2 arguments
	# 1.What?
	# 2.Where?
	pygame_screen.blit(background_image, [0,0])
	# draw the hero wins on the screen
	font = pygame.font.Font(None, 25)
	wins_text = font.render("Wins: %d" % (hero['wins']), True, (0,0,0))
	pygame_screen.blit(wins_text, [40,40])	
	# draw the hero
	pygame_screen.blit(hero_image, [hero['x'], hero['y']])
	# draw the goblin
	pygame_screen.blit(goblin_image, [goblin['x'], goblin['y']])
	# draw the monster
	pygame_screen.blit(monster_image, [monster['x'], monster['y']])
	# clear the screen for next time
	pygame.display.flip()







