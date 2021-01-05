import pygame
import sys
import os

'''
Variables
'''

# put variables here
worldx = 960
worldy = 720
fps    = 40  # frame rate
ani    = 4   # animation cycles
BLUE  = (25, 25, 200)
BLACK = (23, 23, 23)
WHITE = (254, 254, 254)
ALPHA = (0,0,0)
main = True

'''
Objects
'''

# put Python classes and functions here

class Enemy(pygame.sprite.Sprite):
    """
    Spawn an enemy
    """    

    def __init__(self,x,y,img):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join('images',img))
        self.image.convert_alpha()     # optimse alpha
        self.image.set_colorkey(ALPHA) # set alpha
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    #def update(self):
        """
        update sprite position
        """
        # self.rect.x = self.rect.x + self.movex
        # self.rect.y = self.rect.y + self.movey

        # # moving left
        # if self.movex < 0:
        #     self.frame += 1
        #     if self.frame > 7*ani:
        #         self.frame = 0
        #     self.image = pygame.transform.flip(self.images[self.frame//ani], True, False)

        # # moving right
        # if self.movex > 0:
        #     self.frame += 1
        #     if self.frame > 7*ani:
        #         self.frame = 0
        #     self.image = self.images[self.frame//ani]

class Player(pygame.sprite.Sprite):
    """
    Spawn a player
    """

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        for i in range(1, 5):
            img = pygame.image.load(os.path.join('images','hero' + str(i) + '.png')).convert()
            img.convert_alpha()     # optimise alpha
            img.set_colorkey(ALPHA) # set alpha
            self.images.append(img)
            self.image = self.images[0]
            self.rect = self.image.get_rect()
            self.movex = 0 # move along X
            self.movey = 0 # move along Y
            self.frame = 0 # count frames

    def control(self,x,y):
        """
        control player movement
        """
        self.movex += x
        self.movey += y

    def update(self):
        """
        update sprite position
        """
        self.rect.x = self.rect.x + self.movex
        self.rect.y = self.rect.y + self.movey

        # moving left
        if self.movex < 0:
            self.frame += 1
            if self.frame > 3*ani:
                self.frame = 0
            self.image = pygame.transform.flip(self.images[self.frame//ani], True, False)

        # moving right
        if self.movex > 0:
            self.frame += 1
            if self.frame > 3*ani:
                self.frame = 0
            self.image = self.images[self.frame//ani]


'''
Setup
'''

# put run-once code here
clock = pygame.time.Clock()
pygame.init()
world = pygame.display.set_mode([worldx,worldy])
backdrop = pygame.image.load(os.path.join('images','stage.png'))
backdropbox = world.get_rect()

player = Player()   # spawn player
player.rect.x = 0   # go to x
player.rect.y = 0   # go to y
player_list = pygame.sprite.Group()
player_list.add(player)
steps = 10

enemy = Enemy(300,0,'enemy0.png')   # spawn enemy
enemy_list = pygame.sprite.Group()
enemy_list.add(enemy)


'''
Main Loop
'''

# put game loop here
while main:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            try:
                sys.exit()
            finally:
                main = False

        if event.type == pygame.KEYDOWN:
            if event.key == ord('q'):
                pygame.quit()
                try:
                    sys.exit()
                finally:
                    main = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                player.control(-steps,0)
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                player.control(steps,0)
            if event.key == pygame.K_UP or event.key == ord('w'):
                print('jump')

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                player.control(steps,0)
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                player.control(-steps,0)
            if event.key == ord('q'):
                pygame.quit()
                sys.exit()
                main = False  

    world.blit(backdrop, backdropbox)
    player.update()         # update player position
    player_list.draw(world) # draw player
    enemy.update()          # update enemy position
    enemy_list.draw(world)  # draw enemy
    pygame.display.flip()
    clock.tick(fps)
