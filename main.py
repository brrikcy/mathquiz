import pygame
import button

#create display window
SCREEN_HEIGHT = 500
SCREEN_WIDTH = 800
global run

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Button Demo')

#load button images
start_img = pygame.image.load('start_btn.png').convert_alpha()
exit_img = pygame.image.load('exit_btn.png').convert_alpha()
option_img=pygame.image.load('option.png').convert_alpha()
#create button instances
start_button = button.Button(100, 200, start_img, 0.8)
exit_button = button.Button(450, 200, exit_img, 0.8)
option1=button.Button(100,300,option_img,0.2)
option2=button.Button(100,400,option_img,0.2)
option3=button.Button(420,300,option_img,0.2)
option4=button.Button(420,400,option_img,0.2)

def game_play():
	global run
	play=True
	while play:
		screen.fill((230,155,100))
		if option1.draw(screen):
			pass
		if option2.draw(screen):
			pass
		if option3.draw(screen):
			pass
		if option4.draw(screen):
			pass
		for event in pygame.event.get():
			# quit game
			if event.type == pygame.QUIT:
				run = False
				play=False

		pygame.display.update()
#game loop
run = True
while run:

	screen.fill((202, 228, 241))

	if start_button.draw(screen):
		game_play()
	if exit_button.draw(screen):
		run=False

	#event handler
	for event in pygame.event.get():
		#quit game
		if event.type == pygame.QUIT:
			run = False

	pygame.display.update()

pygame.quit()