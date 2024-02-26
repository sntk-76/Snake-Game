from tkinter import * 

#-----------------Game Variables-----------------
GAME_HEIGHT = 700
GAME_WIDTH = 900
GAME_SPACE = 10
SPEED_RANGE = 200
SNAKE_COLOR = "green"
FOOD_COLOR = "red"
BACKGROUND_COLOR = "black"
DIRECTION = 'down'
score = 0
#-----------------Game Variables-----------------

#-----------------Snake functions-----------------
def restart_game():
    pass




#-----------------window adjusment-----------------
window = Tk()
window.title("Snake Game")
window.resizable(False, False)

label = Label(window, text=f"Score: {score} " , font=("Arial", 12))
label.pack()

canvas = Canvas(window, width=GAME_WIDTH, height=GAME_HEIGHT, bg=BACKGROUND_COLOR)
canvas.pack()

restart = Button(window, text="Restart", font=("Arial", 12),fg="red", command = restart_game)
restart.pack()

window.update() 

window_heigh = window.winfo_height()
window_width = window.winfo_width()
screen_height = window.winfo_screenheight()
screen_width = window.winfo_screenwidth()

x = int((screen_width / 2) - (window_width / 2))
y = int((screen_height / 2) - (window_heigh / 2))

window.geometry(f'{window_width}x{window_heigh}+{x}+{y-40}')

window.mainloop()