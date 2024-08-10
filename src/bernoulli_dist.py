import numpy as np
import matplotlib.pyplot as plt

# Parameters: Bernoulli Distribution
p = 0.3    # success probability
q = 1 - p  # failure probability

x     = np.array([0, 1])
pmf_x = np.array([q, p])

# Cartesian plane setup
fig, ax = plt.subplots()

ax.set_title('Bernoulli Distribution (p = 0.3)')

ax.set_xlabel('Outcome')
ax.set_xticks(x)
ax.set_xlim(-0.5, 1.5)

ax.set_ylabel('Success Probability')

ax.grid()

# Plot data
ax.bar(x, pmf_x, color='blue', alpha=0.5, width=0.4)

# Render
plt.show()

