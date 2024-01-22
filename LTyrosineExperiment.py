import numpy as np
import matplotlib.pyplot as plt

feature_data = [1, 2]
conjunction0_data = [17, 31]
conjunction1_data = [13, 23]
n = len(feature_data) #2

# Generate slope averages for three different distributions
Feature_avg = np.mean(feature_data) #1.5
Conjunction0_avg = np.mean(conjunction0_data) #24
Conjunction1_avg = np.mean(conjunction1_data) #18

# Standard deviation calcs for error bars
feature_std = np.std(feature_data, ddof=1) #0.707106781 
conjunction0_std = np.std(conjunction0_data, ddof=1) #9.899494937
conjunction1_std = np.std(conjunction1_data, ddof=1) #7.071067812

# Plot the barchart and error bars
plt.bar(['Feature', '$Conjunction_{0}$', '$Conjunction_{Tyr}$'], [Feature_avg, Conjunction0_avg, Conjunction1_avg], color ='maroon', width = 0.4)
plt.errorbar(['Feature', '$Conjunction_{0}$', '$Conjunction_{Tyr}$'], [Feature_avg, Conjunction0_avg, Conjunction1_avg], yerr=[feature_std, conjunction0_std, conjunction1_std], fmt='o', color='k', capsize=5, markersize=0)
plt.xticks(['Feature', '$Conjunction_{0}$', '$Conjunction_{Tyr}$'], fontsize=14)
plt.xlabel("Search Type", fontsize=18)
plt.ylabel("$Slope_{speed per distractor}$", fontsize=18)
plt.show()