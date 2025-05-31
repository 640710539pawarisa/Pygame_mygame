#การนับคะแนนในเกม************
#รับค่าจากkeyboard*****

#****เราอยากทำอะไร = นับคะแนนเมื่อ ball ชนกับ paddle ในการเรียกใช้งาน keyboard
#ไปแก้ไขในส่วนการชน
#สร้างตัวแปรให้เก็บคะแนน
# score = 0

#ต่อยอดมาจาก basicpygame17.py

#การเรียกใช้งาน pygame
import pygame 

#การเรียกใช้งาน random
import random

#เริ่มใช้งาน pygame ,หรือ ประกาศใช้งาน pygame
pygame.init()

#หัวข้อเกม
pygame.display.set_caption("My First Game")

#ตั้งค่าสีหน้าจอเกม(RGB) ,ชื่อตัวแปรสี = (R,G,B)
WHITE = (255,255,255) #สีขาว
BLACK = (0,0,0) #สีดํา
GREEN = (0,255,0) #สีเขียว
RED = (255,0,0) #สีแดง
BLUE = (0,0,255) #สีฟ้า
YELLOW = (255,255,0) #สีเหลือง
PURPULE = (255,0,255) #สีม่วง

#ความเร็วในการเคลื่อนที่
#ตัวแปรเก็บค่าความเร็วในการเคลื่อนไหว
SPEED = 5
#อยากให้มันสมูทมากกว่านี้ ต้องเอาตัว frame rate มาใช้ ** ปัจจุบัน 60 frame rate ต่อวินาที

#สร้างตัวแปรเก็บค่าความเร็วในการเคลื่อนไหว ball *******************
BALL_SPEED = 2

#FPS 
#ตัวแปรเก็บค่า frame rate
FPS = 60
#สร้าง class ในการกําหนดค่า frame rate
clock = pygame.time.Clock()


#สร้างตัวแปรเก็บขนาดของหน้าจอเกม ****มาดูส่วนนี้
SCREEN_W = 600
SCREEN_H = 600


#สร้างหน้าจอเกม ขนาดหน้าจอเกม
screen = pygame.display.set_mode((SCREEN_W,SCREEN_H))  #รูปแบบ surface
#ความกว้าง x ความสูง ของหน้าจอ แล้วเก็บไว้ในตัวแปร screen

#แสดงหน้าจอเกม ,ใช้ while loop ในการแสดงหน้าจอเกม

#ตั้งค่าสีหน้าจอเกม
screen.fill(BLACK) #fill เหมือนการเทกระป๋องสี

#โหลดรูปภาพ

paddle = pygame.image.load("image/paddle.png")
ball = pygame.image.load("image/ball.png")

#โหลดรูปภาพ แล้วเก็บไว้ในตัวแปร paddle

#ปรับขนาดรูปภาพ **
# pygame.transform.scale(รูปภาพ,ขนาด) #ปรับขนาดรูปภาพ **
paddle = pygame.transform.scale(paddle,(120,30))
ball = pygame.transform.scale(ball,(50,50))

#ตั้งค่าคุณสมบัติ paddle object
paddle_rect = paddle.get_rect() #เรียกใช้ตําแหน่งของหน้าจอเกมที่เราสร้าง
#คำนวณหาจุดกึ่งกลางของหน้าจอเกมมาทำตรงนี้ **
paddle_rect.centerx = SCREEN_W//2
paddle_rect.centery = SCREEN_H//2 + 200 #อยากให้อยู่ตรงกลางด้านล่าง

#ตั้งค่าคุณสมบัติ ball object
ball_rect = ball.get_rect() #เรียกใช้ตําแหน่งของหน้าจอเกมที่เราสร้าง
#กำหนดให้ ball_rect อยู่ตรงกลางหน้าจอเกม  **
# ball_rect.center = (SCREEN_W //2 , SCREEN_H //2-100) #อยากให้อยู่ตรงกลางด้านบน ใช้คําสั่งนี้

ball_rect.x =random.randint(0,SCREEN_W - 32) #คือไม่ให้มันสุ่มติดขอบเกินไป ,ตำแหน่งเริ่มต้นของ ball
ball_rect.y = 0

#*********เพิ่มส่วนนี้**
score = 0


running = True #คือเงื่อนไขการทํางานของหน้าจอเกม ถ้า running = True จะทํางาน
while running:
    for event in pygame.event.get(): #การทํางานของหน้าจอเกม ,get คือการเรียกใช้งานหน้าจอเกม
        if event.type == pygame.QUIT: #ตรวจสอบว่าปิดหน้าจอเกมไหม
            running = False #ถ้าปิดหน้าจอเกม จะเป็น False และหน้าจอเกมจะหยุดการทํางาน
    
    #การชน 
    if paddle_rect.colliderect(ball_rect):
        score += 1 #เพิ่มคะแนนเมื่อball ชนกับ paddle
        print(score) 
        #แล้วสุ่มบอลใหม่ ให้บอลเก่าหายปเมื่อชนกับ paddle แล้ว
        ball_rect.x = random.randint(0,SCREEN_W - 32) #การสุ่ม ball_rect ใหม่ ,คือตำแหน่งเริ่มต้น
        ball_rect.y = 0   
        
    #รับค่าจากผู้เล่น        
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddle_rect.left > 0:
            paddle_rect.x -= SPEED
    if keys[pygame.K_RIGHT] and paddle_rect.right < SCREEN_W:
            print("RIGHT ARROW")
            paddle_rect.x += SPEED
    
    #เพิ่มโค้ดส่วนนี้***************8
    #การเคลื่อนที่ ball
    if ball_rect.y < SCREEN_H:
        ball_rect.y += SPEED #เคลื่อน ball ลงด้านล่าง
    else:
        #ทะลุขอบจอ
        ball_rect.x = random.randint(0,SCREEN_W - 32) #การสุ่ม ball_rect ใหม่ ,คือตำแหน่งเริ่มต้น
        ball_rect.y = 0
        
    #มองภาพเป็นแกน x และ y ในหน้าจอเกม
    #***
    #วาดภาพสีดำขึ้นมาก่อนแล้ว ค่อยสร้าง paddle ตามที่เมาส์คลิก มันจะได้สร้างทีละอันแล้วหายไป แบบวนลูป
    screen.fill(BLACK) 
    #แสดงรูปภาพในหน้าจอเกม***
    #หน้าจอเกม.blit(รูปภาพ,ตําแหน่ง(x,y))
    screen.blit(paddle,paddle_rect)
    
    #เพิ่มการทํางานในหน้าจอเกมตรงนี้*****
    screen.blit(ball,ball_rect)
    
    
#สั่งอัพเดตหน้าจอเกม
    pygame.display.update()
#เพิ่ม fps ในหน้าจอเกม
    clock.tick(FPS)
#ปิดหน้าจอเกม
pygame.quit()

