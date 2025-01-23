# Install Numpy and Panda 
```bash
!pip install numpy
!pip install pandas
```
# Module Importation
```python
import numpy as np
import pandas as pd
```

# Solution Number 1
```python
data = [30,35,40]
name = ["2015 Sales", "2016 Sales", "2017 Sales"]
print(pd.DataFrame(data,index=name, columns=['Product A']))
```
> Result :
`            Product A
2015 Sales         30
2016 Sales         35
2017 Sales         40`

# Solution Number 2
```python
print("Old ap : \n", np.arange(1,7).reshape(2,3))
print("New ap :\n", np.vstack((np.arange(1,7).reshape(2,3), np.arange(1,4)*100)))
```
> Result :
`Old ap : 
 [[1 2 3]
 [4 5 6]]
New ap :
 [[  1   2   3]
 [  4   5   6]
 [100 200 300]]`
