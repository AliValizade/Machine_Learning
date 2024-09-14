import arcade
from modules.snake import Snake
from modules.apple import Apple

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 400
SNAKE_SIZE = 16

class Game(arcade.Window):
    def __init__(self):
        super().__init__(width=SCREEN_WIDTH, height=SCREEN_HEIGHT, title='Snake')
        arcade.set_background_color(arcade.color.SAND)
        self.snake = Snake(SCREEN_WIDTH, SCREEN_HEIGHT, SNAKE_SIZE)
        self.apple = Apple(SCREEN_WIDTH, SCREEN_HEIGHT)
        self.game_over = False
        self.move_delay = 0.15  # Control snake speed (lower values make it faster)
        self.time_since_last_move = 0

    def on_draw(self):
        arcade.start_render()
        if not self.game_over:
            self.snake.draw()
            self.apple.draw()
            score = f"Score: {self.snake.score}"
            arcade.draw_text(score, 20, SCREEN_HEIGHT - 20, arcade.color.DARK_BLUE, 15)
            if arcade.check_for_collision(self.apple, self.snake):
                self.snake.eat()
                self.apple = Apple(SCREEN_WIDTH, SCREEN_HEIGHT)
        else:
            arcade.draw_text('Game Over!', 140, 250, arcade.color.DARK_RED, 30)
            arcade.draw_text('Press "Q" to Quit!', 130, 150, arcade.color.RED, 24)

    def on_key_release(self, key: int, modifiers: int):
        if not self.game_over:
            if key == arcade.key.UP and self.snake.change_y != -SNAKE_SIZE:
                self.snake.change_y = SNAKE_SIZE
                self.snake.change_x = 0
            elif key == arcade.key.DOWN and self.snake.change_y != SNAKE_SIZE:
                self.snake.change_y = -SNAKE_SIZE
                self.snake.change_x = 0
            elif key == arcade.key.LEFT and self.snake.change_x != SNAKE_SIZE:
                self.snake.change_x = -SNAKE_SIZE
                self.snake.change_y = 0
            elif key == arcade.key.RIGHT and self.snake.change_x != -SNAKE_SIZE:
                self.snake.change_x = SNAKE_SIZE
                self.snake.change_y = 0
        if key == arcade.key.Q:
            arcade.exit()
    
    def on_update(self, delta_time: float):
        if not self.game_over:
            self.time_since_last_move += delta_time

            # Only move the snake if enough time has passed
            if self.time_since_last_move > self.move_delay:
                self.snake.move()
                self.time_since_last_move = 0  # Reset timer

            # Check for collisions with the wall
            if (self.snake.center_x < 0 or 
                self.snake.center_x > SCREEN_WIDTH or 
                self.snake.center_y < 0 or 
                self.snake.center_y > SCREEN_HEIGHT):
                self.game_over = True

            # Check for collisions with self
            head_position = (self.snake.center_x, self.snake.center_y)
            if head_position in self.snake.body[1:]:
                self.game_over = True
        
game_board = Game()
arcade.run()