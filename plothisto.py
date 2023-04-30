import numpy as np
import matplotlib.pyplot as plt
from rcparams import rcparams

# Load data from the file
data = np.loadtxt('histo.xvg', comments=['#', '@'])
x = data[:,0]
y = data[:,1:]

rcparams()

# Create a plot
fig, ax = plt.subplots()
ax.plot(x, y, linewidth=1.5)

# Add labels and title
ax.set_xlabel(r'$\xi$')
ax.set_ylabel('Count')
ax.set_title('Umbrella histograms')

# Save your plot
plt.tight_layout()
plt.savefig('histo.png', dpi=300)
