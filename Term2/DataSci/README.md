# Summary

## **Pandas: DataFrame**

### **Creating a DataFrame**
```python
import pandas as pd
from numpy.random import rand

df = pd.DataFrame(rand(5,4), index='A B C D E'.split(), columns='W X Y Z'.split())
df
```

### **Selecting Data**
1. **Grab a single column**
```python
df['W']
```
2. **Select multiple columns**
```python
df[['W', 'Z']]
```
3. **Create a new column**
```python
df['NEW'] = df['W'] + df['Z']
df
```
4. **Remove a column (vertical removal)**
```python
df.drop('NEW', axis=1)
```
5. **Modify DataFrame (in-place column removal)**
```python
df.drop('NEW', axis=1, inplace=True)
```
6. **Remove a row (horizontal removal)**
```python
df.drop('NEW', axis=0)
```
7. **Select rows**
```python
df.loc['A']  # Select row by label
df.iloc[2]   # Select row by index
df.loc[['A','B'],['W','Y']]  # Select specific rows and columns
```
8. **Reset index**
```python
df.reset_index()
```
9. **Select values from multi-index DataFrame**
```python
df.xs('G1')
df.xs(('G1',1))
df.xs(1, level='Num')
```

## **Handling Missing Data**
```python
import numpy as np

df = pd.DataFrame({'A':[1,2,np.nan],
                   'B':[5,np.nan,np.nan],
                   'C':[1,2,3]})
```
1. **Drop NA values (rows/columns)**
```python
df.dropna()  # Drop rows with NA
df.dropna(axis=1)  # Drop columns with NA
```
2. **Drop with threshold**
```python
df.dropna(thresh=2)
```
3. **Fill missing values**
```python
df.fillna(value="STH")
df['A'].fillna(value=df['A'].mean())  # Fill with column mean
df.fillna(value=df.mean())  # Fill all NA with mean
```

## **Pandas: GroupBy**
```python
data = {'Company':['SCG','SCG','PTT','PTT','KTB','KTB','KTB'],
        'Person':['Somsri','Charlie','Somchai','Kaew','Noo','Sarah','MY'],
        'Sales':[200,120,340,124,243,350,333]}

df = pd.DataFrame(data)
```
- **Summation**: `df['Sales'].sum()`
- **Group by**: `df.groupby('Company')`
- **Find median per group**:
```python
by_comp = df.groupby("Company")
by_comp[['Sales']].mean()
df.groupby('Company')['Sales'].mean()
```
- **Find min value in groups**: `by_comp.min()`
- **Count elements in each group**: `by_comp.count()`
- **Descriptive statistics**: `by_comp.describe()`
- **Transpose statistics**: `by_comp.describe().transpose()`
- **Select a specific group**: `by_comp.describe().transpose()['PTT']`

## **Pandas: Merging, Joining, Concatenating**

### **Concatenation**
```python
pd.concat([df1, df2, df3])
```
- **Concatenate along columns**
```python
pd.concat([df1, df2, df3], axis=1)
```

### **Merging**
```python
pd.merge(left, right, how='inner', on='key')
```

### **Joining**
```python
left.join(right)
right.join(left)
left.join(right, how='outer')
left.join(right, how='inner')
```

## **Pandas: Operations**
- **Get unique values**: `df['col2'].unique()`
- **Count unique values**: `df['col2'].nunique()`
- **Value counts**: `df['col2'].value_counts()`

### **Selecting Data with Conditions**
```python
newdf = df[(df['col1'] > 2) & (df['col2'] == 444)]
```
- **Remove column permanently**: `del df['col1']`
- **Sort values**: `df.sort_values(by='col2')`
- **Check for null values**: `df.isnull()`

### **Pivot Table**
```python
df.pivot_table(values='D', index=['A'], columns=['C'])
```

## **Pandas: Data Input and Output**
```python
from google.colab import drive
drive.mount('/content/drive')
```
- **Read CSV**: `df = pd.read_csv(path)`
- **Save CSV**: `df.to_csv(path, index=False)`

## **Matplotlib**

### **Basic Plotting**
```python
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
```
```python
plt.plot([1, 2, 3, 4], [1, 4, 9, 16])
plt.suptitle('Score for Data')
plt.ylabel('Numbers')
plt.xlabel('Scale')
plt.show()
```
```python
x = np.array([2022,2023,2024,2025,2026,2027])
y = np.array([146,201,239,489,329,412])
plt.plot(x, y)
```

## **Seaborn**

### **Basic Plots**
```python
sns.scatterplot(x='total_bill', y='tip', data=df)
sns.lineplot(x='size', y='tip', data=df)
sns.barplot(x='day', y='total_bill', data=df)
```

### **Distribution Plots**
```python
sns.histplot(df['total_bill'], bins=20, kde=True)
sns.kdeplot(df['total_bill'])
sns.boxplot(x='day', y='total_bill', data=df)
sns.violinplot(x='day', y='total_bill', data=df)
```

### **Categorical Plots**
```python
sns.countplot(x='sex', data=df)
sns.stripplot(x='day', y='total_bill', data=df, jitter=True)
sns.swarmplot(x='day', y='total_bill', data=df)
```

### **Advanced Seaborn Features**
```python
sns.pairplot(df, hue='sex')
sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
sns.regplot(x='total_bill', y='tip', data=df)
sns.lmplot(x='total_bill', y='tip', hue='sex', data=df)
```

### **Saving Plots**
```python
plt.savefig('plot.png', dpi=300)
```

