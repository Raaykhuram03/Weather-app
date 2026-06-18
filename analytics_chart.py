import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class WeatherAnalytics:
    BG         = "#0f172a"
    SPINE      = "#334155"
    LINE       = "#38bdf8"
    LABEL      = "#94a3b8"
    ANNOTATION = "#cbd5e1"

    @staticmethod
    def embed_temperature_trend(master_frame: tk.Frame, forecast_data: list[dict]) -> None:
        for widget in master_frame.winfo_children():
            widget.destroy()