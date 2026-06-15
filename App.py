import sys
import tkinter as tk
from tkinter import messagebox

import requests
from dotenv import load_dotenv

from api_handler import WeatherAPI
from analytics_chart import WeatherAnalytics

load_dotenv()


class WeatherAppUI:
    BG_DARK    = "#1e293b"
    BG_PANEL   = "#0f172a"
    ACCENT     = "#2563eb"
    ACCENT_HV  = "#1d4ed8"
    TEXT_DIM   = "#64748b"
    TEXT_MID   = "#94a3b8"
    TEXT_BRIGHT = "#cbd5e1"

    def __init__(self, root: tk.Tk) -> None:
        self.root = root
        self.root.title("Weather Dashboard")
        self.root.geometry("700x680")
        self.root.configure(bg=self.BG_DARK)
        try:
            self.api_engine = WeatherAPI()
        except ValueError as err:
            messagebox.showerror("Initialisation Error", str(err))
            sys.exit(1)
       self._build_layout()

    def _build_layout(self) -> None:

      self._build_search_bar()
       self._build_metrics_panel()
       self._build_chart_panel()

       def _build_search_bar(self) -> None:

       frame = tk.Frame(self.root, bg=self.BG_DARK)
        frame.pack(pady=20)
        self.city_entry = tk.Entry(
              frame, font=("Helvetica", 14), width=22,
             bd=0, highlightthickness=1, highlightbackground="#475569",
        )

       self.city_entry.grid(row=0, column=0, padx=10, ipady=4)
        self.city_entry.focus()
         self.city_entry.bind("<Return>", lambda _e: self._run_search())
        tk.Button(
            frame, text="Search", font=("Helvetica", 11, "bold"),
             bg=self.ACCENT, fg="white",
             activebackground=self.ACCENT_HV, activeforeground="white",
             bd=0, padx=15, cursor="hand2",
              command=self._run_search,
        ).grid(row=0, column=1)

