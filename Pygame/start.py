import pygame
import os

WIDTH, HEIGHT = 1000, 700
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("First Game!")

BLUE = (66, 66, 245)
BLACK = (0, 0, 0)

BORDER = pygame.Rect(0, HEIGHT/2 - 5, WIDTH, 10)

FPS = 60
VEL = 5
CHARACTER_WIDTH, CHARACTER_HEIGHT = 135, 120

JAMES1 = pygame.image.load(
    os.path.join("gyani_slayer69", "lejames.png"))
JAMESone = pygame.transform.scale(JAMES1, (CHARACTER_WIDTH, CHARACTER_HEIGHT))
HARDEN1 = pygame.image.load(
    os.path.join("gyani_slayer69", "james is hard.png"))
HARDENone = pygame.transform.scale(HARDEN1, (CHARACTER_WIDTH, CHARACTER_HEIGHT)) 

def draw_window(top, bottom):
    WIN.fill(BLUE)
    pygame.draw.rect(WIN, BLACK, BORDER)
    WIN.blit(JAMESone, (bottom.x, bottom.y))
    WIN.blit(HARDENone, (top.x, top.y))
    pygame.display.update()

def lebron_movement(keys_pressed, bottom):
        if keys_pressed[pygame.K_LEFT] and bottom.x - VEL > 0: # LEFT
            bottom.x -= VEL
        if keys_pressed[pygame.K_RIGHT] and bottom.x + VEL + bottom.width < BORDER.x: # RIGHT
            bottom.x += VEL
        if keys_pressed[pygame.K_UP] and bottom.y - VEL > 0 < BORDER.x: # UP
            bottom.y -= VEL
        if keys_pressed[pygame.K_DOWN] and bottom.y + VEL + bottom.width < HEIGHT: # DOWN
            bottom.y += VEL

def harden_movement(keys_pressed, top): 
        if keys_pressed[pygame.K_z] and top.x - VEL > 0: # LEFT
            top.x -= VEL
        if keys_pressed[pygame.K_c] and top.x + VEL + top.width < BORDER.x: # RIGHT
            top.x += VEL
        if keys_pressed[pygame.K_s] and top.y - VEL > 0: # UP
            top.y -= VEL
        if keys_pressed[pygame.K_x] and top.y + VEL + top.height < HEIGHT: # DOWN
            top.y += VEL

def main():
    top = pygame.Rect(425, 50, CHARACTER_WIDTH, CHARACTER_HEIGHT)
    bottom = pygame.Rect(425, 550, CHARACTER_WIDTH, CHARACTER_HEIGHT)
    
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        keys_pressed = pygame.key.get_pressed()
        lebron_movement(keys_pressed, bottom)
        harden_movement(keys_pressed, top)
        draw_window(top, bottom)

    pygame.quit()

if __name__ == "__main__":
    main()
