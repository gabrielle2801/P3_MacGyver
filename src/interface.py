import pygame
from constants import SPRITES_COLUMMS, SPRITES_LINES, sprite_size, Y_SIZE, \
    X_SIZE
# from model import Game


pygame.init()
window_title = "Save MacGyver"
pygame.display.set_caption(window_title)
windows_surface = (SPRITES_COLUMMS, SPRITES_LINES)
window = pygame.display.set_mode(windows_surface)
rect_window = window.get_rect()


IMAGE_REF = {"floor": "ressource/Floor.png",
             "wall": "ressource/Wall4.png",
             "player": "ressource/MacGyver.png",
             "guardian": "ressource/Gardien.png",
             "needle": "ressource/aiguille.png",
             "pipe": "ressource/tube_plastique.png",
             "ether": "ressource/ether.png"
             }


def load_image(image):
    return pygame.transform.scale(
        pygame.image.load(image), (sprite_size, sprite_size)).convert()


def display(matrix, message, message_item, message_win):
    window.fill((31, 49, 52))
    for i in range(Y_SIZE):
        for j in range(X_SIZE):
            if matrix[i][j] == '+':
                window.blit(load_image(
                    IMAGE_REF["wall"]), (j * sprite_size,
                                         (i + 1) * sprite_size))
            elif matrix[i][j] == '-':
                window.blit(load_image(
                    IMAGE_REF["floor"]), (j * sprite_size,
                                          (i + 1) * sprite_size))
            elif matrix[i][j] == 'D':
                window.blit(load_image(
                    IMAGE_REF["player"]), (j * sprite_size,
                                           (i + 1) * sprite_size))
            elif matrix[i][j] == 'A':
                window.blit(load_image(
                    IMAGE_REF["guardian"]), (j * sprite_size,
                                             (i + 1) * sprite_size))
            elif matrix[i][j] == 'needle':
                window.blit(load_image(
                    IMAGE_REF["needle"]), (j * sprite_size,
                                           (i + 1) * sprite_size))
            elif matrix[i][j] == 'plastic_tube':
                window.blit(load_image(
                    IMAGE_REF["pipe"]), (j * sprite_size,
                                         (i + 1) * sprite_size))
            elif matrix[i][j] == 'ether':
                window.blit(load_image(
                    IMAGE_REF["ether"]), (j * sprite_size,
                                          (i + 1) * sprite_size))

    font = pygame.font.SysFont("helvetica.ttc", 20)
    message = font.render(
        message, True, pygame.Color("#FFFFFF"))
    message_rect = message.get_rect()
    message_rect.bottom = rect_window.bottom
    window.blit(message, message_rect)

    font_item = pygame.font.SysFont("helvetica.ttc", 20)
    message_item = font_item.render(
        message_item, True, pygame.Color("#FFFFFF"))
    message_rect = message.get_rect()
    message_rect.left = rect_window.left
    window.blit(message_item, message_rect)

    font_win = pygame.font.SysFont("helvetica bold.ttc", 60)
    message_win = font_win.render(
        message_win, True, pygame.Color("#FFFFFF"))
    message_rect = message_win.get_rect()
    message_rect.center = rect_window.center
    window.blit(message_win, message_rect)
    # window.fill((31, 49, 52, 0), special_flags=pygame.BLEND_RGBA_MULT)
    pygame.display.flip()
