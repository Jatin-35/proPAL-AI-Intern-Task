import pandas as pd
from datetime import datetime
import os


class MetricsLogger:
    def __init__(self, filename="call_metrics.xlsx"):
        self.filename = filename
        self.metrics = []

    def log(self, session_id, eou_delay, ttft, ttfb, total_latency):
        self.metrics.append({
            "Session ID": session_id,
            "EOU Delay (ms)": eou_delay,
            "TTFT (ms)": ttft,
            "TTFB (ms)": ttfb,
            "Total Latency (ms)": total_latency,
            "Timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })

    def save(self):
        df = pd.DataFrame(self.metrics)
        if os.path.exists(self.filename):
            existing_df = pd.read_excel(self.filename)
            df = pd.concat([existing_df, df], ignore_index=True)
        df.to_excel(self.filename, index=False)
        print(f"Metrics saved to {self.filename}")
        