import pygame
import math
import random
# init
pygame.init()
screen = pygame.display.set_mode((1200, 800))
font = pygame.font.Font('font/FFFFORWA.TTF', 50)
clock = pygame.time.Clock()
pygame.display.set_caption("Don't Crash the cat: Back for Blood")

# static graphics load
skyblock = pygame.image.load('graphics/placeholder_background.jpg').convert()

# story
# intro
# 1st
text1 = font.render('So you want to hear a story, eh?', True, (255, 255, 255))
text11 = font.render('press SPACE to continue', True, (255, 255, 255))
background1 = pygame.image.load('graphics/PLACEHOLDER1.jpg')
text1 = pygame.transform.scale(text1, (text1.get_width()/2, text1.get_height()/2))
text11 = pygame.transform.scale(text11, (text11.get_width()/4, text11.get_height()/4))
# 2nd
text2 = font.render('There was a cat planet, in a galaxy far away...', True, (255, 255, 255))
background2 = pygame.image.load('graphics/PLACEHOLDER1.jpg')
text2 = pygame.transform.scale(text2, (text2.get_width()/2, text2.get_height()/2))
# 3rd
text3 = font.render('...where all cats lived lazy and care-free lives.', True, (255, 255, 255))
background3 = pygame.image.load('graphics/PLACEHOLDER1.jpg')
text3 = pygame.transform.scale(text3, (text3.get_width()/2, text3.get_height()/2))
# 4th
text4 = font.render('And suddenly, everything has changed.', True, (255, 255, 255))
background4 = pygame.image.load('graphics/PLACEHOLDER1.jpg')
text4 = pygame.transform.scale(text4, (text4.get_width()/2, text4.get_height()/2))
# 5th
text5 = font.render('Unknown threat, from the stars.', True, (255, 255, 255))
background5 = pygame.image.load('graphics/PLACEHOLDER1.jpg')
text5 = pygame.transform.scale(text5, (text5.get_width()/2, text5.get_height()/2))
# 6th
text6 = font.render('A war has begun, that claimed many lives.', True, (255, 255, 255))
background6 = pygame.image.load('graphics/PLACEHOLDER1.jpg')
text6 = pygame.transform.scale(text6, (text6.get_width()/2, text6.get_height()/2))
# 7th
text7 = font.render('But when everything seemed to be lost...', True, (255, 255, 255))
background7 = pygame.image.load('graphics/PLACEHOLDER1.jpg')
text7 = pygame.transform.scale(text7, (text7.get_width()/2, text7.get_height()/2))
# 8th
text8 = font.render('...an ancient cat, a pallas cat with unimaginable powers...', True, (255, 255, 255))
background8 = pygame.image.load('graphics/PLACEHOLDER1.jpg')
text8 = pygame.transform.scale(text8, (text8.get_width()/2, text8.get_height()/2))
# 9th
text9 = font.render('...came to rescue, with one goal - to kill the invaders', True, (255, 255, 255))
background9 = pygame.image.load('graphics/PLACEHOLDER1.jpg')
text9 = pygame.transform.scale(text9, (text9.get_width()/2, text9.get_height()/2))
# 10th
# tutaj cały ten, title screen


# Sprites
class CAT(pygame.sprite.Sprite):
    def __init__(self, pos):
        super(CAT, self).__init__()
        self.image = pygame.image.load('graphics/pngegg.png').convert_alpha()
        self.rect = self.image.get_rect(midbottom=(64, 64))
        self.rect.center = pos
        self.playerSpeed = 5
        self.bulletType = 1
        self.currentHP = 1000
        self.maxHP = 1000
        self.targetHP = 1000
        self.hpBarLen = 200
        self.hpRatio = self.maxHP / self.hpBarLen
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

class GameStage():
    def __init__(self):
        self.level = 'intro'
        self.introScene = 1

    def stageManager(self):
        if self.level == 'intro':
            self.intro()
        if self.level == 'level01':
            self.level01()

    def intro(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.introScene += 1
        if self.introScene == 1:
            screen.blit(background1, (0, 0))
            screen.blit(text1, (screen.get_width()/2 - text1.get_width()/2, 700))
            screen.blit(text11, (screen.get_width()/2 - text11.get_width()/2, 750))
        if self.introScene == 2:
            screen.blit(background2, (0, 0))
            screen.blit(text2, (screen.get_width()/2 - text2.get_width()/2, 700))
        if self.introScene == 3:
            screen.blit(background3, (0, 0))
            screen.blit(text3, (screen.get_width() / 2 - text3.get_width() / 2, 700))
        if self.introScene == 4:
            screen.blit(background4, (0, 0))
            screen.blit(text4, (screen.get_width() / 2 - text4.get_width() / 2, 700))
        if self.introScene == 5:
            screen.blit(background5, (0, 0))
            screen.blit(text5, (screen.get_width() / 2 - text5.get_width() / 2, 700))
        if self.introScene == 6:
            screen.blit(background6, (0, 0))
            screen.blit(text6, (screen.get_width() / 2 - text6.get_width() / 2, 700))
        if self.introScene == 7:
            screen.blit(background7, (0, 0))
            screen.blit(text7, (screen.get_width() / 2 - text7.get_width() / 2, 700))
        if self.introScene == 8:
            screen.blit(background8, (0, 0))
            screen.blit(text8, (screen.get_width() / 2 - text8.get_width() / 2, 700))
        if self.introScene == 9:
            screen.blit(background9, (0, 0))
            screen.blit(text9, (screen.get_width() / 2 - text9.get_width() / 2, 700))
        if self.introScene == 10:
            self.level = 'level01'
        pygame.display.flip()
        clock.tick(60)

    def level01(self):
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
        explosions.draw(screen)
        explosions.update()
        pygame.display.flip()
        clock.tick(60)


# Sprite group initialisation
bullets = pygame.sprite.Group()
partridgesNormal = pygame.sprite.Group()
explosions = pygame.sprite.Group()
theCat = CAT((600, 700))
gameStage = GameStage()

# Custom events
createEnemyEvent, t = pygame.USEREVENT+1, 1000
pygame.time.set_timer(createEnemyEvent, t)

# main loop
while True:
    gameStage.stageManager()

