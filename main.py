import tkinter as tk
from tkinter import messagebox

# Note: Ensure Databases.db exists in your local environment.
# Commented out if you need to run tests without the database module.
try:
    from Databases.db import initialize_database, log_action
except ImportError:
    # Fallback dummy functions if Databases folder isn't configured yet
    def initialize_database(): pass
    def log_action(action): print(f"Log: {action}")

class SecurityDashboard:
    def __init__(self, root):
        self.root = root
        self.root.title("CyberToolkit")
        self.root.geometry("900x600")
        self.root.resizable(False, False)

        initialize_database()

        # =========================
        # 🎨 THEME
        # =========================
        self.bg = "#0b1020"
        self.sidebar_bg = "#111a33"
        self.panel_bg = "#0f1a2e"
        self.purple = "#6d28d9"
        self.light_blue = "#38bdf8"
        self.text = "#e2e8f0"
        self.active_btn = "#1f2a4a"

        self.root.configure(bg=self.bg)

        # Track active button
        self.active_button = None

        # Start main page
        self.show_main_page()

    # =========================
    # 🏠 MAIN PAGE
    # =========================
    def show_main_page(self):
        self.clear_window()

        main = tk.Frame(self.root, bg=self.bg)
        main.pack(fill="both", expand=True)

        tk.Label(
            main,
            text="🛡 CyberToolkit",
            font=("Arial", 26, "bold"),
            bg=self.bg,
            fg=self.light_blue
        ).pack(pady=50)

        tk.Label(
            main,
            text="Cybersecurity Learning & Toolkit Platform",
            font=("Arial", 13),
            bg=self.bg,
            fg=self.text
        ).pack()

        tk.Button(
            main,
            text="Enter System",
            font=("Arial", 12, "bold"),
            bg=self.purple,
            fg="white",
            relief="flat",
            padx=25,
            pady=10,
            command=self.show_dashboard
        ).pack(pady=40)

    # =========================
    # 🧭 DASHBOARD
    # =========================
    def show_dashboard(self):
        self.clear_window()

        # Layout
        self.container = tk.Frame(self.root, bg=self.bg)
        self.container.pack(fill="both", expand=True)

        self.sidebar = tk.Frame(self.container, bg=self.sidebar_bg, width=200)
        self.sidebar.pack(side="left", fill="y")

        self.main_area = tk.Frame(self.container, bg=self.panel_bg)
        self.main_area.pack(side="right", fill="both", expand=True)

        # =========================
        # TOP HEADER (REAL SOFTWARE FEEL)
        # =========================
        self.header = tk.Frame(self.main_area, bg="#0d1528", height=50)
        self.header.pack(fill="x")

        tk.Label(
            self.header,
            text="CyberToolkit Dashboard",
            bg="#0d1528",
            fg=self.light_blue,
            font=("Arial", 12, "bold")
        ).pack(side="left", padx=15)

        # =========================
        # SIDEBAR TITLE
        # =========================
        tk.Label(
            self.sidebar,
            text="CYBER TOOLKIT",
            bg=self.sidebar_bg,
            fg=self.light_blue,
            font=("Arial", 14, "bold")
        ).pack(pady=20)

        # =========================
        # NAV BUTTONS
        # =========================
        self.btn_home = self.create_nav_button("Home", self.show_home)
        self.btn_analyzer = self.create_nav_button("Password Analyzer", self.show_analyzer)
        self.btn_generator = self.create_nav_button("Password Generator", self.show_generator)
        self.btn_hash = self.create_nav_button("Hash Generator", self.show_hash)
        self.btn_vault = self.create_nav_button("Credential Vault", self.show_vault)
        self.btn_about = self.create_nav_button("About", self.show_about)
        self.create_nav_button("Exit", self.root.quit, danger=True)

        self.show_home()

    # =========================
    # BUTTON CREATION (WITH ACTIVE STATE)
    # =========================
    def create_nav_button(self, text, command, danger=False):
        color = "#ef4444" if danger else self.purple

        btn = tk.Button(
            self.sidebar,
            text=text,
            command=lambda b=text: self.set_active(b, command),
            bg=color,
            fg="white",
            activebackground=self.light_blue,
            activeforeground="black",
            relief="flat",
            font=("Arial", 10, "bold"),
            padx=10,
            pady=8,
            width=20
        )
        btn.pack(pady=5)
        return btn

    # =========================
    # ACTIVE BUTTON STYLE
    # =========================
    def set_active(self, name, command):
        self.clear_main()

        # Reset all sidebar buttons visually
        for widget in self.sidebar.winfo_children():
            if isinstance(widget, tk.Button):
                # Ensure we don't accidentally turn the red exit button purple
                if widget.cget("text") == "Exit":
                    widget.configure(bg="#ef4444")
                else:
                    widget.configure(bg=self.purple)

        # Run page
        command()

    # =========================
    # CLEAR FUNCTIONS
    # =========================
    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def clear_main(self):
        for widget in self.main_area.winfo_children():
            if widget != self.header:
                widget.destroy()

    # =========================
    # 🏠 HOME PAGE (REAL SOFTWARE DASHBOARD LOOK)
    # =========================
    def show_home(self):
        tk.Label(
            self.main_area,
            text="Welcome Back",
            font=("Arial", 20, "bold"),
            bg=self.panel_bg,
            fg=self.text
        ).pack(pady=20)

        # Cards row
        card_frame = tk.Frame(self.main_area, bg=self.panel_bg)
        card_frame.pack(pady=20)

        self.make_card(card_frame, "Modules", "4 Active", 0)
        self.make_card(card_frame, "Security", "Stable", 1)
        self.make_card(card_frame, "Version", "1.0", 2)

        # Status panel
        status = tk.Frame(self.main_area, bg=self.sidebar_bg, padx=20, pady=15)
        status.pack(pady=30, fill="x", padx=20)

        tk.Label(
            status,
            text="System Status: ONLINE • All modules loaded successfully",
            bg=self.sidebar_bg,
            fg=self.light_blue
        ).pack()

    # =========================
    # CARD DESIGN
    # =========================
    def make_card(self, parent, title, value, col):
        frame = tk.Frame(parent, bg="#151f3a", padx=20, pady=15)
        frame.grid(row=0, column=col, padx=10)

        tk.Label(
            frame,
            text=title,
            bg="#151f3a",
            fg=self.light_blue,
            font=("Arial", 10, "bold")
        ).pack()

        tk.Label(
            frame,
            text=value,
            bg="#151f3a",
            fg="white",
            font=("Arial", 12, "bold")
        ).pack()

    # =========================
    # PAGES
    # =========================
    def show_analyzer(self):
        self.clear_main()
        log_action("Opened Password Analyzer")
        self.simple_page("Password Analyzer")

    def show_generator(self):
        self.clear_main()
        log_action("Opened Password Generator")
        self.simple_page("Password Generator")

    def show_hash(self):
        self.clear_main()
        log_action("Opened Hash Generator")
        self.simple_page("Hash Generator")

    def show_vault(self):
        self.clear_main()
        log_action("Opened Credential Vault")
        self.simple_page("Credential Vault")

    def show_about(self):
        self.clear_main()
        log_action("Opened About Page")
        
        about_text = (
            "CyberToolkit Project\n\n"
            "Modules:\n"
            "• Password Analyzer\n"
            "• Password Generator\n"
            "• Hash Generator\n"
            "• Credential Vault\n\n"
            "OSSD FINAL SEMESTER PROJECT"
        )
        
        tk.Label(
            self.main_area,
            text=about_text,
            justify="left",
            bg=self.panel_bg,
            fg=self.text,
            font=("Arial", 11)
        ).pack(pady=20)

    # =========================
    # TEMPLATE PAGE
    # =========================
    def simple_page(self, title):
        tk.Label(
            self.main_area,
            text=title,
            font=("Arial", 16, "bold"),
            bg=self.panel_bg,
            fg=self.text
        ).pack(pady=20)

        tk.Button(
            self.main_area,
            text="Coming Soon",
            bg=self.purple,
            fg="white",
            relief="flat",
            command=lambda: messagebox.showinfo("Info", "Module Under Development")
        ).pack(pady=10)


# =========================
# RUN APPLICATION
# =========================
if __name__ == "__main__":
    root = tk.Tk()
    app = SecurityDashboard(root)
    root.mainloop()