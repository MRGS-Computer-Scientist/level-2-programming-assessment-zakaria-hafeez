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

        # Create login page
        self.login_page = LoginPage(self)
        self.show_login()

        self.window.mainloop()

    def show_login(self):
        self.login_page.pack(fill=BOTH, expand=True)

    def show_main_app(self):
        self.login_page.pack_forget()
        self.create_sidebar()
        self.create_content_frame()
        self.show_home()

    def create_sidebar(self):
        self.sidebar_frame = Frame(self.window, background="light gray", width=168)
        self.sidebar_frame.pack(side='left', fill=Y)

        self.sidebar_label = Label(self.sidebar_frame, text="Study Buddy", bg="light gray", font=self.title_font)
        self.sidebar_label.pack(pady=25, padx=25)

        self.home_button = Button(self.sidebar_frame, text="Home", height=2, width=10, bg='light gray', font=self.button_font,
                                  borderwidth=0, highlightthickness=0, command=self.show_home)
        self.home_button.pack(pady=5, padx=8)
        self.home_button.bind("<Enter>", self.on_enter)
        self.home_button.bind("<Leave>", self.on_leave)
    
        self.calendar_button = Button(self.sidebar_frame, text="Calendar", height=2, width=10, bg='light gray', font=self.button_font,
                                      borderwidth=0, highlightthickness=0, command=self.show_calendar)
        self.calendar_button.pack(pady=5, padx=8)
        self.calendar_button.bind("<Enter>", self.on_enter)
        self.calendar_button.bind("<Leave>", self.on_leave)

        self.spacer_frame = Frame(self.sidebar_frame, height=250, bg="light gray")
        self.spacer_frame.pack(pady=5, padx=5)

        self.exit_button = Button(self.sidebar_frame, text="Exit", height=2, width=10, background="light gray", font=self.exit_button_font,
                                  borderwidth=0, highlightthickness=0, command=self.exit)
        self.exit_button.pack(side='bottom', anchor='sw', pady=80, padx=60)
        self.exit_button.bind("<Enter>", self.on_enter_exit)
        self.exit_button.bind("<Leave>", self.on_leave_exit)

    def create_content_frame(self):
        self.content_frame = Frame(self.window, background="white")
        self.content_frame.pack(side='left', fill=BOTH, expand=True, padx=20, pady=20)

        self.reminders = {}
        self.load_reminders()

    def show_home(self):
        self.clear_content()

        self.name_label = Label(self.content_frame, text="Hi, 'Buddy!'", font=self.header_font, bg="white")
        self.name_label.pack(anchor='nw')

        self.upcoming_label = Label(self.content_frame, text="Upcoming Events", font=self.subheader_font, bg="white")
        self.upcoming_label.pack(anchor='nw', pady=(20, 10))

        self.assessments_frame = Frame(self.content_frame, bg="white")
        self.assessments_frame.pack(anchor='nw', pady=(0, 20))

        sorted_reminders = sorted(self.reminders.items())

        for date, reminders in sorted_reminders:
            for reminder in reminders:
                self.create_assessment_frame(date, *reminder.split(", "))

    def show_results(self):
        self.clear_content()

        results_label = Label(self.content_frame, text="Results", font=self.header_font, bg="white")
        results_label.pack(anchor='nw')

    def show_calendar(self):
        self.clear_content()

        self.calendar_label = Label(self.content_frame, text="Calendar", font=self.header_font, bg="white")
        self.calendar_label.pack(anchor='nw', pady=(20, 10))

        self.calendar_desc_label = Label(self.content_frame, text="Use this Calendar Functionality to keep track of your assessments as we will remind you of anything that is coming up soon. We will help you stay on top and on track with your work and we will help you stay organised if you were our calendar function.", bg="white", font=("Arial", 12), wraplength=700, anchor="w", justify="left")
        self.calendar_desc_label.pack(anchor='nw', pady=(10, 10))

        self.input_frame = Frame(self.content_frame, bg="white")
        self.input_frame.pack(pady=20)

        Label(self.input_frame, text="Year:", bg="white").grid(row=0, column=0)
        self.year_entry = Entry(self.input_frame)
        self.year_entry.insert(END, datetime.now().year)
        self.year_entry.grid(row=0, column=1)

        Label(self.input_frame, text="Month:", bg="white").grid(row=0, column=2)
        self.month_combobox = ttk.Combobox(self.input_frame, values=list(range(1, 13)))
        self.month_combobox.grid(row=0, column=3)
        self.month_combobox.current(datetime.today().month - 1)

        self.display_button = Button(self.input_frame, text="Display Calendar", command=self.display_calendar)
        self.display_button.grid(row=0, column=4, padx=10)

        self.days_frame = Frame(self.content_frame, bg="lightblue")
        self.days_frame.pack(expand=True, fill=BOTH, padx=20, pady=20)

        self.display_calendar()

    def create_assessment_frame(self, date, subject, time, name):
        frame = Frame(self.assessments_frame, bg="#86D8F2", height=200, width=800)
        frame.pack_propagate(False)
        frame.pack(fill='x', pady=10)

        date_label = Label(frame, text=date, font=self.content_font, bg="#86D8F2")
        date_label.pack(side='left', padx=50, pady=20)

        subject_label = Label(frame, text=subject, font=self.content_font, bg="#86D8F2")
        subject_label.pack(side='left', padx=50, pady=20)

        time_label = Label(frame, text=time, font=self.content_font, bg="#86D8F2")
        time_label.pack(side='left', padx=50, pady=20)

        name_label = Label(frame, text=name, font=self.content_font, bg="#86D8F2")
        name_label.pack(side='left', padx=50, pady=20)

    def clear_content(self):
        for widget in self.content_frame.winfo_children():
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

    def save_reminders(self):
        with open("reminders.json", "w") as file:
            json.dump(self.reminders, file)

    def load_reminders(self):
        if os.path.exists("reminders.json"):
            with open("reminders.json", "r") as file:
                self.reminders = json.load(file)
                self.reminders = {k: [v] if isinstance(v, str) else v for k, v in self.reminders.items()}
                self.reminders = {k: v for k, v in self.reminders.items() if isinstance(v, list)}
                self.reminders = {k: v for k, v in self.reminders.items() if v}

    def add_reminder(self, date, reminder):
        if date in self.reminders:
            self.reminders[date].append(reminder)
        else:
            self.reminders[date] = [reminder]
        self.save_reminders()
    #This allows the user to delete a reminder that they have set accidentally/ no longer need.
    def remove_reminder(self, date, reminder):
        if date in self.reminders:
            if reminder in self.reminders[date]:
                self.reminders[date].remove(reminder)
                if not self.reminders[date]:
                    del self.reminders[date]
                self.save_reminders()
                return True
        return False

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

    def add_reminder_from_dialog(self, date, subject, time, name, dialog):
        if subject and time and name:
            reminder = f"{subject}, {time}, {name}"
            self.add_reminder(date, reminder)
            self.display_calendar()
            dialog.destroy()
        else:
            messagebox.showerror("Invalid Input", "Please fill in all fields.")

    def delete_reminder_dialog(self, date, reminder):
        dialog = Toplevel(self.window)
        dialog.title("Delete Reminder")
        dialog.geometry("300x200")

        Label(dialog, text=f"Are you sure you want to delete the reminder '{reminder}' on {date}?").pack(pady=5)
        Button(dialog, text="Delete", command=lambda: self.delete_reminder(date, reminder, dialog)).pack(pady=10)
        Button(dialog, text="Cancel", command=dialog.destroy).pack(pady=10)

    def delete_reminder(self, date, reminder, dialog):
        if self.remove_reminder(date, reminder):
            self.display_calendar()
            dialog.destroy()


class LoginPage(Frame):

    def __init__(self, app):
        super().__init__(app.window)
        self.app = app
        self.config(bg="white")

        self.credentials_file = "credentials.json"
        self.credentials = self.load_credentials()

        self.header_font = font.Font(family="Arial", size=24, weight="bold")
        self.subheader_font = font.Font(family="Arial", size=18)
        self.button_font = font.Font(family="Georgia", size=14)
        self.content_font = font.Font(family="Arial", size=14)

        self.create_login_frame()

    def create_login_frame(self):
        self.login_frame = Frame(self, bg="white")
        self.login_frame.pack(expand=True)

        self.login_label = Label(self.login_frame, text="Login", font=self.header_font, bg="white")
        self.login_label.pack(pady=20)

        Label(self.login_frame, text="Name:", font=self.content_font, bg="white").pack(pady=5)
        self.username_entry = Entry(self.login_frame, font=self.content_font)
        self.username_entry.pack(pady=5)

        Label(self.login_frame, text="Password:", font=self.content_font, bg="white").pack(pady=5)
        self.password_entry = Entry(self.login_frame, show='*', font=self.content_font)
        self.password_entry.pack(pady=5)

        self.login_button = Button(self.login_frame, text="Login", font=self.button_font, command=self.login)
        self.login_button.pack(pady=20)

        self.signup_label = Label(self.login_frame, text="Don't have an account? Sign up here.", font=self.subheader_font, bg="white", fg="blue", cursor="hand2")
        self.signup_label.pack(pady=10)
        self.signup_label.bind("<Button-1>", self.show_signup_frame)

    def show_signup_frame(self, event=None):
        self.login_frame.pack_forget()
        self.signup_frame = Frame(self, bg="white")
        self.signup_frame.pack(expand=True)

        self.signup_label = Label(self.signup_frame, text="Sign Up", font=self.header_font, bg="white")
        self.signup_label.pack(pady=20)

        Label(self.signup_frame, text="Username:", font=self.content_font, bg="white").pack(pady=5)
        self.signup_username_entry = Entry(self.signup_frame, font=self.content_font)
        self.signup_username_entry.pack(pady=5)

        Label(self.signup_frame, text="Password:", font=self.content_font, bg="white").pack(pady=5)
        self.signup_password_entry = Entry(self.signup_frame, show='*', font=self.content_font)
        self.signup_password_entry.pack(pady=5)

        self.signup_button = Button(self.signup_frame, text="Sign Up", font=self.button_font, command=self.signup)
        self.signup_button.pack(pady=20)

        self.back_to_login_label = Label(self.signup_frame, text="Already have an account? Login here.", font=self.subheader_font, bg="white", fg="blue", cursor="hand2")
        self.back_to_login_label.pack(pady=10)
        self.back_to_login_label.bind("<Button-1>", self.show_login_frame)

    def show_login_frame(self, event=None):
        self.signup_frame.pack_forget()
        self.create_login_frame()

    def load_credentials(self):
        if os.path.exists(self.credentials_file):
            with open(self.credentials_file, "r") as file:
                return json.load(file)
        return {}

    def save_credentials(self):
        with open(self.credentials_file, "w") as file:
            json.dump(self.credentials, file)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if username in self.credentials and self.credentials[username] == password:
            messagebox.showinfo("Login Successful", "Welcome!")
            self.app.show_main_app()
        else:
            messagebox.showerror("Login Failed", "Invalid username or password.")

    def signup(self):
        username = self.signup_username_entry.get()
        password = self.signup_password_entry.get()

        if username and password:
            if username in self.credentials:
                messagebox.showerror("Sign Up Failed", "Username already exists.")
            else:
                self.credentials[username] = password
                self.save_credentials()
                messagebox.showinfo("Sign Up Successful", "Account created. Please login.")
                self.show_login_frame()
        else:
            messagebox.showerror("Sign Up Failed", "Please fill in all fields.")

if __name__ == "__main__":
    app = App()
