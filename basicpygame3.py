#การวาดรูปแบบ surface ,รูปทรงต่าง ๆ
#เอาจาก basicpygame2 มาต่อยอด
#เพิ่มโค้ดส่วนที่ ออกแบบรูปทรงต่าง ๆ******


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
screen.fill(PURPULE) #fill เหมือนการเทกระป๋องสี

#ออกแบบรูปทรงต่าง ๆ
#วาดรูปแบบ surface ต่าง ๆ

#วาดเส้นตรง
# pygame.draw.line(surface,color,start_pos,end_pos,width) #วาดเส้น
pygame.draw.line(screen,YELLOW,(0,0),(SCREEN_W,SCREEN_H),5) #วาดเส้น

#วาดสี่เหลี่ยม
# pygame.draw.rect(surface,color,(x,y,width,height)) #วาดสี่เหลี่ยม
pygame.draw.rect(screen,RED,(100,100,100,100)) #วาดสี่เหลี่ยม

#วาดวงกลม
# pygame.draw.circle(surface,color,center,radius,width) #วาดวงกลม
pygame.draw.circle(screen,BLUE,(100,100),50,5) #วาดวงกลม



running = True #คือเงื่อนไขการทํางานของหน้าจอเกม ถ้า running = True จะทํางาน
while running:
    for event in pygame.event.get(): #การทํางานของหน้าจอเกม ,get คือการเรียกใช้งานหน้าจอเกม
        if event.type == pygame.QUIT: #ตรวจสอบว่าปิดหน้าจอเกมไหม
            running = False #ถ้าปิดหน้าจอเกม จะเป็น False และหน้าจอเกมจะหยุดการทํางาน

#สั่งอัพเดตหน้าจอเกม
    pygame.display.update()
#ปิดหน้าจอเกม
pygame.quit()

