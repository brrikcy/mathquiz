import pygame
def game_over(score):
    import pygame

    pygame.init()
    width, height = 800, 600
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("GAME OVER")

    pygame.font.init()
    font1 = pygame.font.Font('score-life.ttf', 80)
    game_over_display = font1.render("GAME OVER", True, ("White"))
    game_over_text_width = font1.size("GAME OVER")[0]


    while True:
        screen.fill((0, 0, 0))
        screen.blit(game_over_display,(400-(game_over_text_width/2),250))



        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()



        pygame.display.flip()
game_over(20)