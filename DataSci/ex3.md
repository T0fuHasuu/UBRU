# Printing list :

    myset = {"name", "student", "age", "heights", "weight"}
    print(myset)

# Checking dimension, shape, size, datatype :


    import numpy as np
    myArray = np.array([1,2,3,4,5,6,7])

    print(f"The Dimension in this array: {myArray.ndim}")

    print(f"The Shape in this array: {myArray.shape}")

    print(f"The Size in this array: {myArray.size}")

    print(f"The Data type in this array: {myArray.dtype}")

# Forming a loop shape :

    import numpy as np

    print(np.arange(1, 10).reshape(3,3))

# Finding shape of the matrice :

    import numpy as np

    print(np.arange(11,19).reshape(2, 4).shape)

# Reshape :

    import numpy as np

    print(np.arange(9))

    print(original_array.reshape(3, 3))

# Reshape for i>1x in matice :

    import numpy as np

    print(np.arange(1,10).reshape(3,3))

    print(original_array.reshape(1,9))  

# Add Matrice as row :

    import numpy as np

    y = np.array([[1, 2], [3, 4]])
    print(np.vstack((y, [11, 12,])))

# Add Matrice as column :

    import numpy as np

    y = np.array([[1, 2], [3, 4]])
    print(np.hstack((y, [11, 12,])))

# Combining in the list :

    import numpy as np

    x = np.array([1, 2, 3, 4])
    print(np.insert(x, 2, [11, 12, 13]))

# Add array in array :

    import numpy as np

    y = np.array([[1,2],[3,4]])
    print(y)

    print(np.hstack((y,[[11],[11]])))

# Slicing elements in column :

    import numpy as np
    y = np.array([[1,2],[3,4]])
    print(y)

    print(y[:, 1:])

# Slicing elements in row :

    import numpy as np
    y = np.array([[1,2],[3,4]])
    print(y)

    print(y[1:, :])

# Sorting rows and columns :

    import numpy as np

    arr = np.array([[2, 7, 3], [8, 3, 5], [4, 0, 9]])

    row_sorted = np.sort(arr, axis=1)

    col_sorted = np.sort(row_sorted, axis=0)

    print(f"The Original Array:\n {arr}\n")
    print(f"Row sorted:\n {row_sorted}\n")
    print(f"Column sorted:\n {col_sorted}\n") 

# Sorting row :

    import numpy as np

    myArray_2 = np.array([[2, 3, 1, 4], [7, 5, 6, 8]])

    sorted_rows = np.sort(myArray_2, axis=1)

    print("Elements sorted by rows:\n", sorted_rows)