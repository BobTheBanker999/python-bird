import pygame
from pygame.locals import *
import random as rand

# constants
SCREEN_W = 800
SCREEN_H = 600

# pygame init
pygame.init()

# classes

# player
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.Surface((50, 50))
        self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect() # lollolol get rekt

        # move to better position
        self.rect.move_ip(100, 100)

        # physics stats
        self.vel = 0
        self.jumpPower = 1.0
        self.accel = 0

    def update(self, keys):
        self.rect.move_ip(0, self.vel+self.accel)

        self.vel += 0.1
        self.accel += 0.1

        if keys[pygame.K_SPACE]:
            self.vel -= self.jumpPower
            self.accel = 0

# obstacle
class Obstacle(pygame.sprite.Sprite):
    def __init__(self):
        super(Obstacle, self).__init__()
        self.surf = pygame.Surface((100, rand.randint(200, 400)))
        self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect()

        self.rect.move_ip(SCREEN_W, 0)

    def update(self):
        self.rect.move_ip(-5, 0)

        if self.rect.right < 0:
            self.kill()

# variables
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()
obstacles = pygame.sprite.Group()
p = Player()
all_sprites.add(p)

# haha score go weee
score = 0

# custom event
ADDOBSTACLE = pygame.USEREVENT + 1
pygame.time.set_timer(ADDOBSTACLE, 3000)


print("Subscribe!!!")

# create window
window = pygame.display.set_mode((SCREEN_W, SCREEN_H))
pygame.display.set_caption("Flappy Bird in 1 hour")

# main game loop

running = True

while running:

    window.fill((0, 0, 0))

    # font variable
    font = pygame.font.SysFont(None, 25)

    for event in pygame.event.get():

        if event.type == QUIT:
            pygame.quit()

        elif event.type == ADDOBSTACLE:
            o = Obstacle()
            obstacles.add(o)
            all_sprites.add(o)
            if p.alive():
                score += 1

    for sprite in all_sprites:
        window.blit(sprite.surf, sprite.rect)

    keys = pygame.key.get_pressed()

    if keys[pygame.K_ESCAPE]:
        pygame.quit()

    # has player collided with obstacle?
    if pygame.sprite.spritecollideany(p, obstacles):
        pygame.quit()

    p.update(keys)
    obstacles.update()

    # render score text
    score_txt = font.render("Score: " + str(score), True, (255, 255, 255))
    window.blit(score_txt, (5, 5))

    clock.tick(30)
    pygame.display.flip()

pygame.quit()
