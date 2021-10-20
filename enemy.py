import pygame, random
from random import randint

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        #Defino los sprites del carpincho
        self.sprites = []
        self.is_animating = False   #Setea que la animacion sea falso
        self.sprites.append(pygame.image.load("carpincho/izquierda/1.png"))
        self.sprites.append(pygame.image.load("carpincho/izquierda/2.png"))
        self.sprites.append(pygame.image.load("carpincho/izquierda/3.png"))
        self.sprites.append(pygame.image.load("carpincho/izquierda/4.png"))
        self.sprites.append(pygame.image.load("carpincho/izquierda/5.png"))
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]
        self.speed = randint(3,8)

        #Dibuja el enemigo, y hace el spawn
        self.rect = self.image.get_rect()
        self.rect.x = 800
        self.rect.y = random.randrange(0, (600 - 190))

    #Funcion que devuelve el tamaño de las imagenes
    def get_width(self):
        return self.image.get_width()

    def get_height(self):
        return self.image.get_height()

    def move(self):
        self.rect.x -= self.speed
        

    #Funcion que cambia cuando el carpincho se mueve o no
    def animate(self):
        self.is_animating = True
        self.move() #Llamo a la funcion para mover al enemigo

    #Funcion update que hace la animacion del carpincho moviendose
    def update(self, speed):
        if self.is_animating == True:
            self.current_sprite += speed
            
            if self.current_sprite >= len(self.sprites):
                self.current_sprite = 0
                self.is_animating = False

            self.image = self.sprites[int(self.current_sprite)]

        #Si el enemigo se va fuera de la pantalla
        if self.rect.left <= (0-(self.image.get_width())):
            self.rect.x = 800   #Cambiar a screen_width
            self.rect.y = random.randrange(0, (600- (self.image.get_width())))   #Cambiar a #screen_hight

        