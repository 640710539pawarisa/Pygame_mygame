#pygame - สร้างเกม ด้วย python ,#สร้างเกม ด้วย labrary pygame  ด้วย ภาษาpython

#การสร้างหน้าจอเกมเปล่าๆ

#การเรียกใช้งาน pygame
import pygame 

#เริ่มใช้งาน pygame ,หรือ ประกาศใช้งาน pygame
pygame.init()

#หัวข้อเกม
pygame.display.set_caption("My First Game")

#สร้างตัวแปรเก็บขนาดของหน้าจอเกม
SCREEN_W = 700
SCREEN_H = 500

#สร้างหน้าจอเกม ขนาดหน้าจอเกม
screen = pygame.display.set_mode((SCREEN_W,SCREEN_H)) 
#ความกว้าง x ความสูง ของหน้าจอ แล้วเก็บไว้ในตัวแปร screen

#แสดงหน้าจอเกม ,ใช้ while loop ในการแสดงหน้าจอเกม
running = True #คือเงื่อนไขการทํางานของหน้าจอเกม ถ้า running = True จะทํางาน
while running:
    for event in pygame.event.get(): #การทํางานของหน้าจอเกม ,get คือการเรียกใช้งานหน้าจอเกม
        if event.type == pygame.QUIT: #ตรวจสอบว่าปิดหน้าจอเกมไหม
            running = False #ถ้าปิดหน้าจอเกม จะเป็น False และหน้าจอเกมจะหยุดการทํางาน

#ปิดหน้าจอเกม
pygame.quit()

