from testdatagenerator.Utilities import luhn
from faker import Faker
from random import randint


class PersonalNumberGenerator:
    def __init__(self):
        self.faker = Faker()

    def pnr(self):
        date = self.faker.date_time()
        pnr = date.strftime("%y%m%d-")
        pnr += str(randint(0, 9)) + str(randint(0, 9)) + str(randint(0, 9))
        return pnr + str(luhn(pnr))

    def generator(self):
        return self.pnr()
