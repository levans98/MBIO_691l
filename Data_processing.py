import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# Data
df = pd.read_csv('coral_forecast.csv')

# Percent change in coral cover
df['coral_cover_change'] = ((df['coral_cover_2100'] - df['coral_cover_2020']) / df['coral_cover_2020']) * 100

# SST Seasonal - Averaging across sites and grouping by model
new_data = df.groupby('model')[['coral_cover_change', 'SST_seasonal']].mean().reset_index()

# Scatter Plot
plt.figure(figsize=(8, 6))
plt.scatter(new_data['SST_seasonal'], new_data['coral_cover_change'], linewidth=2)
plt.title('Average Predicted Change in Coral Cover vs SST Seasonal')
plt.xlabel('SST Seasonal')
plt.ylabel('Average Percentage Change in Coral Cover')
plt.grid(True)
plt.text(0.5, -0.15, "Figure 1: This scatter plot shows the average change in coral cover for each model as a function of seasonal Sea Surface Temperature (SST). As SST increases, the average percent change in coral cover does not have a correlation.", ha="center", va="center", transform=plt.gca().transAxes, wrap=True)
plt.tight_layout(rect=[0, 0.05, 1, 1])
plt.savefig("SST_scatter_plot.svg", format="svg")
plt.show()

# SST and PH over time
plt.figure(figsize=(10, 6))
plt.plot(['2020', '2100'], [df['SST_2020'].mean(), df['SST_2100'].mean()], marker='o', label="SST")
plt.plot(['2020', '2100'], [df['pH_2020'].mean(), df['pH_2100'].mean()], marker='o', label="pH")
plt.xlabel("Year")
plt.ylabel("Average Value")
plt.title("Average SST and pH Over Time")
plt.legend()
plt.text(0.5, -0.15, "Figure 2: This line plot shows predicted average SST and pH over time. SST increases throughout time, and pH slightly decreases.", ha="center", va="center", transform=plt.gca().transAxes, wrap=True)
plt.tight_layout(rect=[0, 0.05, 1, 1]) 
plt.savefig("SST_and_pH_Plot.svg", format="svg")
plt.show()

# Bar plot - Average coral cover change by model
avg_coral_change_by_model = df.groupby('model')['coral_cover_change'].mean().reset_index()
plt.figure(figsize=(10, 6))
plt.bar(avg_coral_change_by_model['model'], avg_coral_change_by_model['coral_cover_change'])
plt.xlabel("Model")
plt.ylabel("Average Coral Cover Change (%)")
plt.title("Average Coral Cover Change by Model")
plt.text(0.5, -0.15, "Figure 3: This bar plot shows the average coral cover change for each model when averaged across sites. Each of the 12 models predicts a decrease in average coral cover across all sites.", ha="center", va="center", transform=plt.gca().transAxes, wrap=True)
plt.tight_layout(rect=[0, 0.05, 1, 1]) 
plt.savefig("Bar_Plot_average_coral_cover.svg", format="svg")
plt.show()
