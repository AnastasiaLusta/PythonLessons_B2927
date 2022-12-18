class Flower:
	def __init__(self):
		self.color = 'None'
		self.name = 'None'
		self.height = 0
	def sun(self):
		print('I like sun')
	def water(self):
		print('I want water')

class Rose(Flower):
	def __init__(self):
		super().__init__()
		self.spikes = True
	def sun(self):
		super().sun()
		print('I want sun')
	def gift(self):
		print('I am gift')

obj = Flower()
obj.sun()
obj.water()

rose = Rose()
rose.sun()
rose.water()
rose.gift()
# class Book:
# 	def __init__(self):
# 		self.pages = 0
# 		self.title = 'None'
# 		self.author = 'None'
# 	def read(self):
# 		print(f'Book {self.title} is being read')
# 	def add_info(self):
# 		try:
# 			self.title = input('Input title: ')
# 			self.author = input('Input author: ')
# 			self.pages = int(input('Input pages: '))
# 			if self.author.isalpha() == False:
# 				raise NameError
# 			if self.pages <= 0:
# 				raise ValueError
# 		except NameError:
# 			print('Wrong names')
# 		except ValueError:
# 			print('Not correct pages')
# 		except:
# 			print('Error')

# obj1 = Book()
# obj1.read()
# obj1.add_info()
# obj1.read()