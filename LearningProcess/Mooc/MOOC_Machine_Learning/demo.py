import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from EX_K_means import KMeans

data=pd.read_csv("")
iris_types=["A","B","C"]
x_axis='len'
y_axis='wid'
plt.figure(figsize=(12,5))
plt.subplot(1,2,1)
for iris_type in iris_types:
    plt.scatter(data[x_axis][data['class']==iris_type],data[y_axis,:][data['class']==iris_type])
plt.title="SB"
plt.legend()
plt.subplot(1,2,2)
plt.scatter(data[x_axis][:], data[y_axis][:])
plt.title="DSB"
plt.show()

