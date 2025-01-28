import pygame
pygame.font.init()
from bird import Bird
from pipe import Pipe
from base import Base
from variables import WIN_WIDTH, WIN_HEIGHT, BIRD_IMGS, PIPE_IMG, BASE_IMG, BG_IMG, STAT_FONT




def draw_window(win, bird, pipes, base, score):
    win.blit(BG_IMG, (0, 0))
    
    for pipe in pipes:
        pipe.draw(win)
        
    text = STAT_FONT.render("Score: " + str(score), 1, (255,255,255))
    win.blit(text, (WIN_WIDTH - 10 - text.get_width(), 10))
        
    base.draw(win)
    bird.draw(win)
    pygame.display.update()





def main():
    bird = Bird(230, 350)
    base = Base(730)
    pipes = [Pipe(600)]
    win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
    clock = pygame.time.Clock()
    score = 0
    
    run = True
    while run:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                
                
        # bird.move()
        add_pipe = False
        remove = []
        for pipe in pipes:
            pipe.move()
            if pipe.collide(bird):
                pass
        
            if pipe.x + pipe.PIPE_TOP.get_width() < 0:
                remove.append(pipe)
                
            if not pipe.passed and pipe.x < bird.x:
                pipe.passed = True
                add_pipe = True
                
            pipe.move()
            
        if add_pipe:
            score += 1
            pipes.append(Pipe(600))
            
        for r in remove:
            pipes.remove(r)
            
        if bird.y + bird.img.get_height() >= 730:
            pass
        
        base.move()
        draw_window(win, bird, pipes, base, score)



    pygame.quit()
    quit()
    
main()