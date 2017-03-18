#  Dog class
class Dog:
	def speak(self):
		return "Gau gau!"
	# toString() function
	def __str__(self):
		return "Dog"

class DogFood:
	def __str__(self):
		return "Dog food"

# Cat class
class Cat:
	def speak(self):
		return "Meow meow!"
	# toString() function
	def __str__(self):
		return "Cat"

class CatFood:
	def __str__(self):
		return "Cat food"

# Concrete factory
class DogFactory:
	# Return a Dog object
	def get_pet(self):
		return Dog()

	# Return a Dog Food object
	def get_food(self):
		return DogFood()

class CatFactory:
	# Return a Dog object
	def get_pet(self):
		return Cat()

	# Return a Dog Food object
	def get_food(self):
		return CatFood()

# Abstract factory
class PetStore:
	def __init__(self, pet_factory=None):
		self._pet_factory = pet_factory

	def show_pet(self):
		pet = self._pet_factory.get_pet()
		pet_food = self._pet_factory.get_food()

		print("Our pet is '{}'!".format(pet))
		print("Out pet says hello by '{}'".format(pet.speak()))
		print("Its food is '{}'!".format(pet_food))

# Create a Concrete factory
dogFactory = DogFactory()
catFactory = CatFactory()

# Create Abstract factory
shopDog = PetStore(dogFactory)
shopCat = PetStore(catFactory)

# Invoke the method to show the detail of our pet
shopDog.show_pet()
shopCat.show_pet()