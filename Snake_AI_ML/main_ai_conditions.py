import arcade
from modules.snake import Snake
from modules.apple import Apple

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 400
SCREEN_TITLE = "Snake-AI"

class Game(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        arcade.set_background_color(arcade.color.KHAKI)
        self.apple = Apple(SCREEN_WIDTH, SCREEN_HEIGHT)
        self.snake = Snake(SCREEN_WIDTH, SCREEN_HEIGHT)
        self.game_over = False

    def on_draw(self):
        arcade.start_render()

        if not self.game_over:
            self.snake.draw()
            self.apple.draw()

            arcade.draw_text(f"SCORE : {self.snake.score}", 20,
                             SCREEN_HEIGHT - 380, arcade.color.YELLOW_ROSE, font_size=16)

        elif self.game_over:
            arcade.exit()

        arcade.finish_render()


    def on_update(self, delta_time: float):
        self.snake.move()

        if self.snake.center_y > self.apple.center_y:
            self.snake.change_x = 0
            self.snake.change_y = -1

        elif self.snake.center_y < self.apple.center_y:
            self.snake.change_x = 0
            self.snake.change_y = 1

        elif self.snake.center_x > self.apple.center_x:
            self.snake.change_x = -1
            self.snake.change_y = 0

        elif self.snake.center_x < self.apple.center_x:
            self.snake.change_x = 1
            self.snake.change_y = 0

        if arcade.check_for_collision(self.snake, self.apple):
            self.snake.eat()
            self.apple = Apple(SCREEN_WIDTH, SCREEN_HEIGHT)

        self.game_over_checker()

    def game_over_checker(self):
        for part in self.snake.body:
            if self.snake.center_x == part["center_x"] and self.snake.center_y == part["center_y"]:
                print("Snake hit his self.")
                self.game_over = True
                self.on_draw()

        if self.snake.center_x <= 8 or self.snake.center_x >= (
                SCREEN_WIDTH - 8) or self.snake.center_y <= 8 or self.snake.center_y >= (SCREEN_HEIGHT - 8):
            print("Snake hit wall.")
            self.game_over = True
            self.on_draw()

    def on_key_release(self, symbol: int, modifiers: int):
        pass


if __name__ == "__main__":
    game = Game()
    arcade.run()