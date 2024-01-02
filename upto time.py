import pygame,random,button,time,sys

# -------------------------------------------------------------------------------------------------


def generate_options(result):
    options = []
    options.append(result)
    for i in range(3):
        option=random.randint(result - 40, result + 40)
        options.append(option)
    options=list(set(options))
    while(len(options)<4):
        options.append(sum(options))
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
    num1 = random.randint(2, 60)
    num2 = num1 * random.randint(2, 30)
    if (num1 < num2):
        temp = num1
        num1 = num2
        num2 = temp

    quest_display = f"{num1} / {num2} is"
    result = int(num1 / num2)
    return (quest_display, result)


def qmod():
    num1 = random.randint(100, 300)
    num2 = random.randint(1, 100)
    result = num1 % num2
    quest_display = f"{num1} % {num2} is"
    return (quest_display, result)


# -------------------------------------------------------------------------------------------------


# create display window
SCREEN_HEIGHT = 500
SCREEN_WIDTH = 800



screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('MATH QUIZ')

# create font object
pygame.font.init()
# font = pygame.font.Font('freesansbold.ttf', 46)
score_and_life_font = pygame.font.Font('score-life.ttf',40)
options_font = pygame.font.Font('score-life.ttf',60)
question_font = pygame.font.Font('score-life.ttf',100)
time_font = pygame.font.Font('score-life.ttf',90)


# load button images
start_img = pygame.image.load('start_btn.png').convert_alpha()
exit_img = pygame.image.load('exit_btn.png').convert_alpha()
option_img = pygame.image.load('option.png').convert_alpha()
logo_img = pygame.image.load('logo.png').convert_alpha()

# create button instances
start_button = button.Button(0, 0, logo_img, 1.0)
exit_button = button.Button(580, 150, exit_img, 0.5)
option1 = button.Button(100, 300, option_img, 0.2)
option2 = button.Button(420, 300, option_img, 0.2)
option3 = button.Button(100, 400, option_img, 0.2)
option4 = button.Button(420, 400, option_img, 0.2)


score=0
life=3
screen_color = (200,200,180)
def game_play():
    global  score,life,isGameon,screen_color
    score_text=f"Score : {score}"
    life_text=f"Life: {life}"
    operations = [qsum, qdif, qpro, qdiv, qmod]
    question = random.choice(operations)
    returned_result = question()
    quest_render = returned_result[0]
    answer = returned_result[1]
    opt_render = generate_options(answer)
    correct_option = opt_render.index(answer) + 1
    print(correct_option)
    question_display = question_font.render(quest_render, True, ("Black"))
    question_text_width=question_font.size(quest_render)[0]
    option1_display = options_font.render(str(opt_render[0]), True, (0, 0, 0))
    option2_display = options_font.render(str(opt_render[1]), True, (0, 0, 0))
    option3_display = options_font.render(str(opt_render[2]), True, (0, 0, 0))
    option4_display = options_font.render(str(opt_render[3]), True, (0, 0, 0))
    score_display=score_and_life_font.render(score_text, True, ("Black"))
    life_display=score_and_life_font.render(life_text, True, ("Black"))
    start_time = time.time()
    time_limit=25

    while isGameon and life>0:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                isGameon = False

        elapsed_time = time.time() - start_time
        remaining_time = round(time_limit - elapsed_time,2)
        time_display=time_font.render(f"{remaining_time}", True, ("Black"))
        time_text_width=time_font.size(f"{remaining_time}")[0]
        screen.fill(screen_color)
        # screen.blit(question_display, (235, 180))
        screen.blit(question_display, (400-(question_text_width/2), 180))
        screen.blit(life_display, (680,30 ))
        screen.blit(score_display,(50,30))
        screen.blit(time_display, (400-(time_text_width/2), 60))
        opt_prs=0
        if option1.draw(screen):
            opt_prs = 1
        elif option2.draw(screen):
            opt_prs = 2
        elif option3.draw(screen):
            opt_prs = 3
        elif option4.draw(screen):
            opt_prs = 4
        screen.blit(option1_display, (200, 310))
        screen.blit(option2_display, (510, 310))
        screen.blit(option3_display, (200, 410))
        screen.blit(option4_display, (510, 410))
        if opt_prs == correct_option:
            score+=1
            screen_color=(20,100,20)
            game_play()
            isGameon=False
        elif opt_prs!=0 or elapsed_time>=time_limit:
            life-=1
            screen_color = (200, 30, 30)
            game_play()
            isGameon = False

        pygame.display.flip()


# game loop
isGameon=True
while isGameon:

    screen.blit(logo_img,(0,0))

    if start_button.draw(screen):
        game_play()


    # event handler
    for event in pygame.event.get():
        # quit game
        if event.type == pygame.QUIT:
            isGameon = False

    pygame.display.update()

pygame.quit()
