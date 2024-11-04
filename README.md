# MBIO_691l
# Final project assignment

This project provides an analysis of coral cover changes over time based on seasonal Sea Surface Temperature (SST) and pH predictions. The analysis includes several data visualizations to illustrate predicted changes in coral cover and the relationship with environmental factors.

# Requirements
Python.\
Libraries: pandas, matplotlib, numpy, seaborn

# Dataset

The dataset 'Coral_Forecast' was given to us and created by Noam with the following variable definitions:

coral_cover_2020/2100: Simulation estimates of tropical coral cover averaged across 2010-2020, and 2090-2100 respectively (km^2).
SST_2020/SST_2100: Mean SST (sea-surface temperature) averaged across 2010-2020, and 2090-2100 respectively (degrees C).
SST_seasonal: Amplitude of the seasonal SST cycle, i.e. difference between summer and winter SST (degrees C).
pH_2020/pH_2100: Mean pH averaged across 2010-2020, and 2090-2100 respectively.
PAR: Benthic Photosynthetically Available Radiation.
longitude/latitude: Longitude/latitude of the site.
model: Simulation configuration, numbered 0-11.

# Figures
The code generates and saves three figures as SVG files (high resolution files of publication quality):

Figure 1: SST Scatter Plot: Shows the predicted change in coral cover vs. seasonal SST.
Figure 2: SST and pH Line Plot: Visualizes average SST and pH trends over time.
Figure 3: Model Bar Plot, comparing average coral cover change by each model.
