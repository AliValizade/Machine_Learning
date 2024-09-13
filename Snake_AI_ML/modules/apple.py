import random, arcade


class Apple(arcade.Sprite):
    def __init__(self, SCREEN_WIDTH, SCREEN_HEIGHT):
        super().__init__()
        self.apple = arcade.Sprite('data/apple.png', scale=1)
        self.apple.center_x = random.randint(10, SCREEN_WIDTH-10) // 8 * 8
        self.apple.center_y = random.randint(10, SCREEN_HEIGHT-10) // 8 * 8
        self.apple.change_x = 0
        self.apple.change_y = 0
        # self.color = arcade.color.RED
        # self.radius = 8
        # self.width = 16
        # self.height = 16
        

    def draw(self):
        self.apple.draw()
        # arcade.draw_circle_filled(self.center_x, self.center_y, self.radius, self.color)