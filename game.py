
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
	"speed": 5,
	"wins": 0,
	"kills": 0,
	"lives": 5
}

goblin = {
	"x": 400,
	"y": 300,
	"speed": 1.5,
	"direction": "N"
}

monster = {
	"x": 200,
	"y": 150,
	"speed": 1
}

directions = [ 'N', 'S', 'E', 'W', 'NE', 'NW', 'SE', 'SW']
	
screen_size = (screen["height"], screen ["width"])
pygame_screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Goblin Chase")
background_image = pygame.image.load('images/background.png')
hero_image = pygame.image.load('images/hero.png')
goblin_image = pygame.image.load('images/goblin.png')
monster_image = pygame.image.load('images/monster.png')

# Add music files
pygame.mixer.music.load('sounds/music.wav')
pygame.mixer.music.play(-1)
win_sound = pygame.mixer.Sound('sounds/win.wav')
lose_sound = pygame.mixer.Sound('sounds/lose.wav')

tick = 0

# //////////////MAIN GAME LOOP//////////////

game_on = True
while game_on:
	tick += 1
	# we are inside the main game loop. I will run as long as the game is True
	# ----EVENTS----
	for event in pygame.event.get():
		# Looping through all events that happened this game loop cycle
		if event.type == pygame.QUIT:
			# the user clicked on the red X to leave the game
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
	
	if keys_down['up'] and hero['y'] > 0:
		hero['y'] -= hero['speed']
	elif keys_down['down'] and hero['y'] < 450:
		hero['y'] += hero['speed']
	if keys_down['left'] and hero['x'] > 0: 
		hero['x'] -= hero['speed']
	elif keys_down['right'] and hero['x'] < 480:
		hero['x'] += hero['speed']

	# Monster chasing hero

	if hero['x'] > monster['x']:
		monster['x'] += monster['speed']
	if hero['x'] < monster['x']:
		monster['x'] -= monster['speed']
	if hero['y'] > monster['y']:
		monster['y'] += monster['speed']
	if hero['y'] < monster['y']:
		monster['y'] -= monster['speed']

	# Update goblin position

	if (goblin['direction'] == 'N'):
		goblin['y'] -= goblin['speed']
	elif (goblin['direction'] == 'S'):
		goblin['y'] += goblin['speed']
	elif (goblin['direction'] == 'E'):
		goblin['x'] += goblin['speed']
	elif (goblin['direction'] == 'W'):
		goblin['x'] -= goblin['speed']
	elif (goblin['direction'] == 'NE'):
		goblin['y'] -= goblin['speed']
		goblin['x'] += goblin['speed']
	elif (goblin['direction'] == 'NW'):
		goblin['y'] -= goblin['speed']
		goblin['x'] -= goblin['speed']
	elif (goblin['direction'] == 'SE'):
		goblin['y'] += goblin['speed']
		goblin['x'] += goblin['speed']
	elif (goblin['direction'] == 'SW'):
		goblin['y'] += goblin['speed']
		goblin['x'] -= goblin['speed']

	if (tick % 20 == 0):
		new_dir_index = randint(0,len(directions) -1)
		goblin['direction'] = directions[new_dir_index]
	
	# Keeping goblin on the screen

	if (goblin['x'] > screen['width']):
		goblin['x'] = 0
	elif (goblin['x'] < 0):
		goblin['x'] = screen['width']
	if (goblin['y'] > screen['height']):
		goblin['y'] = 0
	elif (goblin['y'] < 0):
		goblin['y'] = screen['height']

	# COLLISION DETECTION!!
	distance_between = fabs(hero['x'] - goblin ['x']) + fabs(hero['y'] - goblin ['y'])
	if (distance_between < 32):
		# the hero and goblin are touching
		# generate a random X > 0, X < screen["width"]
		# generate a random Y > 0, Y < screen['height']
		rand_x = randint(0, screen['width'] - 50)
		rand_y = randint(0, screen['height'] - 50)
		goblin['x'] = rand_x
		goblin['y'] = rand_y
		# update the hero's wins
		hero['wins'] += 1
	distance_between = fabs(hero['x'] - monster ['x']) + fabs(hero['y'] - monster ['y'])
	if (distance_between < 32):
		rand_x = randint(0, screen['width']- 50)
		rand_y = randint(0, screen['height']- 50)
		monster['x'] = rand_x
		monster['y'] = rand_y		
		# update hero's lives
		hero['lives'] -= 1
		win_sound.play()
	# ----RENDER!----
	# blit takes 2 arguments
	# 1.What?
	# 2.Where?
	pygame_screen.blit(background_image, [0,0])
	# draw the hero wins on the screen
	font = pygame.font.Font(None, 25)
	wins_text = font.render("Wins: %d" % (hero['wins']), True, (0,0,0))
	lives_text = font.render("Lives remaining: %d" % (hero['lives']), True, (0,0,0))
	pygame_screen.blit(wins_text, [40,40])	
	pygame_screen.blit(lives_text, [40,60])

	if hero['lives'] == 0:
		game_over_text = font.render("YOU\'RE DEAD!!", True, (0,0,0))
		pygame_screen.blit(game_over_text, [100,150])
	# draw the hero
	pygame_screen.blit(hero_image, [hero['x'], hero['y']])
	# draw the goblin
	pygame_screen.blit(goblin_image, [goblin['x'], goblin['y']])
	# draw the monster
	pygame_screen.blit(monster_image, [monster['x'], monster['y']])
	# clear the screen for next time
	pygame.display.flip()







