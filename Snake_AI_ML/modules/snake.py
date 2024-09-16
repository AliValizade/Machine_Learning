import arcade


class Snake(arcade.Sprite):
    def __init__(self, SCREEN_WIDTH, SCREEN_HEIGHT):
        super().__init__()
        self.width = 16
        self.height = 16
        self.center_x = SCREEN_WIDTH // 2
        self.center_y = SCREEN_HEIGHT // 2
        self.color1 = arcade.color.DARK_BROWN
        self.color2 = arcade.color.LIGHT_BROWN
        self.change_x = 1
        self.change_y = 1
        self.speed = 8
        self.score = 0
        self.body = []

    def draw(self):
        arcade.draw_circle_filled(self.center_x, self.center_y, self.width//2, arcade.color.DARK_GREEN)

        # Draw the body of the snake as squares
        for i, segment in enumerate(self.body):
            color = self.color1 if i % 2 == 0 else self.color2
            arcade.draw_rectangle_filled(segment[0], segment[1], self.width, self.height, color)


    def move(self):
        self.body.append([self.center_x, self.center_y])
        if len(self.body) > self.score +1:
            self.body.pop(0)
        self.center_x += self.change_x * self.speed
        self.center_y += self.change_y * self.speed


    def eat(self):
        self.score += 1
