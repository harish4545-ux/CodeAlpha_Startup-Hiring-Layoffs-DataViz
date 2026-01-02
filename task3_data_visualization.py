import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style="whitegrid")
plt.rcParams["figure.figsize"] = (10, 6)

df = pd.read_csv("startup_hiring_layoffs.csv")

print(df.head())
print(df.info())
print(df.isnull().sum())

df["Hiring_Count"] = df["Hiring_Count"].fillna(0)
df["Layoff_Count"] = df["Layoff_Count"].fillna(0)

df["Year"] = df["Year"].astype(int)
df["Hiring_Count"] = df["Hiring_Count"].astype(int)
df["Layoff_Count"] = df["Layoff_Count"].astype(int)

df["Net_Employment"] = df["Hiring_Count"] - df["Layoff_Count"]

yearly_summary = df.groupby("Year")[["Hiring_Count", "Layoff_Count", "Net_Employment"]].sum().reset_index()

sector_summary = df.groupby("Sector")[["Hiring_Count", "Layoff_Count"]].sum().reset_index()

city_layoffs = df.groupby("City")["Layoff_Count"].sum().reset_index().sort_values(by="Layoff_Count", ascending=False)

startup_layoffs = df.groupby("Startup")["Layoff_Count"].sum().reset_index().sort_values(by="Layoff_Count", ascending=False).head(10)

plt.figure()
plt.plot(yearly_summary["Year"], yearly_summary["Hiring_Count"], marker="o", label="Hiring")
plt.plot(yearly_summary["Year"], yearly_summary["Layoff_Count"], marker="o", label="Layoffs")
plt.title("Hiring vs Layoffs Trend (2023–2025)")
plt.xlabel("Year")
plt.ylabel("Employees")
plt.legend()
plt.tight_layout()
plt.show()

plt.figure()
sns.barplot(x="Year", y="Net_Employment", data=yearly_summary)
plt.title("Net Employment Change by Year")
plt.xlabel("Year")
plt.ylabel("Net Employment")
plt.tight_layout()
plt.show()

plt.figure()
sns.barplot(x="Hiring_Count", y="Sector", data=sector_summary.sort_values("Hiring_Count", ascending=False))
plt.title("Sector-wise Hiring (2023–2025)")
plt.xlabel("Hiring Count")
plt.ylabel("Sector")
plt.tight_layout()
plt.show()

plt.figure()
sns.barplot(x="Layoff_Count", y="City", data=city_layoffs.head(10))
plt.title("Top 10 Cities by Layoffs")
plt.xlabel("Layoff Count")
plt.ylabel("City")
plt.tight_layout()
plt.show()

df.to_csv("tableau_clean_data.csv", index=False)

yearly_summary.to_csv("tableau_yearly_summary.csv", index=False)

sector_summary.to_csv("tableau_sector_summary.csv", index=False)

city_layoffs.to_csv("tableau_city_layoffs.csv", index=False)

print("✅ TASK 3 COMPLETED: Tableau-ready CSV files created")
