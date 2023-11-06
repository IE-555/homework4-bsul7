#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np
import matplotlib.pyplot as plt

# Generate synthetic data for average monthly temperatures (in Celsius)
months = np.arange(1, 13)  # Months from January to December
avg_temperatures = [6.2, 7.9, 9.3, 14.1, 19.1, 23.1, 24.5, 25.3, 20.1, 14.1, 10.1, 6.0]  # Average temperatures for each month

# Create a polar plot
plt.figure(figsize=(8, 8))
ax = plt.subplot(111, polar=True)

# Convert months to radians for the polar plot
months_rad = np.radians(np.linspace(0, 360, len(months), endpoint=False))

# Plot average temperatures as a line on the polar plot
ax.plot(months_rad, avg_temperatures, marker='o', linestyle='-')

# Set labels for each month
ax.set_xticks(months_rad)
ax.set_xticklabels(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])

# Set radial gridlines
ax.set_yticks([0, 5, 10, 15, 20, 25, 30])
ax.grid(True)

# Add a title
plt.title('Average Monthly Temperatures', va='bottom')

# Show the polar plot
plt.show()


# In[ ]:





# In[ ]:




