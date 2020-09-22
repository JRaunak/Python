import pygame
from random import randint
from math import *
from pygame.mixer import *

#Initialize Pygame
pygame.init()

#Defining displAlien_change_Y object and creating screen
screen=pygame.display.set_mode((800,600))

#Adding background
background=pygame.image.load('Dependencies/background.png')

#Title and icon
pygame.display.set_caption('Space Invaders')
icon=pygame.image.load('Dependencies/Icon.png')
pygame.display.set_icon(icon)

#Score
score_value=0
style=pygame.font.Font('freesansbold.ttf',32)
def ShowScore():
    score=style.render('Score: '+str(score_value),True,(255,255,255))
    screen.blit(score,(10,10))

#Safe Zone
def SafeZone():
    font2=pygame.font.Font('freesansbold.ttf',15)
    zone=font2.render('-'*160,True,(255,255,255))
    words=font2.render('Safe Zone',True,(255,255,255))
    screen.blit(words,(0,450))
    screen.blit(zone,(0,464))

#Game Over
def GameOver():
    Over_style=pygame.font.Font('freesansbold.ttf',64)
    Over=Over_style.render('GAME OVER',True,(255,255,255))
    screen.blit(Over,(200,250))


class Object:
    def __init__(self,image,X,Y,dX,dY):
        self.Image=pygame.image.load(image)
        self.X=X
        self.Y=Y
        self.dX=dX
        self.dY=dY

    def Draw(self):
        screen.blit(self.Image,(int(self.X),int(self.Y)))

class Bullets(Object):
    def __init__(self,Image,X,Y,dX,dY):
        Object.__init__(self,Image,X,Y,dX,dY)
        self.state='ready'

    def Fire(self):
        Object.Draw(self)
        self.state='fire'

    def Hit(self,AX,AY):
        distance=sqrt(pow(AX-self.X,2)+pow(AY-self.Y,2))
        if distance<30:
            return True
        else:
            return False

Player = Object('Dependencies/Ship.png',368.0,500.0,0,0)     #Object Instance as SpaceShip

Bullet = Bullets('Dependencies/bullet.png',0,500,0,4.0)      #Bullets Instance as a Bullet

#Data of AlienShip==========================================================================================================#    
AlienImgs=['Dependencies/Alien1.png','Dependencies/Alien2.png','Dependencies/Alien3.png']                                   #
Aliens=list()                                                                                                               #    
No_of_Aliens=10                                                                                                             #
for i in range(No_of_Aliens):                                                                                               #
    Aliens.append(Object(AlienImgs[randint(0,2)],randint(0,61)*12,randint(3,12)*8,1.5-(randint(0,1)*3.0),randint(30,40)))   #
#===========================================================================================================================#

#Sounds=====================================#
music.load('Dependencies/background.wav')   #
music.play(-1)#=============================#

running=True                                                    
while running:                                                  
    screen.blit(background,(0,0))                               
    SafeZone()                                                  
                                                      
    for event in pygame.event.get():                            
        #To close the Screen============#                       
        if event.type==pygame.QUIT:     #                       
            running=False               #                       
            pygame.quit()#==============#                       
                             
        #Ship Movement======================================#   
        if event.type==pygame.KEYDOWN:                         
            if event.key==pygame.K_LEFT: Player.dX=-1.2        
            elif event.key==pygame.K_RIGHT: Player.dX=1.2                                                       
            #Fire a Bullet==========================#         
            if event.key==pygame.K_SPACE:                     
                if Bullet.state=='ready':                     
                    Bullet_sound=Sound('Dependencies/laser.wav')
                    Bullet_sound.play()                       
                Bullet.X=Player.X+20                   
                Bullet.Fire()     

        if event.type==pygame.KEYUP:                           
            Player.dX=0                                        
    Player.X+=Player.dX                                        
    if Player.X<0: Player.X=0                               
    elif Player.X>736: Player.X=736
                                 
    if Bullet.Y<10:                                             
        Bullet.Y=500                                            
        Bullet.state='ready'                                    

    if Bullet.state=='fire':                                    
        Bullet.Fire()                                           
        Bullet.Y-=Bullet.dY                                     
                   
    #Alien Movement=====================================#       
    for i in range(No_of_Aliens):                       
        #                                                      
        Aliens[i].X+=Aliens[i].dX                              
        if Aliens[i].X<0:                                      
            Aliens[i].dX=1.5                                  
            Aliens[i].Y+=Aliens[i].dY                         
        elif Aliens[i].X>736:                                  
            Aliens[i].dX=-1.5                                  
            Aliens[i].Y+=Aliens[i].dY                          

        #When an Alien is hit by a Bullet===========#   
        if Bullet.Hit(Aliens[i].X,Aliens[i].Y):     #          
            Explode_sound=Sound('Dependencies/explosion.wav')   
            Explode_sound.play()                    #          
            Bullet.Y=500                            #          
            Bullet.state='ready'                    #         
            score_value+=1                          #          
            Aliens[i].X=randint(0,61)*12            #          
            Aliens[i].Y=randint(3,12)*8#============#          
  
        #Game Over==========================#            
        if Aliens[i].Y>400:                                   
            for j in range(No_of_Aliens):                     
                Aliens[j].Y=750                        
            GameOver()              
   
        Aliens[i].Draw() 
        
    Player.Draw()                                               
    
    #Printing the score=#                                       
    ShowScore()                                   
    pygame.display.update()
