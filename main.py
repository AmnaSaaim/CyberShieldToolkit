import tkinter as tk
from tkinter import ttk, messagebox


class SecurityDashboard:

    def __init__(self, root):
        self.root = root
        self.root.title("Cybersecurity Toolkit")
        self.root.geometry("900x600")
        self.root.resizable(False, False)

        # Theme
        self.style = ttk.Style()
        self.style.theme_use("clam")

        # Title
        title_label = tk.Label(
            root,
            text="Cybersecurity Toolkit",
            font=("Arial", 18, "bold"),
            pady=15
        )
        title_label.pack()

        # Notebook
        self.notebook = ttk.Notebook(root)
        self.notebook.pack(expand=True, fill="both", padx=10, pady=10)

        # Tabs
        self.tab_analyzer = ttk.Frame(self.notebook)
        self.tab_generator = ttk.Frame(self.notebook)
        self.tab_hash = ttk.Frame(self.notebook)
        self.tab_vault = ttk.Frame(self.notebook)
        self.tab_about = ttk.Frame(self.notebook)

        self.notebook.add(self.tab_analyzer, text="Password Analyzer")
        self.notebook.add(self.tab_generator, text="Password Generator")
        self.notebook.add(self.tab_hash, text="Hash Generator")
        self.notebook.add(self.tab_vault, text="Credential Vault")
        self.notebook.add(self.tab_about, text="About")

        # Setup tabs
        self.setup_analyzer_tab()
        self.setup_generator_tab()
        self.setup_hash_tab()
        self.setup_vault_tab()
        self.setup_about_tab()

        # Status bar
        status = tk.Label(
            root,
            text="CyberShield Toolkit v1.0 | OSSD Final Project",
            bd=1,
            relief=tk.SUNKEN,
            anchor=tk.W
        )
        status.pack(side=tk.BOTTOM, fill=tk.X)

    # Member 2
    def setup_analyzer_tab(self):
        label = tk.Label(
            self.tab_analyzer,
            text="Password Strength Analyzer (Member 2)",
            font=("Arial", 12)
        )
        label.pack(pady=20)

        btn = ttk.Button(
            self.tab_analyzer,
            text="Analyze Password",
            command=lambda: messagebox.showinfo(
                "Module",
                "Password Analyzer Module Coming Soon"
            )
        )
        btn.pack()

    # Member 3
    def setup_generator_tab(self):
        label = tk.Label(
            self.tab_generator,
            text="Password Generator (Member 3)",
            font=("Arial", 12)
        )
        label.pack(pady=20)

        btn = ttk.Button(
            self.tab_generator,
            text="Generate Password",
            command=lambda: messagebox.showinfo(
                "Module",
                "Password Generator Module Coming Soon"
            )
        )
        btn.pack()

    # Member 4
    def setup_hash_tab(self):
        label = tk.Label(
            self.tab_hash,
            text="Hash Generator (Member 4)",
            font=("Arial", 12)
        )
        label.pack(pady=20)

        btn = ttk.Button(
            self.tab_hash,
            text="Generate Hash",
            command=lambda: messagebox.showinfo(
                "Module",
                "Hash Generator Module Coming Soon"
            )
        )
        btn.pack()

    # Member 5
    def setup_vault_tab(self):
        label = tk.Label(
            self.tab_vault,
            text="Credential Vault & URL Checker (Member 5)",
            font=("Arial", 12)
        )
        label.pack(pady=20)

        btn = ttk.Button(
            self.tab_vault,
            text="Open Vault",
            command=lambda: messagebox.showinfo(
                "Module",
                "Vault Module Coming Soon"
            )
        )
        btn.pack()

    # About Tab
    def setup_about_tab(self):
        info = """
CyberShield Toolkit

Open Source Software Development Project

Modules:
• Password Analyzer
• Password Generator
• Hash Generator
• Credential Vault

Team Members:
Member 1 - Dashboard & Integration
Member 2 - Password Analyzer
Member 3 - Password Generator
Member 4 - Hash Generator
Member 5 - Vault & URL Checker
"""

        label = tk.Label(
            self.tab_about,
            text=info,
            justify="left",
            font=("Arial", 11)
        )
        label.pack(pady=20)


if __name__ == "__main__":
    root = tk.Tk()
    app = SecurityDashboard(root)
    root.mainloop()