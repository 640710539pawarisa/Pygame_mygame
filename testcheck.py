import pygame          # นำเข้าโมดูล pygame สำหรับทำเกมหรือ GUI ง่ายๆ
import random          # ใช้สำหรับสุ่มค่าตำแหน่งปุ่ม No ให้หนีไปตำแหน่งใหม่

pygame.init()          # เริ่มต้นใช้งานโมดูล pygame

# ตั้งชื่อหน้าต่างของเกม/แอป
pygame.display.set_caption("You are Gay ?")

# สร้างหน้าจอขนาด 800x600 พิกเซล
screen = pygame.display.set_mode((800, 600))

# กำหนดค่าสีต่างๆ ด้วย RGB
White = (255, 255, 255)
Gray = (128, 128, 128)
Black = (0, 0, 0)
Green = (0, 255, 0)
Red = (255, 0, 0)

# โหลดฟอนต์จากไฟล์ .ttf (ขนาดใหญ่ และขนาดเล็ก)
font_big = pygame.font.Font("Font\\Coiny.ttf", 50)     # ฟอนต์ใหญ่ไว้ใช้แสดงข้อความหลัก
font_small = pygame.font.Font("Font\\Coiny.ttf", 30)   # ฟอนต์เล็กไว้ใช้ในอนาคตถ้าต้องการ

# โหลดรูปภาพปุ่ม "Yes" และ "No"
check_yes = pygame.image.load("image\\yes.png")
check_no = pygame.image.load("image\\no.png")

# ปรับขนาดภาพให้พอดีกับหน้าจอ (กว้าง x สูง)
check_yes = pygame.transform.scale(check_yes, (190, 100))
check_no = pygame.transform.scale(check_no, (200, 100))

# สร้างกรอบสี่เหลี่ยม (Rect) จากรูปภาพ เพื่อง่ายต่อการจัดวางและตรวจจับการคลิก
rect_yes = check_yes.get_rect()
rect_no = check_no.get_rect()

# กำหนดตำแหน่งเริ่มต้นของปุ่ม "Yes" และ "No" บนหน้าจอ
rect_yes.topleft = (150, 250)
rect_no.topleft = (450, 250)

# สร้างตัวแปรเพื่อควบคุมหน้าจอปัจจุบัน (main = หน้าหลัก, yes_screen = หน้าหลังคลิก Yes)
current_screen = "main"

# ตัวแปรควบคุมลูปหลักของเกม/โปรแกรม
running = True

# ลูปหลัก ทำงานไปเรื่อยๆ จนกว่าจะปิดหน้าต่าง
while running:
    # วนตรวจสอบเหตุการณ์ต่างๆ เช่น การคลิก หรือปิดหน้าต่าง
    for event in pygame.event.get():
        if event.type == pygame.QUIT:       # ถ้ากดปิดหน้าต่าง
            running = False                 # ออกจากลูป = ปิดโปรแกรม

        # เงื่อนไข: ถ้ากำลังอยู่ในหน้าจอหลัก
        #การใช้ if current_screen == ... เพื่อสร้างหลายหน้า (Scene)
        if current_screen == "main":  # ถ้าอยู่ในหน้าจอหลัก
            if event.type == pygame.MOUSEBUTTONDOWN:  # ถ้าเมาส์ถูกคลิก
                if rect_yes.collidepoint(event.pos):  # ถ้าคลิกโดนปุ่ม Yes
                    current_screen = "yes_screen"     # เปลี่ยนไปยังหน้าจอ Yes
                if rect_no.collidepoint(event.pos):   # ถ้าคลิกโดนปุ่ม No
                    # สุ่มตำแหน่งใหม่ให้ปุ่ม No (ให้มันหนี!)
                    new_x = random.randint(0, 800 - rect_no.width) #random.randintคือ
                    new_y = random.randint(0, 600 - rect_no.height)
                    rect_no.topleft = (new_x, new_y)

    # -------------------------------------------------
    # ส่วนการวาดหน้าจอ (ตาม state ปัจจุบัน)
    # -------------------------------------------------

    if current_screen == "main":
        screen.fill(Gray)     # ล้างหน้าจอด้วยสีเทา (พื้นหลัง)
        
        # สร้างข้อความ "Are you Gay ?" ด้วยฟอนต์ใหญ่ สีดำ
        message = font_big.render("Are you Gay ?", True, Black)
        
        # วางข้อความบนหน้าจอ ตำแหน่ง x = 250, y = 100
        screen.blit(message, (250, 100))
        
        # วาดปุ่ม "Yes" และ "No" ที่ตำแหน่งที่ตั้งไว้
        screen.blit(check_yes, rect_yes)
        screen.blit(check_no, rect_no)

    elif current_screen == "yes_screen": #current_screen == "yes_screen": คือ ถ้าปัจจุบันอยู่ในหน้าจอ Yes
        screen.fill(Green)    # ล้างหน้าจอด้วยสีขาว (พื้นหลังใหม่)
        
        # สร้างข้อความใหม่ว่า "You clicked YES!" สีดำ
        message = font_big.render("Welcome My Game", True, Black)
        
        # วางข้อความไว้ตรงกลางประมาณ (x=200, y=250)
        screen.blit(message, (200, 250))
        
        

    # อัปเดตการแสดงผลทุกอย่างบนหน้าจอ
    pygame.display.update()

# ออกจาก pygame เมื่อปิดหน้าต่าง
pygame.quit()
