# MBIO_691l
Final project assignment
#scicom-project
#Final project for MBIO 691
#Overview
This project provides an analysis of coral cover changes over time based on seasonal Sea Surface Temperature (SST) and pH predictions. The analysis includes several data visualizations to illustrate predicted changes in coral cover and the relationship with environmental factors.

#Dataset
We were given a dataset called coral_forcast from Noam, below details each variable and what it means.
coral_cover_2020/2100: Simulation estimates of tropical coral cover averaged across 2010-2020, and 2090-2100 respectively.
SST_2020/SST_2100: Mean SST (sea-surface temperature) averaged across 2010-2020, and 2090-2100 respectively (degrees C).
SST_seasonal: Amplitude of the seasonal SST cycle, i.e. difference between summer and winter SST (degrees C).
pH_2020/pH_2100: Mean pH averaged across 2010-2020, and 2090-2100 respectively.
PAR: Benthic Photosynthetically Available Radiation.
longitude/latitude: Longitude/latitude of the site.
model : Simulation configuration, numbered 0-11.

#Requirements
Python
Libraries: pandas, matplotlib, numpy, seaborn
You can install the required libraries using:
#Figures
The code generates and saves three figures as SVG files (For publication level resolution):
Figure_1: SST Scatter Plot: Shows the predicted change in coral cover vs. seasonal SST.
Figure_2: SST and pH Line Plot: Visualizes average SST and pH trends over time.
Figure_3: Model Bar Plot: Compares average coral cover change by model.