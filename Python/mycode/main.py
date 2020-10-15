import pygame

pygame.init()

screen = pygame.display.set_mode((960,720))

class Cup(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        # image
        img = pygame.image.load('coffeecup.png').convert()
        self.image = img

        # volume
        self.rect = self.image.get_rect()
        self.rect.x = 10
        self.rect.y = 10

cup = Cup()

while True:
    pygame.display.update()
    screen.blit(cup.image, cup.rect)