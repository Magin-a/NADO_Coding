import pygame
pygame.init() #초기화 (반드시 필요)

#화면 크기 설정
screen_width = 480 #가로 크기
screen_height = 640 # 세로크기
screen = pygame.display.set_mode((screen_width, screen_height))


#화면 타이틀  설정
pygame.display.set_caption("Making Game") # 게임 이름

#FPS
clock = pygame.time.Clock()

#배경이미지 불러오기
background = pygame.image.load("C:/Users/박영웅/Desktop/python연습장/이온2파이썬/나도코딩/Pygame_basic/background.png")

#캐릭터(스프라이트) 불러오기
character = pygame.image.load("C:/Users/박영웅/Desktop/python연습장/이온2파이썬/나도코딩/Pygame_basic/character.png")
character_size = character.get_rect().size   #.get_rect().size로 인해 캐릭터 이미지의 가로세로 크기 설정 
character_width = character_size[0] #캐릭터의 가로 크기
character_height = character_size[1] #캐릭터의 세로 크기
character_x_pos = (screen_width / 2) - (character_width / 2)  #화면 가로의 절반 크기에 해당하는 곳에 위치
character_y_pos = screen_height - character_height # 화면 세로 크기의 가장 아래에 해당하는 곳에 위치

#이동할 좌표
to_x = 0
to_y = 0

#이동속도
character_speed = 0.6

# 이벤트 루프
running = True #게임이 진행중인가?
while running:
    dt = clock.tick(10) #게임화면의 초당 프레임 수를 설정

#캐릭터가 100만큼 이동을 해야함
# 10 fps: 1초동안에 10번 동작 -> 1번에 10만큼 동작
# 20 fps: 1초동안에 20번 동작 -> 1번에 5만큼 동작

    print("fps : " + str(clock.get_fps())) #fps 확인

    for event in pygame.event.get(): #필수요소: 프로그램이 종료하기 않게 사용자가 키보드 입력을 한다던지 마우스 입력은 한다든지 체크함
        if event.type == pygame.QUIT: #창 모서리에 x버튼을 눌렀을시에 발생하는 조건문
            running = False #게임이 진행중이 아님

        if event.type == pygame.KEYDOWN: #키가 눌러졌는지 확인
            if event.key == pygame.K_LEFT: #캐릭터 왼쪽으로 
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT: #캐릭터 오른쪽으로
                to_x += character_speed
            elif event.key == pygame.K_UP: #캐릭터 위로
                to_y -= character_speed
            elif event.key == pygame.K_DOWN: #캐릭터 아래로
                to_y += character_speed
    
    if event.type == pygame.KEYUP: #방향키 때면 멈춤
        if event.key == pygame.K_LEFT or  pygame.K_RIGHT:
            to_x = 0
        elif event.key == pygame.K_UP or pygame.K_DOWN:
            to_y = 0

    character_x_pos += to_x *dt
    character_y_pos += to_y *dt
    
    #가로 세로 경계값 처리
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width
    elif character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos > screen_height - character_height:
        character_y_pos = screen_height - character_height


    screen.blit(background, (0, 0)) #배경 그리기 

    screen.blit(character, (character_x_pos, character_y_pos)) #캐릭터의 위치값을 계산해서 지정해줘야한다
    
    pygame.display.update() #게임화면을 다시 그리기(필요: pygame에서는 매번 그려주어야한다.)
# pygame 종료
pygame.quit()