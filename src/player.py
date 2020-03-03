from constants import MAX_NUMBER_ITEM, WEAPONS_LIST


class Player:

    def __init__(self, game):
        self.game = game
        self.list_collect = 0

    def move_up(self):
        self.game.player_position[0] -= 1
        self.game.check_maze(self.game.player_position)
        self.game.update_maze(self.game.player_position)

    def move_down(self):
        self.game.player_position[0] += 1
        self.game.check_maze(self.game.player_position)
        self.game.update_maze(self.game.player_position)

    def move_left(self):
        self.game.player_position[1] -= 1
        self.game.check_maze(self.game.player_position)
        self.game.update_maze(self.game.player_position)

    def move_right(self):
        self.game.player_position[1] += 1
        self.game.check_maze(self.game.player_position)
        self.game.update_maze(self.game.player_position)

    def has_all_items(self):
        return self.list_collect == MAX_NUMBER_ITEM

    def collect_item(self, position_items):
        y_axe, x_axe = position_items
        if self.game.matrix[y_axe][x_axe] in WEAPONS_LIST:
            self.list_collect += 1
            self.game.matrix[y_axe][x_axe] = "-"
        self.game.message_item = f"You have got {self.list_collect}"
