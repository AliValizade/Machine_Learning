import random, arcade


class Apple(arcade.Sprite):
    def __init__(self, SCREEN_WIDTH, SCREEN_HEIGHT):
        super().__init__()
        self.apple = arcade.Sprite('data/apple.png', scale=1)
        self.apple.center_x = random.randint(10, SCREEN_WIDTH-10)
        self.apple.center_y = random.randint(10, SCREEN_HEIGHT-10)
        self.apple.change_x = 0
        self.apple.change_y = 0
        # self.apple.color = arcade.color.RED
        # self.apple.size = 10
        # self.apple.width = 20
        # self.apple.height = 20
        

    def draw(self):
        self.apple.draw()