num1 = num2 = sign = ''
while num1 == '' or num2 == '' or sign == '':
	try:
		num1 = int(input('Number1: '))
		sign = input('Sign: ')
		num2 = int(input('Number2: '))
		if num2 == 0 and sign == '/':
			raise ZeroDivisionError
	except ValueError:
		print('Wrong value')
	except ZeroDivisionError:
		sign = ''
		print("You can't divide by zero")
	except:
		print('Something is wrong!')
	if sign == '+':
		print(f"{num1} + {num2} = {num1+num2}")

# Добавить оcтальные операции. Если должны произойти какие-то еще исключительные операции, то обработать их в try-except.
# Сделать проверку на введенный знак. Доступны только арифметические!
# Попросить пользователя ввести имя. Если он вводит числа, то обрабатываем данную исключительную ситуацию и пишем ему, что в имени цифр не может быть
	


# try:
# 	a = input()
# 	if a == 'stop':
# 		raise SyntaxError
# 	print(5/0)

# except SyntaxError:
# 	print('You said forbidden word')
# except ZeroDivisionError:
# 	print("You can't divide by zero")
# except:
# 	print("Error")
	
# print('Hello world!')



# class Human:
# 	def __init__(self, name):
# 		self.name = name
# 		self.appearance = 5
# 		self.status = False
# 	def live(self):
# 		print(self.name, 'is alive')
# 	def eat(self):
# 		print('Eating time')

# class Woman(Human):
# 	def live(self):
# 		super().live()
# 		print('What a wonderful day of', self.name)
# 	def cook(self):
# 		print(self.name, 'is cooking')
		
# class Man(Human):
# 	def __init__(self, name):
# 		super().__init__(name)
# 		self.money = 50
# 	def work(self):
# 		self.money += 10
# 		print(self.name, 'is working')
# 		print('Money: ', self.money)

# human = Human('Bob')
# human.live()
# w1 = Woman('Clara')
# w1.live()
# w1.cook()
# m1 = Man('John')
# m1.live()
# m1.work()

# Создать класс Животное. От него наследуются классы Котик, Собачка и Хомячок. В классе есть 3 поля (характеристики) и 2 поведения (методы). В классах конкретных животных добавить по 1 дополнительному поведения

# from random import *

# class University:
# 	def __init__(self, title, faculty):
# 		self.title = title
# 		self.faculty = faculty
# 		self.budget = False
# 	def studying(self, name):
# 		print(name, 'is studying')
# 	def isbudget(self):
# 		if self.budget == True:
# 			print('Congrats! You are on budget')
# 		else:
# 			print('Pay money and study!')

# class Student:
# 	def __init__(self, name):
# 		self.name = name
# 		self.gladness = 50
# 		self.progress = 0
# 		self.alive = True
# 	def ask_budget(self):
# 		if self.progress >= 20:
# 			univer.budget = True
# 	def say_hello(self):
# 		print('Hello!')
# 	def to_study(self):
# 		print('Time to study')
# 		self.progress += 15
# 		self.gladness -= 10
# 	def to_sleep(self):
# 		print('Sleep time')
# 		self.gladness += 5
# 	def to_chill(self):
# 		print('Chill time')
# 		self.gladness += 15
# 		self.progress -= 5
# 	def is_alive(self):
# 		if self.progress < -40:
# 			print('You are bad student')
# 			self.alive = False
# 		elif self.gladness < 15:
# 			print('Depression...')
# 			self.alive = False
# 		elif self.progress > 100:
# 			print('Amazing!')
# 			self.alive = False
# 	def statistics(self):
# 		print('Gladness = ', self.gladness, ' Progress = ', self.progress)
# 		print('Budget = ', univer.budget)
# 	def live(self, day):
# 		day = 'Day ' + str(day) + ' of ' + self.name + ' life'
# 		print(day)
# 		live_cube = randint(1,4)
# 		if live_cube == 1:
# 			self.ask_budget()
# 			self.to_study()
# 			univer.studying(self.name)
# 		elif live_cube == 2:
# 			self.to_sleep()
# 		elif live_cube == 3:
# 			self.to_chill()
# 		elif live_cube == 4:
# 				self.say_hello()
# 		self.statistics()
# 		self.is_alive()

# univer = University('Step', 'Computer Science')
# human = Student('Anton')
# for day in range(10):
# 	if human.alive == False:
# 		break
# 	human.live(day)

