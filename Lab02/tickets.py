class Ticket:
    def __init__(self, number):
        self.price = 1000
        self.number = number
        self.name = 'Regular'

    def get_price(self):
        print(f'Price: {self.price}')

    def info(self):
        print(f"Type: {self.name} Ticket number: {self.number}. Price: {self.price}")


class Regular(Ticket):
    def __init__(self, number):
        super().__init__(number)


class Advance(Ticket):
    def __init__(self, number):
        super().__init__(number)
        self.price = self.price * 40 / 100
        self.name = 'Advance'


class Student(Ticket):
    def __init__(self, number):
        super().__init__(number)
        self.price = self.price * 50 / 100
        self.name = 'Student'


class Late(Ticket):
    def __init__(self, number):
        super().__init__(number)
        self.price = self.price + (self.price * 10 / 100)
        self.name = 'Late'


ticket1 = Advance(1)
ticket1.get_price()
ticket1.info()
ticket2 = Regular(2)
ticket2.info()
