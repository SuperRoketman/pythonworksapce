# quiz) 하늘에서 떨어지는 똥피하기 게임을 만드시오

# [게임 조건]
# 1. 캐릭터는 화면 가장 아래에 위치, 좌우로만 이동 가능
# 2. 똥은 화면 가장 위에서 떨어짐. x 좌표는 매번 랜덤으로 설정
# 3. 캐릭터가 똥을 피하면 다음 똥이 다시 떨어짐
# 4. 캐릭터가 똥과 충돌하면 게임 종료
# 5. FPS는 30으로 고정

# [게임 이미지]
# 1. 배경 : 640 * 480 (세로, 가로) - background.png
# 2. 캐릭터 : 70 * 70 - character.png
# 3. 똥 : 70 * 70 - enemy.png


# 나
# import pygame
# from random import*
# #####################################################
# # 기본 초기화 (반드시 해야 하는 것들)
# pygame.init()

# #화면 크기 설정
# screen_width = 480 # 가로 크기
# screen_height = 640 # 세로 크기
# screen = pygame.display.set_mode((screen_width, screen_height))

# # 화면 타이틀 설정
# pygame.display.set_caption("Rocketman Game")

# # FPS
# clock = pygame.time.Clock()
# #####################################################

# # 1. 사용자 게임 초기화 (배경화면, 게임 이미지, 좌표, 속도, 폰트 등)
# background = pygame.image.load("E:\\githubdesktop-SuperRoketman\\pythonworksapce\\pygame_basic\\background.png")


# character = pygame.image.load("E:\\githubdesktop-SuperRoketman\\pythonworksapce\\pygame_basic\\character.png")

# character_size = character.get_rect().size # 캐릭터에게 정사각형부여, 사이즈는 사진사이즈
# character_width = character_size[0] # character_size 의 가로 크기
# character_height = character_size[1] # charac_size 의 세로 크기

# character_x_pos = (screen_width / 2) - (character_width / 2)
# character_y_pos = screen_height - character_height

# character_speed = 0.6

# to_x = 0


# enemy = pygame.image.load("E:\\githubdesktop-SuperRoketman\\pythonworksapce\\pygame_basic\\enemy.png")

# enemy_size = enemy.get_rect().size # 이미지의 크기를 구해옴
# enemy_width = enemy_size[0] # 에네미의 가로 크기
# enemy_height = enemy_size[1] # 에네미의 세로 크기

# enemy_x_pos = randrange(0, (screen_width) - (enemy_width))
# enemy_y_pos = -enemy_height

# start_ticks = pygame.time.get_ticks()

# enemy_speed = 0.6

# to_y = enemy_speed

# enemy_y_pos += to_y * dt

# running = True
# while running:
#     dt = clock.tick(30) # 게임 화면의 초당 프레임 수를 설정

#     #speed_up = (pygame.time.get_ticks() - start_ticks)/6000
#     #enemy_speed = 0.6 + speed_up

#     #to_y = enemy_speed

#     #enemy_y_pos += to_y * dt  # 74줄 부터 79줄 까진 스피드 업을 위한 문장,, 굳이 필요 없음

#     if enemy_y_pos >= screen_height:
#         enemy_x_pos = randrange(0, (screen_width) - (enemy_width))
#         enemy_y_pos = -enemy_height

#     # 2. 이벤트 처리 (키보드, 마우스 등)
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False

#         if event.type == pygame.KEYDOWN: #키가 눌러졌는지 확인
#             if event.key == pygame.K_LEFT:
#                 to_x -= character_speed # to_x = to_x - 5
#             elif event.key == pygame.K_RIGHT:
#                 to_x += character_speed

#         if event.type == pygame.KEYUP:
#             if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
#                 to_x = 0

#         if enemy_y_pos == screen_height:
#             enemy_x_pos = randrange(0, (screen_width) - (enemy_width))
#             enemy_y_pos = -enemy_height


#     # 3. 게임 캐릭터 위치 정의
#     character_x_pos += to_x * dt

#     # 가로 경게값 처리
#     if character_x_pos < 0:
#         character_x_pos = 0
#     elif character_x_pos > screen_width - character_width:
#         character_x_pos = screen_width - character_width
 
#     # 4. 충돌 처리
#     character_rect = character.get_rect()
#     character_rect.left = character_x_pos
#     character_rect.top = character_y_pos

#     enemy_rect = enemy.get_rect()
#     enemy_rect.left = enemy_x_pos
#     enemy_rect.top = enemy_y_pos


#     if character_rect.colliderect(enemy_rect):
#         print("GAME OVER, Record is " + str(round(enemy_speed, 2)))
#         running = False


#     # 5. 화면에 그리기
#     screen.blit(background, (0, 0)) # 배경 그리기

#     screen.blit(character, (character_x_pos, character_y_pos))

#     screen.blit(enemy, (enemy_x_pos, enemy_y_pos))

#     pygame.display.update()


# pygame.quit()


#유튜바
import random
import pygame
from pygame.constants import KEYDOWN, KEYUP
#####################################################
# 기본 초기화 (반드시 해야 하는 것들)
pygame.init()

#화면 크기 설정
screen_width = 480 # 가로 크기
screen_height = 640 # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("Rocketman Game")

# FPS
clock = pygame.time.Clock()
#####################################################

# 1. 사용자 게임 초기화 (배경화면, 게임 이미지, 좌표, 속도, 폰트 등)
# 배경 만들기
background = pygame.image.load("E:\\githubdesktop-SuperRoketman\\pythonworksapce\\pygame_basic\\background.png")

# 캐릭터 만들기
character = pygame.image.load("E:\\githubdesktop-SuperRoketman\\pythonworksapce\\pygame_basic\\character.png")
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width / 2) - (character_width / 2)
character_y_pos = screen_height - character_height

# 이동 위치
to_x = 0
character_speed = 10

# 똥 만들기

ddong = pygame.image.load("E:\\githubdesktop-SuperRoketman\\pythonworksapce\\pygame_basic\\enemy.png")
ddong_size = ddong.get_rect().size
ddong_width = ddong_size[0]
ddong_height = ddong_size[1]
ddong_x_pos = random.randint(0, screen_width - ddong_width)
ddong_y_pos = 0

ddong_speed = 10


running = True
while running:
    dt = clock.tick(30) # 게임 화면의 초당 프레임 수를 설정

    # 2. 이벤트 처리 (키보드, 마우스 등)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                to_x += character_speed

        if event.type == KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0

    # 3. 게임 캐릭터 위치 정의
    character_x_pos += to_x

    if character_x_pos <0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    ddong_y_pos += ddong_speed

    if ddong_y_pos > screen_height:
        ddong_y_pos = 0
        ddong_x_pos = random.randint(0, screen_width - ddong_width)
 
    # 4. 충돌 처리
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    ddong_rect = ddong.get_rect()
    ddong_rect.left = ddong_x_pos
    ddong_rect.top = ddong_y_pos

    if character_rect.colliderect(ddong_rect):
        print("충돌했어요.")
        running = False

    # 5. 화면에 그리기
    screen.blit(background, (0, 0))
    screen.blit(character, (character_x_pos, character_y_pos))
    screen.blit(ddong, (ddong_x_pos, ddong_y_pos))

    pygame.display.update()


pygame.quit()