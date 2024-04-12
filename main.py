# Pandas: How to Filter a DataFrame by value counts

import pandas as pd


df = pd.DataFrame({
    'name': ['Alice', 'Bobby', 'Carl', 'Dan', 'Ethan'],
    'sales': [1, 3, 5, 7, 7],
    'salary': [175.1, 180.2, 190.3, 205.4, 210.5],
})

print(df)

print('-' * 50)

result = df.groupby('sales').filter(lambda x: len(x) > 1)
print(result)