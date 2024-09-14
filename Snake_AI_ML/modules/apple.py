import random, arcade

class Apple(arcade.Sprite):
    def __init__(self, SCREEN_WIDTH, SCREEN_HEIGHT):
        super().__init__()
        self.center_x = random.randint(10, SCREEN_WIDTH-10) // 8 * 8
        self.center_y = random.randint(10, SCREEN_HEIGHT-10) // 8 * 8  
        self.color = arcade.color.RED
        self.radius = 8

        # Set teh hit-box   
        self.set_hit_box([(self.radius, 0), (-self.radius, 0), (0, self.radius), (0, -self.radius)])

    def draw(self):
        arcade.draw_circle_filled(self.center_x, self.center_y, self.radius, self.color)