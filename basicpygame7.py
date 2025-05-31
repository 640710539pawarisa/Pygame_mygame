#getRect() หรือ คือการเรียกใช้ตําแหน่งของหน้าจอเกมที่เราสร้าง ******

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

#getRect() หรือ คือการเรียกใช้ตําแหน่งของหน้าจอเกมที่เราสร้าง
screen_rect = screen.get_rect()  #ดูขนาดของหน้าจอเกม***** แล้วเก็บไว้ในตัวแปร screen_rect

print(screen_rect.width)#ดูความกว้างของหน้าจอเกม
print(screen_rect.height)#ดูความสูงของหน้าจอเกม
print(screen_rect.size) #ดูความกว้าง x ความสูงของหน้าจอเกม
print(screen_rect.centerx) #ดูจุดกึ่งกลางตามแนวแกน  x ของหน้าจอเกม ,screen_w//2 = 200
print(screen_rect.centery) #ดูจุดกึ่งกลางตามแนวแกน  y ของหน้าจอเกม ,screen_h//2 = 250
print(screen_rect.center) #ดูตําแหน่งกลางของหน้าจอเกม คือ (จุดกึ่งกลางตามแนวแกน x มารวมกับ จุดกึ่งกลางตามแนวแกน y)


running = True #คือเงื่อนไขการทํางานของหน้าจอเกม ถ้า running = True จะทํางาน
while running:
    for event in pygame.event.get(): #การทํางานของหน้าจอเกม ,get คือการเรียกใช้งานหน้าจอเกม
        if event.type == pygame.QUIT: #ตรวจสอบว่าปิดหน้าจอเกมไหม
            running = False #ถ้าปิดหน้าจอเกม จะเป็น False และหน้าจอเกมจะหยุดการทํางาน
    

#สั่งอัพเดตหน้าจอเกม
    pygame.display.update()
#ปิดหน้าจอเกม
pygame.quit()

