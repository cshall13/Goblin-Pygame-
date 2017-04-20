
# Include pygame which we got from pip 
import pygame

# In order to use pygame, we have to run the init method
pygame.init()


screen = {
	"height": 512,
	"width": 480
}

screen_size = (screen["height"], screen ["width"])
pygame_screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Goblin Chase")

game_on = True

while game_on:
	# we are inside the main game loop. I will run as long as the game is True
	for event in pygame.event.get():
		# Looping through all events that happened this game loop cycle
		if event.type == pygame.QUIT:
			# the use clicked on the red X to leave the game
			game_on = False 
			# update our boolean, so pygame can escape the loop 