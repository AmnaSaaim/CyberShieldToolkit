import tkinter as tk
import string

def check_password_strength(*args):
    password = password_entry.get()
    
    
    score = 0
    feedback = ""
    
    if len(password) >= 8:
        score += 1
    else:
        feedback += "• Make it 8+ characters\n"
        
    if any(c.isupper() for c in password):
        score += 1
    else:
        feedback += "• Add an uppercase letter\n"
        
    if any(c.islower() for c in password):
        score += 1
    else:
        feedback += "• Add a lowercase letter\n"
        
    if any(c.isdigit() for c in password):
        score += 1
    else:
        feedback += "• Add a number\n"
        
    special_chars = set(string.punctuation)
    if any(c in special_chars for c in password):
        score += 1
    else:
        feedback += "• Add a special character (e.g. @, #, $)\n"

    if not password:
        result_label.config(text="Enter a password", fg="gray")
        tips_label.config(text="")
        return

    if score <= 2:
        result_label.config(text="Strength: WEAK 🔴", fg="#e74c3c")
    elif score <= 4:
        result_label.config(text="Strength: MEDIUM 🟡", fg="#f39c12")
    else:
        result_label.config(text="Strength: STRONG 🟢", fg="#2ecc71")
        feedback = "Perfect! Your password is secure."

    tips_label.config(text=feedback)

root = tk.Tk()
root.title("Password Strength Analyzer")
root.geometry("400x350")
root.config(bg="#1e1e2e") 

title_lbl = tk.Label(root, text="CyberShield Password Tool", font=("Arial", 16, "bold"), bg="#1e1e2e", fg="#cdd6f4")
title_lbl.pack(pady=20)

input_label = tk.Label(root, text="Type your password below:", bg="#1e1e2e", fg="#a6adc8")
input_label.pack(pady=5)

password_var = tk.StringVar()
password_var.trace_add("write", check_password_strength) # Triggers check whenever text changes
password_entry = tk.Entry(root, textvariable=password_var, font=("Arial", 12), width=25, show="*")
password_entry.pack(pady=5)

result_label = tk.Label(root, text="Enter a password", font=("Arial", 14, "bold"), bg="#1e1e2e", fg="gray")
result_label.pack(pady=15)

tips_label = tk.Label(root, text="", font=("Arial", 10), bg="#1e1e2e", fg="#bac2de", justify="left")
tips_label.pack(pady=10)

root.mainloop()
