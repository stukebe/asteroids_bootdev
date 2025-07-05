from circleshape import *
from constants import *
import random

class Asteroid(CircleShape):
	def __init__(self, x, y , radius):
		super().__init__(x, y, radius)

	def draw(self, screen):
		pygame.draw.circle(screen, (255,255,255), self.position, self.radius, width=2)

	def update(self, dt):
		self.position += (self.velocity * dt)

	def split(self):
		self.kill()
		if self.radius <= ASTEROID_MIN_RADIUS:
			return
		else:
			random_angle = random.uniform(20,50)
			ast_1_velocity = self.velocity.rotate(random_angle)
			ast_2_velocity = self.velocity.rotate(-random_angle)
			new_radius = self.radius - ASTEROID_MIN_RADIUS
			asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius)
			asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius)
			asteroid_1.velocity = ast_1_velocity * 1.2
			asteroid_2.velocity = ast_2_velocity * 1.2