import numpy as np
import matplotlib.pyplot as plt
from rcparams import rcparams

# Load data from the file
with open('bsProfs.xvg') as f:
    data_str = f.read()

rcparams()

# Split data into separate arrays based on the '&' symbol
data_list = data_str.split('&')
data = []
for d in data_list:
    if not d.strip():
        continue
    data.append(np.loadtxt(d.strip().split('\n'), comments=['#', '@']))

# Create a plot for each array of data
fig, ax = plt.subplots()
rcparams()

for d in data:
    x = d[:,0]
    y = d[:,1]
    ax.plot(x, y)

# Add labels and title
ax.set_xlabel(r'$\xi$')
ax.set_ylabel('Free energy (kJ/mol)')

# Set your x-axis limits here
ax.set_xlim(0, 1.4)

# Download the plot
plt.tight_layout()
plt.savefig('bsProfs.png', dpi=300)