from tkinter import Tk, Button, Label, DISABLED


# Main window
window = Tk()
window.title('button')
window.config(bg='#0f5c4d')
window.geometry(f'{300}x{300}+{100}+{100}')
window.resizable(True, True)


# Button
def add_label():
    label = Label(window, text='new').pack()

      
def counter():
    global count
    count += 1
    btn_3['text'] = f'Counter...{count}'
    
count = 0
    
btn_1 = Button(
        window,
        text='New...',
        command=add_label
    ).pack()
    
btn_2 = Button(
        window,
        text='Lambda...',
        state=DISABLED,
        command=lambda: Label(window, text='lambda').pack()
    ).pack()

 
btn_3 = Button(
        window,
        text=f'Counter...{count}',
        command=counter,
        bg='yellow',
        activebackground='blue',  
    )
btn_3.pack()





if __name__ == '__main__':
    window.mainloop()