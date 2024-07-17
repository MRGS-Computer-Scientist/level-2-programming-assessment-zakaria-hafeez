from tkinter import *
from tkinter import font
from tkinter import ttk, messagebox
from datetime import datetime
import json
import calendar
import os

class App:

    def __init__(self):
        self.window = Tk()
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()
        self.window.geometry(f"{screen_width}x{screen_height}")  # Set initial size to screen size
        self.window.title("Study App")
        self.window.config(bg="white")

        # Fonts
        self.title_font = font.Font(family="Brush Script MT", size=20, weight="bold")
        self.button_font = font.Font(family="Georgia", size=14)
        self.exit_button_font = font.Font(family="Lucida Handwriting", size=14, weight="bold")
        self.header_font = font.Font(family="Arial", size=24, weight="bold")
        self.subheader_font = font.Font(family="Arial", size=18, weight="bold")
        self.content_font = font.Font(family="Arial", size=14)

        # Dictionary to store reminders
        self.reminders = {}
        self.load_reminders()  # Load reminders from file

        # Show the login screen by default
        self.show_login()

        self.window.mainloop()

    def show_login(self):
        self.clear_content()
        self.login_frame = Frame(self.window, bg="white")
        self.login_frame.pack(fill=BOTH, expand=True)

        self.login_label = Label(self.login_frame, text="Login", font=self.header_font, bg="white")
        self.login_label.pack(pady=(50, 10))

        Label(self.login_frame, text="Username:", font=self.content_font, bg="white").pack(pady=(10, 5))
        self.username_entry = Entry(self.login_frame, font=self.content_font)
        self.username_entry.pack(pady=(0, 10))

        Label(self.login_frame, text="Password:", font=self.content_font, bg="white").pack(pady=(10, 5))
        self.password_entry = Entry(self.login_frame, font=self.content_font, show='*')
        self.password_entry.pack(pady=(0, 10))

        self.login_button = Button(self.login_frame, text="Login", font=self.button_font, command=self.login)
        self.login_button.pack(pady=(10, 5))

        self.signup_button = Button(self.login_frame, text="Sign Up", font=self.button_font, command=self.show_signup)
        self.signup_button.pack(pady=(10, 5))

    def show_signup(self):
        self.clear_content()
        self.signup_frame = Frame(self.window, bg="white")
        self.signup_frame.pack(fill=BOTH, expand=True)

        self.signup_label = Label(self.signup_frame, text="Sign Up", font=self.header_font, bg="white")
        self.signup_label.pack(pady=(50, 10))

        Label(self.signup_frame, text="Username:", font=self.content_font, bg="white").pack(pady=(10, 5))
        self.signup_username_entry = Entry(self.signup_frame, font=self.content_font)
        self.signup_username_entry.pack(pady=(0, 10))

        Label(self.signup_frame, text="Password:", font=self.content_font, bg="white").pack(pady=(10, 5))
        self.signup_password_entry = Entry(self.signup_frame, font=self.content_font, show='*')
        self.signup_password_entry.pack(pady=(0, 10))

        self.signup_submit_button = Button(self.signup_frame, text="Submit", font=self.button_font, command=self.signup)
        self.signup_submit_button.pack(pady=(10, 5))

        self.back_to_login_button = Button(self.signup_frame, text="Back to Login", font=self.button_font, command=self.show_login)
        self.back_to_login_button.pack(pady=(10, 5))

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        if self.validate_login(username, password):
            self.show_main_app()
        else:
            messagebox.showerror("Login Failed", "Invalid username or password")

    def signup(self):
        username = self.signup_username_entry.get()
        password = self.signup_password_entry.get()
        if self.save_user_credentials(username, password):
            messagebox.showinfo("Sign Up Success", "Account created successfully! Please login.")
            self.show_login()
        else:
            messagebox.showerror("Sign Up Failed", "Username already exists. Please choose another username.")

    def validate_login(self, username, password):
        if os.path.exists("users.json"):
            with open("users.json", "r") as file:
                users = json.load(file)
                if username in users and users[username] == password:
                    return True
        return False

    def save_user_credentials(self, username, password):
        if os.path.exists("users.json"):
            with open("users.json", "r") as file:
                users = json.load(file)
        else:
            users = {}

        if username in users:
            return False

        users[username] = password
        with open("users.json", "w") as file:
            json.dump(users, file)
        return True

    def show_main_app(self):
        # Creating the Side Bar (Grey Background)
        self.login_frame.pack_forget()
        self.sidebar_frame = Frame(self.window, background="light gray", width=168)
        self.sidebar_frame.pack(side='left', fill=Y)

        # Title in Nav (With Font)
        self.sidebar_label = Label(self.sidebar_frame, text="Study Buddy", bg="light gray", font=self.title_font)
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
        self.exit_button.pack(side='bottom', anchor='sw', pady=80, padx=60)  # Positioned at the bottom left
        self.exit_button.bind("<Enter>", self.on_enter_exit)
        self.exit_button.bind("<Leave>", self.on_leave_exit)

        # Main content area
        self.content_frame = Frame(self.window, background="white")
        self.content_frame.pack(side='left', fill=BOTH, expand=True, padx=20, pady=20)

        self.show_home()

    def show_home(self):
        # Clear existing content
        self.clear_content()

        # Hi, 'NAME!' label
        self.name_label = Label(self.content_frame, text="Hi, 'Buddy!'", font=self.header_font, bg="white")
        self.name_label.pack(anchor='nw')

        # Upcoming Events label
        self.upcoming_label = Label(self.content_frame, text="Upcoming Events", font=self.subheader_font, bg="white")
        self.upcoming_label.pack(anchor='nw', pady=(20, 10))

        self.assessments_frame = Frame(self.content_frame, bg="white")
        self.assessments_frame.pack(anchor='nw', pady=(0, 20))

        # Sort reminders by date
        sorted_reminders = sorted(
            ((datetime.strptime(date, '%Y-%m-%d'), reminders) for date, reminders in self.reminders.items()),
            key=lambda x: x[0]
        )

        # Display sorted reminders
        for date_obj, reminders in sorted_reminders:
            date_str = date_obj.strftime('%Y-%m-%d')
            for reminder in reminders:
                self.create_assessment_frame(date_str, *reminder.split(", "))

    def show_results(self):
        self.clear_content()
        # Results content
        results_label = Label(self.content_frame, text="Results", font=self.header_font, bg="white")
        results_label.pack(anchor='nw')

    def show_calendar(self):
        # Clear previous content in the content frame
        self.clear_content()

        # Create and pack the calendar-related widgets
        self.calendar_label = Label(self.content_frame, text="Calendar", font=self.header_font, bg="white")
        self.calendar_label.pack(anchor='nw', pady=(20, 10))

        self.calendar_desc_label = Label(self.content_frame, text="Use this Calendar Functionality to keep track of your assessments as we will remind you of anything that is coming up soon. We will help you stay on top and on track with your work and we will help you stay organised if you were our calendar function.", bg="white", font=("Arial", 12), wraplength=700, anchor="w", justify="left")
        self.calendar_desc_label.pack(anchor='nw', pady=(10, 10))

        # Frame for year and month input
        self.input_frame = Frame(self.content_frame, bg="white")
        self.input_frame.pack(pady=20)

        # Entry field for year
        Label(self.input_frame, text="Year:", bg="white").grid(row=0, column=0)
        self.year_entry = Entry(self.input_frame)
        self.year_entry.insert(END, datetime.now().year)
        self.year_entry.grid(row=0, column=1)

        # Combobox for month selection
        Label(self.input_frame, text="Month:", bg="white").grid(row=0, column=2)
        self.month_combobox = ttk.Combobox(self.input_frame, values=list(range(1, 13)))
        self.month_combobox.grid(row=0, column=3)
        self.month_combobox.current(datetime.today().month - 1)  # Set default value to the current month

        # Button to display calendar
        self.display_button = Button(self.input_frame, text="Display Calendar", command=self.display_calendar)
        self.display_button.grid(row=0, column=4, padx=10)

        # Frame for displaying calendar
        self.days_frame = Frame(self.content_frame, bg="lightblue")
        self.days_frame.pack(expand=True, fill=BOTH, padx=20, pady=20)

        # Display initial calendar
        self.display_calendar()

    def clear_content(self):
        # Clear the content frame without destroying it
        for widget in self.content_frame.winfo_children():
            widget.destroy()


    def create_assessment_frame(self, date, subject, time, name):
        frame = Frame(self.assessments_frame, bg="#86D8F2", height=200, width=800)  # Increase height and width here
        frame.pack_propagate(False)
        frame.pack(fill='x', pady=10)

        date_label = Label(frame, text=date, font=self.content_font, bg="#86D8F2")
        date_label.pack(side='left', padx=50, pady=20)  # Adjust padding

        subject_label = Label(frame, text=subject, font=self.content_font, bg="#86D8F2")
        subject_label.pack(side='left', padx=50, pady=20)  # Adjust padding

        time_label = Label(frame, text=time, font=self.content_font, bg="#86D8F2")
        time_label.pack(side='left', padx=50, pady=20)  # Adjust padding

        name_label = Label(frame, text=name, font=self.content_font, bg="#86D8F2")
        name_label.pack(side='left', padx=50, pady=20)  # Adjust padding

    def clear_content(self):
        for widget in self.window.winfo_children():
            widget.destroy()

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

    # Function to save reminders to a JSON file
    def save_reminders(self):
        with open("reminders.json", "w") as file:
            json.dump(self.reminders, file)

    # Function to load reminders from a JSON file
    def load_reminders(self):
        if os.path.exists("reminders.json"):
            with open("reminders.json", "r") as file:
                self.reminders = json.load(file)
                # Convert any single reminder strings to lists
                self.reminders = {k: [v] if isinstance(v, str) else v for k, v in self.reminders.items()}
                # Ensure all reminder entries are lists
                self.reminders = {k: v for k, v in self.reminders.items() if isinstance(v, list)}
                self.reminders = {k: v for k, v in self.reminders.items() if v}

    # Function to add a reminder
    def add_reminder(self, date, reminder):
        if date in self.reminders:
            self.reminders[date].append(reminder)
        else:
            self.reminders[date] = [reminder]
        self.save_reminders()

    # Function to remove a reminder, allows the user to remove the reminder that they added on with a clear x symbol. Allows the user to undo their mistake.
    def remove_reminder(self, date, reminder):
        if date in self.reminders:
            if reminder in self.reminders[date]:
                self.reminders[date].remove(reminder)
                if not self.reminders[date]:  # If the list is empty, remove the key
                    del self.reminders[date]
                self.save_reminders()
                return True
        return False

    # Function to display the calendar for the selected month and year
    def display_calendar(self):
        for widget in self.days_frame.winfo_children():
            widget.destroy()

        try:
            year = int(self.year_entry.get())
            month = int(self.month_combobox.get())
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid year and month.")
            return

        cal = calendar.Calendar()
        days = cal.itermonthdays(year, month)

        # Display days of the week
        weekdays = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
        for col, weekday in enumerate(weekdays):
            day_label = Label(self.days_frame, text=weekday, bg="lightblue", width=10)
            day_label.grid(row=0, column=col, padx=1, pady=1, sticky="nsew")

        row = 1
        column = 0

        for day in days:
            if day != 0:
                date_str = f"{year}-{month:02d}-{day:02d}"
                day_frame = Frame(self.days_frame, bg="white", borderwidth=1, relief="solid")
                day_frame.grid(row=row, column=column, padx=1, pady=1, sticky="nsew")
                day_label = Label(day_frame, text=str(day), bg="white")
                day_label.pack(anchor='nw')
                reminder_button = Button(day_frame, text="+", command=lambda d=date_str: self.add_reminder_dialog(d))
                reminder_button.pack(anchor='ne')
                if date_str in self.reminders:
                    for reminder in self.reminders[date_str]:
                        reminder_frame = Frame(day_frame, bg="white")
                        reminder_frame.pack(anchor='sw', fill='x')
                        reminder_label = Label(reminder_frame, text=reminder, bg="white")
                        reminder_label.pack(side='left')
                        delete_button = Button(reminder_frame, text="x", command=lambda d=date_str, r=reminder: self.delete_reminder_dialog(d, r))
                        delete_button.pack(side='right')
            column += 1
            if column == 7:
                column = 0
                row += 1

        self.days_frame.grid_rowconfigure(list(range(row + 1)), weight=1)
        self.days_frame.grid_columnconfigure(list(range(7)), weight=1)

    # Function to show a dialog to add a reminder
    def add_reminder_dialog(self, date):
        dialog = Toplevel(self.window)
        dialog.title("Add Reminder")
        dialog.geometry("300x300")

        Label(dialog, text=f"Add reminder for {date}:").pack(pady=10)
        
        Label(dialog, text="Subject:").pack(pady=5)
        subject_entry = Entry(dialog)
        subject_entry.pack(pady=5)
        
        Label(dialog, text="Time (e.g., Period 4 or 14:00):").pack(pady=5)
        time_entry = Entry(dialog)
        time_entry.pack(pady=5)
        
        Label(dialog, text="Name of item:").pack(pady=5)
        name_entry = Entry(dialog)
        name_entry.pack(pady=5)
        
        Button(dialog, text="Add", command=lambda: self.add_reminder_from_dialog(date, subject_entry.get(), time_entry.get(), name_entry.get(), dialog)).pack(pady=10)

    # Function to handle adding reminder from the dialog
    def add_reminder_from_dialog(self, date, subject, time, name, dialog):
        if subject and time and name:
            reminder = f"{subject}, {time}, {name}"
            self.add_reminder(date, reminder)
            self.display_calendar()
            dialog.destroy()
        else:
            messagebox.showerror("Invalid Input", "Please fill in all fields.")

    # Function to show a dialog to delete a reminder
    def delete_reminder_dialog(self, date, reminder):
        dialog = Toplevel(self.window)
        dialog.title("Delete Reminder")
        dialog.geometry("300x200")

        Label(dialog, text=f"Are you sure you want to delete the reminder '{reminder}' on {date}?").pack(pady=5)
        Button(dialog, text="Delete", command=lambda: self.delete_reminder(date, reminder, dialog)).pack(pady=10)
        Button(dialog, text="Cancel", command=dialog.destroy).pack(pady=10)

    # Function to handle deleting a reminder from the dialog
    def delete_reminder(self, date, reminder, dialog):
        if self.remove_reminder(date, reminder):
            self.display_calendar()
            dialog.destroy()

if __name__ == "__main__":
    app = App()
