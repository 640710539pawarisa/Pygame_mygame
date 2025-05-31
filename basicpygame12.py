#การกำหนด fps ในหน้าจอเกม ************
#รับค่าจากkeyboard*****

#****เราอยากทำอะไร = เราอยากเพิ่ม frame rate ให้วัตถุเกมมัน smooth มากขึ้น  **********88


#ต่อยอดมาจาก basicpygame11.py

#การเรียกใช้งาน pygame
import pygame 

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

#*****เพิ่มโค้ดส่วนนี้
#FPS 
#ตัวแปรเก็บค่า frame rate
FPS = 60
#สร้าง class ในการกําหนดค่า frame rate
clock = pygame.time.Clock()

#สร้างตัวแปรเก็บขนาดของหน้าจอเกม
SCREEN_W = 700
SCREEN_H = 500


#สร้างหน้าจอเกม ขนาดหน้าจอเกม
screen = pygame.display.set_mode((SCREEN_W,SCREEN_H))  #รูปแบบ surface
#ความกว้าง x ความสูง ของหน้าจอ แล้วเก็บไว้ในตัวแปร screen

#แสดงหน้าจอเกม ,ใช้ while loop ในการแสดงหน้าจอเกม

#ตั้งค่าสีหน้าจอเกม
screen.fill(WHITE) #fill เหมือนการเทกระป๋องสี

#โหลดรูปภาพ
# pygame.image.load(path) #โหลดรูปภาพ *****
paddle = pygame.image.load("image\paddle.png") 
#โหลดรูปภาพ แล้วเก็บไว้ในตัวแปร paddle

#ปรับขนาดรูปภาพ **
# pygame.transform.scale(รูปภาพ,ขนาด) #ปรับขนาดรูปภาพ **
paddle = pygame.transform.scale(paddle,(120,50))

#ตั้งค่าคุณสมบัติ paddle
paddle_rect = paddle.get_rect() #เรียกใช้ตําแหน่งของหน้าจอเกมที่เราสร้าง
#คำนวณหาจุดกึ่งกลางของหน้าจอเกมมาทำตรงนี้ **
paddle_rect.centerx = SCREEN_W//2
paddle_rect.centery = SCREEN_H//2


running = True #คือเงื่อนไขการทํางานของหน้าจอเกม ถ้า running = True จะทํางาน
while running:
    for event in pygame.event.get(): #การทํางานของหน้าจอเกม ,get คือการเรียกใช้งานหน้าจอเกม
        if event.type == pygame.QUIT: #ตรวจสอบว่าปิดหน้าจอเกมไหม
            running = False #ถ้าปิดหน้าจอเกม จะเป็น False และหน้าจอเกมจะหยุดการทํางาน
    #เพิ่มการทํางานในหน้าจอเกมตรงนี้*****
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]: #คำสั่งเปลี่ยนตำแหน่ง โดยใช้คีย์บอร์ด กดปุ่มขึ้น
            paddle_rect.y -= SPEED #คือการขยับpaddle ที่ตําแหน่ง y ทีละ 1
    if keys[pygame.K_DOWN]:
            paddle_rect.y += SPEED
    if keys[pygame.K_LEFT]:
            paddle_rect.x -= SPEED
    if keys[pygame.K_RIGHT]:
            print("RIGHT ARROW")
            paddle_rect.x += SPEED
    
    #มองภาพเป็นแกน x และ y ในหน้าจอเกม
    #*****
    #วาดภาพสีขาวขึ้นมาก่อนแล้ว ค่อยสร้าง paddle ตามที่เมาส์คลิก มันจะได้สร้างทีละอันแล้วหายไป แบบวนลูป
    screen.fill(WHITE) 
    #แสดงรูปภาพในหน้าจอเกม***
    #หน้าจอเกม.blit(รูปภาพ,ตําแหน่ง(x,y))
    screen.blit(paddle,paddle_rect)
#สั่งอัพเดตหน้าจอเกม
    pygame.display.update()
#เพิ่ม fps ในหน้าจอเกม
    clock.tick(FPS)
#ปิดหน้าจอเกม
pygame.quit()

