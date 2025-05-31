
import pygame          # นำเข้าโมดูล pygame สำหรับทำเกมหรือ GUI ง่ายๆ
import random          # ใช้สำหรับสุ่มตำแหน่งปุ่ม No ให้เปลี่ยนที่หนี

pygame.init()          # เริ่มต้นใช้งาน pygame

# ตั้งชื่อหน้าต่างของเกม/แอป
pygame.display.set_caption("You are Gay ?")

# สร้างหน้าจอขนาด 800x600 พิกเซล
screen = pygame.display.set_mode((800, 600))

# กำหนดค่าสี RGB
White = (255, 255, 255)
Gray = (128, 128, 128)
Black = (0, 0, 0)
Green = (0, 255, 0)
Red = (255, 0, 0)

# โหลดฟอนต์ขนาดใหญ่-เล็ก จากไฟล์
font_big = pygame.font.Font("Font/Coiny.ttf", 50)
font_small = pygame.font.Font("Font/Coiny.ttf", 30)

# โหลดรูปภาพปุ่ม "Yes", "No", และ "Play"
check_yes = pygame.image.load("image/yes.png")
check_no = pygame.image.load("image/no.png")
play = pygame.image.load("image/playy.webp")

# ปรับขนาดภาพให้เหมาะสม
check_yes = pygame.transform.scale(check_yes, (190, 100))
check_no = pygame.transform.scale(check_no, (200, 100))
play = pygame.transform.scale(play, (150, 150))

# สร้างกล่องสี่เหลี่ยม (Rect) สำหรับตรวจจับตำแหน่งของแต่ละปุ่ม
rect_yes = check_yes.get_rect()
rect_no = check_no.get_rect()
rect_play = play.get_rect()  # สำหรับปุ่ม Play

# กำหนดตำแหน่งเริ่มต้นของปุ่มบนหน้าจอ
rect_yes.topleft = (150, 250)
rect_no.topleft = (450, 250)
rect_play.topleft = (350, 350)  # วางปุ่ม Play ในหน้าจอ yes_screen

# ตัวแปรควบคุมว่าอยู่หน้าจอไหน (main, yes_screen, game)
current_screen = "main"

# ตัวแปรควบคุมลูปหลักของเกม/โปรแกรม
running = True

# ลูปหลักของเกม
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # ถ้าปิดหน้าต่าง
            running = False

        # -------------------------------
        # ตรวจจับคลิกในหน้าจอหลัก
        # -------------------------------
        if current_screen == "main":
            if event.type == pygame.MOUSEBUTTONDOWN:
                if rect_yes.collidepoint(event.pos):  # คลิกปุ่ม Yes
                    current_screen = "yes_screen"     # ไปหน้าจอใหม่
                if rect_no.collidepoint(event.pos):   # คลิกปุ่ม No
                    # สุ่มตำแหน่งใหม่ให้ปุ่ม No หนีไป
                    new_x = random.randint(0, 800 - rect_no.width)
                    new_y = random.randint(0, 600 - rect_no.height)
                    rect_no.topleft = (new_x, new_y)

        # -------------------------------
        # ตรวจจับคลิกในหน้าจอ Yes
        # -------------------------------
        elif current_screen == "yes_screen":
            if event.type == pygame.MOUSEBUTTONDOWN:
                if rect_play.collidepoint(event.pos):  # ถ้าคลิกปุ่ม Play
                    print("Play button clicked!")      # แสดงข้อความใน console
                    current_screen = "game"            # ไปยังหน้าจอเกม

    # -------------------------------
    # แสดงผลหน้าจอตามสถานะ
    # -------------------------------
    if current_screen == "main":
        screen.fill(Gray)  # พื้นหลังสีเทา
        message = font_big.render("Are you Gay ?", True, Black)  # ข้อความคำถาม
        screen.blit(message, (250, 100))  # วางข้อความ
        screen.blit(check_yes, rect_yes)  # วางปุ่ม Yes
        screen.blit(check_no, rect_no)    # วางปุ่ม No

    elif current_screen == "yes_screen":
        screen.fill(Black)  # พื้นหลังสีดำ
        message = font_big.render("Welcome My Game", True, White)  # ข้อความต้อนรับ
        screen.blit(message, (200, 250))  # วางข้อความ
        screen.blit(play, rect_play)      # วางปุ่ม Play

    elif current_screen == "game":
        import start_game
        start_game() # เรียกใช้งานฟังก์ชัน start_game ,เข้าเกม




    # อัปเดตหน้าจอทุกเฟรม
    pygame.display.update()

# ออกจาก pygame
pygame.quit()
