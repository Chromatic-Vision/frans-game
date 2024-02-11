from main import game
from script import Event
import pygame
import os.path
from game import TILE_SIZE


s = pygame.image.load(os.path.join('assets', 'tiles', 'misc', 'title.bmp'))

cursor_y = 0


def overlay(screen: pygame.Surface):
    if not game.current_map_name == "title":
        game.unregister_event(overlay_id)
        return

    screen.blit(s, (0, 0))

    x = 5 * TILE_SIZE
    y = 9
    size = 4
    text_size = 8
    space = 2
    pygame.draw.polygon(screen, (255, 255, 255),
                        [
                            (x, cursor_y * space * size + size // 2 + y),
                            (x + size // 2, cursor_y * space * size + y),
                            (x + size, cursor_y * space * size + size // 2 + y),
                            (x + size // 2, (cursor_y * space + 1) * size + y),
                        ])

    game.text_renderer.render(screen, (7 * text_size, 1 * text_size, 1000, 40), "Commencer")
    game.text_renderer.render(screen, (7 * text_size, 2 * text_size, 1000, 40), "Continuer")
    game.text_renderer.render(screen, (7 * text_size, 3 * text_size, 1000, 40), "Quitter")
    # game.text_renderer.render(screen, (7 * text_size, 4 * text_size, 1000, 40), "ÀàÂâÆæÇç\nÉéÈèÊêËë\nÎîÏïÔôŒœ\nÙùÛûÜüŸÿ")

    # pygame.draw.rect(screen, (255, 255, 255), (0, cursor_y * 10, 10, 10))


def key_pressed(event):

    if not game.current_map_name == "title":
        game.unregister_event(key_pressed_id)
        return

    global cursor_y

    if (event.key == pygame.K_s or event.key == pygame.K_DOWN) and cursor_y < 2:
        cursor_y += 1
    if (event.key == pygame.K_w or event.key == pygame.K_UP) and cursor_y > 0:
        cursor_y -= 1

    if event.key == pygame.K_RETURN or event.key == pygame.K_SPACE:

        if cursor_y == 0:
            game.refresh_map("house")
            game.player.y += TILE_SIZE * 3
        elif cursor_y == 1:
            return
        elif cursor_y == 2:
            game.run = False


overlay_id = game.register_event(Event.OVERLAY, overlay)
key_pressed_id = game.register_event(Event.KEYDOWN, key_pressed)
