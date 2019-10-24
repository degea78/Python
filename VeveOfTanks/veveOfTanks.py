import pygame
from pygame.locals import *
import random


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
enemyImg = pygame.image.load("VeveOfTanks\\enemyTank.png")
enemyX = random.randint(0, 800)
enemyY = random.randint(50, 160)

# enemy move
enemyX_change = 2
enemyY_change = 30

def player(x,y):
    screen.blit(playerImg, (x, y))

def enemy(x,y):
    screen.blit(enemyImg, (x, y))

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
    enemyX += enemyX_change    

    # Set enemy boundry left/right
    if enemyX  <= 0:
        enemyX_change =+ 2
        enemyY += enemyY_change
    elif enemyX >= 736:
        enemyX_change =-2 
        enemyY += enemyY_change    

    player(playerX, playerY)
    enemy(enemyX, enemyY)
    pygame.display.update()