import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import ticker
from mpl_toolkits.mplot3d import Axes3D

# -------------------------
# Data
# -------------------------
data = [
    # Age 18
    (18, 5_000, 95), (18, 25_000, 90), (18, 100_000, 85),
    (18, 500_000, 80), (18, 1_000_000, 75),
    (18, 5_000_000, 70), (18, 20_000_000, 65), (18, 50_000_000, 60),

    # Age 30
    (30, 5_000, 85), (30, 25_000, 90), (30, 100_000, 85),
    (30, 500_000, 80), (30, 1_000_000, 75),
    (30, 5_000_000, 70), (30, 20_000_000, 65), (30, 50_000_000, 60),

    # Age 45
    (45, 5_000, 70), (45, 25_000, 72), (45, 100_000, 75),
    (45, 500_000, 70), (45, 1_000_000, 65),
    (45, 5_000_000, 60), (45, 20_000_000, 55), (45, 50_000_000, 52),

    # Age 60
    (60, 5_000, 50), (60, 25_000, 52), (60, 100_000, 55),
    (60, 500_000, 60), (60, 1_000_000, 55),
    (60, 5_000_000, 50), (60, 20_000_000, 45), (60, 50_000_000, 40),

    # Age 70 (new)
    (70, 5_000, 40), (70, 25_000, 42), (70, 100_000, 45),
    (70, 500_000, 48), (70, 1_000_000, 45),
    (70, 5_000_000, 42), (70, 20_000_000, 38), (70, 50_000_000, 35),

    # Age 75
    (75, 5_000, 35), (75, 25_000, 38), (75, 100_000, 40),
    (75, 500_000, 50), (75, 1_000_000, 45),
    (75, 5_000_000, 40), (75, 20_000_000, 35), (75, 50_000_000, 32),
]


df = pd.DataFrame(data, columns=["Age", "Portfolio", "RiskPct"])

# -------------------------
# Heatmap (Best Overall View)
# -------------------------
heatmap = df.pivot(index="Portfolio", columns="Age", values="RiskPct")

plt.figure(figsize=(10, 6))
plt.imshow(heatmap, aspect="auto", origin="lower")
plt.colorbar(label="Risk Assets (%)")

plt.xticks(range(len(heatmap.columns)), heatmap.columns)
plt.yticks(range(len(heatmap.index)), [f"${v:,.0f}" for v in heatmap.index])

plt.xlabel("Age")
plt.ylabel("Portfolio Size")
plt.title("Ideal Risk Allocation by Age and Portfolio Size")

plt.tight_layout()
plt.show()

# -------------------------
# 3D Surface Plot (Creator / Presentation Friendly)
# -------------------------
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection="3d")

x = df["Age"].values
y = np.log10(df["Portfolio"].values)
z = df["RiskPct"].values

ax.plot_trisurf(x, y, z)

ax.set_xlabel("Age")
ax.set_ylabel("Log10 Portfolio Size")
ax.set_zlabel("Risk Assets (%)")
ax.set_title("Risk Tolerance Surface")

ax.yaxis.set_major_formatter(
    ticker.FuncFormatter(lambda val, _: f"${int(10**val):,}")
)

plt.tight_layout()
plt.show()
