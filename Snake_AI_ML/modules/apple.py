import random, arcade

class Apple(arcade.Sprite):
    def __init__(self, SCREEN_WIDTH, SCREEN_HEIGHT):
        super().__init__()
        self.center_x = random.randint(16, SCREEN_WIDTH - 16) // 8 * 8
        self.center_y = random.randint(16, SCREEN_HEIGHT - 16) // 8 * 8
        self.change_x = 0
        self.change_y = 0
        self.size = 16
        self.width = 16
        self.height = 16  
        self.color = arcade.color.RED
        self.radius = 8

    def draw(self):
        arcade.draw_circle_filled(self.center_x, self.center_y, self.radius, self.color)
