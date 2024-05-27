from tkinter import *
from tkinter import font
from app_settings import *
from os import path

class App():

    def __init__(self):
        self.window = Tk()
        self.window.geometry(str(w_width) + "x" + str(w_height))
        self.window.title(app_title)

        # Semi Cursive Fonts
        self.title_font = font.Font(family="Brush Script MT", size=20, weight="bold")
        self.button_font = font.Font(family="Georgia", size=14)
        self.exit_button_font = font.Font(family="Lucida Handwriting", size=14, weight="bold")

        # Creating the Side Bar (Grey Background)
        self.sidebar_frame = Frame(self.window, background="light gray", width=168)
        self.sidebar_frame.pack(side='left', fill=Y)

        # Title in Nav (With Font)
        self.sidebar_label = Label(self.sidebar_frame, text="Study Buddy", bg="light gray", font=self.title_font)
        self.sidebar_label.pack(pady=25, padx=25)

        # Home button in the sidebar
        self.home_button = Button(self.sidebar_frame, text="Home", height=2, width=10, bg='light gray', font=self.button_font,
        borderwidth=0, highlightthickness=0)
        self.home_button.pack(pady=5, padx=8)
        self.home_button.bind("<Enter>", self.on_enter)
        self.home_button.bind("<Leave>", self.on_leave)

        # Results button in the sidebar
        self.results_button = Button(self.sidebar_frame, text="Results", height=2, width=10, bg='light gray', font=self.button_font,
        borderwidth=0, highlightthickness=0)
        self.results_button.pack(pady=5, padx=8)
        self.results_button.bind("<Enter>", self.on_enter)
        self.results_button.bind("<Leave>", self.on_leave)

        # Calendar button in the sidebar
        self.calendar_button = Button(self.sidebar_frame, text="Calendar", height=2, width=10, bg='light gray', font=self.button_font,
        borderwidth=0, highlightthickness=0)
        self.calendar_button.pack(pady=5, padx=8)
        self.calendar_button.bind("<Enter>", self.on_enter)
        self.calendar_button.bind("<Leave>", self.on_leave)

        # Spacer frame to push the Exit button to the bottom
        self.spacer_frame = Frame(self.sidebar_frame, height=250, bg="light gray")
        self.spacer_frame.pack(pady=5, padx=5)

       # Exit button in the sidebar
        self.exit_button = Button(self.sidebar_frame, text="Exit", height=2, width=10, background="light gray", font=self.exit_button_font,
        borderwidth=0, highlightthickness=0, command=self.exit) 
        self.exit_button.pack(pady=5, padx=5)
        self.exit_button.bind("<Enter>", self.on_enter_exit)
        self.exit_button.bind("<Leave>", self.on_leave)

        self.window.mainloop()

    def on_enter(self, event):
        event.widget['background'] = 'gray'

    def on_leave(self, event):
        event.widget['background'] = 'light gray'

    def on_enter_exit(self, event):
        event.widget['background'] = 'red'

    def exit(self):
        self.window.destroy()