from abc import abstractmethod


class Animal:
    @abstractmethod
    def speak(self):
        raise NotImplementedError


class Dog(Animal):
    def speak(self):
        return "Bowwow~"


class Cat(Animal):
    def speak(self):
        return "Meow~"
