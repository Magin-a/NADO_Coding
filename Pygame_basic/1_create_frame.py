import pygame
pygame.init() #초기화 (반드시 필요)

#화면 크기 설정
screen_width = 480 #가로 크기
screen_height = 640 # 세로크기
screen = pygame.display.set_mode((screen_width, screen_height))

#화면 타이틀  설정
pygame.display.set_caption("Making Game") # 게임 이름

# 이벤트 루프
running = True #게임이 진행중인가?
while running:
    for event in pygame.event.get(): #필수요소: 프로그램이 종료하기 않게 사용자가 키보드 입력을 한다던지 마우스 입력은 한다든지 체크함
        if event.type == pygame.QUIT: #창 모서리에 x버튼을 눌렀을시에 발생하는 조건문
            running = False #게임이 진행중이 아님



# pygame 종료
pygame.quit()
