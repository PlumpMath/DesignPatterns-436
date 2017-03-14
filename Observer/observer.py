class Subject(object):
	def __init__(self):
		self._observers = []

	# Append observer to the list
	def attach(self, observer):
		if observer not in self._observers:
			self._observers.append(observer)

	# Remove the observer
	def detach(self, observer):
		try:
			self._observers.remove(observer)
		except ValueError:
			pass

	# Notify the observer when update Core
	def notify(self, modifier=None):
		for observer in self._observers:
			if modifier != observer:
				observer.update(self)

# Inherits from the Subject class
class Core(Subject):
	def __init__(self, name=""):
		Subject.__init__(self)
		self._name = name
		self._status = "" # Initialize the status of Son Tung MTP fanpage
	
	# Getter
	@property 
	def status(self):
		return self._status

	# Setter
	@status.setter
	def status(self, status):
		self._status = status 
		self.notify()# Notify the observer when changes the status

# Fan of Son Tung MTP - Skyer
class Sky:
	def update(self, subject):
		print("Important Notice from {}: {}".format(subject._name, subject._status))


################
# Testing
################

# Create subject
fanpage = Core("Facebook fanpage")

# Create skyer
sky1 = Sky()
sky2 = Sky()

# Attach sky to the fanpage(This action like sky using their fb following Son Tung MTP fan page)
fanpage.attach(sky1)
fanpage.attach(sky2)

# Add new status in Son Tung MTP fanpage
fanpage.status = "Ngay mai Tung di ban chim tren nui Everest nha sky oiiiiiiiiiiiii"
fanpage.status = "Mv Lac Troi da duoc hon 100tr luot view"

# Detach sky(This action like sky unfollow fb fanpage)
fanpage.detach(sky1)

# When Son Tung MTP fb add new status only sky2 get noitice
fanpage.status = "Hom nay buon qua"
