# Dog class
class Dog:
	def __init__(self, name):
		self._name = name

	def speak(self):
		return "Gau gau!"

# Cat class
class Cat:
	def __init__(self, name):
		self._name = name

	def speak(self):
		return "Meow meow!"


# The factory method
def get_pet(pet="dog"):
	pets = dict(dog=Dog("Hope"), cat=Cat("Peace")) # "Hope" and "Peace" are default name we define

	return pets[pet]

# Test
d= get_pet("dog")
print d.speak()

c = get_pet("cat")
print c.speak()
