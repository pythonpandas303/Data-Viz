import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
df = pd.read_csv('C:/Users/megal/Desktop/Regis/MSDS640/Week2/data_backup_4-2021/cleaned_sentencing3.csv')
x = df.COMMITMENT_TERM
y = df.LENGTH_OF_CASE_in_Days
plt.scatter(x,y, s=1, cmap='Reds', marker='1')
plt.xlabel('Commitment Term')
plt.ylabel('Trial Length')
plt.title('Sentencing by Trial Length and Term')
plt.show()