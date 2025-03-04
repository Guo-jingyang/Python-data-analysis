import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

mu = 0
sigma = 1

x = np.linspace(mu - 4*sigma, mu + 4*sigma, 100)
y = norm.pdf(x, mu, sigma)

plt.figure(figsize=(8, 6))
plt.plot(x, y, label=f'Gaussian Distribution ($\mu={mu}$, $\sigma={sigma}$)')
plt.legend()
plt.show()
