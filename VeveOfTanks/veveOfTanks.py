import pygame
from pygame.locals import *


# Initialise screen
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Veve Of Tanks')
icon = pygame.image.load('VeveOfTanks\iconTank.PNG')
pygame.display.set_icon(icon)

# PlayerImage
playerImg = pygame.image.load("VeveOfTanks\\tank.png")
playerX = 370
playerY = 480
# player move
playerX_change = 0
playerY_change = 0

def player(x,y):
    screen.blit(playerImg, (x, y))

# Game loop 
running = True
while running:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # Move tank left and right
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -0.3
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.3
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
        # Move tank up and down
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                playerY_change = -0.3
            if event.key == pygame.K_DOWN:
                playerY_change = 0.3
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                playerY_change = 0
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
    # Player move in loop
    playerX += playerX_change
    playerY += playerY_change
    player(playerX, playerY)
    pygame.display.update()