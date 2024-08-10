"""
NOTE: This variant of the Negative Binomial Distribution counts
      failures until the r-th success -- not trials.
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import nbinom

# Parameters: Negative Binomial Distributions
p1 = 0.25
p2 = 0.50
p3 = 0.75
p4 = 0.85
p5 = 1.00

r = 5

x1 = np.arange(40)
x2 = np.arange(40)
x3 = np.arange(40)
x4 = np.arange(40)
x5 = np.arange(40)

pmf_x1 = nbinom.pmf(k=x1, n=r, p=p1)
pmf_x2 = nbinom.pmf(k=x2, n=r, p=p2)
pmf_x3 = nbinom.pmf(k=x3, n=r, p=p3)
pmf_x4 = nbinom.pmf(k=x4, n=r, p=p4)
pmf_x5 = nbinom.pmf(k=x5, n=r, p=p5)

# Cartesian plane setup
fig, ax = plt.subplots()

ax.set_title('Negative Binomial Distributions (constant r)')

ax.set_xlabel('Number of failures until the r-th success')
ax.set_xticks(np.arange(0, 26, 5))
ax.set_xticks(np.arange(0, 26), minor=True)
ax.set_xlim(-1, 26)

ax.set_ylabel('P (X failures until the r-th success')

# Plot data
ax.plot(x1, pmf_x1, marker='o', linestyle=':', color='red',    alpha = 0.6,
        label = 'X1~Nb(r=5, p=0.25)')
ax.plot(x2, pmf_x2, marker='o', linestyle=':', color='green',  alpha = 0.6,
        label = 'X2~Nb(r=5, p=0.50)')
ax.plot(x3, pmf_x3, marker='o', linestyle=':', color='blue',   alpha = 0.6,
        label = 'X3~Nb(r=5, p=0.75)')
ax.plot(x4, pmf_x4, marker='o', linestyle=':', color='orange', alpha = 0.6,
        label = 'X4~Nb(r=5, p=0.85)')
ax.plot(x5, pmf_x5, marker='o', linestyle=':', color='teal',   alpha = 0.6,
        label = 'X5~Nb(r=5, p=1.00)')

# Render
ax.grid()
ax.legend()
plt.show()
