import tkinter as tk
from tkinter import messagebox

def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x_coordinate = int((screen_width / 2) - (width / 2))
    y_coordinate = int((screen_height / 2) - (height / 2))
    window.geometry(f"{width}x{height}+{x_coordinate}+{y_coordinate}")

def handle_login():
    username = username_entry.get()
    password = password_entry.get()
    if username == "admin" and password == "password":
        messagebox.showinfo("Login Successful", "Welcome to the Payroll System!")
        root.destroy()
    else:
        messagebox.showerror("Login Failed", "Invalid username or password!")

root = tk.Tk()
root.title("Payroll System Login")
root.configure(bg="white")

# Center the window
window_width = 400
window_height = 300
center_window(root, window_width, window_height)

# Header
header = tk.Label(root, text="LOGIN", font=("Arial", 20, "bold"), bg="white", fg="darkblue")
header.pack(pady=20)

# Username
username_label = tk.Label(root, text="Username:", font=("Arial", 12), bg="white", fg="black")
username_label.pack(anchor="w", padx=40)
username_entry = tk.Entry(root, font=("Arial", 12), width=30)
username_entry.pack(pady=5)

# Password
password_label = tk.Label(root, text="Password:", font=("Arial", 12), bg="white", fg="black")
password_label.pack(anchor="w", padx=40)
password_entry = tk.Entry(root, font=("Arial", 12), width=30, show="*")
password_entry.pack(pady=5)

# Login Button
login_button = tk.Button(
    root,
    text="Login",
    font=("Arial", 12, "bold"),
    bg="cornflowerblue",
    fg="white",
    width=15,
    command=handle_login
)
login_button.pack(pady=20)

# Footer
footer = tk.Label(root, text="© Ramirez Payroll System", font=("Arial", 10), bg="white", fg="gray")
footer.pack(side="bottom", pady=10)

root.mainloop()
