import pygame
import time as tm
import numpy
from math import *
pygame.init()
pygame.display.set_caption('differential drive robot');
print("\n\nuse arrow keys to move and space to brake\n");
def rot_center(image, angle):
    orig_rect = image.get_rect()
    rot_image = pygame.transform.rotate(image, angle)
    rot_rect = orig_rect.copy()
    rot_rect.center = rot_image.get_rect().center
    rot_image = rot_image.subsurface(rot_rect).copy()
    return rot_image

screen=pygame.display.set_mode((600,600));
screen.fill([255,255,255]);
exit=False
#pygame.draw.line(screen,(255,0,0),(150,200),(150,400),5);
x=150;
y=400;
c1=0;
time=0.1;
speed1=0;
speed2=0;
radius=40/pi;
length=60;
theta=-pi/2;


while not exit:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit=True;
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_UP:
                speed1=speed1+2;
                speed2=speed2+2;
            if event.key==pygame.K_DOWN:
                speed1=speed1-2;
                speed2=speed2-2;
            if event.key==pygame.K_LEFT:
                if(speed1>0):
                    speed2=speed2+5;
                elif(speed1<0):
                    speed2=speed2-5;
            if event.key==pygame.K_RIGHT:
                if(speed2>0):
                    speed1=speed1+5;
                elif(speed2<0):
                    speed1=speed1-5;
            if event.key==pygame.K_SPACE:
                speed1=0;
                speed2=0;
        if event.type==pygame.KEYUP:
            if event.key==pygame.K_UP:
                speed1=speed1+2;
                speed2=speed2+2;
            if event.key==pygame.K_DOWN:
                speed1=speed1-2;
                speed2=speed2-2;
            if event.key==pygame.K_LEFT:
                speed2=speed1;
            if event.key==pygame.K_RIGHT:
                speed1=speed2;
            if event.key==pygame.K_SPACE:
                speed1=0;
                speed2=0;
                
    m1=[[cos(theta),-sin(theta),0],[sin(theta),cos(theta),0],[0,0,1]];
    m2=[radius/2*(speed1+speed2),0,radius/(2*length)*(speed1-speed2)];
    rr=numpy.dot(m1,m2);
    xp=x;
    yp=y;
    tp=theta;
    x=rr[0]*time+x;
    y=rr[1]*time+y;
    theta=rr[2]*time+theta;
    if(theta<=2*pi):
        theta=theta+2*pi;
    if(theta>2*pi):
        theta=theta-2*pi;
    
    if(y+50>=600 or y-50<=0 or x+50>=600 or x-50<=0):
        speed1=0;
        speed2=0;
        x=xp;
        y=yp;
        theta=tp;
    
        
    car=pygame.image.load('robot.jpg');
    car=rot_center(car,-degrees(theta));
    screen.fill([255,255,255]);
    screen.blit(car,(x-50,y-50));
    pygame.display.update();
    tm.sleep(time);
    
pygame.quit();
quit();
    
