class Temperature:
    def __init__(self, celsius):
        self.celsius=celsius

    def to_fahrenheit(self):
        fahrenheit=self.celsius*1.8+32
        return fahrenheit

t=Temperature(25)
print("섭씨:",t.celsius)
print("화씨:",t.to_fahrenheit())
