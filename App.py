from tkinter import *
from tkinter import font
from app_settings import *

class App():

    def __init__(self):
        self.window = Tk()
        self.window.geometry("800x600") 
        self.window.title("Study App")
        self.window.config(bg="white")  # Assuming bg_color is "white"

        # Fonts
        self.title_font = font.Font(family="Brush Script MT", size=20, weight="bold")
        self.button_font = font.Font(family="Georgia", size=14)
        self.exit_button_font = font.Font(family="Lucida Handwriting", size=14, weight="bold")
        self.header_font = font.Font(family="Arial", size=24, weight="bold")
        self.subheader_font = font.Font(family="Arial", size=18, weight="bold")
        self.content_font = font.Font(family="Arial", size=14)

        # Creating the Side Bar (Grey Background)
        self.sidebar_frame = Frame(self.window, background="light gray", width=168)
        self.sidebar_frame.pack(side='left', fill=Y)

        # Title in Nav (With Font)
        self.sidebar_label = Label(self.sidebar_frame, text="Study App", bg="light gray", font=self.title_font)
        self.sidebar_label.pack(pady=25, padx=25)

        # Home button in the sidebar
        self.home_button = Button(self.sidebar_frame, text="Home", height=2, width=10, bg='light gray', font=self.button_font,
                                  borderwidth=0, highlightthickness=0, command=self.show_home)
        self.home_button.pack(pady=5, padx=8)
        self.home_button.bind("<Enter>", self.on_enter)
        self.home_button.bind("<Leave>", self.on_leave)

        # Results button in the sidebar
        self.results_button = Button(self.sidebar_frame, text="Results", height=2, width=10, bg='light gray', font=self.button_font,
                                     borderwidth=0, highlightthickness=0, command=self.show_results)
        self.results_button.pack(pady=5, padx=8)
        self.results_button.bind("<Enter>", self.on_enter)
        self.results_button.bind("<Leave>", self.on_leave)

        # Calendar button in the sidebar
        self.calendar_button = Button(self.sidebar_frame, text="Calendar", height=2, width=10, bg='light gray', font=self.button_font,
                                      borderwidth=0, highlightthickness=0, command=self.show_calendar)
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

        # Main content area
        self.content_frame = Frame(self.window, background="white")
        self.content_frame.pack(side='left', fill=BOTH, expand=True, padx=20, pady=20)

        # Show the home screen by default
        self.show_home()

        self.window.mainloop()

    def show_home(self):
        self.clear_content()
        # Hi, 'NAME!' label
        self.name_label = Label(self.content_frame, text="Hi, 'NAME!'", font=self.header_font, bg="white")
        self.name_label.pack(anchor='nw')

        # Upcoming Assessments label
        self.upcoming_label = Label(self.content_frame, text="Upcoming Assessments", font=self.subheader_font, bg="white")
        self.upcoming_label.pack(anchor='nw', pady=(20, 10))

        self.assessments_frame = Frame(self.content_frame, bg="white")
        self.assessments_frame.pack(anchor='nw', pady=(0, 20))

        # Assessment frames
        self.assessments = [
            ("January 18th", "English Essay", "Period 4"),
            ("February 9th", "Calculus", "Period 2"),
            ("April 14th", "Physics, Mechanics", "Period 5"),
        ]

        for assessment in self.assessments:
            self.create_assessment_frame(*assessment)

    def show_results(self):
        self.clear_content()
        # Results content
        results_label = Label(self.content_frame, text="Results", font=self.header_font, bg="white")
        results_label.pack(anchor='nw')
        # Add more widgets to show results

    def show_calendar(self):
        self.clear_content()
        # Calendar content
        calendar_label = Label(self.content_frame, text="Calendar", font=self.header_font, bg="white")
        calendar_label.pack(anchor='nw')
        # Add more widgets to show calendar

    def clear_content(self):
        # Destroy all widgets in the content frame
        for widget in self.content_frame.winfo_children():
            widget.destroy()

    def create_assessment_frame(self, date, subject, period):
        frame = Frame(self.assessments_frame, bg="#86D8F2", height=120, width=400)
        frame.pack_propagate(False)
        frame.pack(fill='x', pady=5)

        date_label = Label(frame, text=date, font=self.content_font, bg="#86D8F2")
        date_label.pack(side='left', padx=25, pady=5)

        subject_label = Label(frame, text=subject, font=self.content_font, bg="#86D8F2", wraplength=100)
        subject_label.pack(side='left', padx=25, pady=5)

        period_label = Label(frame, text=period, font=self.content_font, bg="#86D8F2", wraplength=100)
        period_label.pack(side='left', padx=25, pady=5)

    def on_enter(self, event):
        event.widget['background'] = 'gray'

    def on_leave(self, event):
        event.widget['background'] = 'light gray'

    def on_enter_exit(self, event):
        event.widget['background'] = 'red'

    def exit(self):
        self.window.destroy()

if __name__ == "__main__":
    app = App()
