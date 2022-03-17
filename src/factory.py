# noinspection PyUnresolvedReferences
from animal import Dog, Cat


class AnimalFactory:
    @staticmethod
    def create(name):
        return eval(name)()
