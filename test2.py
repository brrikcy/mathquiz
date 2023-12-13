import pygame
import button
import random
#-------------------------------------------------------------------------------------------------
def generate_options(res):
    options = []
    options.append(res)
    for i in range(3):
        options.append(random.randint(res-40,res+40))
    random.shuffle(options)
    for j in options:
        print(j)
    answer = int(input("choose an answer: "))
    if answer == res:
        print("correct")
    else:
        print("wrong")
def qsum():
    num1 = random.randint(1, 1000)
    num2 = random.randint(1, 1000)
    result=num1+num2
    # print(f"{num1} + {num2} ")
    # generate_options(result)
    s = f"{num1} + {num2} is"
    return s
def qdif():
    num1 = random.randint(1, 1000)
    num2 = random.randint(1, 1000)
    result=num1-num2
    # print(f"{num1} - {num2} is ")
    # generate_options(result)
    s = f"{num1} - {num2} is"
    return s
def qpro():
    num1 = random.randint(1, 50)
    num2 = random.randint(1, 100)
    result=num1*num2
    # print(f"{num1} * {num2} is ")
    # generate_options(result)
    s = f"{num1} * {num2} is"
    return s
def qdiv():
    num1 = random.randint(1, 1000)
    num2 = random.randint(1, 100)
    if num1<50:
        num1+=random.randint(40,100)
    if num1%num2==0:
        # print(f"{num1} / {num2} is ")
        s = f"{num1} / {num2} is"
        return s
        result=num1/num2
        # generate_options(int(result))

    else:
        qdiv()
def qmod():
    num1 = random.randint(1, 300)
    num2 = random.randint(1, 300)
    result=num1%num2
    # print(f"{num1} % {num2} is ")
    s= f"{num1} % {num2} is"
    # generate_options(result)
    return s


#-------------------------------------------------------------------------------------------------




#create display window
SCREEN_HEIGHT = 500
SCREEN_WIDTH = 800
global run

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Button Demo')

#create font object
pygame.font.init()
font = pygame.font.Font('freesansbold.ttf',46)
operations=[qsum,qdif,qpro,qdiv,qmod]
question=random.choice(operations)
print(question)
quest=question()
print(quest)
text=font.render(quest,True,("White"))


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
        screen.blit(text, (220, 230))
        if option1.draw(screen):
            pass
        if option2.draw(screen):
            pass
        if option3.draw(screen):
            pass
        if option4.draw(screen):
            pass
        for event in pygame.event.get():
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
