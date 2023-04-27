# To plot a PMF (Potential Mean Force) curve with error bars from bootstrapping method

import numpy as np
import matplotlib.pyplot as plt
from rcparams import rcparams

# Load data from the file
data = np.loadtxt('bsResult.xvg', comments=['#', '@'])

# Call the function
rcparams()

# Extract x, y, and y_err data
x = data[:, 0]
y = data[:, 1]
y_err = data[:, 2]

# Create a plot with error bars
fig, ax = plt.subplots()
ax.errorbar(x, y, yerr=y_err, fmt='o', ecolor='black', color='black', capsize=1, capthick=0.8, markersize=4, linewidth=0.8)

# Add labels and title
## x -> xi in greek 
ax.set_xlabel(r'$\xi$ (nm)')
ax.set_ylabel('Free energy (kJ/mol)')
# ax.set_title('Average and stddev from bootstrapping')

xlim = (0, 1.2)
mask = np.where((x >= xlim[0]) & (x <= xlim[1]))

ax.set_xlim(xlim)

# I want to express the maximum and minimum value of y-axis by utilizing axhline. 
# Simultaneously, I'll express the max value - min value by using ax.text. 
## axhline in the max and min region
ax.axhline(y[mask].max(), color='black', linestyle='--', linewidth=0.8)
ax.axhline(y[mask].min(), color='black', linestyle='--', linewidth=0.8)

## axvline in the max and min region
ax.axvline(x[mask][y[mask].argmin()], color='black', linestyle='--', linewidth=0.8)

## ax.text of the max - min value 
ax.text(0.75, -1.2, r'$\Delta$G = %.2f kJ/mol' % (y[mask].max() - y[mask].min()), ha='center', va='top')

# Title of this plot
ax.set_title('Ala-Ala PMF with bootstrapping', fontsize=12, fontweight='normal')

# Save the plot
plt.savefig('bsResult.png', dpi=300, bbox_inches='tight')