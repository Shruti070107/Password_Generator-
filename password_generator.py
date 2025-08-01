import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    try:
        length = int(length_var.get())
        if length <= 0:
            raise ValueError
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid positive number.")
        return

    chars = ""
    if var_upper.get():
        chars += string.ascii_uppercase
    if var_lower.get():
        chars += string.ascii_lowercase
    if var_digits.get():
        chars += string.digits
    if var_symbols.get():
        chars += string.punctuation

    if not chars:
        messagebox.showwarning("No Options Selected", "Please select at least one character type.")
        return

    password = ''.join(random.choice(chars) for _ in range(length))
    result_entry.delete(0, tk.END)
    result_entry.insert(0, password)
    evaluate_strength(password)

def copy_to_clipboard():
    password = result_entry.get()
    if password:
        root.clipboard_clear()
        root.clipboard_append(password)
        messagebox.showinfo("Copied", "Password copied to clipboard!")
    else:
        messagebox.showwarning("Empty", "No password to copy.")

def evaluate_strength(password):
    score = 0
    if any(c.islower() for c in password): score += 1
    if any(c.isupper() for c in password): score += 1
    if any(c.isdigit() for c in password): score += 1
    if any(c in string.punctuation for c in password): score += 1
    if len(password) >= 12: score += 1

    if score <= 2:
        strength_label.config(text="Strength: Weak", fg="red")
    elif score == 3 or score == 4:
        strength_label.config(text="Strength: Medium", fg="orange")
    else:
        strength_label.config(text="Strength: Strong", fg="green")

# GUI Setup
root = tk.Tk()
root.title("Password Generator")
root.geometry("400x420")
root.configure(bg="white")

tk.Label(root, text="🔐 Password Generator", font=("Arial", 16, "bold"), bg="white").pack(pady=10)

tk.Label(root, text="Password Length:", bg="white").pack()
length_var = tk.StringVar(value="12")
tk.Entry(root, textvariable=length_var, width=10, justify="center").pack(pady=5)

var_upper = tk.BooleanVar(value=True)
var_lower = tk.BooleanVar(value=True)
var_digits = tk.BooleanVar(value=True)
var_symbols = tk.BooleanVar(value=False)

tk.Checkbutton(root, text="Include Uppercase Letters", variable=var_upper, bg="white").pack()
tk.Checkbutton(root, text="Include Lowercase Letters", variable=var_lower, bg="white").pack()
tk.Checkbutton(root, text="Include Digits", variable=var_digits, bg="white").pack()
tk.Checkbutton(root, text="Include Special Characters", variable=var_symbols, bg="white").pack()

tk.Button(root, text="Generate Password", command=generate_password, bg="#4CAF50", fg="white", width=20).pack(pady=10)

result_entry = tk.Entry(root, font=("Arial", 12), justify='center', width=30)
result_entry.pack(pady=5)

tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard, bg="#2196F3", fg="white", width=20).pack()

strength_label = tk.Label(root, text="", font=("Arial", 12, "bold"), bg="white")
strength_label.pack(pady=10)

root.mainloop()
