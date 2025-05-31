# การเรียกใช้งาน pygame
import pygame

# การเรียกใช้งาน random
import random

def start_game():  # <<< ใส่ไว้ครอบโค้ดทั้งหมด
    # เริ่มใช้งาน pygame ,หรือ ประกาศใช้งาน pygame
    pygame.init()

    # หัวข้อเกม
    pygame.display.set_caption("My First Game")

    # ตั้งค่าสีหน้าจอเกม (RGB)
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    GREEN = (0, 255, 0)
    RED = (255, 0, 0)
    BLUE = (0, 0, 255)
    YELLOW = (255, 255, 0)
    PURPULE = (255, 0, 255)

    # ความเร็วในการเคลื่อนที่
    SPEED = 5
    BALL_SPEED = 2

    # FPS
    FPS = 60
    clock = pygame.time.Clock()

    # ขนาดของหน้าจอเกม
    SCREEN_W = 600
    SCREEN_H = 600
    screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))

    # ตั้งค่าสีหน้าจอเกม
    screen.fill(BLACK)

    # โหลดรูปภาพ
    paddle = pygame.image.load("image/paddle.png")
    ball = pygame.image.load("image/ball.png")

    # ปรับขนาดรูปภาพ
    paddle = pygame.transform.scale(paddle, (120, 30))
    ball = pygame.transform.scale(ball, (50, 50))

    # ตั้งค่าคุณสมบัติ paddle
    paddle_rect = paddle.get_rect()
    paddle_rect.centerx = SCREEN_W // 2
    paddle_rect.centery = SCREEN_H // 2 + 200

    # ตั้งค่าคุณสมบัติ ball
    ball_rect = ball.get_rect()
    ball_rect.x = random.randint(0, SCREEN_W - 32)
    ball_rect.y = 0

    # ระบบคะแนน
    score = 0
    font = pygame.font.Font("Font/Coiny.ttf", 30)

    score_txt = font.render("Score : " + str(score), True, WHITE)
    score_rect = score_txt.get_rect()
    score_rect.topleft = (10, 10)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # การชน
        if paddle_rect.colliderect(ball_rect):
            score += 1
            score_txt = font.render("Score : " + str(score), True, WHITE)
            ball_rect.x = random.randint(0, SCREEN_W - 32)
            ball_rect.y = 0

        # รับค่าจากผู้เล่น
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and paddle_rect.left > 0:
            paddle_rect.x -= SPEED
        if keys[pygame.K_RIGHT] and paddle_rect.right < SCREEN_W:
            print("RIGHT ARROW")
            paddle_rect.x += SPEED

        # การเคลื่อนที่ของ ball
        if ball_rect.y < SCREEN_H:
            ball_rect.y += SPEED
        else:
            ball_rect.x = random.randint(0, SCREEN_W - 32)
            ball_rect.y = 0

        # วาดพื้นหลังใหม่
        screen.fill(BLACK)

        # แสดง paddle และ ball
        screen.blit(paddle, paddle_rect)
        screen.blit(ball, ball_rect)

        # แสดงคะแนน
        screen.blit(score_txt, score_rect)

        # อัปเดตหน้าจอ
        pygame.display.update()
        clock.tick(FPS)

    # ปิดหน้าจอเกม
    pygame.quit()

start_game() #เริ่มเล่นเกม