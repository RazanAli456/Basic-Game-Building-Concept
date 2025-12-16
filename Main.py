#Write a program to create a Pygame window with a rectangle in it.
#Keep the background colour as - black RGB(0,0,0) and color of the rectangle as
#blue (0, 125, 255). Position the rectangle anywhere on the screen
#Try changing the values of top, left,
#height and width to see how the position and size of the rectangle changes.
import pygame
pygame.init()
screen=pygame.display.set_mode((500,500))
screen.fill((0,0,0))
done=False
while not done:
    for e in pygame.event.get():
        if e.type==pygame.QUIT:
            pygame.quit()
            done=True
        else:
            pygame.draw.rect(screen,(0,125,255),pygame.Rect(40,40,80,30))
            pygame.display.update()