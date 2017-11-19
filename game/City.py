class City(object):

    def __init__(self):
        self.__factories = []

    def addFactory(Factory f):
    	self.__factories.add(f)

    @property
    def factories(self):
        return self.__factories
