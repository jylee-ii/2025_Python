import pygame
import random

pygame.init()

WIDTH, HEIGHT = 600, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("총알을 피해서 미로 탈출하자!")

clock = pygame.time.Clock()

# player, bullet 이미지 로드
player_img = pygame.image.load("player.png")
player_img = pygame.transform.scale(player_img, (40, 40))

bullet_img = pygame.image.load("bullet.png")
bullet_img = pygame.transform.scale(bullet_img, (20, 10))


# 난이도/제한시간 변수 추가
level = 1
time_limit = 30
time_counter = 0

bullet_timer = 0        # 총알 생성 간격 세기 위한 타이머
BULLET_INTERVAL = 45    # 총알 생성 주기

running = True
game_over = False
next_level_ready = False  # 목적지 도달 후 Enter 

# Player 클래스
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = player_img
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2, 60) # 60으로 플레이어 위치 위쪽으로 고정
        self.speed = 3

    def update(self):
        global game_over    #게임오버 상태 변경 가능하도록 전역변수 사용
        keys = pygame.key.get_pressed()
        # 기존 위치 저장 (이동하기 전에 위치 저장)
        old_x = self.rect.x
        old_y = self.rect.y

        # x축 이동
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed

        # 벽 충돌 시 x축 기존 위치로
        for wall in maze_walls:
            if self.rect.colliderect(wall):
                game_over = True
                self.rect.x = old_x
                break

        # y축 이동
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed

        # 벽 충돌 시 y축 기존 위치로
        for wall in maze_walls:
            if self.rect.colliderect(wall):
                game_over =True
                self.rect.y = old_y
                break

        # 화면 밖 방지 코드
        self.rect.clamp_ip(screen.get_rect())

# Bullet 클래스
class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, speed):
        super().__init__()
        self.image = bullet_img
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y) # 총알 왼쪽 위 좌표(총알 처음 생성 위치 설정)
        self.speed = speed  

    def update(self):
        self.rect.x += self.speed
        
        # 화면 밖일 경우 총알 삭제
        if self.rect.right < 0 or self.rect.left > WIDTH:
            self.kill() 


# 미로 벽 생성
maze_walls = [
    pygame.Rect(0, 0, 50, HEIGHT),         # 왼쪽 벽
    pygame.Rect(WIDTH-50, 0, 50, HEIGHT),  # 오른쪽 벽

    pygame.Rect(50, 150, 200, 20),   # 1번 가로 벽
    pygame.Rect(350, 150, 200, 20),  # 2번 가로 벽
    pygame.Rect(100, 300, 400, 20),  # 3번 가로 벽
    pygame.Rect(50, 450, 200, 20),   # 4번 가로 벽
    pygame.Rect(350, 450, 200, 20),  # 5번 가로 벽
    pygame.Rect(100, 600, 400, 20)
]


# 목적지 생성
goal_rect = pygame.Rect(200, 760, 200, 25)

all_sprites = pygame.sprite.Group()
bullet_group = pygame.sprite.Group()

player = Player()
all_sprites.add(player)


running = True
game_over = False

# 게임 종료 폰트 설정
font = pygame.font.SysFont(None, 36)


# 게임 리셋 함수 (R 눌렀을 때)
def reset_game():
    #전역변수로 써서 초기화하기
    global bullet_timer, game_over, time_limit, time_counter
    player.rect.center = (WIDTH//2, 60)
    for bullet in bullet_group:
        bullet.kill()
    bullet_timer = 0
    game_over = False
    next_level_ready = False
    time_limit = 30
    level = 1


# 다음 단계로 가는 함수 (Enter 눌렀을 때)
def next_level():
    global bullet_timer, game_over, time_limit, time_counter, level, next_level_ready
    player.rect.center = (WIDTH // 2, 60)
    for bullet in bullet_group:
        bullet.kill()
    bullet_timer = 0
    game_over = False
    next_level_ready = False  # 전역 변수로 반드시 선언
    level += 1
    time_limit = max(10, 30 - level ** 2)
    time_counter = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            # 미로 벽에 부딪혀 게임오버 후 R -> 리셋
            if game_over and event.key == pygame.K_r:
                reset_game()

            # 게임오버 후 Enter -> 다음 단계로
            if next_level_ready and event.key == pygame.K_RETURN:
                next_level()



    if not game_over and not next_level_ready:
        all_sprites.update()
        bullet_group.update()

        # 제한 시간 처리
        time_counter +=1
        if time_counter>=60:
            time_counter = 0
            time_limit -=1
        
        if time_limit<=0:
            game_over = True
        
        # 총알 속도, 생성 간격 => 난이도 올리기
        bullet_speed = 4 + level
        current_bullet_interval = max(15, BULLET_INTERVAL - level*5)


        # 총알 생성
        bullet_timer +=1
        if bullet_timer >= current_bullet_interval:
            bullet_timer = 0

            y = random.randint(150, HEIGHT - 200)
        
            spawn_side = random.choice(["left", "right"]) #좌/우로 총알 이동

            if spawn_side == "left":
                bullet = Bullet(0, y, bullet_speed)    # 오른쪽으로 이동
            else:
                bullet = Bullet(WIDTH, y, -bullet_speed)    # 왼쪽으로 이동

            all_sprites.add(bullet)
            bullet_group.add(bullet)

        
        # 총알 충돌
        if pygame.sprite.spritecollide(player, bullet_group, False):
            game_over = True

        # 목적지 도달
        if player.rect.colliderect(goal_rect):
            next_level_ready = True

    # 그리기
    screen.fill((25, 25, 25))   #회색으로 설정

    # 미로 벽 -> 미로의 형태 만들기
    for wall in maze_walls:
        pygame.draw.rect(screen, (180, 180, 180), wall)

    # 목적지 그리기
    pygame.draw.rect(screen, (90, 160, 255), goal_rect)

    all_sprites.draw(screen)

    # 남은 시간 표시
    time_text=font.render(f"TIME : {time_limit}", True, (255, 255, 255))
    screen.blit(time_text, (20, 20))

    # 현재 레벨 표시
    level_text=font.render(f"LEVEL: {level}", True, (255, 255, 255))
    screen.blit(level_text, (20, 60))


    # 게임오버 메시지
    # 목적지 도달해서 다음 단계로 넘어가기
    if next_level_ready:
        next_text = font.render("GOAL! Press Enter", True, (0, 255, 0))
        next_x = (WIDTH - next_text.get_width()) // 2
        next_y = (HEIGHT - next_text.get_height()) // 2
        screen.blit(next_text, (next_x, next_y)) 

    # 미로 벽에 부딪힌 경우 R 눌러서 리셋
    if game_over:
        over_text = font.render("GAME OVER (Press R to Reset)", True, (255, 0, 0))
        over_x = (WIDTH - over_text.get_width()) // 2  # 글씨 정중앙에 배치
        over_y = (HEIGHT - over_text.get_height()) // 2 
        screen.blit(over_text, (over_x, over_y))    


    pygame.display.flip()
    clock.tick(60)

pygame.quit()
