class Person:
    """This is a person"""
    @property
    def name(self):
        print('inside getter')
        return self._name

    @name.setter
    def name(self, name):
        print('inside setter')
        self._name = name

    @name.deleter
    def name(self):
        print('inside deleter')
        del self._name


p = Person()
p.name = 'Apoorba'
print(p.name)
del p.name
