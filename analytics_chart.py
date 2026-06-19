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
        if not forecast_data:
            tk.Label(
                master_frame,
                text="No forecast data available.",
                bg=WeatherAnalytics.BG, fg=WeatherAnalytics.LABEL,
                font=("Helvetica", 10, "italic"),
            ).pack(pady=20)
            return

        days  = [item["day"][:3] for item in forecast_data]
        temps = [item["temp"]    for item in forecast_data]

        fig, ax = plt.subplots(figsize=(5, 2.4), facecolor=WeatherAnalytics.BG)
        ax.set_facecolor(WeatherAnalytics.BG)

        ax.plot(days, temps, marker="o", color=WeatherAnalytics.LINE, linewidth=2.5, markersize=6)

        temp_min = min(temps)
        temp_max = max(temps)
        padding  = max(2.0, (temp_max - temp_min) * 0.25)
        ax.set_ylim(temp_min - padding, temp_max + padding)    