import pygame
import serial

pygame.init()
screen = pygame.display.set_mode((810, 570))
clock = pygame.time.Clock()

# arduino = serial.Serial('COM3', 9600)

x, y = 40, 35
radius = 10

gap = 80  # Espaçamento entre as paredes
wall_thickness = 10  # Espessura das paredes
wall_height = 80  # Altura das paredes horizontais
wall_length = 80  # Comprimento das paredes horizontais

walls = [
    # Paredes externas (bordas da tela)
    pygame.Rect(0, 0, 810, wall_thickness),  # Parede superior
    pygame.Rect(0, 0, wall_thickness, 570),  # Parede esquerda
    pygame.Rect(0, 570 - wall_thickness, 810, wall_thickness),  # Parede inferior
    pygame.Rect(810 - wall_thickness, 0, wall_thickness, 570),  # Parede direita

    # pygame.Rect(1 * gap, wall_thickness, wall_thickness, wall_height),
    pygame.Rect(2 * gap, wall_thickness, wall_thickness, wall_height),
    # pygame.Rect(3 * gap, wall_thickness, wall_thickness, wall_height),
    pygame.Rect(4 * gap, wall_thickness, wall_thickness, wall_height),
    # pygame.Rect(5 * gap, wall_thickness, wall_thickness, wall_height),
    # pygame.Rect(6 * gap, wall_thickness, wall_thickness, wall_height),
    pygame.Rect(7 * gap, wall_thickness, wall_thickness, wall_height),
    # pygame.Rect(8 * gap, wall_thickness, wall_thickness, wall_height),
    # pygame.Rect(9 * gap, wall_thickness, wall_thickness, wall_height),
    pygame.Rect(10 * gap, wall_thickness, wall_thickness, wall_height),

    pygame.Rect(1 * gap, wall_thickness + wall_height, wall_thickness, wall_height),
    # pygame.Rect(2 * gap, wall_thickness + wall_height, wall_thickness, wall_height),
    # pygame.Rect(3 * gap, wall_thickness + wall_height, wall_thickness, wall_height),
    pygame.Rect(4 * gap, wall_thickness + wall_height, wall_thickness, wall_height),
    pygame.Rect(5 * gap, wall_thickness + wall_height, wall_thickness, wall_height),
    pygame.Rect(6 * gap, wall_thickness + wall_height, wall_thickness, wall_height),
    # pygame.Rect(7 * gap, wall_thickness + wall_height, wall_thickness, wall_height),
    # pygame.Rect(8 * gap, wall_thickness + wall_height, wall_thickness, wall_height),
    pygame.Rect(9 * gap, wall_thickness + wall_height, wall_thickness, wall_height),
    pygame.Rect(10 * gap, wall_thickness + wall_height, wall_thickness, wall_height),

    pygame.Rect(1 * gap, wall_thickness + ( 2 * wall_height), wall_thickness, wall_height),
    # pygame.Rect(2 * gap, wall_thickness + ( 2 * wall_height), wall_thickness, wall_height),
    # pygame.Rect(3 * gap, wall_thickness + ( 2 * wall_height), wall_thickness, wall_height),
    pygame.Rect(4 * gap, wall_thickness + ( 2 * wall_height), wall_thickness, wall_height),
    pygame.Rect(5 * gap, wall_thickness + ( 2 * wall_height), wall_thickness, wall_height),
    # pygame.Rect(6 * gap, wall_thickness + ( 2 * wall_height), wall_thickness, wall_height),
    # pygame.Rect(7 * gap, wall_thickness + ( 2 * wall_height), wall_thickness, wall_height),
    pygame.Rect(8 * gap, wall_thickness + ( 2 * wall_height), wall_thickness, wall_height),
    pygame.Rect(9 * gap, wall_thickness + ( 2 * wall_height), wall_thickness, wall_height),
    pygame.Rect(10 * gap, wall_thickness + ( 2 * wall_height), wall_thickness, wall_height),

    pygame.Rect(1 * gap, wall_thickness + ( 3 * wall_height), wall_thickness, wall_height),
    # pygame.Rect(2 * gap, wall_thickness + ( 3 * wall_height), wall_thickness, wall_height),
    # pygame.Rect(3 * gap, wall_thickness + ( 3 * wall_height), wall_thickness, wall_height),
    pygame.Rect(4 * gap, wall_thickness + ( 3 * wall_height), wall_thickness, wall_height),
    # pygame.Rect(5 * gap, wall_thickness + ( 3 * wall_height), wall_thickness, wall_height),
    # pygame.Rect(6 * gap, wall_thickness + ( 3 * wall_height), wall_thickness, wall_height),
    # pygame.Rect(7 * gap, wall_thickness + ( 3 * wall_height), wall_thickness, wall_height),
    # pygame.Rect(8 * gap, wall_thickness + ( 3 * wall_height), wall_thickness, wall_height),
    pygame.Rect(9 * gap, wall_thickness + ( 3 * wall_height), wall_thickness, wall_height),
    pygame.Rect(10 * gap, wall_thickness + ( 3 * wall_height), wall_thickness, wall_height),

    # pygame.Rect(1 * gap, wall_thickness + ( 4 * wall_height), wall_thickness, wall_height),
    # pygame.Rect(2 * gap, wall_thickness + ( 4 * wall_height), wall_thickness, wall_height),
    pygame.Rect(3 * gap, wall_thickness + ( 4 * wall_height), wall_thickness, wall_height),
    pygame.Rect(4 * gap, wall_thickness + ( 4 * wall_height), wall_thickness, wall_height),
    # pygame.Rect(5 * gap, wall_thickness + ( 4 * wall_height), wall_thickness, wall_height),
    pygame.Rect(6 * gap, wall_thickness + ( 4 * wall_height), wall_thickness, wall_height),
    pygame.Rect(7 * gap, wall_thickness + ( 4 * wall_height), wall_thickness, wall_height),
    pygame.Rect(8 * gap, wall_thickness + ( 4 * wall_height), wall_thickness, wall_height),
    # pygame.Rect(9 * gap, wall_thickness + ( 4 * wall_height), wall_thickness, wall_height),
    pygame.Rect(10 * gap, wall_thickness + ( 4 * wall_height), wall_thickness, wall_height),

    # pygame.Rect(1 * gap, wall_thickness + ( 5 * wall_height), wall_thickness, wall_height),
    # pygame.Rect(2 * gap, wall_thickness + ( 5 * wall_height), wall_thickness, wall_height),
    pygame.Rect(3 * gap, wall_thickness + ( 5 * wall_height), wall_thickness, wall_height),
    # pygame.Rect(4 * gap, wall_thickness + ( 5 * wall_height), wall_thickness, wall_height),
    # pygame.Rect(5 * gap, wall_thickness + ( 5 * wall_height), wall_thickness, wall_height),
    # pygame.Rect(6 * gap, wall_thickness + ( 5 * wall_height), wall_thickness, wall_height),
    pygame.Rect(7 * gap, wall_thickness + ( 5 * wall_height), wall_thickness, wall_height),
    # pygame.Rect(8 * gap, wall_thickness + ( 5 * wall_height), wall_thickness, wall_height),
    pygame.Rect(9 * gap, wall_thickness + ( 5 * wall_height), wall_thickness, wall_height),
    pygame.Rect(10 * gap, wall_thickness + ( 5 * wall_height), wall_thickness, wall_height),

    pygame.Rect(1 * gap, wall_thickness + ( 6 * wall_height), wall_thickness, wall_height),
    # pygame.Rect(2 * gap, wall_thickness + ( 6 * wall_height), wall_thickness, wall_height),
    # pygame.Rect(3 * gap, wall_thickness + ( 6 * wall_height), wall_thickness, wall_height),
    pygame.Rect(4 * gap, wall_thickness + ( 6 * wall_height), wall_thickness, wall_height),
    # pygame.Rect(5 * gap, wall_thickness + ( 6 * wall_height), wall_thickness, wall_height),
    # pygame.Rect(6 * gap, wall_thickness + ( 6 * wall_height), wall_thickness, wall_height),
    # pygame.Rect(7 * gap, wall_thickness + ( 6 * wall_height), wall_thickness, wall_height),
    # pygame.Rect(8 * gap, wall_thickness + ( 6 * wall_height), wall_thickness, wall_height),
    pygame.Rect(9 * gap, wall_thickness + ( 6 * wall_height), wall_thickness, wall_height),
    pygame.Rect(10 * gap, wall_thickness + ( 6 * wall_height), wall_thickness, wall_height),


# Plataformas horizontais
    

    # pygame.Rect(wall_thickness, 1 * gap, wall_length, wall_thickness),
    pygame.Rect(wall_thickness, 2 * gap, wall_length, wall_thickness),
    # pygame.Rect(wall_thickness, 3 * gap, wall_length, wall_thickness),
    # pygame.Rect(wall_thickness, 4 * gap, wall_length, wall_thickness),
    pygame.Rect(wall_thickness, 5 * gap, wall_length, wall_thickness),
    # pygame.Rect(wall_thickness, 6 * gap, wall_length, wall_thickness),

    # pygame.Rect(wall_thickness + ( 1 * wall_length), 1 * gap, wall_length, wall_thickness),
    # pygame.Rect(wall_thickness + ( 1 * wall_length), 2 * gap, wall_length, wall_thickness),
    pygame.Rect(wall_thickness + ( 1 * wall_length), 3 * gap, wall_length, wall_thickness),
    # pygame.Rect(wall_thickness + ( 1 * wall_length), 4 * gap, wall_length, wall_thickness),
    pygame.Rect(wall_thickness + ( 1 * wall_length), 5 * gap, wall_length, wall_thickness),
    # pygame.Rect(wall_thickness + ( 1 * wall_length), 6 * gap, wall_length, wall_thickness),

    pygame.Rect(wall_thickness + ( 2 * wall_length), 1 * gap, wall_length, wall_thickness),
    pygame.Rect(wall_thickness + ( 2 * wall_length), 2 * gap, wall_length, wall_thickness),
    pygame.Rect(wall_thickness + ( 2 * wall_length), 3 * gap, wall_length, wall_thickness),
    pygame.Rect(wall_thickness + ( 2 * wall_length), 4 * gap, wall_length, wall_thickness),
    pygame.Rect(wall_thickness + ( 2 * wall_length), 5 * gap, wall_length, wall_thickness),
    pygame.Rect(wall_thickness + ( 2 * wall_length), 6 * gap, wall_length, wall_thickness),

    # pygame.Rect(wall_thickness + ( 3 * wall_length), 1 * gap, wall_length, wall_thickness),
    pygame.Rect(wall_thickness + ( 3 * wall_length), 2 * gap, wall_length, wall_thickness),
    # pygame.Rect(wall_thickness + ( 3 * wall_length), 3 * gap, wall_length, wall_thickness),
    # pygame.Rect(wall_thickness + ( 3 * wall_length), 4 * gap, wall_length, wall_thickness),
    # pygame.Rect(wall_thickness + ( 3 * wall_length), 5 * gap, wall_length, wall_thickness),
    # pygame.Rect(wall_thickness + ( 3 * wall_length), 6 * gap, wall_length, wall_thickness),

    # pygame.Rect(wall_thickness + ( 4 * wall_length), 1 * gap, wall_length, wall_thickness),
    # pygame.Rect(wall_thickness + ( 4 * wall_length), 2 * gap, wall_length, wall_thickness),
    # pygame.Rect(wall_thickness + ( 4 * wall_length), 3 * gap, wall_length, wall_thickness),
    # pygame.Rect(wall_thickness + ( 4 * wall_length), 4 * gap, wall_length, wall_thickness),
    pygame.Rect(wall_thickness + ( 4 * wall_length), 5 * gap, wall_length, wall_thickness),
    pygame.Rect(wall_thickness + ( 4 * wall_length), 6 * gap, wall_length, wall_thickness),

    # pygame.Rect(wall_thickness + (5 * wall_length), 1 * gap, wall_length, wall_thickness),
    # pygame.Rect(wall_thickness + (5 * wall_length), 2 * gap, wall_length, wall_thickness),
    pygame.Rect(wall_thickness + (5 * wall_length), 3 * gap, wall_length, wall_thickness),
    pygame.Rect(wall_thickness + (5 * wall_length), 4 * gap, wall_length, wall_thickness),
    pygame.Rect(wall_thickness + (5 * wall_length), 5 * gap, wall_length, wall_thickness),
    # pygame.Rect(wall_thickness + (5 * wall_length), 6 * gap, wall_length, wall_thickness),

    pygame.Rect(wall_thickness + (6 * wall_length), 1 * gap, wall_length, wall_thickness),
    pygame.Rect(wall_thickness + (6 * wall_length), 2 * gap, wall_length, wall_thickness),
    pygame.Rect(wall_thickness + (6 * wall_length), 3 * gap, wall_length, wall_thickness),
    # pygame.Rect(wall_thickness + (6 * wall_length), 4 * gap, wall_length, wall_thickness),
    # pygame.Rect(wall_thickness + (6 * wall_length), 5 * gap, wall_length, wall_thickness),
    pygame.Rect(wall_thickness + (6 * wall_length), 6 * gap, wall_length, wall_thickness),

    pygame.Rect(wall_thickness + (7 * wall_length), 1 * gap, wall_length, wall_thickness),
    pygame.Rect(wall_thickness + (7 * wall_length), 2 * gap, wall_length, wall_thickness),
    pygame.Rect(wall_thickness + (7 * wall_length), 3 * gap, wall_length, wall_thickness),
    pygame.Rect(wall_thickness + (7 * wall_length), 4 * gap, wall_length, wall_thickness),
    # pygame.Rect(wall_thickness + (7 * wall_length), 5 * gap, wall_length, wall_thickness),
    pygame.Rect(wall_thickness + (7 * wall_length), 6 * gap, wall_length, wall_thickness),

    # pygame.Rect(wall_thickness + (8 * wall_length), 1 * gap, wall_length, wall_thickness),
    # pygame.Rect(wall_thickness + (8 * wall_length), 2 * gap, wall_length, wall_thickness),
    # pygame.Rect(wall_thickness + (8 * wall_length), 3 * gap, wall_length, wall_thickness),
    pygame.Rect(wall_thickness + (8 * wall_length), 4 * gap, wall_length, wall_thickness),
    # pygame.Rect(wall_thickness + (8 * wall_length), 5 * gap, wall_length, wall_thickness),
    # pygame.Rect(wall_thickness + (8 * wall_length), 6 * gap, wall_length, wall_thickness),

    # pygame.Rect(wall_thickness + (9 * wall_length), 1 * gap, wall_length, wall_thickness),
    pygame.Rect(wall_thickness + (9 * wall_length), 2 * gap, wall_length, wall_thickness),
    # pygame.Rect(wall_thickness + (9 * wall_length), 3 * gap, wall_length, wall_thickness),
    # pygame.Rect(wall_thickness + (9 * wall_length), 4 * gap, wall_length, wall_thickness),
    # pygame.Rect(wall_thickness + (9 * wall_length), 5 * gap, wall_length, wall_thickness),
    # pygame.Rect(wall_thickness + (9 * wall_length), 6 * gap, wall_length, wall_thickness),
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
