import tkinter as tk
import random

class SnakeGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Snake Game")
        self.canvas = tk.Canvas(master, width=400, height=400, bg='black')
        self.canvas.pack()

        self.snake = [(20, 20), (20, 30), (20, 40)]
        self.snake_dir = (0, -10)  # Comienza moviéndose hacia arriba
        self.food_position = self.place_food()
        self.score = 0

        self.master.bind("<KeyPress>", self.change_direction)
        self.update_game()

    def place_food(self):
        x = random.randint(0, 39) * 10
        y = random.randint(0, 39) * 10
        return (x, y)

    def change_direction(self, event):
        if event.keysym == 'Up':
            self.snake_dir = (0, -10)
        elif event.keysym == 'Down':
            self.snake_dir = (0, 10)
        elif event.keysym == 'Left':
            self.snake_dir = (-10, 0)
        elif event.keysym == 'Right':
            self.snake_dir = (10, 0)

    def update_game(self):
        self.move_snake()
        self.check_collisions()
        self.canvas.delete(tk.ALL)
        self.draw_snake()
        self.draw_food()
        self.master.after(100, self.update_game)

    def move_snake(self):
        head_x, head_y = self.snake[0]
        new_head = (head_x + self.snake_dir[0], head_y + self.snake_dir[1])
        self.snake.insert(0, new_head)

        if new_head == self.food_position:
            self.food_position = self.place_food()
            self.score += 1
        else:
            self.snake.pop()  # Elimina la última parte de la serpiente

    def check_collisions(self):
        head_x, head_y = self.snake[0]

        # Colisión con los límites
        if head_x < 0 or head_x >= 400 or head_y < 0 or head_y >= 400:
            self.game_over()

        # Colisión consigo mismo
        if len(self.snake) != len(set(self.snake)):
            self.game_over()

    def draw_snake(self):
        for segment in self.snake:
            x, y = segment
            self.canvas.create_rectangle(x, y, x + 10, y + 10, fill='green')

    def draw_food(self):
        x, y = self.food_position
        self.canvas.create_oval(x, y, x + 10, y + 10, fill='red')

    def game_over(self):
        self.canvas.create_text(200, 200, text="GAME OVER", fill="white", font=("Arial", 24))
        self.master.after_cancel(self.update_game)  # Detener el juego

if __name__ == "__main__":
    root = tk.Tk()
    game = SnakeGame(root)
    root.mainloop()
