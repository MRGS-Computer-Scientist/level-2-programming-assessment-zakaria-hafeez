from tkinter import *
from app_settings import *
from os import path

class App():

    def __init__(self):
        self.window = Tk()
        self.window.geometry(str(w_width) + "x" + str(w_height))
        self.window.title(app_title)

        # Creating the Side Bar
        self.sidebar_frame = Frame(self.window, background="light gray", width=168)
        self.sidebar_frame.pack(side='left', fill=Y)

        # Title in Nav
        self.sidebar_label = Label(self.sidebar_frame, text="Study Buddy", bg="light gray")
        self.sidebar_label.pack(pady=25, padx=25)

        # Home button in the sidebar
        self.home_button = Button(self.sidebar_frame, text="Home", height=2, width=10, bg='light gray')
        self.home_button.pack(pady=5, padx=5)

        # Calendar button in the sidebar
        self.calendar_button = Button(self.sidebar_frame, text="Calendar", height=2, width=10, bg='light gray')
        self.calendar_button.pack(pady=5, padx=5)

        # Main frame
        self.main_frame = Frame(self.window, background=bg_color, width=w_width, height=(w_height-200))
        self.main_frame.pack(fill=BOTH, expand=True)  # Fill the available space

        # Bottom frame
        self.bottom_frame = Frame(self.window, background=bg_color, width=w_width, height=100)
        self.bottom_frame.pack(side='bottom', fill=X)  # Fill horizontally

        # Spacer frame to push the Exit button to the bottom
        self.spacer_frame = Frame(self.sidebar_frame, height=250, bg="light gray")
        self.spacer_frame.pack(pady=5, padx=5)

        # Exit button in the sidebar
        self.exit_button = Button(self.sidebar_frame, text="Exit", height=2, width=10, background="light gray", command=self.exit)
        self.exit_button.pack(pady=5, padx=5)
        
        self.window.mainloop()

    def exit(self):
        self.window.destroy()
