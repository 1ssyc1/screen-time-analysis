"""
Screen Time Analysis: Before vs. After
Requirements: pip install pandas matplotlib
"""

import pandas as pd
import matplotlib.pyplot as plt

# 1. Load data (hours; 15 mins = 0.25)
df = pd.DataFrame({
    "app":    ["TikTok", "Instagram", "Messenger", "Facebook"],
    "before": [12, 8, 4, 0.25],
    "after":  [3, 0.25, 2.5, 0.25],
})

# 2. Calculate changes
df["change_hrs"] = df["after"] - df["before"]
df["pct_change"] = (df["change_hrs"] / df["before"] * 100).round(1)

# 3. Totals
total_before = df["before"].sum()
total_after = df["after"].sum()
total_pct = (total_after - total_before) / total_before * 100

# 4. Print report
print(df.to_string(index=False))
print(f"\nTotal before: {total_before} hrs")
print(f"Total after:  {total_after} hrs")
print(f"Overall change: {total_pct:.1f}%")

# 5. Chart
ax = df.plot(x="app", y=["before", "after"], kind="bar",
             color=["#e4572e", "#2e86ab"], figsize=(9, 5))
ax.set_title("Screen Time: Before vs. After")
ax.set_ylabel("Hours")
ax.set_xlabel("")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("screen_time_chart.png", dpi=150)
plt.show()