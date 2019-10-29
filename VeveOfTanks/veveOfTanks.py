import pygame
from pygame.locals import *
import random
import math


# Initialise screen
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Veve Of Tanks')
icon = pygame.image.load('VeveOfTanks\iconTank.PNG')
pygame.display.set_icon(icon)

# Backgrownd
background = pygame.image.load("VeveOfTanks\desertTexture.jpg")

# Player
playerImg = pygame.image.load("VeveOfTanks\\tank.png")
playerX = 370
playerY = 480

# player move
playerX_change = 0
playerY_change = 0

# Enemy
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6

for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load("VeveOfTanks\\enemyTank.png"))
    enemyX.append(random.randint(0, 750))
    enemyY.append(random.randint(20, 110))
    enemyX_change.append(2)
    enemyY_change.append(40)

# bullet ready
bulletImg = pygame.image.load("VeveOfTanks\\bullet.png")
bulletX = 0
bulletY = playerY
bulletY_change = 5
bulletX_change = 0
bullet_state = "ready"

# Finish
theEnd = pygame.font.Font('freesansbold.ttf', 115)
theEndX = 350
theEndY = 400

# Scor
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)
textX = 10
textY = 10

def theEndFin(x,y):
    the_End = font.render("THE END", True, (255, 255, 255))
    screen.blit(the_End, (x, y))

def showScore(x,y):
    score = font.render("Score: " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))

def player(x,y):
    screen.blit(playerImg, (x, y))

def enemy(x,y,i):
    screen.blit(enemyImg[i], (x, y))

def fire_bullet(x,y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x+16,y+10))

# Colision
def isColision (enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt((math.pow(enemyX - bulletX, 2)) + (math.pow(enemyY - bulletY, 2))) 
    if distance <  27:
        return True
    else:
        return False

# Colision with player
def isColision2 (enemyX, enemyY, playerX, playerY):
    distance = math.sqrt((math.pow(enemyX - playerX, 2)) + (math.pow(enemyY - playerY, 2))) 
    if distance <  27:
        return True
    else:
        return False

# Game loop 
running = True
while running:
    screen.fill((0, 0, 0))
    # background image
    screen.blit(background, (0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # Move tank left and right
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -2
            if event.key == pygame.K_RIGHT:
                playerX_change = 2
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
        # Move tank up and down
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                playerY_change = -2
            if event.key == pygame.K_DOWN:
                playerY_change = 2
            if event.key == pygame.K_SPACE:
                if bullet_state is "ready":
                    # Get the current x cordinate of the tank
                    bulletX = playerX
                    bulletY = playerY
                    fire_bullet(bulletX, bulletY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                playerY_change = 0
            
    # Player move in loop
    playerX += playerX_change
    playerY += playerY_change    
     
    # Set boundry left/right
    if playerX  <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736 
    # Set boundry up/down
    if playerY  <= 0:
        playerY = 0
    elif playerY >= 536:
        playerY = 536

    # Enemy move in loop
    for i in range(num_of_enemies):  
        enemyX[i] += enemyX_change[i]
        # Set enemy boundry left/right
        if enemyX[i]  <= 0:
            enemyX_change[i] =+ 2
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 736:
            enemyX_change[i] =-2 
            enemyY[i] += enemyY_change[i] 
        # Collision
        collision = isColision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            bulletY = playerY
            bulletX = playerX
            bullet_state= "ready"
            score_value += 1
            enemyX[i] = random.randint(0, 750)
            enemyY[i] = random.randint(20, 110)

        # Collision
        collision2 = isColision2(enemyX[i], enemyY[i], playerX, playerY)
        if collision2:
            playerX = 370
            playerY = 480            
            num_of_enemies = 0
                    
        enemy(enemyX[i], enemyY[i], i)

    # Bullet Movement
    if bulletY <= 0:
        bulletY = playerY
        bullet_state = "ready"

    if bullet_state is "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change
    if num_of_enemies == 0:
        theEndFin(theEndX, theEndY)

    player(playerX, playerY)
    showScore(textX, textY)  
    pygame.display.update()