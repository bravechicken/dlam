#-*- coding: utf-8 -*-
import sys
import pygame

WIDTH=800
HEIGHT=500
R=255
G=255
B=255
x = 0
y = 0
IMAGE_NUM=18
STEP=100

def draw(screen,i):
	img = pygame.image.load("duo/"+str(i)+".png")
	global x,y
	if(y<=0): x=x+STEP
	if(x>=WIDTH-200): y=y+STEP
	if(y>=HEIGHT-200): x=x-STEP
	if(x<=0): y=y-STEP

	screen.blit(img,[x,y])
	pygame.display.flip()

def erase(screen):
	pygame.draw.rect(screen,[R,G,B],[0,0,WIDTH,HEIGHT],0) 

pygame.init()

screen = pygame.display.set_mode([WIDTH,HEIGHT])
screen.fill([R,G,B])
#pygame.draw.circle(screen, [255,0,0], [100,100],30,0)


#播放哆啦A梦mp3
pygame.mixer.init()
pygame.mixer.music.load("./duo/song.wav")
pygame.mixer.music.play()

count=1
while (count<IMAGE_NUM+1):
	erase(screen)
	draw(screen,count)
	pygame.time.delay(200)
	count=count+1
	if(count==IMAGE_NUM+1): count=1


while True:
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			sys.exit()