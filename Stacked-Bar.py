import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('Path')
df.groupby(['Var_1', 'Var_2']).size().unstack().plot(kind='bar',stacked=True)
plt.legend(bbox_to_anchor=(1,1), loc="upper left")
plt.show()