import tkinter as tk
from tkinter import messagebox
import re

def check_password_strength():
    password = entry.get()
    length_error = len(password) < 8
    digit_error = re.search(r"\d", password) is None
    uppercase_error = re.search(r"[A-Z]", password) is None
    lowercase_error = re.search(r"[a-z]", password) is None
    symbol_error = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password) is None

    errors = {
        "Too short (minimum 8 characters)": length_error,
        "Missing a digit": digit_error,
        "Missing an uppercase letter": uppercase_error,
        "Missing a lowercase letter": lowercase_error,
        "Missing a special character": symbol_error,
    }

    if not any(errors.values()):
        messagebox.showinfo("Result", "✅ Strong password!")
    else:
        msg = "❌ Weak password:\n\n"
        for issue, flag in errors.items():
            if flag:
                msg += " - " + issue + "\n"
        messagebox.showwarning("Result", msg)

# Create GUI
root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("400x200")

label = tk.Label(root, text="Enter Password:", font=("Arial", 12))
label.pack(pady=10)

entry = tk.Entry(root, show="*", width=30, font=("Arial", 12))
entry.pack()

check_button = tk.Button(root, text="Check Strength", command=check_password_strength, font=("Arial", 12), bg="#4CAF50", fg="white")
check_button.pack(pady=20)

root.mainloop()
