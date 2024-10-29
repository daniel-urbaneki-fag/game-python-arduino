import pygame
import serial
import time

import tkinter as tk
from PIL import Image, ImageTk
import random
import os

pygame.init()
screen = pygame.display.set_mode((810, 570))
clock = pygame.time.Clock()

arduino = serial.Serial('COM1', 9600)

def jogo_bandeira():
    flags = [
        {"state": "Acre", "src": "bandeiras/acre.png"},
        {"state": "Alagoas", "src": "bandeiras/alagoas.png"},
        {"state": "Amapá", "src": "bandeiras/amapa.png"},
        {"state": "Amazonas", "src": "bandeiras/amazonas.png"},
        {"state": "Bahia", "src": "bandeiras/bahia.png"},
        {"state": "Ceará", "src": "bandeiras/ceara.png"},
        {"state": "Distrito Federal", "src": "bandeiras/distritofederal.png"},
        {"state": "Espírito Santo", "src": "bandeiras/espiritosanto.png"},
        {"state": "Goiás", "src": "bandeiras/goias.png"},
        {"state": "Maranhão", "src": "bandeiras/maranhao.png"},
        {"state": "Mato Grosso", "src": "bandeiras/matogrosso.png"},
        {"state": "Mato Grosso do Sul", "src": "bandeiras/matogrossosul.png"},
        {"state": "Minas Gerais", "src": "bandeiras/minasgerais.png"},
        {"state": "Pará", "src": "bandeiras/para.png"},
        {"state": "Paraíba", "src": "bandeiras/paraiba.png"},
        {"state": "Paraná", "src": "bandeiras/parana.png"},
        {"state": "Pernambuco", "src": "bandeiras/pernambuco.png"},
        {"state": "Piauí", "src": "bandeiras/piaui.png"},
        {"state": "Rio de Janeiro", "src": "bandeiras/riodejaneiro.png"},
        {"state": "Rio Grande do Sul", "src": "bandeiras/riograndedosul.png"},
        {"state": "Rio Grande do Norte", "src": "bandeiras/riograndenorte.png"},
        {"state": "Rondônia", "src": "bandeiras/rondonia.png"},
        {"state": "Roraima", "src": "bandeiras/roraima.png"},
        {"state": "Santa Catarina", "src": "bandeiras/santacatarina.png"},
        {"state": "São Paulo", "src": "bandeiras/saopaulo.png"},
        {"state": "Sergipe", "src": "bandeiras/sergipe.png"},
        {"state": "Tocantins", "src": "bandeiras/tocantins.png"},
    ]

    current_flag_index = 0
    score = 0
    WINNING_SCORE = 270

    def shuffle(array):
        random.shuffle(array)

    def load_flag():
        nonlocal current_flag_index
        if score >= WINNING_SCORE:
            end_game()
            return
        
        flag = flags[current_flag_index]
        
        img = Image.open(flag["src"])
        img = img.resize((300, 200), Image.Resampling.LANCZOS)
        img_tk = ImageTk.PhotoImage(img)
        
        flag_label.config(image=img_tk)
        flag_label.image = img_tk

        other_states = [f["state"] for f in flags if f["state"] != flag["state"]]
        random_states = random.sample(other_states, 3)
        options = [flag["state"]] + random_states
        random.shuffle(options)

        option1.config(text=options[0])
        option2.config(text=options[1])
        option3.config(text=options[2])
        option4.config(text=options[3])

    def check_answer(selected_option):
        nonlocal current_flag_index, score
        correct_state = flags[current_flag_index]["state"]
        
        if selected_option == correct_state:
            result_label.config(text="Acertou! Parabéns")
            score += 10
            score_label.config(text=f"Pontuação: {score}")
        else:
            result_label.config(text="Errado! Vamos para a próxima.")
        
        current_flag_index = (current_flag_index + 1) % len(flags)
        window.after(1500, load_flag)

    def end_game():
        result_label.config(text="Parabéns, você venceu!")
        restart_button.pack()

    def restart_game():
        nonlocal score, current_flag_index
        score = 0
        current_flag_index = 0
        score_label.config(text=f"Pontuação: {score}")
        shuffle(flags)
        load_flag()
        result_label.config(text="")
        restart_button.pack_forget()

    def set_background():
        image_path = os.path.join(os.path.dirname(__file__), "Bandeira_Nacional.png")
        bg_image = Image.open(image_path)
        bg_image = bg_image.resize((1366, 768), Image.Resampling.LANCZOS)
        bg_photo = ImageTk.PhotoImage(bg_image)

        bg_label = tk.Label(window, image=bg_photo)
        bg_label.image = bg_photo
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)

    # Configuração da janela
    window = tk.Tk()
    window.title("Jogo de Bandeiras do Brasil")
    window.geometry("1366x768")

    set_background()

    flag_label = tk.Label(window)
    flag_label.pack(pady=20)

    option1 = tk.Button(window, text="", width=20, command=lambda: check_answer(option1["text"]))
    option1.pack(pady=5)

    option2 = tk.Button(window, text="", width=20, command=lambda: check_answer(option2["text"]))
    option2.pack(pady=5)

    option3 = tk.Button(window, text="", width=20, command=lambda: check_answer(option3["text"]))
    option3.pack(pady=5)

    option4 = tk.Button(window, text="", width=20, command=lambda: check_answer(option4["text"]))
    option4.pack(pady=5)

    result_label = tk.Label(window, text="", font=("Arial", 24), fg="blue")
    result_label.pack(pady=20)

    score_label = tk.Label(window, text=f"Pontuação: {score}", font=("Arial", 24))
    score_label.pack(pady=20)

    restart_button = tk.Button(window, text="Reiniciar Jogo", command=restart_game)
    restart_button.pack_forget()

    shuffle(flags)
    load_flag()

    window.mainloop()

def jogo_labirinto():
    start_ticks = pygame.time.get_ticks()
    fontTime = pygame.font.Font(None, 36)

    finish_time = None

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

    def check_finish(x, y, radius, area_finish):
        ball_rect = pygame.Rect(x - radius, y - radius, radius * 2, radius * 2)
        if ball_rect.colliderect(area_finish):
            return True
        return False

    running = True
    game_over = False
    finish_game = False

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        if not game_over and not finish_game:
            data = arduino.readline().decode('utf-8').strip()
            if data:
                try:
                    print(data.split())
                    xValue, yValue, _ = data.split()
                    xValue = int(xValue.split(":")[1])
                    yValue = int(yValue.split(":")[1])
                    x += (xValue - 507) // 50
                    y += (yValue - 505) // 50
                except ValueError:
                    pass
            
            screen.fill((0, 0, 0))

            seconds = (pygame.time.get_ticks() - start_ticks) // 1000
            time_text = fontTime.render(f"Tempo: {seconds}s", True, (255, 255, 255))
            screen.blit(time_text, (20, 20))

            for wall in walls:
                pygame.draw.rect(screen, (255, 255, 255), wall)

            area_finish = pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(730, 90, 70, 70))

            pygame.draw.circle(screen, (255, 0, 0), (x, y), radius)

            if check_collision(x, y, radius, walls):
                game_over = True
            
            if check_finish(x, y, radius, area_finish):
                finish_game = True

        elif finish_game and not game_over:
            if finish_time is None:
                finish_time = (pygame.time.get_ticks() - start_ticks) // 1000

            font = pygame.font.Font(None, 74)
            text = font.render("Você ganhou !!!", True, (0, 255, 0))
            screen.blit(text, (250, 250))

            time_text = font.render(f"Tempo: {finish_time}s", True, (0, 255, 0))
            screen.blit(time_text, (250, 300))

        else:
            font = pygame.font.Font(None, 74)
            text = font.render("Game Over", True, (255, 0, 0))
            screen.blit(text, (250, 250))

        pygame.display.flip()
        clock.tick(60)

font = pygame.font.Font(None, 74)

buttons = ["Jogo da Bandeira", "Jogo Labirinto"]
selected_button = 0

running = True
while running:
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    data = arduino.readline().decode('utf-8').strip()
    try:
        xValue, yValue, button = data.split()

        buttonPress = int(button.split(":")[1])
        y = int(yValue.split(":")[1])

        print(y)

        if y > 900:
            selected_button = (selected_button + 1) % len(buttons)

        elif y < 100:
            selected_button = (selected_button - 1) % len(buttons)
        
        if buttonPress == 0:
            if selected_button == 0:
                jogo_bandeira()
                running = False
            elif selected_button == 1:
                jogo_labirinto()
                running = False
    except ValueError:
        pass
    
    # Renderização dos botões
    for i, text in enumerate(buttons):
        color = (255, 0, 0) if i == selected_button else (255, 255, 255)
        button_text = font.render(text, True, color)
        screen.blit(button_text, (200, 200 + i * 100))
    
    pygame.display.flip()
    clock.tick(30)

pygame.quit()
arduino.close()