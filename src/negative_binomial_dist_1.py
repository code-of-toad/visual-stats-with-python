"""
NOTE: This variant of the Negative Binomial Distribution counts
      failures until the r-th success -- not trials.
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import nbinom

# Parameters: Negative Binomial Distribution
p = 0.5

r1 = 1
r2 = 3
r3 = 5
r4 = 7
r5 = 9

x1 = np.arange(40)
x2 = np.arange(40)
x3 = np.arange(40)
x4 = np.arange(40)
x5 = np.arange(40)

pmf_x1 = nbinom.pmf(k=x1, n=r1, p=p)
pmf_x2 = nbinom.pmf(k=x2, n=r2, p=p)
pmf_x3 = nbinom.pmf(k=x3, n=r3, p=p)
pmf_x4 = nbinom.pmf(k=x4, n=r4, p=p)
pmf_x5 = nbinom.pmf(k=x5, n=r5, p=p)

# Cartesian plane setup
fig, ax = plt.subplots()

ax.set_title('Negative Binomial Distributions (constant p)')

ax.set_xlabel('Number of failures until the r-th success')
ax.set_xticks(np.arange(0, 26, 5))
ax.set_xticks(np.arange(0, 26), minor=True)
ax.set_xlim(-1, 26)

ax.set_ylabel('P (X failures until the r-th success')

# Plot data
ax.plot(x1, pmf_x1, marker='o', linestyle=':', color='red',    alpha = 0.6,
        label = 'X1~Nb(r=1, p=0.5)')
ax.plot(x2, pmf_x2, marker='o', linestyle=':', color='green',  alpha = 0.6,
        label = 'X2~Nb(r=3, p=0.5)')
ax.plot(x3, pmf_x3, marker='o', linestyle=':', color='blue',   alpha = 0.6,
        label = 'X3~Nb(r=5, p=0.5)')
ax.plot(x4, pmf_x4, marker='o', linestyle=':', color='orange', alpha = 0.6,
        label = 'X4~Nb(r=7, p=0.5)')
ax.plot(x5, pmf_x5, marker='o', linestyle=':', color='teal',   alpha = 0.6,
        label = 'X5~Nb(r=9, p=0.5)')

# Render
ax.grid()
ax.legend()
plt.show()
