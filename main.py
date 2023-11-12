import pygame
import math
import random
# init
pygame.init()
screen = pygame.display.set_mode((1200, 800))
font = pygame.font.Font('font/FFFFORWA.TTF', 50)
clock = pygame.time.Clock()
pygame.display.set_caption("Don't Crash the cat: Back for Blood")
ctr = 0
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

def getFont(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("font/FFFFORWA.TTF", size)

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
        self.hpBarLen = 200
        self.hpRatio = self.maxHP / self.hpBarLen
        self.hpChangeSpeed = 5
        self.isAlive = True

    def getDamage(self, amount):
        if self.currentHP > 0:
            self.currentHP -= amount
        if self.currentHP < 0:
            self.currentHP = 0

    def getHealth(self, amount):
        if self.currentHP < self.maxHP:
            self.currentHP += amount
        if self.currentHP > self.maxHP:
            self.currentHP = self.maxHP

    def hpBar(self):
        pygame.draw.rect(screen, (255, 0, 0), (40, screen.get_height() - 65, self.currentHP / self.hpRatio, 25))
        pygame.draw.rect(screen, (255, 255, 255), (40, screen.get_height() - 65, self.hpBarLen, 25), 4)

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

    def draw(self, surf):
        self.rect = self.bullet.get_rect(center=self.pos)
        surf.blit(self.bullet, self.rect)

    def update(self):
        self.pos = (self.pos[0] + self.dir[0] * self.speed,
                    self.pos[1] + self.dir[1] * self.speed)
        self.rect.move_ip(0,5)
        self.draw(screen)
        if self.pos[0] > screen.get_width() or self.pos[0] < 0 or self.pos[1] > screen.get_height() or self.pos[1] < 0:
            print("aua")
            self.kill()


class PartridgeNormal(pygame.sprite.Sprite):
    def __init__(self, x, y, tx, ty, scale, speed):
        pygame.sprite.Sprite.__init__(self)
        self.pos = (x, y)
        self.target = (tx, ty)
        self.angle = self.getAngle(self.pos, self.target)
        self.image = pygame.image.load('graphics/placeholder_duck.png')
        self.image = pygame.transform.scale(self.image, (scale, scale))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        # self.x_speed = speed * random.random()
        # self.y_speed = speed
        self.speed = speed
        self.hp = 100
        self.image = pygame.transform.rotate(self.image, -1 * math.degrees(self.angle) - 90)
        self.image = pygame.transform.flip(self.image, 1, 0)
        self.damageVis = 0

    def checkColisions(self):
        hits = []
        hits = pygame.sprite.spritecollide(self, bullets, 1)
        for hit in hits:
            self.hp -= 25
            dmgP = damagePanel(self.rect.x, self.rect.y, 25, 20, (255, 0, 125))
            damages.add(dmgP)
            print('hit')

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
        self.checkColisions()
        if self.rect.y > screen.get_height():
            self.kill()
        # self.moveDown()
        self.goCrazyv2()
        if self.hp <= 0:
            explosion = Explosion2Firework(self.rect.centerx, self.rect.centery, 250)
            explosions.add(explosion)
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
            img = pygame.image.load(f"graphics/PixelSimulations/Explosion2/{num}.png")
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
        self.introScene = 1
        self.levelIntroDone = False
        self.level01Done = False

    def stageManager(self):
        if self.level == "menu":
            self.mainMenu()
        if self.level == 'intro':
            self.intro()
        if self.level == 'level01':
            self.level01()

    def mainMenu(self):
        menuText = font.render("DON'T CRASH THE CAT: BACK FOR BLOOD", True, (243, 245, 156))
        menuText = pygame.transform.scale(menuText, (menuText.get_width() / 2, menuText.get_height() / 2))
        isRunning = True
        while isRunning:
            screen.fill((75, 4, 94))
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
                        self.level = 'intro'
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
            self.level = 'level01'
            self.levelIntroDone = True
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
                partridgesNormal.add(PartridgeNormal(random.randrange(100, 1100), -100, random.randrange(100, 1100), 1000, 100, 5))
                partridgesNormal.add(PartridgeNormal(random.randrange(100, 1100), -100, random.randrange(100, 1100), 1000, 100, 5))
        theCat.updateSprite(screen)
        partridgesNormal.update()
        bullets.update()
        explosions.update()
        damages.update()
        pygame.display.flip()
        clock.tick(60)


# Sprite group initialisation
damages = pygame.sprite.Group()
bullets = pygame.sprite.Group()
partridgesNormal = pygame.sprite.Group()
explosions = pygame.sprite.Group()
theCat = CAT((screen.get_width()/2-32, 700))
game = Game()

# Custom events
createEnemyEvent, t = pygame.USEREVENT+1, 1000
pygame.time.set_timer(createEnemyEvent, t)

# main loop
while True:
    game.stageManager()

