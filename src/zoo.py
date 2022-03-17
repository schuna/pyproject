from factory import AnimalFactory


class Zoo:
    def __init__(self):
        self.animals = []
        self.names = ["Dog", "Cat"]

    def create(self):
        for name in self.names:
            self.animals.append(AnimalFactory.create(name))

    def show_all(self):
        result = []
        for animal in self.animals:
            result.append(animal.speak())
        return "\n".join(result)


if __name__ == '__main__':
    zoo = Zoo()
    zoo.create()
    print(zoo.show_all())