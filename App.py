from tkinter import *
from tkinter import font, ttk
import calendar
from datetime import datetime

class App:

    def __init__(self):
        self.window = Tk()
        self.window.geometry("800x600")
        self.window.title("Study App")
        self.window.config(bg="white")

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
        # Add more widgets to show results as needed

    def show_calendar(self):
        self.clear_content()
        # Calendar content
        calendar_label = Label(self.content_frame, text="Calendar", font=self.header_font, bg="white")
        calendar_label.pack(anchor='nw')

        # Year entry
        self.year_entry = Entry(self.content_frame, width=5, font=self.content_font)
        self.year_entry.pack(anchor='nw', padx=(0, 10), pady=10)
        self.year_entry.insert(0, datetime.now().year)

        # Month combobox
        self.month_combobox = ttk.Combobox(self.content_frame, values=list(range(1, 13)), font=self.content_font, width=3)
        self.month_combobox.pack(anchor='nw', padx=(0, 10), pady=10)
        self.month_combobox.set(datetime.now().month)

        # Show calendar button
        show_button = Button(self.content_frame, text="Show Calendar", command=self.display_calendar)
        show_button.pack(anchor='nw', pady=10)

        self.reminders = {}  # Dictionary to store reminders

    def display_calendar(self):
        # Get the year and month from entry fields
        year = int(self.year_entry.get())
        month = int(self.month_combobox.get())

        # Create a calendar object
        cal = calendar.monthcalendar(year, month)

        # Create a new Tkinter window for the calendar
        calendar_window = Toplevel(self.window)
        calendar_window.title(f"Calendar - {calendar.month_name[month]} {year}")

        # Create labels to display the days of the week
        days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
        for i, day in enumerate(days):
            Label(calendar_window, text=day, width=5, font=('Arial', 10, 'bold')).grid(row=0, column=i)

        # Display the calendar data
        for week_num, week in enumerate(cal, start=1):
            for day_num, day in enumerate(week):
                if day != 0:
                    # Determine the color of the label based on the day
                    label_color = 'red' if day_num in (5, 6) else 'black'

                    # Create a label for the date
                    date_label = Label(calendar_window, text=day, width=5, font=('Arial', 10), fg=label_color)
                    date_label.grid(row=week_num, column=day_num)

                    # Bind click event to each date label
                    date_label.bind("<Button-1>", lambda event, d=day, m=month: self.open_reminder_window(event, d, m))

    def open_reminder_window(self, event, day, month):
        # Check if there is an existing reminder for the selected date
        if (day, month) in self.reminders:
            existing_reminder = self.reminders[(day, month)]
            # Open a window to display existing reminder
            reminder_window = Toplevel(self.window)
            reminder_window.title(f"Existing Reminder - {day}/{month}")

            # Label to display existing reminder
            Label(reminder_window, text=existing_reminder, font=('Arial', 12)).pack(pady=10)
        else:
            # Create a new window for adding a reminder
            add_reminder_window = Toplevel(self.window)
            add_reminder_window.title(f"Add Reminder - {day}/{month}")

            Label(add_reminder_window, text="Reminder:", font=('Arial', 12)).pack(pady=10)
            reminder_entry = Entry(add_reminder_window, width=40, font=('Arial', 12))
            reminder_entry.pack(pady=10)

            def save_reminder():
                reminder_text = reminder_entry.get()
                self.reminders[(day, month)] = reminder_text
                add_reminder_window.destroy()

            save_button = Button(add_reminder_window, text="Save", command=save_reminder)
            save_button.pack(pady=10)

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

        subject_label = Label(frame, text=subject, font=self.content_font, bg="#86D8F2")
        subject_label.pack(side='left', padx=25, pady=5)

        period_label = Label(frame, text=period, font=self.content_font, bg="#86D8F2")
        period_label.pack(side='left', padx=25, pady=5)

    def on_enter(self, event):
        event.widget.config(bg='gray')

    def on_leave(self, event):
        event.widget.config(bg='light gray')

    def on_enter_exit(self, event):
        event.widget.config(bg='dark gray')

    def on_leave_exit(self, event):
        event.widget.config(bg='light gray')

    def exit(self):
        self.window.destroy()

if __name__ == "__main__":
    app = App()
