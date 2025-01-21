import pandas as pd
import matplotlib.pyplot as plt

data = {'Nome': ['Alice', 'Bob'], 'Idade': [25, 30]}
df = pd.DataFrame(data)
print(df)

plt.plot([1, 2, 3], [4, 5, 6])
plt.show()