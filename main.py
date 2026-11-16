import pygame
import sys
import math


def main():
    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    clock = pygame.time.Clock()
    running = True  
    ball_pos = pygame.Vector2(540, 560)
    pivot_pos = pygame.Vector2(640, 150)

    g = 10
    l = 1
    angle_0 = math.pi / 4

    angle_accel = -(g / l) * math.sin(angle_0)
    t = 0
    dt = 0
    right = False
    down = False
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill((0,0,0))

        angle = angle_0 * math.cos(math.sqrt(g/l) * (t + dt))

        if ball_pos.x <= 540:
            right = True
        elif ball_pos.x >= 740:
            right = False
        
        if right:
            ball_pos.x += l * math.sin(angle) 
        else:
            ball_pos.x -= l * math.sin(angle) 

        if (ball_pos.x >= 640 and right) or (ball_pos.x < 640 and not right):
            down = False
        elif (ball_pos.x <= 540 and right) or (ball_pos.x >= 740 and not right):
            down = True
        
        if down:
            ball_pos.y += l * math.cos(angle) 
        else:
            ball_pos.y -= l * math.cos(angle) 

        pygame.draw.line(screen,(255,255,255),pivot_pos,ball_pos,2)
        pygame.draw.circle(screen,(255,0,0),ball_pos,30,1)

        
        pygame.display.flip()
        dt = clock.tick(60) / 1000
    
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()