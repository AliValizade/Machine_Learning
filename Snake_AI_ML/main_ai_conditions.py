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
        if key == arcade.key.Q:
            arcade.exit()
    
    def on_update(self, delta_time: float):
        
        if not self.game_over:
            if self.snake.center_x < self.apple.center_x:
                self.snake.change_x = SNAKE_SIZE
            elif self.snake.center_x > self.apple.center_x:
                self.snake.change_x = -SNAKE_SIZE
            else:
                self.snake.change_x = 0
            
            if self.snake.center_y < self.apple.center_y:
                self.snake.change_y = SNAKE_SIZE
            elif self.snake.center_y > self.apple.center_y:
                self.snake.change_y = -SNAKE_SIZE
            else:
                self.snake.change_y = 0
            self.snake.move()
            if arcade.check_for_collision(self.apple, self.snake):
                self.snake.eat()
                self.apple = Apple(SCREEN_WIDTH, SCREEN_HEIGHT)
        
game_board = Game()
arcade.run()