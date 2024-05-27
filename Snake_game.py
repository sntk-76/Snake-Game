from tkinter import *
from random import randint

#-----------------Game Variables-----------------
GAME_HEIGHT = 700
GAME_WIDTH = 900
GAME_SPACE = 25
SPEED_RANGE = 200
SNAKE_COLOR = "green"
SNAKE_SIZE = 3
FOOD_COLOR = "red"
BACKGROUND_COLOR = "black"
DIRECTION = 'right'
score = 0
#-----------------Game Variables-----------------

#-----------------class snake -------------------------
class Snake:
    def __init__(self):
        self.body_size = SNAKE_SIZE
        self.coordinates = []
        self.squares = []

        for i in range(SNAKE_SIZE):
            self.coordinates.append([0, 0])

        for x, y in self.coordinates:
            square = canvas.create_rectangle(x, y, x + GAME_SPACE, y + GAME_SPACE, fill=SNAKE_COLOR, tag="snake")
            self.squares.append(square)

#-----------------class food -------------------------
class Food:
    def __init__(self):
        x = randint(0, (GAME_WIDTH // GAME_SPACE) - 1) * GAME_SPACE
        y = randint(0, (GAME_HEIGHT // GAME_SPACE) - 1) * GAME_SPACE
        self.coordinates = [x, y]
        canvas.create_oval(x, y, x + GAME_SPACE, y + GAME_SPACE, fill=FOOD_COLOR, tag="food")

#-----------------movement functions -----------------
def move_snake():
    global DIRECTION, score

    x, y = snake.coordinates[0]

    if DIRECTION == 'up':
        y -= GAME_SPACE
    elif DIRECTION == 'down':
        y += GAME_SPACE
    elif DIRECTION == 'left':
        x -= GAME_SPACE
    elif DIRECTION == 'right':
        x += GAME_SPACE

    snake.coordinates.insert(0, [x, y])
    square = canvas.create_rectangle(x, y, x + GAME_SPACE, y + GAME_SPACE, fill=SNAKE_COLOR)
    snake.squares.insert(0, square)

    if x == food.coordinates[0] and y == food.coordinates[1]:
        score += 1
        label.config(text=f"Score: {score}")
        canvas.delete("food")
        food.__init__()
    else:
        snake.coordinates.pop()
        canvas.delete(snake.squares.pop())

    if check_collision(snake):
        game_over()
    else:
        window.after(SPEED_RANGE, move_snake)

def restart_game():
    global score, DIRECTION, snake, food
    canvas.delete(ALL)
    score = 0
    DIRECTION = 'right'
    label.config(text=f"Score: {score}")
    snake = Snake()
    food = Food()
    move_snake()

def game_over():
    canvas.create_text(canvas.winfo_width() / 2, canvas.winfo_height() / 2, font=('Terminal', 60), text='GAME OVER', fill='#DF1A2F', tags='gameover')

def change_direction(new_dir):
    global DIRECTION
    if new_dir == 'left' and DIRECTION != 'right':
        DIRECTION = new_dir
    elif new_dir == 'right' and DIRECTION != 'left':
        DIRECTION = new_dir
    elif new_dir == 'up' and DIRECTION != 'down':
        DIRECTION = new_dir
    elif new_dir == 'down' and DIRECTION != 'up':
        DIRECTION = new_dir

def check_collision(snake):
    x, y = snake.coordinates[0]
    if x < 0 or x >= GAME_WIDTH or y < 0 or y >= GAME_HEIGHT:
        return True
    for sq in snake.coordinates[1:]:
        if x == sq[0] and y == sq[1]:
            return True
    return False

#-----------------window adjustment-----------------
window = Tk()
window.title("Snake Game")
window.resizable(False, False)

label = Label(window, text=f"Score: {score}", font=("Arial", 12))
label.pack()

canvas = Canvas(window, width=GAME_WIDTH, height=GAME_HEIGHT, bg=BACKGROUND_COLOR)
canvas.pack()

restart = Button(window, text="Restart", font=("Arial", 12), fg="red", command=restart_game)
restart.pack()

window.update()

window_height = window.winfo_height()
window_width = window.winfo_width()
screen_height = window.winfo_screenheight()
screen_width = window.winfo_screenwidth()

x = int((screen_width / 2) - (window_width / 2))
y = int((screen_height / 2) - (window_height / 2))

window.geometry(f'{window_width}x{window_height}+{x}+{y-40}')
window.bind("<Up>", lambda event: change_direction('up'))
window.bind("<Down>", lambda event: change_direction('down'))
window.bind("<Left>", lambda event: change_direction('left'))
window.bind("<Right>", lambda event: change_direction('right'))

snake = Snake()
food = Food()

move_snake()

window.mainloop()
