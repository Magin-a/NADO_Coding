import pygame
pygame.init() #초기화 (반드시 필요)

#화면 크기 설정
screen_width = 480 #가로 크기
screen_height = 640 # 세로크기
screen = pygame.display.set_mode((screen_width, screen_height))


#화면 타이틀  설정
pygame.display.set_caption("Making Game") # 게임 이름

#배경이미지 불러오기
background = pygame.image.load("C:/Users/박영웅/Desktop/python연습장/이온2파이썬/나도코딩/Pygame_basic/background.png")

# 이벤트 루프
running = True #게임이 진행중인가?
while running:
    for event in pygame.event.get(): #필수요소: 프로그램이 종료하기 않게 사용자가 키보드 입력을 한다던지 마우스 입력은 한다든지 체크함
        if event.type == pygame.QUIT: #창 모서리에 x버튼을 눌렀을시에 발생하는 조건문
            running = False #게임이 진행중이 아님
    
    # screen.fill((0, 0, 255)) #튜플형태(R,G,B) 색깔채우기
    screen.blit(background, (0, 0)) #배경 그리기 
    
    pygame.display.update() #게임화면을 다시 그리기(필요: pygame에서는 매번 그려주어야한다.)
# pygame 종료
pygame.quit()


