class Car:
    def __init__(self, model, odometer=0):
        self.model=model
        self.odometer=0

    def drive(self, km):
        self.odometer+=km
        return self.odometer

    def info(self):
        return f"모델: {self.model}, 주행거리: {self.odometer}km"

c=Car("BMW")
c.drive(50)
c.drive(70)
print(c.info())
