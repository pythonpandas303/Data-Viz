import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
plt.rcParams['font.size'] = 7.0
y = np.array([0.692918, 0.029989, 0.012137, 0.008318])
labels = ["Chicago PD", "Cook County Sheriff", "Cicero PD", "Chicago Heights PD"]
explode = [0.2, 0, 0, 0]
plt.pie(y, explode=explode, normalize=True, labels=labels, autopct='%1.0f%%')
plt.title('Top 4 Agencies')
plt.suptitle('Cases by Law Enforcement Agency', fontsize=10)