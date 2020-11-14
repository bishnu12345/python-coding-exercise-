class Person:
    # this is docstring
    '''This is person'''
    def setName(self, name):
        print('inside set')
        self._name = name

    def getName(self):
        print('inside get')
        return self._name

    def delName(self):
        print('inside delete')
        del self._name

    name = property(getName, setName, delName, 'Person Class')


p = Person()
p.name = 'Apoorba'
print(p.name)
print(p.__doc__)