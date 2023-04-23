import random 
import pygame
#########################################################
# 기본 초기화 (반드시 해야 하는 것들))
pygame.init() #초기화

# 화면 크기 설정
screen_width = 1280 # 가로
screen_height = 1280 # 세로
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("Pang Game")

#FPS
clock = pygame.time.Clock()
#########################################################

# 1. 사용자 게임 초기화(배경화면, 게임 이미지, 좌표, 속도, 폰트 등)

# 배경 이미지 불러오기
background = pygame.image.load("/Users/imseunghyun/Documents/Pang/pygame_basic/design-space-paper-textured-background.jpg")

# 캐릭터 불러오기
character = pygame.image.load("/Users/imseunghyun/Documents/Pang/pygame_basic/dog.png")
character_size = character.get_rect().size # 이미지 크기를 구해옴
character_width = character_size[0] # 캐릭터 가로 크기
character_height = character_size[1] # 캐릭터 세로 크기
character_x_pos = (screen_width / 2) - (character_width / 2) # 화면 가로의 절반 크기에 해당하는 곳에 위치
character_y_pos = screen_height - character_height #화면 세로 크기 가장 아래에 해당하는 곳에 위치

# 이동할 좌표
to_x = 0

# 이동속도
character_speed = 10

# 똥 만들기
ddong = pygame.image.load("/Users/imseunghyun/Documents/Pang/pygame_basic/ddong.png")
ddong_size = ddong.get_rect().size # 이미지 크기를 구해옴
ddong_width = ddong_size[0] # 캐릭터 가로 크기
ddong_height =ddong_size[1] # 캐릭터 세로 크기
ddong_x_pos = random.randint(0, screen_width - ddong_width)
ddong_y_pos = 0 
ddong_speed = 10


# 이벤트 루프
running = True # 게임이 진행중인가 확인
while running:
    dt = clock.tick(30) # 게임화면의 초당 프레임 수를 설정

    # 2. 이벤트 처리(키보드, 마우스 등)
    for event in pygame.event.get(): # 마우스나 키보드 동작 체크
        if event.type == pygame.QUIT: # 창이 닫히는 이번트가 발생하였는가
            running = False # 게임이 진행중이 아님을 설정

        if event.type == pygame.KEYDOWN: # 키가 눌러졌는지 확인
            if event.key == pygame.K_LEFT:
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                to_x += character_speed

        if event.type == pygame.KEYUP: # 방향기를 떼면 멈춤
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0

    # 3. 게임 캐릭터 위치 정의
    character_x_pos += to_x

    # 가로 경계값 처리
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    ddong_y_pos += ddong_speed

    if ddong_y_pos > screen_height:
        ddong_y_pos = 0
        ddong_x_pos = random.randint(0, screen_width - ddong_width)


    # 4. 충돌 처리
    # 충동 처리를 위한 rect 정보 업데이트
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    ddong_rect = ddong.get_rect()
    ddong_rect.left = ddong_x_pos
    ddong_rect.top = ddong_y_pos

    # 충돌 체크
    if character_rect.colliderect(ddong_rect):
        print("충돌했어요")
        running = False
        
    # 5. 화면에 그리기
    screen.blit(background, (0, 0)) # 배경 그리기
    screen.blit(character, (character_x_pos, character_y_pos)) # 캐릭터 그리기
    
    screen.blit(ddong, (ddong_x_pos, ddong_y_pos)) # 적 그리기

    
    pygame.display.update() # 게임 화면을 다시 그리기 

# 잠시 대기
pygame.time.delay(2000) # 2초 정도 대기

# 파이게임 종료
pygame.quit()