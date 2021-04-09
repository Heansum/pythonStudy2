import  pygame
import sys
import random

def showScore(score, x, y, screen):
    font = pygame.font.Font(None, 24)
    text = font.render("Score: " + str(score).zfill(6), True, (0, 0, 0))
    textRect = text.get_rect()
    textRect.centerx = x
    textRect.centery = y
    screen.blit(text, textRect)


pygame.init()
screen = pygame.display.set_mode((480, 640))

FPS = 60
fpsClock = pygame.time.Clock()

asteroidtimer = 100

asteroids = [[20, 0, 0]]

score = 0

try:
    spaceshipimg = pygame.image.load("./img/spaceship.png")
    asteroid0 = pygame.image.load("./img/asteroid00.png")
    asteroid1 = pygame.image.load("./img/asteroid01.png")
    asteroid2 = pygame.image.load("./img/asteroid02.png")
    asteroidimgs = (asteroid0, asteroid1, asteroid2)
    gameover = pygame.image.load("./img/gameover.jpg")

    takeoffsound = pygame.mixer.Sound("./audio/takeoff.wav")
    landingsound = pygame.mixer.Sound("./audio/landing.wav")

    takeoffsound.play()
except Exception as err:
    print("그림 또는 효과음 삽입에 문제가 있습니다. ", err)
    pygame.quit()
    sys.exit(0)

screen.fill((255, 255, 255))
screen.blit(spaceshipimg, (240, 600))
screen.blit(asteroidimgs[0], (240, 320))

pygame.display.flip()




running = True
while running:
    # 사양이 좋은 컴퓨터든 사양이 좋지 못한 컴퓨터든
    # 일정한 속도로 게임을 즐기게 하기 위해서
    # while문의 속도를 조절
    # 1초에 30번 while문을 반복해라
    # 사양이 좋지 못한 컴퓨터가 1초에 10번밖에 반복하지 못한다?

    fpsClock.tick(FPS)

    print("실행")

    # 종료 버튼을 누르기 전까지 게임이 실행되어야한다.
    for event in pygame.event.get():
        # 종료 버튼을 눌렀다면은
        if event.type == pygame.QUIT:
            # 게임을 종료해라
            pygame.quit()
            sys.exit(0)
            break

    screen.fill((255, 255, 255))

    score = score + 1
    showScore(score, 400, 10, screen)
    if score % 100 == 0:
        FPS += 2

    position = pygame.mouse.get_pos()
    spaceshippos = (position[0] - 10, 600)
    screen.blit(spaceshipimg, spaceshippos)

    spaceshipRect = pygame.Rect(spaceshipimg.get_rect())
    spaceshipRect.left = spaceshippos[0]
    spaceshipRect.top = spaceshippos[1]


    # 떨어질 행성을 생성하고
    asteroidtimer -= 10
    if asteroidtimer <= 0:
        randomX = random.randint(5, 475)
        asteroidType = random.randint(0, 2)
        asteroids.append([randomX, 0, asteroidType])
        asteroidtimer = random.randint(50, 200)

    # 생성한 행성을 떨어뜨린다
    index = 0
    for stone in asteroids:
        stone[1] += 5

        if stone[1] > 640:
            asteroids.pop(index)

        stoneRect = pygame.Rect(asteroidimgs[stone[2]].get_rect())
        stoneRect.left = stone[0]
        stoneRect.top = stone[1]
        if stoneRect.colliderect(spaceshipRect):
            asteroids.pop(index)
            running = False

        screen.blit(asteroidimgs[stone[2]], (stone[0], stone[1]))
        index += 1

#    screen.blit(asteroidimgs[0], (240, 320))

    pygame.display.flip()

    landingsound.play()

screen.blit(gameover, (0, 0))
showScore(score, screen.get_rect().centerx, screen.get_rect().centery, screen)
pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)













