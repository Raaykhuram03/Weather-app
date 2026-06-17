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

    def _build_metrics_panel(self) -> None:
        self.metrics_frame = tk.LabelFrame(
            self.root, text=" Current Weather ",
            font=("Helvetica", 11, "bold"),
            bg=self.BG_PANEL, fg=self.TEXT_MID, bd=1, relief="solid",
        )
        self.metrics_frame.pack(pady=10, padx=25, fill="x")
        self.metrics_label = tk.Label(
            self.metrics_frame,
            text="Enter a city name above and press Search.",
            font=("Helvetica", 11, "italic"),
            bg=self.BG_PANEL, fg=self.TEXT_DIM,
        )
        self.metrics_label.pack(pady=25)

    def _build_chart_panel(self) -> None:
        self.chart_frame = tk.LabelFrame(
            self.root, text=" 5-Day Temperature Forecast ",
            font=("Helvetica", 11, "bold"),
            bg=self.BG_PANEL, fg=self.TEXT_MID, bd=1, relief="solid",
        )
        self.chart_frame.pack(pady=10, padx=25, fill="both", expand=True)
        self.chart_placeholder = tk.Label(
             self.chart_frame,
              text="Chart will appear here after a search.",
               font=("Helvetica", 10, "italic"),
           bg=self.BG_PANEL, fg="#475569",
        )
        self.chart_placeholder.pack(pady=40)