from turtle import Turtle
ALIGHNMENT = 'center'
FONT = ('Courier',24,'normal')
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('white')
        self.hideturtle()
        self.penup()
        self.goto(0, 260)
        self.updated_score()
    def updated_score(self):
        self.write(f'score: {self.score}', align=ALIGHNMENT, font= FONT)
    def point(self):
        self.score += 1
        self.clear()
        self.updated_score()
    def game_over(self):
        self.clear()
        self.goto(0,0)
        self.updated_score()
        self.goto(0, 30)
        self.write('GAME OVER',align=ALIGHNMENT,font=FONT)

