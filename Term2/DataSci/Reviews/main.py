import Mid_Term as x
import numpy as np
import pandas as pd
def line():
    print("---------------------------------------------------------")

print("Print Set : ",x.a)
print("Print Index 2 Value : ",x.a[2])
print("index 2[:1] : ",x.a[0][:1]," index 3 : ",x.a[3])
line()

# Insert
x.a.insert(0, 'Capybara')
print("Inserted Set : ",x.a)
line()

# Pop
x.a.pop(3)
print("Pop calling with inserted Capy : ",x.a)
line()

# Dictionary
print("Dictionary : ",x.b)
line()

# Adding
x.b['Overflow'] = '12:99pm'
print("Addition : ",x.b)
line()

# Popping 
x.b.pop('john wick 4', None)
print("Delete John wick : ",x.b)
line()

# Displaying sets
print("Set A : ",x.a)
print("Set B : ",x.c)
line()

# Combine
print("Combine Set A & B :", list(set(x.a + x.c)))
line()
# AND function
print("Only Set A & B :", list(set(x.a) & set(x.c)))
line()
# Not the same
print("Only Set A & B :", list(set(x.a) ^ set(x.c)))
line()

# Looping
for item in x.a:
    print("Word : ",item)
line()
    
# Loop half pyramid 
for i in range(1, 11):
    print((str(i) + ' ') * i)
line()
    
    
# Numpy
arr = np.array([[1,2,3,4,5,6,7],
               [1,2,3,4,5,6,7],
               [1,2,3,4,5,6,7]])
print("Array : \n",arr)
print("Dimensional : ",arr.ndim)
print("Shape : ",arr.shape)
print("Size : ",arr.size)
print("Datatype : ",arr.dtype)
line()

# Shaping
print(np.arange(1,13).reshape(3,4))
line()

# Arranging specificly
print(np.arange(11, 19).reshape(2,4),"\nShape : 2,4")
line()

# Arranging From original 
arr = [0,1,2,3,4,5,6,7,8]
print(np.array(arr).reshape(3,3))
line()

# Arranging From original 
arr = [0,1,2,3,4,5]
print(np.array(arr).reshape(3,2))
line()

# Add columns 
arr = [[0,1,2],[3,4,5],[6,7,8]]
print(np.hstack((arr, [[33],[34],[35]])))
line()

# To insert 
arr = [0,1,2,3,4,5]
print(np.insert(np.array(arr), 2, [33,44,55]))
line()

# Slicing 
arr = [[9,3,5],[3,6,1],[8,6,1]]
print(np.array(arr)[:,1:])
print(np.array(arr)[1:,:])
line()

# Sorting
print("Orginal : \n",np.array(arr))
print("Row Sorted : \n",np.sort(np.array(arr), axis=1))
print("Column Sorted : \n",np.sort(np.sort(np.array(arr), axis=1), axis=0))
line()

# Sort row only 
myArray_2 = np.array([[2, 3, 1, 4], [7, 5, 6, 8]])
print(np.sort((myArray_2), axis=1))
line()

# Calculation 
print(x.d%x.e,
      " ",
      x.d*x.e,
      " ",
      x.d+x.e,
      " ",
      x.d//x.d,
      " ",
      x.e*x.d,
      " ",)
line()

# Power
print(x.d**x.e)
line()

# Function 
print((x.d + x.e) * (x.d - x.e))
line()

# Comparing
print(np.any((x.d + x.e) * (x.d - x.e)>4))
line()

# Sum of product
print(np.sum(x.d*x.e))
line()

# Finding Min max 
print("Max : ",np.max(np.array(x.arr)))
print("Min : ",np.min(np.array(x.arr)))
print("Index Max : ",np.argmax(np.array(x.arr)))
print("Index Min : ",np.argmin(np.array(x.arr)))
line()

# Using formula
print(np.mean(np.array(x.arr)),
      np.var(np.array(x.arr)),
      np.std(np.array(x.arr)))
line()

# assigning value to matrice
x.arr_1[0, 0] = 5
x.arr_1[1, 1] = 5
x.arr_1[2, 2] = 5
print(x.arr_1)
line()

# Slice assign matrice 
array = np.full((4, 4), 9)
array[1,:] = 5
print(array)
# [[9 9 9 9]
#  [5 5 5 5]
#  [9 9 9 9]
#  [9 9 9 9]]
line()

# Slicing 
my_list = [10, 20, 30, 40, 50]
print(my_list[1:4])     #[20, 30, 40]
print(my_list[:3])      #[10, 20, 30]
print([my_list[0], my_list[2], my_list[4]])     # [10, 30, 50]
print(my_list[::-1])    #[50, 40, 30, 20, 10]
line()

# Slicing again
my_list = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(my_list[0, 1:])       #[2 3]
print(my_list[:, 0])            #[1 4 7]
print(my_list[1:, 1:])      #[[5 6], [8 9]]
line()

## Panda
name = ['a','b','c']
data = [1,2,3]
print(pd.Series(data, index=name))
line()

# organize
name = np.arange(4,7)
col = ['A','B','C']
data = [[0,0,3],
        [0,4,1],
        [10,20,30]]
print(pd.DataFrame(data, index=name, columns=col))
line()

# Series
data = np.arange(1,5)
name = ['a','b','c','d']
print(pd.Series(data, index=name))
line()

# Dataframe 
r1 = np.arange(1,5)
r2 = np.arange(1,5) * 100
r3 = np.arange(1,5) * 1000
data = np.vstack([r1,r2,r3])
col = ['a','b','c','d']
df = pd.DataFrame(data, columns=col)
print(df)
line()
print(df.loc[[0,2],['b','d']])
line()
print(df.loc[1:, :'c'])
line()

# DataFrame 
col = ['max_speed', 'shield']
name = ['cobra', 'viper', 'sidewinder']
data = [[1,2],[4,5],[7,8]]
df = pd.DataFrame(data, index=name, columns=col)
print(df)
line()
print(df.loc['viper'])
line()
print(df.loc[['viper', 'sidewinder']])
line()
print(df.loc[['cobra', 'viper'],['max_speed']])
line()
print(df.loc[['sidewinder'], ['max_speed', 'shield']])
line()