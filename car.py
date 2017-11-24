class Car(object):
    def __init__ (self, price, speed, fuel, mileage, tax):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        self.tax = tax
    def display_all(self):
        print self.price
        print self.speed
        print self.fuel
        print self.mileage
        print self.tax

blue = Car(15000, '85mph', 'Half-full', 50582, 0.15)
red = Car(5000, '25mph', 'Full', 110000, 0.10)
yellow = Car(2000, '90mph', 'Empty', 195000, 0.10)
green = Car(37500, '95mph', 'Half-full', 45000, 0.15)
purple = Car(150000, '210mph', 'Empty', 1000, 0.15)
black = Car(25000, '100mph', 'Full', 65000, 0.15)

# blue.display_all()
# red.display_all()
# yellow.display_all()
# green.display_all()
# purple.display_all()
# black.display_all()
