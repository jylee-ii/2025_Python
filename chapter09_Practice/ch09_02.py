class Dog:
    def __init__(self,name,age,tricks):
        self.name = name
        self.age = age
        self.tricks = tricks

    def bark(self):
        print(f"{self.name}가 짖고있습니다.")

    def info(self):
        print(f"이름:{self.name}, 나이:{self.age}")

    def show_tricks(self):
        tricks=','.join(self.tricks)
        print(f"{self.name}의 장기는 {tricks}입니다.")

    
dog1=Dog("바둑이",3,["뒹굴기","달리기"])
dog2=Dog("멍멍이",5,["먹기"])



dog1.show_tricks()
dog2.show_tricks()



