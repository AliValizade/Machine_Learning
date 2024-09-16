import arcade
from modules.snake import Snake
from modules.apple import Apple

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 400
SCREEN_TITLE = "Snake-AI"
SNAKE_SIZE = 16

class Game(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        arcade.set_background_color(arcade.color.KHAKI)
        self.game_over = False
        self.apple = Apple(SCREEN_WIDTH, SCREEN_HEIGHT)
        self.snake = Snake(SCREEN_WIDTH, SCREEN_HEIGHT)
        self.move_delay = 0.15  # Control snake speed (lower values make it faster)
        self.time_since_last_move = 0

    def on_draw(self):
        arcade.start_render()

        if not self.game_over:

            self.snake.draw()
            self.apple.draw()

            arcade.draw_text(f"SCORE : {self.snake.score}", SCREEN_WIDTH - 300,
                             SCREEN_HEIGHT - 30, arcade.color.YELLOW_ROSE, font_size=20)

        elif self.game_over:
            arcade.exit()

        arcade.finish_render()

    def on_update(self, delta_time: float):
        if not self.game_over:
            self.time_since_last_move += delta_time

            # Only move the snake if enough time has passed
            if self.time_since_last_move > self.move_delay:
                self.snake.move()
                self.time_since_last_move = 0  # Reset timer

            if arcade.check_for_collision(self.snake, self.apple):
                self.snake.eat()
                self.apple = Apple(SCREEN_WIDTH, SCREEN_HEIGHT)

        self.game_over_checker()

    def game_over_checker(self):
        for segment in self.snake.body:
            if self.snake.center_x == segment[0] and self.snake.center_y == segment[1]:
                print("Snake hit his self.")
                self.game_over = True
                self.on_draw()

        if self.snake.center_x <= 8 or self.snake.center_x >= (
                SCREEN_WIDTH - 8) or self.snake.center_y <= 8 or self.snake.center_y >= (SCREEN_HEIGHT - 8):
            print("Snake hit wall.")
            self.game_over = True
            self.on_draw()

    def on_key_release(self, key: int, modifiers: int):
        if key == arcade.key.UP:
            self.snake.change_x = 0
            self.snake.change_y = 1
        elif key == arcade.key.DOWN:
            self.snake.change_x = 0
            self.snake.change_y = -1
        elif key == arcade.key.RIGHT:
            self.snake.change_x = 1
            self.snake.change_y = 0
        elif key == arcade.key.LEFT:
            self.snake.change_x = -1
            self.snake.change_y = 0
            
        if key == arcade.key.Q:
            arcade.exit()


if __name__ == "__main__":
    game = Game()
    arcade.run()