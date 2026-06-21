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

        for day, temp in zip(days, temps):
            ax.annotate(
                f"{temp:.1f}°C", (day, temp),
                textcoords="offset points", xytext=(0, 10),
                ha="center", color=WeatherAnalytics.ANNOTATION,
                fontsize=8, fontweight="bold",
            )

        ax.tick_params(colors=WeatherAnalytics.LABEL, labelsize=9)
        ax.set_ylabel("°C", color=WeatherAnalytics.LABEL, fontsize=9)

        for spine_name, visible in [("bottom", True), ("left", True), ("top", False), ("right", False)]:
            spine = ax.spines[spine_name]
            spine.set_visible(visible)
            if visible:
                spine.set_color(WeatherAnalytics.SPINE)

        ax.grid(True, linestyle="--", alpha=0.15, color="#cbd5e1")
        fig.tight_layout()

        canvas = FigureCanvasTkAgg(fig, master=master_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill="both", expand=True)
        plt.close(fig)