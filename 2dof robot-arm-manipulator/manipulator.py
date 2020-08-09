import pygame
import numpy
from math import *

print('2dof revolute joint planar manipulator');
l1=float(input('enter link 1 length(max 125): '));
l2=float(input('enter link 2 length(max 125): '));
t1=radians(float(input('enter theta 1 in degree: ')));
t2=radians(float(input('enter theta 2 in degree: ')));

print('\n   DH TABLE  \n');
print('   |{:^10}|{:^10}|{:^10}|{:^10}|'.format('theta','d','a','alpha'));
print('{:^40}'.format('__________________________________________________'));
print(' 1 |{:^10.6}|{:^10}|{:^10}|{:^10}|'.format(t1,0,l1,0));
print(' 2 |{:^10.6}|{:^10}|{:^10}|{:^10}|'.format(t2,0,l2,0));

a1=[[cos(t1),-sin(t1),0,l1*cos(t1)],[sin(t1),cos(t1),0,l1*sin(t1)],[0,0,1,0],[0,0,0,1]];
a2=[[cos(t2),-sin(t2),0,l2*cos(t2)],[sin(t2),cos(t2),0,l2*sin(t2)],[0,0,1,0],[0,0,0,1]];
a=numpy.dot(a1,a2);
x1=a1[0][3];
y1=a1[1][3];
z1=0;
x=a[0][3];
y=a[1][3];
z=0.0;
print('\ntransformation matrix A1\n');
for i in a1:
    print('{:^13.7} {:^13.7} {:^13.7} {:^13.7}'.format(float(i[0]),float(i[1]),float(i[2]),float(i[3])));

print('\ntransformation matrix A2\n');
for i in a2:
    print('{:^13.7} {:^13.7} {:^13.7} {:^13.7}'.format(float(i[0]),float(i[1]),float(i[2]),float(i[3])));

print('\ntransformation matrix A=A1*A2\n');
for i in a:
    print('{:^13.7} {:^13.7} {:^13.7} {:^13.7}'.format(float(i[0]),float(i[1]),float(i[2]),float(i[3])));

print('\n\nposition of tooltip :');
print('x : ',x,' y : ',y,' z : ',z);
pygame.init();
pygame.display.set_caption('2dof manipulator');
pygame.font.init();
f1=pygame.font.SysFont('Comic Sans MS',20);
f2=pygame.font.SysFont('Arial',15);
screen=pygame.display.set_mode((600,600));
screen.fill([202,207,201]);

pygame.draw.line(screen,(0,0,0),(300,50),(300,550),5);
pygame.draw.line(screen,(0,0,0),(50,300),(550,300),5);
pygame.draw.line(screen,(80,139,211),(300,300),(x1+300,300-y1),10);
pygame.draw.line(screen,(89,208,83),(x+300,300-y),(x1+300,300-y1),10);
pygame.draw.ellipse(screen,(255,0,0),[x+300-10,300-y-10,20,20],10);
pygame.draw.ellipse(screen,(255,0,0),[300-10,300-10,20,20],10);
pygame.draw.ellipse(screen,(255,0,0),[x1+300-10,300-y1-10,20,20],10);

color_pt=(250,124,41);
pygame.draw.circle(screen,color_pt,(300,100),5,5);
pygame.draw.circle(screen,color_pt,(300,200),5,5);
pygame.draw.circle(screen,color_pt,(300,400),5,5);
pygame.draw.circle(screen,color_pt,(300,500),5,5);
pygame.draw.circle(screen,color_pt,(100,300),5,5);
pygame.draw.circle(screen,color_pt,(200,300),5,5);
pygame.draw.circle(screen,color_pt,(400,300),5,5);
pygame.draw.circle(screen,color_pt,(500,300),5,5);

tt=f1.render('X,Y : 1 unit:100',False,(0,0,0));
screen.blit(tt,(250,15));
t=' ( {:.5} , {:.5} )'.format(str(x),str(y));
pos=f2.render(t,False,(0,0,0));
screen.blit(pos,(x+300-20,300-y-30));

exit=False
while not exit:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit=True;
        pygame.display.update();

pygame.quit();
quit();
