import pandas as pd
import numpy as np
df = pd.DataFrame({
    'x': np.array([0, 1, 2, 3, 4, 5]),
    'y': np.array([0, 1, 2, 3.5, 4, 5])+2,
})

c = df.corr().iloc[0, 1]
print(c)
# print(type(c))
