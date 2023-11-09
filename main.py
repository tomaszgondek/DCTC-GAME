import pygame
import math
import random
# init
pygame.init()
screen = pygame.display.set_mode((1200, 800))
font = pygame.font.Font('font/FFFFORWA.TTF', 50)
clock = pygame.time.Clock()
pygame.display.set_caption("Don't Crash the cat: Back for Blood")
score = '0'
scoreImg = font.render(score, True, (0, 0, 0))

# static graphics load
skyblock = pygame.image.load('graphics/placeholder_background.jpg').convert()

# Sprites
class CAT(pygame.sprite.Sprite):
    def __init__(self, pos):
        super(CAT, self).__init__()
        self.image = pygame.image.load('graphics/pngegg.png').convert_alpha()
        self.rect = self.image.get_rect(midbottom=(64, 64))
        self.rect.center = pos

    def moveRight(self, pixels):
        self.rect.x += pixels
        if self.rect.x > 1200 - self.image.get_width():
            self.rect.x = 1200 - self.image.get_width()

    def moveLeft(self, pixels):
        self.rect.x -= pixels
        if self.rect.x < 0:
            self.rect.x = 0

    def moveUp(self, pixels):
        self.rect.y -= pixels
        if self.rect.y < 0:
            self.rect.y = 0

    def moveDown(self, pixels):
        self.rect.y += pixels
        if self.rect.y > 800 - self.image.get_height():
            self.rect.y = 800 - self.image.get_height()

    def playerInput(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.moveLeft(5)
        if keys[pygame.K_d]:
            self.moveRight(5)
        if keys[pygame.K_w]:
            self.moveUp(5)
        if keys[pygame.K_s]:
            self.moveDown(5)

    def draw(self, surface):
        surface.blit(self.image, (self.rect.x, self.rect.y))

    def updateSprite(self, surface):
        self.playerInput()
        self.draw(surface)


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.pos = (x, y)
        mx, my = pygame.mouse.get_pos()
        self.dir = (mx - x, my - y)
        length = math.hypot(*self.dir)
        if length == 0.0:
            self.dir = (0, -1)
        else:
            self.dir = (self.dir[0]/length, self.dir[1]/length)
        angle = math.degrees(math.atan2(-self.dir[1], self.dir[0]))
        self.bullet = pygame.Surface((30, 2)).convert_alpha()
        self.bullet.fill((180, 45, 45))
        self.bullet = pygame.transform.rotate(self.bullet, angle)
        self.speed = 20
        self.rect = self.bullet.get_rect()

    def update(self):
        self.pos = (self.pos[0]+self.dir[0]*self.speed,
                    self.pos[1]+self.dir[1]*self.speed)

    def draw(self, surf):
        self.rect = self.bullet.get_rect(center=self.pos)
        surf.blit(self.bullet, self.rect)

    def updateSprite(self, surface):
        self.rect.move_ip(0,5)
        self.draw(surface)


class FlyEnemy(pygame.sprite.Sprite):
    def __init__(self, x1, y):
        pygame.sprite.Sprite.__init__(self)
        self.pos = (x1, y)
        self.image = pygame.image.load('graphics/placeholder_duck.png')
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect()
        self.rect.center = (x1, y)


    def moveDown(self):
        self.rect.y += 5

    def draw(self, surface):
        surface.blit(self.image, (self.rect.x, self.rect.y))

    def update(self):
        self.moveDown()


class Explosion2Firework(pygame.sprite.Sprite):
    def __init__(self, x, y, scale):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        for num in range(1, 20):
            img = pygame.image.load(f"graphics/PixelSimulations/Explosion2/{num}.png")
            img = pygame.transform.scale(img, (scale, scale))
            self.images.append(img)
        self.index = 0
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        self.counter = 0

    def update(self):
        explosionSpeed = 2
        self.counter += 1
        if self.counter >= explosionSpeed and self.index < len(self.images) - 1:
            self.counter = 0
            self.index += 1
            self.image = self.images[self.index]
        if self.index >= len(self.images) - 1 and self.counter >= explosionSpeed:
            self.kill()


# Sprite group initialisation
bullets = pygame.sprite.Group()
flies = pygame.sprite.Group()
explosions = pygame.sprite.Group()
theCat = CAT((600, 700))

# Custom events
createEnemyEvent, t = pygame.USEREVENT+1, 1000
pygame.time.set_timer(createEnemyEvent, t)

# main loop
while True:
    # skyblock
    screen.blit(skyblock, (0, 0))
    # handling user input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            bullets.add(Bullet(*(theCat.rect.x + 20, theCat.rect.y + 25)))
            bullets.add(Bullet(*(theCat.rect.x + 40, theCat.rect.y + 25)))
        if event.type == createEnemyEvent:
            flies.add(FlyEnemy(random.randrange(100, 1100), 0))
    # updating player
    theCat.updateSprite(screen)
    # handling enemies and bullets
    for fly in flies:
        fly.update()
        if fly.rect.y > screen.get_height():
            flies.remove(fly)
    for bullet in bullets:
        bullet.update()
        bullet.draw(screen)
        if not screen.get_rect().collidepoint(bullet.pos):
            bullets.remove(bullet)
    for fly in flies:
        flies.draw(screen)
    # hit collisions, score and animations
    getHits = pygame.sprite.groupcollide(flies, bullets, True, True)
    for hit in getHits:
        explosion = Explosion2Firework(hit.rect.centerx, hit.rect.centery, 150)
        explosions.add(explosion)
        print(hit)
        score = int(score)
        score += 1
        print(score)
        score = str(score)
        scoreImg = font.render(score, True, (0, 0, 0))
    explosions.draw(screen)
    explosions.update()
    screen.blit(scoreImg, (10, 10))
    # updating frame
    pygame.display.flip()
    clock.tick(60)
