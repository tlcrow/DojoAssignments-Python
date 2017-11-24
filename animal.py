class Animal(object):
    def __init__ (self, name):
        self.name = name
        self.health = 100
    
    def walk(self):
        self.health = self.health - 1
        return self

    def run(self):
        self.health = self.health - 5
        return self

    def healthInfo(self):
        print self.health

cat = Animal("cat")
cat.walk().walk().walk().run().run().healthInfo()

class Dog(Animal):
    def __init__(self,name):
        super(Dog, self).__init__(name)
        self.health = 150

    def pet(self):
        self.health += 5
        return self

twizzler = Dog("dog")
twizzler.walk().walk().walk().run().run().pet().healthInfo()

class Dragon(Animal):
    def __init__(self,name):
        super(Dragon, self).__init__(name)
        self.health = 170

    def fly(self):
        self.health -= 10
        return self

    def healthInfo(self):
        super(Dragon, self).healthInfo()
        print "I am a dragon"

pete = Dragon("Pete")
pete.healthInfo()

class Bear(Animal):
    def __init__(self,name):
        super(Bear, self).__init__(name)
        self.health = 210

picnic = Bear("Picnic")
picnic.walk().healthInfo()