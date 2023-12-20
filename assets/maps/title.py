import pygame
import os.path


s = pygame.image.load(os.path.join('assets', 'tiles', 'misc', 'title.bmp'))

cursor_y = 0


def overlay(screen: pygame.Surface):
    screen.blit(s, (0, 0))

    x = 40
    y = 9
    size = 4
    pygame.draw.polygon(screen, (255, 255, 255),
                        [
                            (x, cursor_y * size + size // 2 + y),
                            (x + size // 2, cursor_y * size + y),
                            (x + size, cursor_y * size + size // 2 + y),
                            (x + size // 2, (cursor_y + 1) * size + y),
                        ])

    game.text_renderer.render(screen, (6, 1, 40, y + 40), "Commencer")
    game.text_renderer.render(screen, (6, 2, 40, y + 40), "Continuer")
    game.text_renderer.render(screen, (6, 3, 40, y + 40), "Quitter")

    # pygame.draw.rect(screen, (255, 255, 255), (0, cursor_y * 10, 10, 10))


def key_pressed(event):
    global cursor_y
    if (event.key == pygame.K_s or event.key == pygame.K_DOWN) and cursor_y < 4:
        cursor_y += 2
    if (event.key == pygame.K_w or event.key == pygame.K_UP) and cursor_y > 0:
        cursor_y -= 2


event(Event.OVERLAY, overlay)
event(Event.KEYDOWN, key_pressed)