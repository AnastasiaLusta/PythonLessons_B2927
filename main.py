from random import *
class Student:
	def __init__(self, name):
		self.name = name
		self.gladness = 50
		self.progress = 0
		self.alive = True
	def say_hello(self):
		print('Hello!')
	def to_study(self):
		print('Time to study')
		self.progress += 5
		self.gladness -= 10
	def to_sleep(self):
		print('Sleep time')
		self.gladness += 5
	def to_chill(self):
		print('Chill time')
		self.gladness += 15
		self.progress -= 5
	def is_alive(self):
		if self.progress < -40:
			print('You are bad student')
			self.alive = False
		elif self.gladness < 15:
			print('Depression...')
			self.alive = False
		elif self.progress > 100:
			print('Amazing!')
			self.alive = False
	def statistics(self):
		print('Gladness = ', self.gladness, ' Progress = ', self.progress)
	def live(self, day):
		day = 'Day ' + str(day) + ' of ' + self.name + ' life'
		print(day)
		live_cube = randint(1,4)
		if live_cube == 1:
			self.to_study()
		elif live_cube == 2:
			self.to_sleep()
		elif live_cube == 3:
			self.to_chill()
		elif live_cube == 4:
			self.say_hello()
		self.statistics()
		self.is_alive()

human = Student('Anton')
for day in range(10):
	if human.alive == False:
		break
	human.live(day)

obj = Student('Harry')
for day in range(10):
	if obj.alive == False:
		break
	obj.live(day)