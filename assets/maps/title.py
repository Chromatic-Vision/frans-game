from main import game
from script import Event
import pygame
import os.path


s = pygame.image.load(os.path.join('assets', 'tiles', 'misc', 'title.bmp'))

cursor_y = 0


def overlay(screen: pygame.Surface):

    if not game.current_map_name == "title":
        return

    screen.blit(s, (0, 0))

    x = 5 * 10
    y = 9
    size = 4
    space = 2
    pygame.draw.polygon(screen, (255, 255, 255),
                        [
                            (x, cursor_y * space * size + size // 2 + y),
                            (x + size // 2, cursor_y * space * size + y),
                            (x + size, cursor_y * space * size + size // 2 + y),
                            (x + size // 2, (cursor_y * space + 1) * size + y),
                        ])

    game.text_renderer.render(screen, (7, 1, 40, 40), "Commencer")
    game.text_renderer.render(screen, (7, 2, 40, 40), "Continuer")
    game.text_renderer.render(screen, (7, 3, 40, 40), "Quitter")
    game.text_renderer.render(screen, (7, 4, 40, 40), "ÀàÂâÆæÇç\nÉéÈèÊêËë\nÎîÏïÔôŒœ\nÙùÛûÜüŸÿ")

    # pygame.draw.rect(screen, (255, 255, 255), (0, cursor_y * 10, 10, 10))


def key_pressed(event):

    if not game.current_map_name == "title":
        return

    global cursor_y

    if (event.key == pygame.K_s or event.key == pygame.K_DOWN) and cursor_y < 2:
        cursor_y += 1
    if (event.key == pygame.K_w or event.key == pygame.K_UP) and cursor_y > 0:
        cursor_y -= 1

    if event.key == pygame.K_RETURN or event.key == pygame.K_SPACE:

        if cursor_y == 0:
            game.refresh_map("test")
        elif cursor_y == 1:
            return
        elif cursor_y == 2:
            game.run = False


event(Event.OVERLAY, overlay)
event(Event.KEYDOWN, key_pressed)