import tkinter as tk
from tkinter import ttk, messagebox

class SecurityDashboard:
    def __init__(self, root):
        self.root = root
        self.root.title("Multi-Tool Security Dashboard")
        self.root.geometry("700x500")
        self.root.resizable(False, False)
        
        # --- Theme / Styling ---
        self.style = ttk.Style()
        self.style.theme_use("clam")
        
        # --- Main Title ---
        title_label = tk.Label(
            root, 
            text="Cybersecurity Multi-Tool Dashboard", 
            font=("Arial", 18, "bold"), 
            pady=15
        )
        title_label.pack()

        # --- Tab Control (The Core Integration Hub) ---
        self.notebook = ttk.Notebook(root)
        self.notebook.pack(expand=True, fill="both", padx=10, pady=10)
        
        # Create tabs for each team member's module
        self.tab_analyzer = ttk.Frame(self.notebook)
        self.tab_generator = ttk.Frame(self.notebook)
        self.tab_hash = ttk.Frame(self.notebook)
        self.tab_vault = ttk.Frame(self.notebook)
        
        self.notebook.add(self.tab_analyzer, text="Password Analyzer")
        self.notebook.add(self.tab_generator, text="Password Generator")
        self.notebook.add(self.tab_hash, text="Hash Generator")
        self.notebook.add(self.tab_vault, text="Credential Vault / URL")

        # Initialize the UI placeholders for each tab
        self.setup_analyzer_tab()
        self.setup_generator_tab()
        self.setup_hash_tab()
        self.setup_vault_tab()

    # --- MEMBER 2 PLACEHOLDER ---
    def setup_analyzer_tab(self):
        label = tk.Label(self.tab_analyzer, text="Password Strength Analyzer (Member 2 Component)", font=("Arial", 12))
        label.pack(pady=20)
        btn = ttk.Button(self.tab_analyzer, text="Analyze (Stub)", command=lambda: messagebox.showinfo("Stub", "Member 2 logic goes here"))
        btn.pack()

    # --- MEMBER 3 PLACEHOLDER ---
    def setup_generator_tab(self):
        label = tk.Label(self.tab_generator, text="Secure Password Generator (Member 3 Component)", font=("Arial", 12))
        label.pack(pady=20)
        btn = ttk.Button(self.tab_generator, text="Generate (Stub)", command=lambda: messagebox.showinfo("Stub", "Member 3 logic goes here"))
        btn.pack()

    # --- MEMBER 4 PLACEHOLDER ---
    def setup_hash_tab(self):
        label = tk.Label(self.tab_hash, text="Cryptographic Hash Generator (Member 4 Component)", font=("Arial", 12))
        label.pack(pady=20)
        btn = ttk.Button(self.tab_hash, text="Hash Data (Stub)", command=lambda: messagebox.showinfo("Stub", "Member 4 logic goes here"))
        btn.pack()

    # --- MEMBER 5 PLACEHOLDER ---
    def setup_vault_tab(self):
        label = tk.Label(self.tab_vault, text="URL Checker & SQLite Vault (Member 5 Component)", font=("Arial", 12))
        label.pack(pady=20)
        btn = ttk.Button(self.tab_vault, text="Access Vault (Stub)", command=lambda: messagebox.showinfo("Stub", "Member 5 logic goes here"))
        btn.pack()

if __name__ == "__main__":
    root = tk.Tk()
    app = SecurityDashboard(root)
    root.mainloop()