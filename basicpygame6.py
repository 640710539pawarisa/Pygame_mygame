#การใช้งานรูปภาพในหน้าจอเกม ****
#นำ รูปภาพมาใช้งาน
#ต่อยอดมาจาก basicpygame3.py

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

#ปรับขนาดรูปภาพ ******
# pygame.transform.scale(รูปภาพ,ขนาด) #ปรับขนาดรูปภาพ *****
paddle = pygame.transform.scale(paddle,(120,50))

#แสดงรูปภาพในหน้าจอเกม
# screen.blit(รูปภาพ, ตําแหน่ง) #แสดงรูปภาพในหน้าจอเกม ***** 

running = True #คือเงื่อนไขการทํางานของหน้าจอเกม ถ้า running = True จะทํางาน
while running:
    for event in pygame.event.get(): #การทํางานของหน้าจอเกม ,get คือการเรียกใช้งานหน้าจอเกม
        if event.type == pygame.QUIT: #ตรวจสอบว่าปิดหน้าจอเกมไหม
            running = False #ถ้าปิดหน้าจอเกม จะเป็น False และหน้าจอเกมจะหยุดการทํางาน
    
    #แสดงรูปภาพในหน้าจอเกม********* 
    #หน้าจอเกม.blit(รูปภาพ,ตําแหน่ง(x,y))
    screen.blit(paddle,(100,100))
#สั่งอัพเดตหน้าจอเกม
    pygame.display.update()
#ปิดหน้าจอเกม
pygame.quit()

