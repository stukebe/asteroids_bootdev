# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import sys
from constants import *
from player import *
from circleshape import *
from asteroid import *
from asteroidfield import *
from shot import *

def main():
	pygame.init()
	clock = pygame.time.Clock()
	dt = 0
	print("Starting Asteroids!")
	print(f"Screen width: {SCREEN_WIDTH}")
	print(f"Screen height: {SCREEN_HEIGHT}")
	
	#create groups
	updatables = pygame.sprite.Group()
	drawables = pygame.sprite.Group()
	Player.containers = (updatables, drawables)
	asteroids = pygame.sprite.Group()
	Asteroid.containers = (asteroids, updatables, drawables)
	AsteroidField.containers = (updatables)
	shots = pygame.sprite.Group()
	Shot.containers = (shots, updatables, drawables)

	screen = pygame.display.set_mode((SCREEN_WIDTH+100, SCREEN_HEIGHT))
	player = Player((SCREEN_WIDTH/2), (SCREEN_HEIGHT/2))
	asteroidfield = AsteroidField()


	#game loop starts
	while True:
		for event in pygame.event.get():
    			if event.type == pygame.QUIT:
        			return
		screen.fill(000000)
		pygame.draw.line(screen, (255,255,255), (SCREEN_WIDTH, 0), (SCREEN_WIDTH, SCREEN_HEIGHT))
		updatables.update(dt)

		#collision check on asteroids
		for asteroid in asteroids:
			if player.collision(asteroid):
				print("Game over!")
				pygame.quit()
				sys.exit()
			for shot in shots:
				if asteroid.collision(shot):
					asteroid.split()
					shot.kill()
		for drawable in drawables:
			drawable.draw(screen)

		pygame.draw.rect(screen, (0,0,0), pygame.Rect(SCREEN_WIDTH+1, 0, 100, SCREEN_HEIGHT))
		pygame.display.flip()
		clock.tick(60)
		dt = clock.tick(60) / 1000

if __name__ == "__main__":
	main()