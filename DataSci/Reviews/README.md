## Python Cheatsheet for Exam

### Imports
```
import Mid_Term as x
import numpy as np
import pandas as pd
```

### Printing and Indexing
```
Print Set: x.a
Print Index 2 Value: x.a[2]
Print index 2[:1]: x.a[0][:1], index 3: x.a[3]
```

### Insert and Pop
```
x.a.insert(0, 'Capybara')
x.a.pop(3)
```

### Dictionary Operations
```
Print Dictionary: x.b
Add Key: x.b['Overflow'] = '12:99pm'
Pop Key: x.b.pop('john wick 4', None)
```

### Sets
```
Combine Sets: list(set(x.a + x.c))
Intersection: list(set(x.a) & set(x.c))
Symmetric Difference: list(set(x.a) ^ set(x.c))
```

### Looping
```
for item in x.a: print("Word:", item)
for i in range(1, 11): print((str(i) + ' ') * i)
```

### Numpy Basics
```
Array Info:
arr.ndim, arr.shape, arr.size, arr.dtype
```

### Numpy Reshaping
```
np.arange(1,13).reshape(3,4)
np.arange(11,19).reshape(2,4)
```

### Column Addition and Insertion
```
np.hstack((arr, [[33],[34],[35]]))
np.insert(np.array(arr), 2, [33,44,55])
```

### Slicing Arrays
```
np.array(arr)[:,1:]
np.array(arr)[1:,:]
```

### Sorting Arrays
```
Row Sort: np.sort(np.array(arr), axis=1)
Column Sort: np.sort(np.sort(np.array(arr), axis=1), axis=0)
Sort Rows Only: np.sort(myArray_2, axis=1)
```

### Calculations
```
x.d % x.e, x.d * x.e, x.d + x.e, x.d // x.d, x.e * x.d
Sum of Products: np.sum(x.d * x.e)
Power: x.d ** x.e
Compare: np.any((x.d + x.e) * (x.d - x.e) > 4)
```

### Finding Min and Max
```
Max: np.max(np.array(x.arr))
Min: np.min(np.array(x.arr))
Index Max: np.argmax(np.array(x.arr))
Index Min: np.argmin(np.array(x.arr))
```

### Statistics
```
Mean: np.mean(np.array(x.arr))
Variance: np.var(np.array(x.arr))
Std Dev: np.std(np.array(x.arr))
```

### Matrix Assignment
```
x.arr_1[0, 0] = 5
x.arr_1[1, 1] = 5
x.arr_1[2, 2] = 5
```

### Slice Assign Matrix
```
array = np.full((4, 4), 9)
array[1,:] = 5
```

### Slicing Lists and Arrays
```
List Slicing:
my_list[1:4], my_list[:3], [my_list[0], my_list[2], my_list[4]], my_list[::-1]
Array Slicing:
my_list[0, 1:], my_list[:, 0], my_list[1:, 1:]
```

### Pandas Basics
```
pd.Series(data, index=name)
pd.DataFrame(data, index=name, columns=col)
```

### DataFrame Access
```
Using loc:
df.loc[[0,2],['b','d']]
df.loc[1:, :'c']
df.loc['viper']
df.loc[['viper', 'sidewinder']]
df.loc[['cobra', 'viper'],['max_speed']]
df.loc[['sidewinder'], ['max_speed', 'shield']]
```

### Data Organization with Pandas
```
Organize:
name = np.arange(4,7)
col = ['A','B','C']
data = [[0,0,3],
        [0,4,1],
        [10,20,30]]
df = pd.DataFrame(data, index=name, columns=col)
```

### DataFrame Operations
```
r1 = np.arange(1,5)
r2 = np.arange(1,5) * 100
r3 = np.arange(1,5) * 1000
data = np.vstack([r1,r2,r3])
col = ['a','b','c','d']
df = pd.DataFrame(data, columns=col)
Access Rows/Cols:
df.loc[[0,2],['b','d']]
df.loc[1:, :'c']
```

