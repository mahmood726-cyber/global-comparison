import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

# Data Sources: Integrated Regional Syntheses (IHME + World Bank)
# 1. Americas (from summary_report.md)
# 2. Asia-Africa (from atlas_2026.md)

def create_global_report():
    data = {
        "Region": ["North America", "South America", "Asia", "Africa"],
        "Continent_Group": ["Americas", "Americas", "Asia-Africa", "Asia-Africa"],
        "Pop (M)": [367, 426, 4700, 1400], # Asia/Africa pops approx 2022
        "Life Expectancy": [80.6, 77.1, 73.0, 64.4],
        "GDP per Capita (USD)": [65000, 9500, 9793, 2899], # North America approx
        "Basic Water Access (%)": [99.0, 94.0, 95.7, 75.8] # Americas approx
    }
    
    df = pd.DataFrame(data)
    
    # 1. Plot Life Expectancy Comparison
    plt.figure(figsize=(10, 6))
    sns.barplot(x="Region", y="Life Expectancy", hue="Continent_Group", data=df)
    plt.title("Global Life Expectancy Comparison (2021-2022)")
    plt.ylabel("Years")
    plt.ylim(60, 85)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.savefig("global_life_expectancy.png")
    
    # 2. Plot Economic Divide (Log Scale)
    plt.figure(figsize=(10, 6))
    g = sns.barplot(x="Region", y="GDP per Capita (USD)", hue="Continent_Group", data=df)
    g.set_yscale("log")
    plt.title("Global Economic Divide (GDP per Capita, Log Scale)")
    plt.ylabel("USD (Log)")
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.savefig("global_economic_divide.png")

    # 3. Create Summary Markdown
    with open("global_comparison_summary.md", "w") as f:
        f.write("# Global Comparative Health & Economic Report (2026)\n\n")
        f.write("## 1. Regional Snapshot\n")
        f.write(df.to_markdown(index=False) + "\n\n")
        f.write("## 2. Key Global Insights\n")
        f.write("- **The Life Expectancy Ladder**: There is a clear ~16-year gap between the highest (North America: 80.6) and lowest (Africa: 64.4) regional life expectancies.\n")
        f.write("- **Economic Divergence**: While Asia has reached economic parity with South America (~$9.7k vs ~$9.5k GDP per capita), Africa remains significantly behind at ~$2.9k.\n")
        f.write("- **Infrastructure Resilience**: Basic water access is nearing universal levels in the Americas and Asia (>94%), but Africa's 75.8% remains the primary global challenge.\n")
        f.write("- **The Convergence Zone**: South America and Asia are currently converging on both economic and health indicators, forming a global 'middle-income' cluster.\n")

if __name__ == "__main__":
    create_global_report()
