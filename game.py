import pygame
import serial

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

# arduino = serial.Serial('COM3', 9600)

x, y = 40, 35
radius = 10

walls = [
    # x, y, largura, altura
    pygame.Rect(0, 0, 800, 10),   # Parede superior
    pygame.Rect(0, 0, 10, 600),   # Parede esquerda
    pygame.Rect(0, 590, 800, 10), # Parede inferior
    pygame.Rect(790, 0, 10, 600), # Parede direita

    pygame.Rect(70, 0, 10, 190),
    pygame.Rect(70, 260, 10, 330),
    pygame.Rect(70, 190, 70, 10),
    pygame.Rect(140, 70, 10, 290),
    pygame.Rect(210, 70, 10, 290),
    pygame.Rect(280, 70, 10, 290),
]

def check_collision(x, y, radius, walls):
    ball_rect = pygame.Rect(x - radius, y - radius, radius * 2, radius * 2)
    for wall in walls:
        if ball_rect.colliderect(wall):
            return True
    return False

running = True
game_over = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if not game_over:
        # data = arduino.readline().decode('utf-8').strip()
        # if data:
        #     try:
        #         print(data.split())
        #         xValue, yValue, _ = data.split()
        #         xValue = int(xValue.split(":")[1])
        #         yValue = int(yValue.split(":")[1])

        #         x += (xValue - 507) // 50
        #         y += (yValue - 505) // 50

        #     except ValueError:
        #         pass

        screen.fill((0, 0, 0))

        for wall in walls:
            pygame.draw.rect(screen, (255, 255, 255), wall)

        pygame.draw.circle(screen, (255, 0, 0), (x, y), radius)

        if check_collision(x, y, radius, walls):
            game_over = True

    else:
        font = pygame.font.Font(None, 74)
        text = font.render("Game Over", True, (255, 0, 0))
        screen.blit(text, (250, 250))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
