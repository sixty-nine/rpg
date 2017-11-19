class Economy(object):
	def __init__(self):
		self.__resources = {}
		self.__resources['gold'] = 1000;
		self.__resources['wood'] = 100;
		self.__resources['iron'] = 100;
		self.__resources['food'] = 100;

	def hasEnough(self, resource, amount):
		if self.__resources.has_key(resource):
			if self.__resources[resource] >= amount:
				return True
		return False

	def produce(self, resource, amount):
		if self.__resources.has_key(resource):
			self.__resources[resource] += amount

	def consume(self, resource, amount):
		if not self.hasEnough(resource, amount):
			return False
		self.__resources[resource] -= amount;
		return True

	@property
	def resources(self):
		return self.__resources

class City(object):

    def __init__(self):
        self.__factories = []

    def addFactory(self, factory):
    	self.__factories.append(factory)

    @property
    def factories(self):
        return self.__factories

class Factory(object):

	def __init__(self, economy):
		self.__economy = economy

	@property
	def economy(self):
		return self.__economy

class Sawmill(Factory):
	 def produce(self):
		if (self.economy.hasEnough('wood', 10)):
			self.economy.consume('wood', 10)
			self.economy.produce('gold', 50)

