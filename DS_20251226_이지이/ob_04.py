class Course:
    def __init__(self, name):
        self.name=name
        self.scores=[]

    def add_score(self, s):
        self.scores.append(s)
        return self.scores
    
    def avg(self):
        avg=sum(self.scores)/len(self.scores)
        return avg

    def info(self):
        return f"과목: {self.name}, 평균: {self.avg()}"

c=Course("파이썬")
c.add_score(80)
c.add_score(90)
print(c.info())