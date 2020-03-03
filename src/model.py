from random import randint
import pygame
from interface import display
from constants import WEAPONS_LIST, MAX_NUMBER_ITEM, Y_SIZE, X_SIZE
from player import Player


class Game:
    pygame.font.init()

    def __init__(self):
        pygame.init()
        self.matrix = [
            [None for x in range(0, X_SIZE)]
            for y in range(0, Y_SIZE)
        ]
        self.player = Player(self)
        self.player_position = None
        self.old_player_position = (0, 0)
        self.load_file()
        self.load_items()
        self.message = ""
        self.message_win = ""
        self.message_item = ""
        self.running = True
        self.start()

    def start(self):
        clock = pygame.time.Clock()
        pygame.init()
        while True:
            clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    pygame.quit()
                    quit()
                elif event.type == pygame.KEYDOWN and self.running:
                    if event.key == pygame.K_DOWN:
                        self.player.move_down()
                    elif event.key == pygame.K_UP:
                        self.player.move_up()
                    elif event.key == pygame.K_RIGHT:
                        self.player.move_right()
                    elif event.key == pygame.K_LEFT:
                        self.player.move_left()

            display(self.matrix, self.message, self.message_item,
                    self.message_win)

    def load_file(self):
        with open("maze.txt", 'r') as maze:
            for y_axe, line in enumerate(maze.readlines()):
                for x_axe, char in enumerate(line.strip()):
                    self.matrix[y_axe][x_axe] = char
                    if char == "D":
                        self.player_position = [y_axe, x_axe]

    def load_items(self):
        random_x = 0
        random_y = 0
        for art in WEAPONS_LIST:
            while self.matrix[random_y][random_x] != "-":
                random_x = randint(0, X_SIZE - 1)
                random_y = randint(0, Y_SIZE - 1)
            self.matrix[random_y][random_x] = art

    def check_maze(self, new_position):
        old_y, old_x = self.old_player_position
        y_axe, x_axe = new_position
        if x_axe < 0 or y_axe < 0 or x_axe >= X_SIZE or\
                y_axe >= Y_SIZE:
            self.player_position = [old_y, old_x]
            self.message = "can not move, try again"
        elif self.matrix[y_axe][x_axe] == "+":
            self.player_position = [old_y, old_x]
            self.message = "It's a wall, try again"
        else:
            self.message = ""

    def update_maze(self, new_position):
        old_y, old_x = self.old_player_position
        y_axe, x_axe = new_position
        self.player.collect_item(new_position)
        self.check_win()
        self.matrix[old_y][old_x] = "-"
        self.matrix[y_axe][x_axe] = "D"
        self.old_player_position = y_axe, x_axe

    def check_win(self):
        y_axe, x_axe = self.player_position
        if not self.matrix[y_axe][x_axe] == "A":
            return

        if not self.player.has_all_items():
            result = MAX_NUMBER_ITEM - self.player.list_collect
            self.message = f"you loose, you missed {result} items"
            self.running = False
        else:
            self.message_win = "YOU WIN !!!"
            self.running = False
