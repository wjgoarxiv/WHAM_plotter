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

# Add labels and title
ax.set_xlabel('Reaction coordinate (nm)')
ax.set_ylabel('E (kJ/mol)')
ax.set_title('Umbrella potential')

# Show the plot
plt.show()
