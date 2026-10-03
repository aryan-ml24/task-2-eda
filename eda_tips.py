"""
Task 2 - Exploratory Data Analysis (EDA)
Dataset: Tips dataset included in data/tips.csv
"""

from pathlib import Path
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

ROOT = Path(__file__).resolve().parent
df = pd.read_csv(ROOT / "data" / "tips.csv")
OUT = ROOT / "outputs"
OUT.mkdir(exist_ok=True)

print("Shape:", df.shape)
print("\nFirst rows:")
print(df.head())
print("\nData types:")
print(df.dtypes)
print("\nMissing values:")
print(df.isna().sum())
print("\nDuplicate rows:", df.duplicated().sum())

numeric_cols = df.select_dtypes(include=np.number).columns.tolist()

print("\nDescriptive statistics:")
print(df[numeric_cols].describe().round(2))

print("\nMedian:")
print(df[numeric_cols].median().round(2))

print("\nSkewness:")
print(df[numeric_cols].skew().round(2))

print("\nCorrelation:")
print(df[numeric_cols].corr().round(2))

sns.set_theme(style="whitegrid")

fig, axes = plt.subplots(2, 2, figsize=(11, 8))
for ax, col in zip(axes.flat, numeric_cols):
    ax.hist(df[col], bins=20)
    ax.set_title(f"Distribution of {col}")
    ax.set_xlabel(col)
    ax.set_ylabel("Frequency")
fig.tight_layout()
fig.savefig(OUT / "numeric_distributions.png", dpi=160)
plt.close(fig)

fig, axes = plt.subplots(2, 2, figsize=(11, 7))
for ax, col in zip(axes.flat, numeric_cols):
    sns.boxplot(x=df[col], ax=ax)
    ax.set_title(col)
fig.tight_layout()
fig.savefig(OUT / "boxplots.png", dpi=160)
plt.close(fig)

fig, ax = plt.subplots(figsize=(8, 6))
sns.heatmap(df[numeric_cols].corr(), annot=True, fmt=".2f", square=True, ax=ax)
ax.set_title("Correlation Matrix")
fig.tight_layout()
fig.savefig(OUT / "correlation_heatmap.png", dpi=160)
plt.close(fig)

fig, ax = plt.subplots(figsize=(8, 5))
sns.scatterplot(data=df, x="total_bill", y="tip", hue="time", style="sex", alpha=0.75, ax=ax)
ax.set_title("Tip vs Total Bill")
fig.tight_layout()
fig.savefig(OUT / "tip_vs_bill.png", dpi=160)
plt.close(fig)

print("\nEDA complete. Check outputs/.")
