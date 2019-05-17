from testdatagenerator import PersonNameGenerator
import re


class EmailGenerator:
    def __init__(self):
        self.p = PersonNameGenerator.PersonNameGenerator()

    def personal_email(self):

        name = self.p.full_name()

        name = name.replace(' ', '')
        name = name.replace('-', '')

        name = re.sub('[åäæá]', 'a', name)
        name = re.sub('[öø]', 'o', name)
        name = re.sub('[é]', 'e', name)
        name = re.sub('[ÿ]', 'y', name)
        name = re.sub('[ûü]', 'u', name)

        return name.lower() + '@example.com'

    def generator(self):
        return self.personal_email()
