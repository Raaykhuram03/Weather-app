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