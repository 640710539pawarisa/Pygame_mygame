#การแสดงข้อความ ในหน้าจอเกม(customfont)*****
#เปลี่ยนจาก sysfont เป็น customfont ******

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

#แสดงข้อความในหน้าจอเกม  ****
#ตั้งค่าข้อความ และฟอนต์ ในหน้าจอเกม *****

# pygame.font.customFont(name,size,bold,italic) #ดึงฟอนต์ customfont
custom_font = pygame.font.Font("Font\Coiny.ttf", 30) #ดึงฟอนต์ customfont
message_text = custom_font.render("Hello My Game",True,BLACK) #แสดงข้อความ ,เก็บไว้ในตัวแปร message_text
title_text = custom_font.render("My First Game",True,PURPULE) #แสดงข้อความ ,เก็บไว้ในตัวแปร title_text

running = True #คือเงื่อนไขการทํางานของหน้าจอเกม ถ้า running = True จะทํางาน
while running:
    for event in pygame.event.get(): #การทํางานของหน้าจอเกม ,get คือการเรียกใช้งานหน้าจอเกม
        if event.type == pygame.QUIT: #ตรวจสอบว่าปิดหน้าจอเกมไหม
            running = False #ถ้าปิดหน้าจอเกม จะเป็น False และหน้าจอเกมจะหยุดการทํางาน
            
    #แสดงข้อความในหน้าจอเกม********* 
    #หน้าจอเกม.blit(ข้อความ,ตําแหน่ง)
    screen.blit(message_text,(200,200))
    screen.blit(title_text,(200,150))

#สั่งอัพเดตหน้าจอเกม
    pygame.display.update()
#ปิดหน้าจอเกม
pygame.quit()

