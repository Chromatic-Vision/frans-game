import json
import pygame
# import renderer

load_filename = 'font.json'
save_filename = 'font.json'

letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ !?.,<>/\\|#~@()'
letter_index = 0

SIZE = 5

try:
    with open(load_filename, 'r') as file:
        out = json.load(file)
except FileNotFoundError:
    out = {}

    for letter in letters:
        out[letter] = []
        for y in range(SIZE):
            line = []
            for x in range(SIZE):
                line.append([0, 0, 0])
            out[letter].append(line)

pygame.init()
screen = pygame.display.set_mode((800, 800))
clock = pygame.time.Clock()
run = True

pygame.display.set_caption(letters[letter_index])

try:
    while run:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    letter_index += 1

                    if letter_index < len(letters):
                        pass
                    else:
                        run = False

                    screen.fill((0, 0, 0))

                    y = 0
                    for line in out[letters[letter_index]]:
                        x = 0
                        for p in line:
                            pygame.draw.rect(screen, p, (x, y, 800 // SIZE, 800 // SIZE))
                            x += 800 // SIZE
                        y += 800 // SIZE

                    pygame.display.set_caption(letters[letter_index])

        mouse_pos = pygame.mouse.get_pos()
        mouse_press = pygame.mouse.get_pressed(5)
        x = mouse_pos[0] // (screen.get_width() // SIZE)
        y = mouse_pos[1] // (screen.get_height() // SIZE)
        if mouse_press[0]:
            out[letters[letter_index]][y][x] = [255, 255, 255]
            pygame.draw.rect(screen, (255, 255, 255), (x * (screen.get_width() // SIZE), mouse_pos[1] // (screen.get_width() // SIZE) * (screen.get_width() // SIZE), (screen.get_width() // SIZE), (screen.get_width() // SIZE)))
        if mouse_press[2]:
            # out[letters[letter_index]][mouse_pos[1] // 40][mouse_pos[0] // 40] = [0, 0, 0]
            # pygame.draw.rect(screen, (0, 0, 0), (mouse_pos[0] // 40 * 40, mouse_pos[1] // 40 * 40, 40, 40))
            out[letters[letter_index]][y][x] = [0, 0, 0]
            pygame.draw.rect(screen, (0, 0, 0), (x * (screen.get_width() // SIZE),
                                                       mouse_pos[1] // (screen.get_width() // SIZE) * (
                                                                   screen.get_width() // SIZE),
                                                       (screen.get_width() // SIZE), (screen.get_width() // SIZE)))

        pygame.display.update()
except Exception:
    with open(save_filename, 'w') as file:
        json.dump(out, file)

pygame.quit()

with open(save_filename, 'w') as file:
    json.dump(out, file)
