from tkinter import Tk, Label, RAISED, LEFT
from screeninfo import get_monitors

monitor = get_monitors()[0]
grid_columns = 16
grid_rows = 9
center_x = monitor.width // 2
center_y = monitor.height // 2
screen_sm_width = round(monitor.width / grid_columns) * (grid_columns - 2)
screen_sm_heigth = round(monitor.height / grid_rows) * (grid_rows - 2)
margin_left = (monitor.width - screen_sm_width) // 2
margin_top = (monitor.height - screen_sm_heigth) // 3



# Main window
window = Tk()
window.title('label')
window.config(bg='#0f5c4d')
window.geometry(f'{screen_sm_width}x{screen_sm_heigth}+{margin_left}+{margin_top}')
window.resizable(True, True)


# Label
label_1 = Label(window, text='LABEL_1')
label_1.pack()

label_2 = Label(window, 
    text='LABEL_2\nother_text',
    bg='#9a9a9a',
    fg='white',
    font=('Hack', 20, 'bold'),
    padx=30,
    pady=15,
    width=20,
    height=4,
    anchor='se',
    relief=RAISED, 
    bd=10,
    justify=LEFT
    ).pack()
label_3 = Label(window, text='LABEL_3').pack()



if __name__ == '__main__':
    window.mainloop()