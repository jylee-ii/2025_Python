class Animal:
    def speak(self):
        print("동물이 소리를 냅니다.")

class Dog:
    def __init__(self):
        self.animal=Animal()

    def speak(self):
        self.animal.speak()
        print("멍멍!")

dog=Dog()
dog.speak()