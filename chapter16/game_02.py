from tkinter import *
import random
import time

# Tkinter
tk=Tk()
tk.title("Game")
tk.resizable(0,0)
tk.wm_attributes("-topmost",1) #게임창이 항상 위로 있도록

canvas=Canvas(tk, width=500, height=400, bd=0, highlightthickness=0)
canvas.pack()
tk.update()

# 게임 클래스 추가 -> "GAME OVER", 재시작 버튼 생성, paddle / ball 객체 관리
class Game:
    def __init__(self):
        # 게임 오버 텍스트, 재시작 버튼 저장할 변수 생성 (None으로 초기화)
        self.game_over_text=None
        self.restart_button=None
        self.score=0 
        self.score_text=canvas.create_text(50, 20, text="점수: 0", fill="black")
        self.paddle=Paddle(canvas, 'blue')
        self.ball=Ball(canvas, self.paddle, 'red', self)

    # 점수 추가 함수
    def update_score(self):
        self.score+=1
        canvas.itemconfig(self.score_text, text=f"점수: {self.score}")


    def game_over(self):
        # 공이 바닥에 닿을 경우 "GAME OVER" 문구, 버튼 1번만 생성되도록 하기
        if not self.game_over_text:
            self.game_over_text=canvas.create_text(250, 200, text="GAME OVER", fill="red")
            # Tkinter-버튼 생성하여 재시작 함수(restart 함수)와 연결
            self.restart_button=Button(tk, text="재시작", command=self.restart)
            self.restart_button.pack()
        
    def restart(self):
        # 재시작 시 기존 내용 모두 지우기
        canvas.delete("all")

        # score 객체 추가
        self.score=0
        self.score_text=canvas.create_text(50, 20, text='점수: 0', fill="black")

        # 새로운 Paddle, Ball 객체 만들기 -> 게임 상태 초기화
        self.paddle=Paddle(canvas, 'blue')
        self.ball=Ball(canvas, self.paddle, 'red', self)

        # restart_button 있으면 위젯 제거
        if self.restart_button:
            self.restart_button.destroy()
            self.restart_button=None
        
        # 게임오버 텍스트(game_over_text) ID 초기화
        self.game_over_text=None

        
class Ball:
    def __init__(self, canvas, paddle, color, game):
        self.canvas=canvas
        self.game=game
        self.id=canvas.create_oval(10, 10, 25, 25, fill=color) #도형 ID
        self.paddle=paddle #패들 객체 기억하도록 수정
        self.canvas.move(self.id, 245, 100) #canvas.move(객체ID, X방향이동, Y방향이동)
    
        # # 공의 속도, 좌우로 움직이던 것을 *수정
        starts=[-3, -2, -1, 1, 2, 3]
        random.shuffle(starts) #리스트 순서를 섞기
        self.x=starts[0]

        self.y=-3

        # # 공의 속도(방향)
        # self.x=0    #좌우 속도 (0은 좌우로 안움직임)
        # self.y=-1   #위쪽(-1)으로 이동


        # 캔버스 높이 저장
        self.canvas_height=self.canvas.winfo_height()
        self.canvas_width=self.canvas.winfo_width() #수정
    
        self.hit_bottom=False

    # 추가: 공이 패들에 부딪혔는지 검사하는 함수
    def hit_paddle(self, pos):
        paddle_pos = self.canvas.coords(self.paddle.id) #패들의 위치 [px1, py1, px2, py2]

        # 가로 방향으로 공과 패들이 겹치는지 확인 
        if pos[2]>=paddle_pos[0] and pos[0] <= paddle_pos[2]: #공의 아래쪽(y2)이 패들의 위-아래 사이에 있는지 확인

            if pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]:
                return True
        return False

    def draw(self):
        self.canvas.move(self.id, self.x, self.y) #매 프레임 공이 위로 1픽셀씩
        pos=self.canvas.coords(self.id) #현재 공의 위치 가져오기[x1, y1, x2, y2]
        print(self.canvas.coords(self.id)) 

        if pos[1]<=0: #천장에 닿음 -> 아래로 방향 전환
            self.y=3 #가장 위, 왼쪽 좌표가 (0,0)이므로 위로 올라갈수록 y=0 / #속도 수정
        
        if pos[3]>=self.canvas_height:
            self.hit_bottom = True #바닥에 닿았을 경우 hit_bottom=True
            self.game.game_over() #바닥에 닿았을 때 "GAME OVER" 문구 나타나게 하기
        # 이미 바닥에 부딪혔다면 더이상 충돌 체크 안해도 됨
        if not self.hit_bottom:
            if self.hit_paddle(pos) == True: #패들과 부딪혔는지 검사
                self.y=-3
                self.game.update_score() #패들에 닿으면 점수 1 증가

        # 화면 왼쪽/ 오른쪽 끝을 넘지 않게 막기
        if pos[0]<=0:
            self.x=3
        if pos[2]>=self.canvas_width:
            self.x=-3


 

class Paddle: #패들 클래스 추가
    def __init__(self, canvas,  color):
        self.canvas=canvas
        self.id=canvas.create_rectangle(0, 0, 100, 10, fill=color)
        self.canvas.move(self.id, 200, 300)

        self.x=0 #처음에는 안움직임
        self.canvas_width=self.canvas.winfo_width() #너비를 저장하고 있기 (벽에 부딪히면 처리하기 위해서)

        self.canvas.bind_all('<KeyPress-Left>', self.turn_left) #키보드 이벤트 연결
        self.canvas.bind_all('<KeyPress-Right>', self.turn_right)

    def turn_left(self, evt):
        self.x=-2 #왼쪽으로 이동 속도

    def turn_right(self, evt):
        self.x=2 #오른쪽으로 이동 속도
    
    def draw(self): #패들을 x 방향으로만 이동
        self.canvas.move(self.id, self.x, 0)
        pos=self.canvas.coords(self.id)

        # 화면 왼쪽/오른쪽 끝을 넘지 않게 막기
        if pos[0]<=0:
            self.x=0
        elif pos[2]>=self.canvas_width:
            self.x=0

# Game 클래스 내부에서 paddle, ball 관리 -> 아래 코드 없어도 됨
# paddle=Paddle(canvas, 'blue') #패들 추가 #수정-패들 먼저 생성해야함
# ball=Ball(canvas, paddle, 'red') #수정 (paddle) 추가

game=Game()


while True:
    if game.ball.hit_bottom == False:
        game.ball.draw()
        game.paddle.draw()
    tk.update_idletasks() #tkinter 내부 작업 처리
    tk.update()
    time.sleep(0.01)
   


tk.mainloop()