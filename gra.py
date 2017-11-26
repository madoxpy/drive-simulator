


from pygame import *
import numpy as np
from random import randint,random,choice

green=(0,255,0)
greengrass=(1,166,17)
black=(0,0,0)
white=(255,255,255)
bluesky=(135,206,235)
r=300
z=10
h=200

init()
window=display.set_mode((600,500))
clock = time.Clock()
Font=font.SysFont("arial",26)


class Line(object):
	def __init__(self,y):
		self.y=y
		self.d=15
	def draw(self):
		draw.line(window, white,(r,self.y),(r,1.03*self.y+self.d),1)
		self.y=self.y*1.03
		if self.y>500:
			self.y=h-10

class Tree(object):
	def __init__(self,y):
		self.y=y*1.5+h-20
		self.size=y/2
		self.sign=choice([-2,1])
		self.x=self.sign*150/z+r
		self.photo =image.load("tree0"+str(randint(1,3))+".png")
		self.vis=False

	def draw(self):
		if self.vis:
			photo=transform.scale(self.photo,(self.size,self.size))
			window.blit(photo,(self.x,self.y))
		self.y=self.y+1
		self.size=self.size+3
		self.x=self.x+self.sign*3
		if self.y>270:
			self.y=10*1.5+h-30
			self.sign=choice([-2,1])
			self.x=self.sign*150/z+r
			self.size=10
			self.photo =image.load("tree0"+str(randint(1,3))+".png")
			self.vis=True
			
			
class Cloud(object):
	def __init__(self,y):
		self.y=y*1.5+h-20
		self.size=y/2
		self.sign=choice([-2,1])
		self.x=self.sign*150/z+r
		self.photo =image.load("cloud0"+str(randint(1,3))+".png")
		self.vis=False

	def draw(self):
		if self.vis:
			photo=transform.scale(self.photo,(self.size,self.size))
			window.blit(photo,(self.x,self.y))
		self.y=self.y-1
		self.size=self.size+3
		self.x=self.x+self.sign*3
		if self.y<0:
			self.y=10*1.5+h-150
			self.sign=choice([-2,1])
			self.x=self.sign*150/z+r
			self.size=10
			self.photo =image.load("cloud0"+str(randint(1,3))+".png")
			self.vis=True

class Car(object):
	def __init__(self):
		self.x=300
		self.size=150
		self.photo =image.load("car.png")
		self.y=390
		self.rect=Rect(self.x-0.3*self.size,self.y+int(self.size*0.3),self.size*0.6,int(self.size*0.45))
		
	def draw(self):
		photo=transform.scale(self.photo,(self.size,int(self.size*0.75)))
		window.blit(photo,(self.x-0.5*self.size,self.y))
		#draw.rect(window,white,self.rect,1)
	def left(self):
		if self.x+(self.y-500)/2>100:
			self.x=self.x-4
			self.rect=Rect(self.x-0.3*self.size,self.y+int(self.size*0.3),self.size*0.6,int(self.size*0.45))
	def right(self):
		if self.x-(self.y-500)/2<500:
			self.x=self.x+4
			self.rect=Rect(self.x-0.3*self.size,self.y+int(self.size*0.3),self.size*0.6,int(self.size*0.45))
	def forward(self):
		if self.y>250:
			self.y=self.y-2
			self.size=self.size-1
		self.rect=Rect(self.x-0.3*self.size,self.y+int(self.size*0.3),self.size*0.6,int(self.size*0.45))
	def back(self):
		if self.y<500:
			self.y=self.y+2
			self.size=self.size+1
		self.rect=Rect(self.x-0.3*self.size,self.y+int(self.size*0.3),self.size*0.6,int(self.size*0.45))

class Police(object):
	def __init__(self):
		self.sign=choice([-1,1])
		self.x=300+self.sign*10
		self.size=20
		self.photo =image.load("police.png")
		self.y=h
		self.rect=Rect(self.x-0.4*self.size,self.y,self.size*0.8,int(self.size*0.75))
	def draw(self,points):
		photo=transform.scale(self.photo,(self.size,int(self.size*0.75)))
		window.blit(photo,(self.x-0.5*self.size,self.y))
		#draw.rect(window,white,self.rect,1)	
		
		
		self.y=self.y+2
		self.x=self.x+self.sign
		
		self.size=self.size+1


		if self.y>450:
			self.sign=choice([-1,1])
			self.x=300+self.sign*10
			self.size=20
			self.photo =image.load("police.png")
			self.y=h
			points=points+1
			
		self.rect=Rect(self.x-0.4*self.size,self.y,self.size*0.8,int(self.size*0.75))
		return points
		#self.x=self.x+self.sign*3
		
lines=[]
for i in range(8):
	lines.append(Line(i*35+h))
	
trees = []
for i in range(5):
	trees.append(Tree(i*10))


clouds = []
for i in range(5):
	clouds.append(Cloud(i*10))
	
grass =image.load("grass.jpg")
sky =image.load("sky.jpg")
grass=transform.scale(grass,(600,500))
sky=transform.scale(sky,(600,500))

player=Car()
enemy=Police()	
end = False 
points=0
while not end:
	for zet in event.get():
		if zet.type ==QUIT:
			end=True
			
	keys = key.get_pressed()
	if keys[K_LEFT] or keys[K_a]:
		player.left()
	if keys[K_RIGHT] or keys[K_d]:
		player.right()
	if keys[K_UP] or keys[K_w]:
		player.forward()
	if keys[K_DOWN] or keys[K_s]:
		player.back()
		
		
	#window.fill(greengrass)
	window.blit(grass,(0,0))

	draw.polygon(window, black, ((-200/z+r,0+h),(200/z+r,0+h),(200+r,500),(-200+r,500)),0)
	for line in lines:
		line.draw()
	

		
	#draw.rect(window, bluesky, Rect(0,0,600,h))
	window.blit(sky,(0,-500+h))
	for cloud in clouds:
		cloud.draw()

	for tree in trees:
		tree.draw()
	points=enemy.draw(points)
	player.draw()
	
	if player.rect.colliderect(enemy.rect):
		points=0
		enemy=Police()	

		
	text = Font.render(str(points),True,(255,255,255))
	window.blit(text,(20,20))
	
	clock.tick(20)
	display.flip()