class Kettle(object):
    power_source = "electricity"

    def __init__(self, make, price):
        self.make = make
        self.price = price
        self.on = False

    def switch_on(self):
        self.on = True


kendwood = Kettle("Kenwood", 8.99)
print(kendwood.make)
print(kendwood.price)

kendwood.price = 12.75
print(kendwood.price)

hamilton = Kettle("Hamilton", 14.55)

print("Models: {} = {}, {} = {}".format(kendwood.make, kendwood.price, hamilton.make, hamilton.price))

print("Models: {0.make} = {0.price}, {1.make} = {1.price}".format(kendwood, hamilton))

print(hamilton.on)
hamilton.switch_on()
print(hamilton.on)

print()

Kettle.switch_on(kendwood)
print(kendwood.on)

print("*" * 150)

kendwood.power = 1.5
print(kendwood.power)

print(Kettle.power_source)
print(kendwood.power_source)
print(hamilton.power_source)

Kettle.power_source = "atomic"

print("*" * 150)

print(Kettle.power_source)
print(kendwood.power_source)
print(hamilton.power_source)

print("*" * 150)

kendwood.power_source = "gas"
print(Kettle.power_source)
print(kendwood.power_source)
print(hamilton.power_source)

print("*" * 150)

print(Kettle.__dict__)
print(kendwood.__dict__)
print(hamilton.__dict__)

print("*" * 150)


