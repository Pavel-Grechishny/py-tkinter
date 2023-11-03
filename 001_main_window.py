from tkinter import Tk, PhotoImage
from screeninfo import get_monitors

# >>> get_monitors()
# [Monitor(x=0, y=0, width=1366, height=768, width_mm=344, height_mm=194, name='\\\\.\\DISPLAY1', is_primary=True)]


# Size small screen
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
main_icon = PhotoImage(file='001_main_icon.png')
window.iconphoto(False, main_icon)
window.title('tkinter')
window.config(bg='#0f5c4d')
window.geometry(f'{screen_sm_width}x{screen_sm_heigth}+{margin_left}+{margin_top}')
window.resizable(True, True)
# window.attributes("-fullscreen", True)


window.mainloop()