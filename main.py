import pygame
import math
import random
# init
pygame.init()
screen = pygame.display.set_mode((1200, 800))
font = pygame.font.Font('font/FFFFORWA.TTF', 50)
clock = pygame.time.Clock()
pygame.display.set_caption("Don't Crash the cat: Back for Blood")
score = 0
scoreImg = font.render(str(score), True, (0, 0, 0))

# static graphics load
skyblock = pygame.image.load('graphics/placeholder_background.jpg').convert()


# Sprites
class CAT(pygame.sprite.Sprite):
    def __init__(self, pos):
        super(CAT, self).__init__()
        self.image = pygame.image.load('graphics/pngegg.png').convert_alpha()
        self.rect = self.image.get_rect(midbottom=(64, 64))
        self.rect.center = pos
        self.playerSpeed = 5
        self.bulletType = 1
        self.currentHP = 200
        self.maxHP = 1000
        self.targetHP = 200
        self.hpBarLen = 200
        self.hpRatio = self.maxHP / self.currentHP
        self.hpChangeSpeed = 5
        self.isAlive = True

    def getDamage(self, amount):
        if self.targetHP > 0:
            self.targetHP -= amount
        if self.targetHP < 0:
            self.targetHP = 0

    def getHealth(self, amount):
        if self.targetHP < self.maxHP:
            self.targetHP += amount
        if self.targetHP > self.maxHP:
            self.targetHP = self.maxHP

        def hpBar(self):
            pygame.draw.rect(screen, (255, 0, 0), (40, screen.get_height() - 65, self.targetHP / self.hpRatio, 25))
            pygame.draw.rect(screen, (255, 255, 255), (40, screen.get_height() - 65, self.hpBarLen, 25), 4)

        # guwno nie dziala
        def hpBarv2(self):
            transition_width = 0
            transition_color = (255, 0, 0)
            if self.currentHP < self.targetHP:
                self.currentHP += self.targetHP
                transition_width = int((self.targetHP - self.currentHP) / self.targetHP)
                transition_color = (0, 255, 0)
            if self.currentHP > self.targetHP:
                self.currentHP -= self.hpChangeSpeed
                transition_width = int((self.targetHP - self.currentHP) / self.hpRatio)
                transition_color = (255, 255, 0)
            health_bar_width = int(self.currentHP / self.hpRatio)
            health_bar = pygame.Rect(10, 45, health_bar_width, 25)
            transition_bar = pygame.Rect(health_bar.right, 45, transition_width, 25)
            pygame.draw.rect(screen, (255, 0, 0), health_bar)
            pygame.draw.rect(screen, transition_color, transition_bar)
            pygame.draw.rect(screen, (255, 255, 255), (10, 45, self.hpBarLen, 25), 4)


    def moveRight(self, pixels):
        self.rect.x += pixels
        if self.rect.x > screen.get_width() - self.image.get_width():
            self.rect.x = screen.get_width() - self.image.get_width()

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
        if self.rect.y > screen.get_height() - self.image.get_height():
            self.rect.y = screen.get_height() - self.image.get_height()

    def playerInput(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.moveLeft(self.playerSpeed)
        if keys[pygame.K_d]:
            self.moveRight(self.playerSpeed)
        if keys[pygame.K_w]:
            self.moveUp(self.playerSpeed)
        if keys[pygame.K_s]:
            self.moveDown(self.playerSpeed)

    def draw(self, surface):
        surface.blit(self.image, (self.rect.x, self.rect.y))


    def updateSprite(self, surface):
        self.hpBar()
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


class PartridgeNormal(pygame.sprite.Sprite):
    def __init__(self, x1, y, scale, speed):
        pygame.sprite.Sprite.__init__(self)
        self.pos = (x1, y)
        self.image = pygame.image.load('graphics/placeholder_duck.png')
        self.image = pygame.transform.scale(self.image, (scale, scale))
        self.rect = self.image.get_rect()
        self.rect.center = (x1, y)
        self.speed = speed
        self.hp = 100

    def moveDown(self):
        self.rect.y += self.speed

    def draw(self, surface):
        surface.blit(self.image, (self.rect.x, self.rect.y))

    def update(self):
        self.moveDown()
        if self.hp < 0:
            self.kill()



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
partridgesNormal = pygame.sprite.Group()
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
            theCat.getHealth(10)
        if event.type == createEnemyEvent:
            partridgesNormal.add(PartridgeNormal(random.randrange(100, 1100), 0, 100, 5))
            partridgesNormal.add(PartridgeNormal(random.randrange(100, 1100), 0, 100, 5))
    # updating player
    theCat.updateSprite(screen)
    # handling enemies and bullets
    for partridge in partridgesNormal:
        partridge.update()
        if partridge.rect.y > screen.get_height():
            partridgesNormal.remove(partridge)
            theCat.getDamage(10)
    for bullet in bullets:
        bullet.update()
        bullet.draw(screen)
        if not screen.get_rect().collidepoint(bullet.pos):
            bullets.remove(bullet)
    for partridge in partridgesNormal:
        partridgesNormal.draw(screen)
    # hit collisions, score and animations
    getHits = pygame.sprite.groupcollide(partridgesNormal, bullets, True, True)
    for hit in getHits:
        explosion = Explosion2Firework(hit.rect.centerx, hit.rect.centery, 250)
        explosions.add(explosion)
        score += 1
        scorestr = score
        scoreImg = font.render(str(scorestr), True, (0, 0, 0))
    explosions.draw(screen)
    explosions.update()
    screen.blit(scoreImg, (10, 10))
    # updating frame
    pygame.display.flip()
    clock.tick(60)
