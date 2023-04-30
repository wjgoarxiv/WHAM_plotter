import numpy as np
import matplotlib.pyplot as plt
from rcparams import rcparams

# Load data from the file
data = np.loadtxt('profile.xvg', comments=['#', '@'])
x = data[:,0]
y = data[:,1]

rcparams()

# Create a plot
fig, ax = plt.subplots()
ax.plot(x, y)

# Set your x-axis limit here
ax.set_xlim(0, 1.4)

# Add labels and title
ax.set_xlabel(r'$\xi$')
ax.set_ylabel('Free energy (kJ/mol)')
ax.set_title('Umbrella potential')

# Save your plot
plt.tight_layout()
plt.savefig('profile.png', dpi=300)
