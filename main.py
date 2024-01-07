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
secCounter = 0

uiBackgroundColor = (37, 0, 46)


# static graphics load
skyblock = pygame.image.load('graphics/placeholder_background.jpg').convert()
playbuttonWide = pygame.image.load('graphics/PLAYBUTTON.jpg')
playbuttonWide = pygame.transform.scale(playbuttonWide, (400, 150))
playbuttonSmall = pygame.image.load('graphics/PLAYBUTTON_SMALL.jpg')
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

def getFont(size):
    return pygame.font.Font("font/FFFFORWA.TTF", size)

def blit_text(surface, text, pos, font, color=pygame.Color('black')):
    words = [word.split(' ') for word in text.splitlines()]  # 2D array where each row is a list of words.
    space = font.size(' ')[0]  # The width of a space.
    max_width, max_height = surface.get_size()
    x, y = pos
    for line in words:
        for word in line:
            word_surface = font.render(word, 0, color)
            word_width, word_height = word_surface.get_size()
            if x + word_width >= max_width:
                x = pos[0]  # Reset the x.
                y += word_height  # Start on new row.
            surface.blit(word_surface, (x, y))
            x += word_width + space
        x = pos[0]  # Reset the x.
        y += word_height  # Start on new row.


class CAT(pygame.sprite.Sprite):
    def __init__(self, pos):
        super(CAT, self).__init__()
        self.images = []
        for i in range(1, 6):
            img = pygame.image.load(f"graphics/manul/{i}.png").convert_alpha()
            img = pygame.transform.scale_by(img, 2)
            self.images.append(img)
        self.index = 0
        self.image = self.images[self.index]
        self.rect = self.image.get_rect(midbottom=(64, 64))
        self.rect.center = pos
        self.initPos = pos
        self.dmgPowerup = 1
        self.playerSpeed = 5
        self.bulletType = 'laser'
        self.currentHP = 1000
        self.maxHP = 1000
        self.hpBarLen = 200
        self.hpRatio = self.maxHP / self.hpBarLen
        self.currentMana = 1000
        self.maxMana = 1000
        self.manaBarLen = 200
        self.manaRatio = self.maxMana / self.manaBarLen
        self.isAlive = True
        self.laserFire = 10
        self.plasmaFire = 50
        self.shotgunFire = 20
        self.shootTime = 0
        self.mask = pygame.mask.from_surface(self.image)
        self.fireCycle = 1
        self.fireFlag = False
        self.ManaCostRedux = 1
        self.counter = 0

    def reset(self):
        self.rect = self.image.get_rect(midbottom=(64, 64))
        self.rect.center = self.initPos
        self.dmgPowerup = 1
        self.playerSpeed = 5
        self.bulletType = 'laser'
        self.currentHP = 1000
        self.maxHP = 1000
        self.hpBarLen = 200
        self.hpRatio = self.maxHP / self.hpBarLen
        self.currentMana = 1000
        self.maxMana = 1000
        self.manaBarLen = 200
        self.manaRatio = self.maxMana / self.manaBarLen
        self.isAlive = True
        self.laserFire = 10
        self.plasmaFire = 50
        self.shotgunFire = 20
        self.shootTime = 0
        self.mask = pygame.mask.from_surface(self.image)
        self.fireCycle = 1
        self.fireFlag = False
        self.ManaCostRedux = 1


    def getDamage(self, amount):
        if self.currentHP > 0:
            self.currentHP -= amount
        if self.currentHP <= 0:
            self.isAlive = False
            self.currentHP = 0


    def getNegMana(self, amount):
        if self.currentMana > 0:
            self.currentMana -= amount
        if self.currentMana < 0:
            self.currentMana = 0

    def getMana(self, amount):
        if self.currentMana < self.maxMana:
            self.currentMana += amount
        if self.currentMana > self.maxMana:
            self.currentMana = self.maxMana

    def getHealth(self, amount):
        if self.currentHP < self.maxHP:
            self.currentHP += amount
        if self.currentHP > self.maxHP:
            self.currentHP = self.maxHP

    def hpBar(self):
        pygame.draw.rect(screen, (255, 0, 0), (40, screen.get_height() - 65, self.currentHP / self.hpRatio, 25))
        pygame.draw.rect(screen, (255, 255, 255), (40, screen.get_height() - 65, self.hpBarLen, 25), 4)

    def manaBar(self):
        pygame.draw.rect(screen, (100, 100, 255), (40, screen.get_height() - 100, self.currentMana / self.manaRatio, 25))
        pygame.draw.rect(screen, (255, 255, 255), (40, screen.get_height() - 100, self.manaBarLen, 25), 4)

    def shoot(self, bulletType):
        self.shootTime += 1
        if self.currentMana > 0:
            if bulletType == 'laser' and self.shootTime >= self.laserFire and self.currentMana >= 60:
                bullets.add(laserBullet(*(self.rect.x + 52, self.rect.y + 14), True, self.dmgPowerup))
                bullets.add(laserBullet(*(self.rect.x + 74, self.rect.y + 14), True, self.dmgPowerup))
                self.shootTime = 0
                self.getNegMana(60 * self.ManaCostRedux)
            if bulletType == 'plasma' and self.shootTime >= self.plasmaFire and self.currentMana >= 250:
                bullets.add(plasmaBullet(*(self.rect.center), True, False, 30, self.dmgPowerup))
                self.shootTime = 0
                self.getNegMana(250 * self.ManaCostRedux)
            if bulletType == 'shotgun' and self.shootTime >= self.shotgunFire and self.currentMana >= 100:
                shotgunB1 = shotgutBullet(*(self.rect.center), 0, True, self.dmgPowerup)
                shotgunB2 = shotgutBullet(*(self.rect.center), 45, True, self.dmgPowerup)
                shotgunB3 = shotgutBullet(*(self.rect.center), -45, True, self.dmgPowerup)
                bullets.add(shotgunB1)
                bullets.add(shotgunB2)
                bullets.add(shotgunB3)
                self.shootTime = 0
                self.getNegMana(100 * self.ManaCostRedux)

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

    def checkColisions(self):
        collisions = []
        collisions = pygame.sprite.spritecollide(self, partridgesNormal, 0, pygame.sprite.collide_mask)
        hits = []
        hits = pygame.sprite.spritecollide(self, bullets, 0, pygame.sprite.collide_mask)
        powerupGets = []
        powerupGets = pygame.sprite.spritecollide(self, powerupsGroup, 0, pygame.sprite.collide_mask)
        for hit in hits:
            if hit.isFriendly == False:
                self.getDamage(hit.carryDMG)
                dmgP = damagePanel(self.rect.x, self.rect.y, hit.carryDMG, 20, (min(65 + hit.carryDMG, 255), 0, max(255 - hit.carryDMG, 0)))
                damages.add(dmgP)
                hit.kill()
        for collision in collisions:
            dmgDone = round(collision.hp*0.75)
            self.getDamage(dmgDone)
            dmgP = damagePanel(self.rect.x, self.rect.y, dmgDone, 20, (min(65 + collision.hp, 255), 0, max(255 - collision.hp, 0)))
            damages.add(dmgP)
            collision.hp = 0
        for powerupGet in powerupGets:
            if powerupGet.type == "DMG":
                self.dmgPowerup = self.dmgPowerup * powerupGet.powerupVal
                powerupGet.kill()
            if powerupGet.type == "HP":
                self.getHealth(powerupGet.powerupVal)
                powerupGet.kill()

    def playerInput(self):
        if self.fireFlag == True:
            self.fireCycle += 1
            if self.fireCycle == 4:
                self.fireCycle = 1
            if self.fireCycle == 1:
                self.bulletType = 'laser'
            elif self.fireCycle == 2:
                self.bulletType = 'plasma'
            elif self.fireCycle == 3:
                self.bulletType = 'shotgun'
            self.fireFlag = False
        left, middle, right = pygame.mouse.get_pressed()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.moveLeft(self.playerSpeed)
        if keys[pygame.K_d]:
            self.moveRight(self.playerSpeed)
        if keys[pygame.K_w]:
            self.moveUp(self.playerSpeed)
        if keys[pygame.K_s]:
            self.moveDown(self.playerSpeed)
        if left:
            self.shoot(self.bulletType)


    def draw(self, surface):
        surface.blit(self.image, (self.rect.x, self.rect.y))


    def updateSprite(self, surface):
        anim = 6
        self.counter += 1
        if self.counter >= anim and self.index < len(self.images) - 1:
            self.counter = 0
            self.index += 1
            self.image = self.images[self.index]
        if self.index >= len(self.images) - 1 and self.counter >= anim:
            self.index = 0
            self.image = self.images[self.index]
        self.draw(screen)
        self.checkColisions()
        self.hpBar()
        self.getMana(3)
        self.manaBar()
        self.playerInput()

class skyBlock(pygame.sprite.Sprite):
    def __init__(self, imagePath, offset):
        pygame.sprite.Sprite.__init__(self)
        self.speed = 0
        self.offset = offset
        self.image = pygame.image.load(imagePath).convert()
        self.height = self.image.get_height()
        self.panels = math.ceil(screen.get_height() / self.image.get_height()) + 2

    def update(self):
        self.speed += self.offset
        if abs(self.speed) > self.image.get_height():
            self.speed = 0
        for i in range (self.panels):
            screen.blit(self.image, (0, i * self.height + self.speed - self.height))


class laserBullet(pygame.sprite.Sprite):
    def __init__(self, x, y, isFriendly, dmgIncrease):
        pygame.sprite.Sprite.__init__(self)
        self.dmgMultip = dmgIncrease
        self.manaCost = 75
        self.carryDMG = 25 * self.dmgMultip
        self.isFriendly = isFriendly
        self.pos = (x, y)
        mx, my = pygame.mouse.get_pos()
        self.dir = (mx - x, my - y)
        length = math.hypot(*self.dir)
        if length == 0.0:
            self.dir = (0, -1)
        else:
            self.dir = (self.dir[0]/length, self.dir[1]/length)
        angle = math.degrees(math.atan2(-self.dir[1], self.dir[0]))
        self.bullet = pygame.image.load('graphics/bullets/Laser_Sprites/14.png').convert_alpha()
        self.bullet = pygame.transform.scale(self.bullet, (32, 32))
        self.bullet = pygame.transform.rotate(self.bullet, angle)
        self.speed = 20
        self.rect = self.bullet.get_rect()
        self.mask = pygame.mask.from_surface(self.bullet)

    def draw(self, surf):
        self.rect = self.bullet.get_rect(center=self.pos)
        surf.blit(self.bullet, self.rect)

    def update(self):
        self.pos = (self.pos[0] + self.dir[0] * self.speed,
                    self.pos[1] + self.dir[1] * self.speed)
        self.rect.move_ip(0,5)
        self.draw(screen)
        if self.pos[0] > screen.get_width() or self.pos[0] < 0 or self.pos[1] > screen.get_height() or self.pos[1] < 0:
            self.kill()

class plasmaBullet(pygame.sprite.Sprite):
    def __init__(self, x, y, isFriendly, isDown, speed, dmgIncrease):
        pygame.sprite.Sprite.__init__(self)
        self.dmgIncrease = dmgIncrease
        self.carryDMG = 185 * dmgIncrease
        self.isFriendly = isFriendly
        self.pos = (x, y)
        if not isDown:
            mx, my = pygame.mouse.get_pos()
        if isDown:
            mx, my = x, 1000
        self.dir = (mx - x, my - y)
        length = math.hypot(*self.dir)
        if length == 0.0:
            self.dir = (0, -1)
        else:
            self.dir = (self.dir[0]/length, self.dir[1]/length)
        angle = math.degrees(math.atan2(-self.dir[1], self.dir[0]))
        self.bullet = pygame.image.load('graphics/bullets/Laser_Sprites/27.png').convert_alpha()
        self.bullet = pygame.transform.scale(self.bullet, (100, 150))
        self.bullet = pygame.transform.rotate(self.bullet, angle)
        self.speed = speed
        self.rect = self.bullet.get_rect()
        self.mask = pygame.mask.from_surface(self.bullet)

    def draw(self, surf):
        self.rect = self.bullet.get_rect(center=self.pos)
        surf.blit(self.bullet, self.rect)

    def update(self):
        self.pos = (self.pos[0] + self.dir[0] * self.speed,
                    self.pos[1] + self.dir[1] * self.speed)
        self.rect.move_ip(0,5)
        self.draw(screen)
        if self.pos[0] > screen.get_width() or self.pos[0] < 0 or self.pos[1] > screen.get_height() or self.pos[1] < 0:
            self.kill()

class plasmaBulletv2(pygame.sprite.Sprite):
    def __init__(self, x, y, isFriendly, isDown, speed, dmgIncrease):
        pygame.sprite.Sprite.__init__(self)
        self.dmgIncrease = dmgIncrease
        self.carryDMG = 185 * dmgIncrease
        self.isFriendly = isFriendly
        self.pos = (x, y)
        if not isDown:
            mx, my = pygame.mouse.get_pos()
        if isDown:
            mx, my = x, 1000
        self.dir = (mx - x, my - y)
        length = math.hypot(*self.dir)
        if length == 0.0:
            self.dir = (0, -1)
        else:
            self.dir = (self.dir[0]/length, self.dir[1]/length)
        angle = math.degrees(math.atan2(-self.dir[1], self.dir[0]))
        self.bullet = pygame.image.load('graphics/bullets/Laser_Sprites/51.png').convert_alpha()
        self.bullet = pygame.transform.scale(self.bullet, (100, 150))
        self.bullet = pygame.transform.rotate(self.bullet, angle)
        self.speed = speed
        self.rect = self.bullet.get_rect()
        self.mask = pygame.mask.from_surface(self.bullet)

    def draw(self, surf):
        self.rect = self.bullet.get_rect(center=self.pos)
        surf.blit(self.bullet, self.rect)

    def update(self):
        self.pos = (self.pos[0] + self.dir[0] * self.speed,
                    self.pos[1] + self.dir[1] * self.speed)
        self.rect.move_ip(0,5)
        self.draw(screen)
        if self.pos[0] > screen.get_width() or self.pos[0] < 0 or self.pos[1] > screen.get_height() or self.pos[1] < 0:
            self.kill()

class shotgutBullet(pygame.sprite.Sprite):
    def __init__(self, x, y, offset, isFriendly, dmgIncrease):
        pygame.sprite.Sprite.__init__(self)
        self.dmgMultip = dmgIncrease
        self.carryDMG = 60 * dmgIncrease
        self.isFriendly = isFriendly
        self.pos = (x, y)
        mx, my = pygame.mouse.get_pos()
        mx += offset
        self.dir = (mx - x, my - y)
        length = math.hypot(*self.dir)
        if length == 0.0:
            self.dir = (0, -1)
        else:
            self.dir = (self.dir[0]/length, self.dir[1]/length)
        angle = math.degrees(math.atan2(-self.dir[1], self.dir[0]))
        self.bullet = pygame.image.load('graphics/bullets/Laser_Sprites/07.png').convert_alpha()
        self.bullet = pygame.transform.scale(self.bullet, (50, 50))
        self.bullet = pygame.transform.rotate(self.bullet, angle)
        self.speed = 30
        self.rect = self.bullet.get_rect()
        self.mask = pygame.mask.from_surface(self.bullet)

    def draw(self, surf):
        self.rect = self.bullet.get_rect(center=self.pos)
        surf.blit(self.bullet, self.rect)

    def update(self):
        self.pos = (self.pos[0] + self.dir[0] * self.speed,
                    self.pos[1] + self.dir[1] * self.speed)
        self.rect.move_ip(0,5)
        self.draw(screen)
        if self.pos[0] > screen.get_width() or self.pos[0] < 0 or self.pos[1] > screen.get_height() or self.pos[1] < 0:
            self.kill()

class sniperBullet(pygame.sprite.Sprite):
    def __init__(self, x, y, isFriendly, tx, ty):
        pygame.sprite.Sprite.__init__(self)
        self.carryDMG = 25
        self.isFriendly = isFriendly
        self.pos = (x, y)
        mx, my = tx, ty
        self.dir = (mx - x, my - y)
        length = math.hypot(*self.dir)
        if length == 0.0:
            self.dir = (0, -1)
        else:
            self.dir = (self.dir[0]/length, self.dir[1]/length)
        angle = math.degrees(math.atan2(-self.dir[1], self.dir[0]))
        self.bullet = pygame.image.load('graphics/bullets/Laser_Sprites/03.png').convert_alpha()
        self.bullet = pygame.transform.scale(self.bullet, (200, 32))
        self.bullet = pygame.transform.rotate(self.bullet, angle)
        self.speed = 20
        self.rect = self.bullet.get_rect()
        self.mask = pygame.mask.from_surface(self.bullet)

    def draw(self, surf):
        self.rect = self.bullet.get_rect(center=self.pos)
        surf.blit(self.bullet, self.rect)

    def update(self):
        self.pos = (self.pos[0] + self.dir[0] * self.speed,
                    self.pos[1] + self.dir[1] * self.speed)
        self.rect.move_ip(0,5)
        self.draw(screen)
        if self.pos[0] > screen.get_width() or self.pos[0] < 0 or self.pos[1] > screen.get_height() or self.pos[1] < 0:
            self.kill()

class sniperBulletv2(pygame.sprite.Sprite):
    def __init__(self, x, y, isFriendly, tx, ty):
        pygame.sprite.Sprite.__init__(self)
        self.carryDMG = 5
        self.isFriendly = isFriendly
        self.pos = (x, y)
        mx, my = tx, ty
        self.dir = (mx - x, my - y)
        length = math.hypot(*self.dir)
        if length == 0.0:
            self.dir = (0, -1)
        else:
            self.dir = (self.dir[0]/length, self.dir[1]/length)
        angle = math.degrees(math.atan2(-self.dir[1], self.dir[0]))
        self.bullet = pygame.image.load('graphics/bullets/Laser_Sprites/10.png').convert_alpha()
        self.bullet = pygame.transform.scale(self.bullet, (200, 50))
        self.bullet = pygame.transform.rotate(self.bullet, angle)
        self.speed = 20
        self.rect = self.bullet.get_rect()
        self.mask = pygame.mask.from_surface(self.bullet)

    def draw(self, surf):
        self.rect = self.bullet.get_rect(center=self.pos)
        surf.blit(self.bullet, self.rect)

    def update(self):
        self.pos = (self.pos[0] + self.dir[0] * self.speed,
                    self.pos[1] + self.dir[1] * self.speed)
        self.rect.move_ip(0,5)
        self.draw(screen)
        if self.pos[0] > screen.get_width() or self.pos[0] < 0 or self.pos[1] > screen.get_height() or self.pos[1] < 0:
            self.kill()

class hellBulletWobbly(pygame.sprite.Sprite):
    def __init__(self, x, y, isFriendly, givenAngle):
        pygame.sprite.Sprite.__init__(self)
        self.sAngle = givenAngle
        self.carryDMG = 15
        self.isFriendly = isFriendly
        self.pos = (x, y)
        mx = math.cos(math.degrees(self.sAngle))
        my = math.sin(math.degrees(self.sAngle))
        self.dir = (mx, my)
        length = math.hypot(*self.dir)
        if length == 0.0:
            self.dir = (0, -1)
        else:
            self.dir = (self.dir[0]/length, self.dir[1]/length)
        angle = math.degrees(math.atan2(-self.dir[1], self.dir[0]))
        self.bullet = pygame.image.load('graphics/bullets/Laser_Sprites/04.png').convert_alpha()
        self.bullet = pygame.transform.scale(self.bullet, (100, 50))
        self.bullet = pygame.transform.rotate(self.bullet, angle)
        self.speed = 10
        self.rect = self.bullet.get_rect()
        self.mask = pygame.mask.from_surface(self.bullet)
        self.toggle = False

    def draw(self, surf):
        self.rect = self.bullet.get_rect(center=self.pos)
        surf.blit(self.bullet, self.rect)

    def bulletSpeed(self):
        if self.toggle == False:
            self.speed -= 1
        elif self.toggle == True:
            self.speed += 1
        if self.speed >= 20:
            self.toggle = False
        if self.speed <= 1:
            self.toggle = True

    def update(self):
        self.bulletSpeed()
        self.pos = (self.pos[0] + self.dir[0] * self.speed,
                    self.pos[1] + self.dir[1] * self.speed)
        self.rect.move_ip(0,5)
        self.draw(screen)
        if self.pos[0] > screen.get_width() or self.pos[0] < 0 or self.pos[1] > screen.get_height() or self.pos[1] < 0:
            self.kill()

class hellBulletRing(pygame.sprite.Sprite):
    def __init__(self, x, y, isFriendly, givenAngle):
        pygame.sprite.Sprite.__init__(self)
        self.sAngle = givenAngle
        self.carryDMG = 10
        self.isFriendly = isFriendly
        self.pos = (x, y)
        mx = math.cos(math.degrees(self.sAngle))
        my = math.sin(math.degrees(self.sAngle))
        self.dir = (mx, my)
        length = math.hypot(*self.dir)
        if length == 0.0:
            self.dir = (0, -1)
        else:
            self.dir = (self.dir[0]/length, self.dir[1]/length)
        angle = math.degrees(math.atan2(-self.dir[1], self.dir[0]))
        self.bullet = pygame.image.load('graphics/bullets/Laser_Sprites/19.png').convert_alpha()
        self.bullet = pygame.transform.scale(self.bullet, (64, 64))
        self.bullet = pygame.transform.rotate(self.bullet, angle)
        self.speed = 10
        self.rect = self.bullet.get_rect()
        self.mask = pygame.mask.from_surface(self.bullet)
        self.toggle = False

    def draw(self, surf):
        self.rect = self.bullet.get_rect(center=self.pos)
        surf.blit(self.bullet, self.rect)

    def update(self):

        self.pos = (self.pos[0] + self.dir[0] * self.speed,
                    self.pos[1] + self.dir[1] * self.speed)
        self.rect.move_ip(0,5)
        self.draw(screen)
        if self.pos[0] > screen.get_width() or self.pos[0] < 0 or self.pos[1] > screen.get_height() or self.pos[1] < 0:
            self.kill()

class PerdixNormal(pygame.sprite.Sprite):
    def __init__(self, x, y, tx, ty, scale, speed):
        pygame.sprite.Sprite.__init__(self)
        self.index = 0
        self.pos = (x, y)
        self.target = (tx, ty)
        self.angle = self.getAngle(self.pos, self.target)
        self.images = []
        for i in range(1, 3):
            img = pygame.image.load(f"graphics/partridge/{i}.png").convert_alpha()
            img = pygame.transform.flip(img, False, True)
            img = pygame.transform.scale_by(img, scale)
            img = pygame.transform.rotate(img, -1 * math.degrees(self.angle) - 90)
            img = pygame.transform.flip(img, 1, 0)
            self.images.append(img)
        self.rect = self.images[self.index].get_rect()
        self.rect.center = (x, y)
        self.speed = speed
        self.hp = 100
        self.image = self.images[self.index]
        self.carryDMG = 20
        self.mask = pygame.mask.from_surface(self.images[self.index])
        self.counter = 0
        self.switch = 0

    def checkColisions(self):
        hits = []
        hits = pygame.sprite.spritecollide(self, bullets, 0)
        for hit in hits:
            if hit.isFriendly == True:
                self.hp -= hit.carryDMG
                dmgP = damagePanel(self.rect.x, self.rect.y, hit.carryDMG, 20, (min(65 + hit.carryDMG, 255), 0, max(255 - hit.carryDMG, 0)))
                hit.kill()
                damages.add(dmgP)

    def getAngle(self, origin, destination):
        x_dist = destination[0] - origin[0]
        y_dist = destination[1] - origin[1]
        return math.atan2(-y_dist, x_dist) % (2 * math.pi)

    def project(self, pos, angle, distance):
        return (pos[0] + (math.cos(angle) * distance),
                pos[1] - (math.sin(angle) * distance))

    def goCrazyv2(self):
        self.pos = self.project(self.pos, self.angle, self.speed)
        self.rect.center = self.pos

    def moveDown(self):
        self.rect.y += self.speed

    def goCrazy(self):
        self.rect.x += self.x_speed
        self.rect.y += self.y_speed

    def draw(self, surface):
        surface.blit(self.image, (self.rect.x, self.rect.y))

    def update(self):
        anim = random.randrange(10, 12)
        self.counter += 1
        if self.counter >= anim and self.switch == 0:
            print(len(self.images))
            self.switch = 1
            self.image = self.images[0]
            self.counter = 0
        if self.counter >= anim and self.switch == 1:
            print("02")
            self.switch = 0
            self.image = self.images[1]
            self.counter = 0
        self.checkColisions()
        if self.rect.y > screen.get_height():
            self.kill()
        # self.moveDown()
        self.goCrazyv2()
        if self.hp <= 0:
            explosion = Explosion2Firework(self.rect.centerx, self.rect.centery, 250)
            explosions.add(explosion)
            global score
            score += 1
            self.kill()
        self.draw(screen)

class powerup(pygame.sprite.Sprite):
    def __init__(self, x, y, value, type):
        pygame.sprite.Sprite.__init__(self)
        self.type = type
        self.speed = 3
        self.powerupVal = value
        self.pos = (x, y)
        self.target = (x, 2000)
        self.image = pygame.image.load('graphics/fredi.jpg').convert_alpha()
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.mask = pygame.mask.from_surface(self.image)

    def moveDown(self):
        self.rect.y += self.speed

    def draw(self, surface):
        surface.blit(self.image, (self.rect.x, self.rect.y))

    def update(self):
        self.moveDown()
        if self.rect.y > screen.get_height():
            self.kill()
        self.draw(screen)

class PerdixShooter(pygame.sprite.Sprite):
    def __init__(self, x, y, scale, speed):
        pygame.sprite.Sprite.__init__(self)
        self.pos = (x, y)
        self.index = 0;
        self.images = []
        for i in range(1, 3):
            img = pygame.image.load(f"graphics/shooter_partridge/{i}.png").convert_alpha()
            img = pygame.transform.flip(img, False, True)
            img = pygame.transform.scale_by(img, scale)
            img = pygame.transform.flip(img, 1, 0)
            self.images.append(img)
        self.rect = self.images[self.index].get_rect()
        self.image = self.images[self.index]
        self.rect.center = (x, y)
        self.speed = speed
        self.hp = 150
        self.carryDMG = 20
        self.Toggle = False
        self.fireRate = 60
        self.fireTick = 0
        self.counter = 0
        self.switch = 0
        self.mask = pygame.mask.from_surface(self.images[self.index])

    def checkColisions(self):
        hits = []
        hits = pygame.sprite.spritecollide(self, bullets, 0)
        for hit in hits:
            if hit.isFriendly == True:
                self.hp -= hit.carryDMG
                hit.kill()
                dmgP = damagePanel(self.rect.x, self.rect.y, hit.carryDMG, 20, (min(65 + hit.carryDMG, 255), 0, max(255 - hit.carryDMG, 0)))
                damages.add(dmgP)

    def moveLeftRight(self):
        if not self.Toggle:
            self.rect.x += self.speed
            if self.rect.x >= screen.get_width() - self.image.get_width():
                self.Toggle = True
        if self.Toggle == True:
            self.rect.x -= self.speed
            if self.rect.x <= 0:
                self.Toggle = False

    def shoot(self):
        self.fireTick += 1
        if self.fireTick >= self.fireRate:
            bullet = plasmaBullet(self.rect.centerx, self.rect.centery+30, False, True, 8, 1)
            bullets.add(bullet)
            self.fireTick = 0


    def draw(self, surface):
        surface.blit(self.image, (self.rect.x, self.rect.y))

    def update(self):
        anim = random.randrange(10, 12)
        self.counter += 1
        if self.counter >= anim and self.switch == 0:
            self.switch = 1
            self.image = self.images[0]
            self.counter = 0
        if self.counter >= anim and self.switch == 1:
            self.switch = 0
            self.image = self.images[1]
            self.counter = 0
        self.checkColisions()
        self.shoot()
        if self.rect.y > screen.get_height():
            self.kill()
        # self.moveDown()
        self.moveLeftRight()
        if self.hp <= 0:
            explosion = Explosion2Firework(self.rect.centerx, self.rect.centery, 250)
            explosions.add(explosion)
            global score
            score += 3
            self.kill()
        self.draw(screen)

class PerdixSniper(pygame.sprite.Sprite):
    def __init__(self, x, y, scale, speed, targetX, targetY):
        pygame.sprite.Sprite.__init__(self)
        self.pos = (x, y)
        self.index = 0;
        self.images = []
        for i in range(1, 3):
            img = pygame.image.load(f"graphics/sniper_partridge/{i}.png").convert_alpha()
            img = pygame.transform.flip(img, False, True)
            img = pygame.transform.scale_by(img, scale)
            img = pygame.transform.flip(img, 1, 0)
            self.images.append(img)
        self.rect = self.images[self.index].get_rect()
        self.image = self.images[self.index]
        self.rect.center = (x, y)
        self.speed = speed
        self.hp = 150
        self.carryDMG = 20
        self.Toggle = False
        self.fireRate = 60
        self.fireTick = 0
        self.counter = 0
        self.switch = 0
        self.mask = pygame.mask.from_surface(self.images[self.index])
        self.target = (targetX, targetY)

    def checkColisions(self):
        hits = []
        hits = pygame.sprite.spritecollide(self, bullets, 0)
        for hit in hits:
            if hit.isFriendly == True:
                self.hp -= hit.carryDMG
                hit.kill()
                dmgP = damagePanel(self.rect.x, self.rect.y, hit.carryDMG, 20, (min(65 + hit.carryDMG, 255), 0, max(255 - hit.carryDMG, 0)))
                damages.add(dmgP)

    def moveLeftRight(self):
        if not self.Toggle:
            self.rect.x += self.speed
            if self.rect.x >= screen.get_width() - self.image.get_width():
                self.Toggle = True
        if self.Toggle == True:
            self.rect.x -= self.speed
            if self.rect.x <= 0:
                self.Toggle = False

    def shoot(self):
        self.fireTick += 1
        if self.fireTick >= self.fireRate:
            bullet = sniperBullet(self.rect.centerx, self.rect.centery+30, False, self.target[0], self.target[1])
            bullets.add(bullet)
            self.fireTick = 0


    def draw(self, surface):
        surface.blit(self.image, (self.rect.x, self.rect.y))

    def update(self):
        anim = random.randrange(10, 12)
        self.counter += 1
        if self.counter >= anim and self.switch == 0:
            self.switch = 1
            self.image = self.images[0]
            self.counter = 0
        if self.counter >= anim and self.switch == 1:
            self.switch = 0
            self.image = self.images[1]
            self.counter = 0
        self.checkColisions()
        self.shoot()
        self.target = (theCat.rect.centerx, theCat.rect.centery)
        if self.rect.y > screen.get_height():
            self.kill()
        # self.moveDown()
        self.moveLeftRight()
        if self.hp <= 0:
            explosion = Explosion2Firework(self.rect.centerx, self.rect.centery, 250)
            explosions.add(explosion)
            global score
            score += 5
            self.kill()
        self.draw(screen)

class frediKamionka(pygame.sprite.Sprite):
    def __init__(self, x, y, scale, speed, targetX, targetY):
        pygame.sprite.Sprite.__init__(self)
        self.pos = (x, y)
        self.image = pygame.image.load('graphics/fredi.jpg').convert_alpha()
        self.image = pygame.transform.scale(self.image, (scale, scale))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.speed = speed
        self.hp = 2000
        self.carryDMG = 20
        self.Toggle = False
        self.fireRatePlasma = 50
        self.fireRateSniper = 100
        self.fireRateHellv2 = 150
        self.fireRateHell = 10
        self.fireTickPlasma = 0
        self.fireTickSniper = 0
        self.fireTickHell = 0
        self.fireTickHellv2 = 0
        self.hellOffset = 0
        self.mask = pygame.mask.from_surface(self.image)
        self.target = (targetX, targetY)

    def checkColisions(self):
        hits = []
        hits = pygame.sprite.spritecollide(self, bullets, 0)
        for hit in hits:
            if hit.isFriendly == True:
                self.hp -= hit.carryDMG
                hit.kill()
                dmgP = damagePanel(self.rect.x, self.rect.y, hit.carryDMG, 20, (min(65 + hit.carryDMG, 255), 0, max(255 - hit.carryDMG, 0)))
                damages.add(dmgP)

    def moveLeftRight(self):
        if not self.Toggle:
            self.rect.x += self.speed
            if self.rect.x >= screen.get_width()/3 - self.image.get_width()/3:
                self.Toggle = True
        if self.Toggle == True:
            self.rect.x -= self.speed
            if self.rect.x <= 0:
                self.Toggle = False

    def shootPlasma(self):
        bullet = plasmaBulletv2(self.rect.centerx, self.rect.centery + 30, False, True, 8, 1)
        bullets.add(bullet)

    def shootSniper(self):
        bullet = sniperBulletv2(self.rect.centerx, self.rect.centery + 30, False, self.target[0], self.target[1])
        bullets.add(bullet)

    def bulletHell(self, offset):
        for i in range(0, 7):
            bullet = hellBulletWobbly(self.rect.centerx, self.rect.centery, False, (60 * i) + offset)
            bullets.add(bullet)

    def bulletHellv2(self):
        for i in range(0, 37):
            bullet = hellBulletRing(self.rect.centerx, self.rect.centery, False, (10 * i))
            bullets.add(bullet)


    def shoot(self):
        self.fireTickPlasma += 1
        self.fireTickSniper += 1
        self.fireTickHell += 1
        self.fireTickHellv2 += 1
        if self.fireTickPlasma >= self.fireRatePlasma:
            self.shootPlasma()
            self.fireTickPlasma = 0
        if self.fireTickSniper >= self.fireRateSniper:
            self.fireTickSniper = 0
        if self.fireTickHell >= self.fireRateHell:
            self.bulletHell(self.hellOffset)
            self.hellOffset += 1
            self.fireTickHell = 0
        if self.fireTickHellv2 >= self.fireRateHellv2:
            self.bulletHellv2()
            self.fireTickHellv2 = 0



    def draw(self, surface):
        surface.blit(self.image, (self.rect.x, self.rect.y))

    def update(self):
        self.checkColisions()
        self.shoot()
        self.target = (theCat.rect.centerx, theCat.rect.centery)
        if self.rect.y > screen.get_height():
            self.kill()
        # self.moveDown()
        self.moveLeftRight()
        if self.hp <= 0:
            explosion = Explosion2Firework(self.rect.centerx, self.rect.centery, 250)
            explosions.add(explosion)
            global score
            score += 5
            self.kill()
        self.draw(screen)

class damagePanel(pygame.sprite.Sprite):
    def __init__(self, x, y, dmg, counter, color):
        pygame.sprite.Sprite.__init__(self)
        self.text = str(dmg)
        self.pos = [x, y]
        self.color = color
        self.image = font.render(self.text, True, self.color)
        self.image = pygame.transform.scale(self.image, (self.image.get_width()/3, self.image.get_height()/3))
        self.killIn = counter
        self.initCounter = 0

    def draw(self, surface):
        surface.blit(self.image, self.pos)

    def update(self):
        self.initCounter += 1
        if self.initCounter >= self.killIn:
            self.kill()
        self.draw(screen)

class Explosion2Firework(pygame.sprite.Sprite):
    def __init__(self, x, y, scale):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        for num in range(1, 20):
            img = pygame.image.load(f"graphics/PixelSimulations/Explosion2/{num}.png").convert_alpha()
            img = pygame.transform.scale(img, (scale, scale))
            self.images.append(img)
        self.index = 0
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        self.counter = 0

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def update(self):
        explosionSpeed = 2
        self.counter += 1
        if self.counter >= explosionSpeed and self.index < len(self.images) - 1:
            self.counter = 0
            self.index += 1
            self.image = self.images[self.index]
        if self.index >= len(self.images) - 1 and self.counter >= explosionSpeed:
            self.kill()
        self.draw(screen)

# handling game itself
class Button:
    def __init__(self, image, pos, text_input, font1, base_color, hovering_color):
        self.image = image
        self.x_pos = pos[0]
        self.y_pos = pos[1]
        self.font = font1
        self.base_color, self.hovering_color = base_color, hovering_color
        self.text_input = text_input
        self.text = self.font.render(self.text_input, True, self.base_color)
        if self.image is None:
            self.image = self.text
        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
        self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

    def update(self, screen1):
        if self.image is not None:
            screen1.blit(self.image, self.rect)
        screen1.blit(self.text, self.text_rect)

    def checkForInput(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            return True
        return False

    def changeColor(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            self.text = self.font.render(self.text_input, True, self.hovering_color)
        else:
            self.text = self.font.render(self.text_input, True, self.base_color)

class Game:
    def __init__(self):
        self.level = 'menu'
        self.saveState = []
        with open('save/levels.txt') as f:
            while True:
                levelSave = f.readline()
                self.saveState.append(levelSave.strip())
                if not levelSave:
                    break
        f.close()
        self.introScene = 1
        self.levelIntroDone = int(self.saveState[0])
        self.level01Done = int(self.saveState[1])
        self.level02Done = int(self.saveState[2])
        self.level03Done = int(self.saveState[3])
        self.level04Done = int(self.saveState[4])
        self.level05Done = int(self.saveState[5])
        self.currentLevel = self.level
        self.secCounter = 0
        self.score = 0

    def saveHandler(self):
        with open('save/levels.txt', 'w') as f:
            f.write(f"{int(self.levelIntroDone)}\n")
            f.write(f"{int(self.level01Done)}\n")
            f.write(f"{int(self.level02Done)}\n")
            f.write(f"{int(self.level03Done)}\n")
            f.write(f"{int(self.level04Done)}\n")
            f.write(f"{int(self.level05Done)}\n")
        f.close()


    def scoreDisplay(self, score):
        scoreImg = font.render(f"SCORE: {score}", True, (0, 0, 100))
        scoreImg = pygame.transform.scale_by(scoreImg, 0.5)
        screen.blit(scoreImg, (1000, 750))

    def stageManager(self):
        if self.level == "menu":
            self.mainMenu()
        if self.level == 'intro':
            self.intro()
        if self.level == 'level01':
            self.level01()
        if self.level == 'level02':
            self.level02()
        if self.level == 'level03':
            self.level03()
        if self.level == 'level04':
            self.level04()
        if self.level == 'level05':
            self.level05()
        if self.level == 'pause':
            self.pause()
        if self.level == 'levelSelector':
            self.levelSelectorP1()
        if self.level == 'levelSelectorP2':
            self.levelSelectorP2()
        if self.level == 'endLevelScreen':
            self.endLevelScreen()
        if self.level == 'failScreen':
            self.failScreen()

    def mainMenu(self):
        menuText = font.render("DON'T CRASH THE CAT: BACK FOR BLOOD", True, (243, 245, 156))
        menuText = pygame.transform.scale(menuText, (menuText.get_width() / 2, menuText.get_height() / 2))
        isRunning = True
        while isRunning:
            screen.fill(uiBackgroundColor)
            menuMousePos = pygame.mouse.get_pos()
            menuRect = menuText.get_rect(center=(screen.get_width()/2, 300))
            playButton = Button(image=(pygame.image.load('graphics/PLAYBUTTON.jpg')),
                                pos=(screen.get_width()/2, 350), text_input="PLAY",
                                font1=getFont(75), base_color=(50, 50, 50), hovering_color=(192, 152, 60))
            quitButton = Button(image=(pygame.image.load('graphics/PLAYBUTTON.jpg')),
                                pos=(screen.get_width() / 2, 600), text_input="QUIT",
                                font1=getFont(75), base_color=(50, 50, 50), hovering_color=(192, 152, 60))

            screen.blit(menuText, (screen.get_width()/2 - menuText.get_width()/2, 150))
            for button in [playButton, quitButton]:
                button.changeColor(menuMousePos)
                button.update(screen)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if playButton.checkForInput(menuMousePos):
                        self.level = 'levelSelector'
                        isRunning = False
                    if quitButton.checkForInput(menuMousePos):
                        pygame.quit()
                        exit()
            pygame.display.flip()
            clock.tick(60)

    def pause(self):
        menuText = font.render("GAME PAUSED", True, (243, 245, 156))
        menuText = pygame.transform.scale(menuText, (menuText.get_width() / 2, menuText.get_height() / 2))
        isRunning = True
        while isRunning:
            screen.fill(uiBackgroundColor)
            menuMousePos = pygame.mouse.get_pos()
            menuRect = menuText.get_rect(center=(screen.get_width()/2, 300))
            playButton = Button(image=(pygame.image.load('graphics/PLAYBUTTON.jpg')),
                                pos=(screen.get_width()/2, 350), text_input="BACK",
                                font1=getFont(75), base_color=(50, 50, 50), hovering_color=(192, 152, 60))
            quitButton = Button(image=(pygame.image.load('graphics/PLAYBUTTON.jpg')),
                                pos=(screen.get_width() / 2, 600), text_input="QUIT",
                                font1=getFont(75), base_color=(50, 50, 50), hovering_color=(192, 152, 60))

            screen.blit(menuText, (screen.get_width()/2 - menuText.get_width()/2, 150))
            for button in [playButton, quitButton]:
                button.changeColor(menuMousePos)
                button.update(screen)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if playButton.checkForInput(menuMousePos):
                        self.level = self.currentLevel
                        isRunning = False
                    if quitButton.checkForInput(menuMousePos):
                        pygame.quit()
                        exit()
            pygame.display.flip()
            clock.tick(60)

    def endLevelScreen(self):
        global score
        scoreText = str(score)
        self.resetGame()
        textEnd = font.render(f"YOU HAVE BEATEN THE LEVEL!", True, (243, 245, 156))
        scoreEnd = font.render(scoreText, True, (243, 245, 156))
        textEnd = pygame.transform.scale(textEnd, (textEnd.get_width() / 2, textEnd.get_height() / 2))
        scoreEnd = pygame.transform.scale(scoreEnd, (scoreEnd.get_width() / 2, scoreEnd.get_height() / 2))
        isRunning = True
        while isRunning:
            screen.fill(uiBackgroundColor)
            menuMousePos = pygame.mouse.get_pos()
            screen.blit(textEnd, (screen.get_width() / 2 - textEnd.get_width() / 2, 100))
            screen.blit(scoreEnd, (screen.get_width() / 2 - scoreEnd.get_width() / 2, 150))
            selectorButton = Button(image=playbuttonWide,
                                 pos=(screen.get_width() / 2, 300), text_input="Next",
                                 font1=getFont(75), base_color=(50, 50, 50), hovering_color=(192, 152, 60))
            quitButton = Button(image=playbuttonWide,
                                pos=(screen.get_width() / 2, 600), text_input="QUIT",
                                font1=getFont(75), base_color=(50, 50, 50), hovering_color=(192, 152, 60))
            for button in [selectorButton, quitButton]:
                button.changeColor(menuMousePos)
                button.update(screen)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if selectorButton.checkForInput(menuMousePos):
                        self.level = 'levelSelector'
                        isRunning = False
                    if quitButton.checkForInput(menuMousePos):
                        pygame.quit()
                        exit()
            pygame.display.flip()
            clock.tick(60)

    def failScreen(self):
        global score
        scoreText = str(score)
        self.resetGame()
        textEnd = font.render(f"YOU CRASHED THE CAT!", True, (243, 245, 156))
        scoreEnd = font.render(scoreText, True, (243, 245, 156))
        textEnd = pygame.transform.scale(textEnd, (textEnd.get_width() / 2, textEnd.get_height() / 2))
        scoreEnd = pygame.transform.scale(scoreEnd, (scoreEnd.get_width() / 2, scoreEnd.get_height() / 2))
        isRunning = True
        while isRunning:
            screen.fill(uiBackgroundColor)
            menuMousePos = pygame.mouse.get_pos()
            screen.blit(textEnd, (screen.get_width() / 2 - textEnd.get_width() / 2, 100))
            screen.blit(scoreEnd, (screen.get_width() / 2 - scoreEnd.get_width() / 2, 150))
            selectorButton = Button(image=playbuttonWide,
                                 pos=(screen.get_width() / 2, 300), text_input="LEVELS",
                                 font1=getFont(75), base_color=(50, 50, 50), hovering_color=(192, 152, 60))
            quitButton = Button(image=playbuttonWide,
                                pos=(screen.get_width() / 2, 600), text_input="QUIT",
                                font1=getFont(75), base_color=(50, 50, 50), hovering_color=(192, 152, 60))
            for button in [selectorButton, quitButton]:
                button.changeColor(menuMousePos)
                button.update(screen)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if selectorButton.checkForInput(menuMousePos):
                        self.level = 'levelSelector'
                        isRunning = False
                    if quitButton.checkForInput(menuMousePos):
                        pygame.quit()
                        exit()
            pygame.display.flip()
            clock.tick(60)


    def levelSelectorP1(self):
        menuText = font.render("LEVELS:", True, (243, 245, 156))
        menuText = pygame.transform.scale(menuText, (menuText.get_width() / 2, menuText.get_height() / 2))
        pageNum = 1
        isRunning = True
        while isRunning:
            screen.fill(uiBackgroundColor)
            menuMousePos = pygame.mouse.get_pos()
            menuRect = menuText.get_rect(center=(screen.get_width()/2, 300))
            pageButton = Button(image=playbuttonSmall,
                                 pos=(screen.get_width() / 2 + 300, screen.get_height() / 2 - 50), text_input=">",
                                 font1=getFont(75), base_color=(50, 50, 50), hovering_color=(192, 152, 60))
            if self.levelIntroDone == True:
                introButton = Button(image=playbuttonSmall,
                                    pos=(screen.get_width()/2 - 100, 250), text_input="00",
                                    font1=getFont(75), base_color=(50, 85, 50), hovering_color=(192, 152, 60))
            else:
                introButton = Button(image=playbuttonSmall,
                                     pos=(screen.get_width()/2 - 100, 250), text_input="00",
                                     font1=getFont(75), base_color=(50, 50, 50), hovering_color=(192, 152, 60))
            if self.level01Done:
                level01Button = Button(image=playbuttonSmall,
                                       pos=(screen.get_width() / 2 + 100, 250), text_input="01",
                                       font1=getFont(75), base_color=(50, 85, 50), hovering_color=(192, 152, 60))
            else:
                level01Button = Button(image=playbuttonSmall,
                                       pos=(screen.get_width() / 2 + 100, 250), text_input="01",
                                       font1=getFont(75), base_color=(50, 50, 50), hovering_color=(192, 152, 60))
            if self.level02Done:
                level02Button = Button(image=playbuttonSmall,
                                       pos=(screen.get_width() / 2 - 100, 450), text_input="02",
                                       font1=getFont(75), base_color=(50, 85, 50), hovering_color=(192, 152, 60))
            else:
                level02Button = Button(image=playbuttonSmall,
                                       pos=(screen.get_width() / 2 - 100, 450), text_input="02",
                                       font1=getFont(75), base_color=(50, 50, 50), hovering_color=(192, 152, 60))
            if self.level03Done:
                level03Button = Button(image=playbuttonSmall,
                                       pos=(screen.get_width() / 2 + 100, 450), text_input="03",
                                       font1=getFont(75), base_color=(50, 85, 50), hovering_color=(192, 152, 60))
            else:
                level03Button = Button(image=playbuttonSmall,
                                       pos=(screen.get_width() / 2 + 100, 450), text_input="03",
                                       font1=getFont(75), base_color=(50, 50, 50), hovering_color=(192, 152, 60))
            quitButton = Button(image=playbuttonWide,
                                pos=(screen.get_width() / 2, 650), text_input="QUIT",
                                font1=getFont(75), base_color=(50, 50, 50), hovering_color=(192, 152, 60))

            screen.blit(menuText, (screen.get_width()/2 - menuText.get_width()/2, 100))
            for button in [introButton, level01Button, level02Button, level03Button, pageButton, quitButton]:
                button.changeColor(menuMousePos)
                button.update(screen)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if introButton.checkForInput(menuMousePos):
                        self.level = 'intro'
                        isRunning = False
                    if level01Button.checkForInput(menuMousePos) and self.levelIntroDone:
                        self.level = 'level01'
                        isRunning = False
                    if level02Button.checkForInput(menuMousePos) and self.level01Done:
                        self.level = 'level02'
                        isRunning = False
                    if level03Button.checkForInput(menuMousePos) and self.level02Done:
                        self.level = 'level03'
                        isRunning = False
                    if pageButton.checkForInput(menuMousePos):
                        self.level = 'levelSelectorP2'
                        isRunning = False
                    if quitButton.checkForInput(menuMousePos):
                        pygame.quit()
                        exit()
            pygame.display.flip()
            clock.tick(60)

    def levelSelectorP2(self):
        menuText = font.render("LEVELS:", True, (243, 245, 156))
        menuText = pygame.transform.scale(menuText, (menuText.get_width() / 2, menuText.get_height() / 2))
        pageNum = 1
        isRunning = True
        while isRunning:
            screen.fill(uiBackgroundColor)
            menuMousePos = pygame.mouse.get_pos()
            menuRect = menuText.get_rect(center=(screen.get_width()/2, 300))
            pageButton = Button(image=playbuttonSmall,
                                pos=(screen.get_width() / 2 - 300, screen.get_height() / 2 - 50), text_input="<",
                                font1=getFont(75), base_color=(50, 50, 50), hovering_color=(192, 152, 60))
            if self.level04Done == True:
                level04Button = Button(image=playbuttonSmall,
                                    pos=(screen.get_width()/2 - 100, 250), text_input="04",
                                    font1=getFont(75), base_color=(50, 85, 50), hovering_color=(192, 152, 60))
            else:
                level04Button = Button(image=playbuttonSmall,
                                     pos=(screen.get_width() / 2 - 100, 250), text_input="04",
                                     font1=getFont(75), base_color=(50, 50, 50), hovering_color=(192, 152, 60))
            if self.level05Done:
                level05Button = Button(image=playbuttonSmall,
                                       pos=(screen.get_width() / 2 + 100, 250), text_input="05",
                                       font1=getFont(75), base_color=(50, 85, 50), hovering_color=(192, 152, 60))
            else:
                level05Button = Button(image=playbuttonSmall,
                                       pos=(screen.get_width() / 2 + 100, 250), text_input="05",
                                       font1=getFont(75), base_color=(50, 50, 50), hovering_color=(192, 152, 60))
            quitButton = Button(image=playbuttonWide,
                                pos=(screen.get_width() / 2, 650), text_input="QUIT",
                                font1=getFont(75), base_color=(50, 50, 50), hovering_color=(192, 152, 60))

            screen.blit(menuText, (screen.get_width()/2 - menuText.get_width()/2, 100))
            for button in [level04Button, level05Button, quitButton, pageButton]:
                button.changeColor(menuMousePos)
                button.update(screen)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if level04Button.checkForInput(menuMousePos) and self.level03Done:
                        self.level = 'level04'
                        isRunning = False
                    if level05Button.checkForInput(menuMousePos) and self.level04Done:
                        self.level = 'level05'
                        isRunning = False
                    if pageButton.checkForInput(menuMousePos):
                        self.level = 'levelSelector'
                        isRunning = False
                    if quitButton.checkForInput(menuMousePos):
                        pygame.quit()
                        exit()
            pygame.display.flip()
            clock.tick(60)

    def intro(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.introScene += 1
                if event.key == pygame.K_p and self.introScene > 1:
                    self.introScene -= 1
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
            self.levelIntroDone = True
            self.saveHandler()
            self.level = 'levelSelector'
        pygame.display.flip()
        clock.tick(60)

    def level01(self):
        self.currentLevel = 'level01'
        if theCat.isAlive == False:
            self.level = "failScreen"
        Background1.update()
        # handling user input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_f:
                    theCat.fireFlag = True
            if event.type == oneSec:
                self.secCounter += 1
                print(self.secCounter)
                if self.secCounter == 1:
                    powerupsGroup.add(powerup(600, 0, 1.5, "DMG"))
                if self.secCounter == 2:
                    partridgesNormal.add(PerdixNormal(random.randint(0, 1000), -100, 400, 1000, 2, 2))
                    partridgesNormal.add(PerdixNormal(random.randint(0, 1000), -100, 400, 1000, 2, 2))
                if self.secCounter == 10:
                    partridgesNormal.add(PerdixShooter(-100, 200, 2, 3))
                    partridgesNormal.add(PerdixShooter(1300, 100, 2, 3))
                    partridgesNormal.add(PerdixShooter(450, 200, 2, 3))
                    partridgesNormal.add(PerdixShooter(-600, 100, 2, 3))
                if self.secCounter == 12:
                    powerupsGroup.add(powerup(500, 20, 1.25, "HP"))
                if self.secCounter == 15:
                    partridgesNormal.add(PerdixNormal(0, -100, 650, 1000, 2, 2))
                    partridgesNormal.add(PerdixNormal(240, -100, 650, 1000, 2, 2))
                if self.secCounter == 17:
                    partridgesNormal.add(PerdixNormal(480, -100, 650, 1000, 2, 2))
                    partridgesNormal.add(PerdixNormal(720, -100, 650, 1000, 2, 2))
                    partridgesNormal.add(PerdixNormal(1200, -100, 650, 1000, 2, 2))
                if self.secCounter == 18:
                    powerupsGroup.add(powerup(500, 20, 1.10, "DMG"))
                if self.secCounter == 20:
                    bigboy = PerdixNormal(0, -100, 300, 100, 3, 2)
                    bigboy.hp = 2000
                    partridgesNormal.add(bigboy)
                if self.secCounter == 25:
                    powerupsGroup.add(powerup(-500, 20, 1.5, "HP"))
                if self.secCounter == 30:
                    for x in range(10):
                        partridgesNormal.add(PerdixNormal(random.randint(0, 1000), -100, 600, 500, 2, 1))
                if self.secCounter >= 60 or score == 30:
                    self.level01Done = True
                    self.saveHandler()
                    self.level = 'endLevelScreen'
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.level = 'pause'
                if event.key == pygame.K_t:
                    self.level = 'endLevelScreen'
        partridgesNormal.update()
        bullets.update()
        explosions.update()
        damages.update()
        powerupsGroup.update()
        self.scoreDisplay(score)
        theCat.updateSprite(screen)
        pygame.display.flip()
        clock.tick(60)

    def level02(self):
        self.currentLevel = 'level02'
        if theCat.isAlive == False:
            self.level = "failScreen"
        Background1.update()
        # handling user input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_f:
                    theCat.fireFlag = True
            if event.type == oneSec:
                self.secCounter += 1
                print(self.secCounter)
                if self.secCounter == 1:
                    for x in range(5):
                        partridgesNormal.add(PerdixNormal(0, -100, 300, 1000, 2, 2))
                if self.secCounter == 8:
                    for x in range(3):
                        partridgesNormal.add(PerdixNormal(random.randrange(0, 1200), random.randrange(100, 800) * -1,
                                                          random.randrange(0, 1200), 1000, 2, random.randrange(2, 3)))
                    powerupsGroup.add(powerup(500, 0, 1.5, "DMG"))
                if self.secCounter == 12:
                    bigboy = PerdixNormal(0, -100, 300, 1000, 3, 4)
                    bigboy.hp = 600
                    for x in range(2):
                        partridgesNormal.add(bigboy)
                    for x in range(4):
                        partridgesNormal.add(PerdixNormal(random.randrange(0, 1200), random.randrange(100, 800) * -1,
                                                          random.randrange(0, 1200), 1000, 2, random.randrange(2, 3)))
                if self.secCounter == 15:
                    partridgesNormal.add(PerdixShooter(-100, 200, 2, 3))
                    partridgesNormal.add(PerdixShooter(1200, 100, 2, 3))
                if self.secCounter == 18:
                    partridgesNormal.add(PerdixSniper(-100, 200, 2, 3, theCat.rect.x, theCat.rect.y))
                if self.secCounter == 20:
                    powerupsGroup.add(powerup(500, 20, 1.5, "DMG"))
                if self.secCounter == 21:
                    partridgesNormal.add(PerdixNormal(random.randrange(0, 1200), random.randrange(100, 800) * -1,
                                                      random.randrange(0, 1200), 1000, 2, random.randrange(2, 3)))
                if self.secCounter == 25:
                    powerupsGroup.add(powerup(-500, 20, 1.5, "HP"))
                if self.secCounter == 30:
                    partridgesNormal.add(PerdixShooter(-100, 200, 2, 3))
                    partridgesNormal.add(PerdixShooter(1200, 100, 2, 3))
                    partridgesNormal.add(PerdixShooter(-100, 200, 2, 3))
                    partridgesNormal.add(PerdixShooter(1200, 100, 2, 3))
                if self.secCounter == 40:
                    bigboy = PerdixNormal(0, 100, 300, 200, 3, 4)
                    bigboy.hp = 1500
                    partridgesNormal.add(bigboy)
                    bigboy2 = PerdixNormal(1200, 100, 300, -200, 3, 4)
                    bigboy2.hp = 1500
                    partridgesNormal.add(bigboy2)
                if self.secCounter >= 60 or score == 40:
                    self.level02Done = True
                    self.saveHandler()
                    self.level = 'endLevelScreen'
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.level = 'pause'
                if event.key == pygame.K_t:
                    self.level = 'endLevelScreen'
        partridgesNormal.update()
        bullets.update()
        explosions.update()
        damages.update()
        powerupsGroup.update()
        self.scoreDisplay(score)
        theCat.updateSprite(screen)
        pygame.display.flip()
        clock.tick(60)

    def level03(self):
        self.currentLevel = 'level03'
        if theCat.isAlive == False:
            self.level = "failScreen"
        Background1.update()
        # handling user input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_f:
                    theCat.fireFlag = True
            if event.type == oneSec:
                self.secCounter += 1
                print(self.secCounter)
                if self.secCounter == 1:
                    partridgesNormal.add(PerdixShooter(-100, 200, 2, 3))
                if self.secCounter >= 60 or score == 40:
                    self.level03Done = True
                    self.saveHandler()
                    self.level = 'endLevelScreen'
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.level = 'pause'
                if event.key == pygame.K_t:
                    self.level = 'endLevelScreen'
        partridgesNormal.update()
        bullets.update()
        explosions.update()
        damages.update()
        powerupsGroup.update()
        self.scoreDisplay(score)
        theCat.updateSprite(screen)
        pygame.display.flip()
        clock.tick(60)

    def level04(self):
        self.currentLevel = 'level04'
        if theCat.isAlive == False:
            self.level = "failScreen"
        Background1.update()
        # handling user input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_f:
                    theCat.fireFlag = True
            if event.type == oneSec:
                self.secCounter += 1
                print(self.secCounter)
                if self.secCounter == 1:
                    partridgesNormal.add(PerdixShooter(-100, 200, 2, 3))
                if self.secCounter >= 60 or score == 40:
                    self.level04Done = True
                    self.saveHandler()
                    self.level = 'endLevelScreen'
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.level = 'pause'
                if event.key == pygame.K_t:
                    self.level = 'endLevelScreen'
        partridgesNormal.update()
        bullets.update()
        explosions.update()
        damages.update()
        powerupsGroup.update()
        self.scoreDisplay(score)
        theCat.updateSprite(screen)
        pygame.display.flip()
        clock.tick(60)

    def resetGame(self):
        global score
        self.secCounter = 0
        score = 0
        partridgesNormal.empty()
        bullets.empty()
        theCat.reset()
        explosions.empty()
        powerupsGroup.empty()


# Sprite group initialisation
damages = pygame.sprite.Group()
bullets = pygame.sprite.Group()
partridgesNormal = pygame.sprite.Group()
explosions = pygame.sprite.Group()
theCat = CAT((screen.get_width()/2-32, 700))
powerupsGroup = pygame.sprite.Group()
game = Game()
Background1 = skyBlock('graphics/tlo.png', 0.5)
# Custom events
oneSec, t = pygame.USEREVENT+1, 1000
pygame.time.set_timer(oneSec, t)

# main loop
while True:
    game.stageManager()

