#Write a program to create a Pygame window with two circles, 
#one solid and another hollow circle with border width 3. 
#Keep the background colour as - white RGB(255, 255, 255)
#and the colour of the rectangle as green (0, 255, 0).
#Try changing the values of centre and radius to see how the position
#and size of the balls change.
import pygame
pygame.init()
screen=pygame.display.set_mode((500,500))
screen.fill((255,255,255))
done=False
while not done:
    for e in pygame.event.get():
        if e.type==pygame.QUIT:
            pygame.quit()
            done=True
        else:
            pygame.draw.circle(screen,"green",(100,100),67)
            pygame.display.update()