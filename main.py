import pygame
import button
import random


# -------------------------------------------------------------------------------------------------
def generate_options(result):
    options = []
    options.append(result)
    for i in range(3):
        options.append(random.randint(result - 40, result + 40))
    random.shuffle(options)
    return options


def qsum():
    num1 = random.randint(1, 1000)
    num2 = random.randint(1, 1000)
    result = num1 + num2
    quest_display = f"{num1} + {num2} is"
    return (quest_display, result)


def qdif():
    num1 = random.randint(1, 1000)
    num2 = random.randint(1, 1000)
    result = num1 - num2
    quest_display = f"{num1} - {num2} is"
    return (quest_display, result)


def qpro():
    num1 = random.randint(1, 50)
    num2 = random.randint(1, 100)
    result = num1 * num2
    quest_display = f"{num1} * {num2} is"
    return (quest_display, result)


def qdiv():
    num1 = random.randint(50, 1000)
    num2 = random.randint(2, 50)
    while (num1 % num2 != 0):
        num2 = random.randint(2, 50)
    quest_display = f"{num1} / {num2} is"
    result = int(num1 / num2)
    return (quest_display, result)


def qmod():
    num1 = random.randint(1, 300)
    num2 = random.randint(1, 300)
    result = num1 % num2
    # print(f"{num1} % {num2} is ")
    quest_display = f"{num1} % {num2} is"
    # generate_options(result)
    return (quest_display, result)


# -------------------------------------------------------------------------------------------------


# create display window
SCREEN_HEIGHT = 500
SCREEN_WIDTH = 800
global run

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Button Demo')

# create font object
pygame.font.init()
font = pygame.font.Font('freesansbold.ttf', 46)
# operations = [qsum, qdif, qpro, qdiv, qmod]
# question = random.choice(operations)
# returned_result = question()
# quest_render = returned_result[0]
# answer = returned_result[1]
# opt_render = generate_options(answer)
# correct_option = opt_render.index(answer) + 1
# question_text = font.render(quest_render, True, ("White"))
# option1_text = font.render(str(opt_render[0]), True, (0, 0, 0))
# option2_text = font.render(str(opt_render[1]), True, (0, 0, 0))
# option3_text = font.render(str(opt_render[2]), True, (0, 0, 0))
# option4_text = font.render(str(opt_render[3]), True, (0, 0, 0))

# load button images
start_img = pygame.image.load('start_btn.png').convert_alpha()
exit_img = pygame.image.load('exit_btn.png').convert_alpha()
option_img = pygame.image.load('option.png').convert_alpha()

# create button instances
start_button = button.Button(100, 200, start_img, 0.8)
exit_button = button.Button(450, 200, exit_img, 0.8)
option1 = button.Button(100, 300, option_img, 0.2)
option2 = button.Button(420, 300, option_img, 0.2)
option3 = button.Button(100, 400, option_img, 0.2)
option4 = button.Button(420, 400, option_img, 0.2)


def game_play():
    operations = [qsum, qdif, qpro, qdiv, qmod]
    question = random.choice(operations)
    returned_result = question()
    quest_render = returned_result[0]
    answer = returned_result[1]
    opt_render = generate_options(answer)
    correct_option = opt_render.index(answer) + 1
    question_text = font.render(quest_render, True, ("White"))
    option1_text = font.render(str(opt_render[0]), True, (0, 0, 0))
    option2_text = font.render(str(opt_render[1]), True, (0, 0, 0))
    option3_text = font.render(str(opt_render[2]), True, (0, 0, 0))
    option4_text = font.render(str(opt_render[3]), True, (0, 0, 0))
    global run
    play = True
    while play:
        screen.fill((230, 155, 100))
        screen.blit(question_text, (250, 230))
        if option1.draw(screen):
            opt_prs = 1
        if option2.draw(screen):
            opt_prs = 2
        if option3.draw(screen):
            opt_prs = 3
        if option4.draw(screen):
            opt_prs = 4
        screen.blit(option1_text, (200, 310))
        screen.blit(option2_text, (500, 310))
        screen.blit(option3_text, (200, 420))
        screen.blit(option4_text, (500, 420))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                play = False
        pygame.display.update()


# game loop
run = True
while run:

    screen.fill((202, 228, 241))

    if start_button.draw(screen):
        game_play()
    if exit_button.draw(screen):
        run = False

    # event handler
    for event in pygame.event.get():
        # quit game
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()
