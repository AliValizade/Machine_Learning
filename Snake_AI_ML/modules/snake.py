import arcade

class Snake(arcade.Sprite):
    def __init__(self, SCREEN_WIDTH, SCREEN_HEIGHT, SNAKE_SIZE):
        super().__init__()
        self.width = SNAKE_SIZE
        self.height = SNAKE_SIZE
        self.score = 1
        self.center_x = SCREEN_WIDTH // 2
        self.center_y = SCREEN_HEIGHT // 2
        self.change_x = 0
        self.change_y = 0
        self.body = [[self.center_x, self.center_y]]

    def draw(self):
        # Draw the head of the snake as a circle
        arcade.draw_circle_filled(self.center_x, self.center_y, self.width // 2, arcade.color.BLUE)

        # Draw the body of the snake as squares
        for i, segment in enumerate(self.body[1:]):
            color = arcade.color.GREEN if i % 2 == 0 else arcade.color.DARK_GREEN
            arcade.draw_rectangle_filled(segment[0], segment[1], self.width, self.height, color)

    def move(self):
        # Add the current head position to the body (this becomes the new segment)
        self.body.append([self.center_x, self.center_y])

        # Move the snake's head
        self.center_x += (self.change_x)
        self.center_y += (self.change_y)

        # Remove the last segment of the body to keep the length consistent with the score
        if len(self.body) > self.score:
            self.body.pop(0)       

    def eat(self):
        self.score += 1
        self.body.append([self.center_x, self.center_y])
        
