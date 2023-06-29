import pygame,sys
import pygame.freetype
from math import pi
pygame.init()
icon=pygame.image.load('PYG03-flower.png')
pygame.display.set_icon(icon)
size=width,height=900,600
screen=pygame.display.set_mode(size,pygame.RESIZABLE)
pygame.display.set_caption("碰撞球")
ball=pygame.image.load('PYG02-ball.gif')
bgcolor=pygame.Color("black")
GOLD=255,251,0
RED=pygame.Color('red')
WHITE=255,255,255
GREEN=pygame.Color("green")


# r1rect=pygame.draw.rect(screen,GOLD,(100,100,200,100),5)
# r2rect=pygame.draw.rect(screen,RED,(210,210,200,100),0)
e1ellipse=pygame.draw.ellipse(screen,GREEN,(50,50,500,300),3)
c1circle=pygame.draw.circle(screen,GOLD,(200,180),30)
c2circle=pygame.draw.circle(screen,GOLD,(400,180),30)
r1rect=pygame.draw.rect(screen,RED,(170,130,60,10),3)
r2rect=pygame.draw.rect(screen,RED,(370,130,60,10))
plist=[(295,170),(285,250),(260,280),(340,280),(315,250),(305,170)]
l1rect=pygame.draw.lines(screen,GOLD,True,plist,2)
a1rect=pygame.draw.arc(screen,RED,(200,220,200,100),1.4*pi,1.9*pi,3)

f1=pygame.freetype.Font("C:\Windows\Fonts\STKAITI.TTF")
f1rect=f1.render_to(screen,(200,80),"世界核平",fgcolor=GREEN,size=50)

f2surf,f2rect=f1.render("世界和平",fgcolor=GOLD,size=50)


# r1polygon=pygame.draw.rect(screen,RED,(210,210,200,100),0)



while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
    screen.blit(f2surf,(200,160))
    pygame.display.update()
