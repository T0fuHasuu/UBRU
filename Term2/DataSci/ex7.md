# Numeric Matrice Mathematic :

    import numpy as np

    a = np.array([2, 4, 6])
    b = np.array([1, 3, 5])

    print(a % b ) 
    print(a * b )
    print(a + b ) 
    print(a // a)  
    print(b * a ) 

# Raising the power of :

    import numpy as np

    a = np.array([2, 4, 6])
    b = np.array([1, 3, 5])

    print("b**a = ", b**a)

# Multiply between addition and substraction :

    import numpy as np

    a = np.array([2, 4, 6])
    b = np.array([1, 3, 5])

    print("Result : ", (a+b)*(a-b))

# Checking If there anything bigger than 2 :

    import numpy as np

    a = np.array([2, 4, 6])
    b = np.array([1, 3, 5])

    print(np.any((a/b) > 2))

# Summation with all the element of matrice mupltiplying :

    import numpy as np

    a = np.array([2, 4, 6])
    b = np.array([1, 3, 5])

    print(np.sum(a*b))

# Finding Min, Max, Index(min, max) :

    import numpy as np

    a = np.array([12, 7, 9, 3, 5, 2])

    print("Max : ", np.max(a)," Min : ", np.min(a), " Max index : ", np.argmax(a), " Min index : ", np.argmin(a),)

# Finding median, Value at risk, standard division :

    import numpy as np

    a = np.array([12, 7, 9, 3, 5, 2])

    print(np.mean(a),np.var(a),np.std(a))

# Placing number in the correct matrice row column :

    import numpy as np

    a = np.array([[0, 0, 0],
                [0, 0, 0],
                [0, 0, 0]])

    a[0, 0] = 5
    a[1, 1] = 5
    a[2, 2] = 5

    print(a)    

# Replace with so on (:) :

    import numpy as np

    print(np.full((4, 4), 9))

    print(array[1, :] = 5)

# Constructing new list :

    my_list = [10, 20, 30, 40, 50]

    print(my_list[1:4])

    print(my_list[:3])

    print([my_list[0], my_list[2], my_list[4]])

    print(my_list[::-1])

# Extracting array in list of desired elements :

    import numpy as np

    my_list = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

    print(my_list[0, 1:])

    print(my_list[:, 0])

    print(my_list[1:, 1:])

# Slicing for spotted row and column :

    import numpy as np

    my_array = np.array([[10, 20, 30, 40],
                        [50, 60, 70, 80],
                        [90, 100, 110, 120]])

    print("ค่าที่อยู่ในแถวที่ 2 คอลัมน์ที่ 3:", my_array[1, 2])

    print("ข้อมูลทั้งหมดในแถวที่ 1:", my_array[0, :])

    print("ข้อมูลทั้งหมดในคอลัมน์ที่ 2 ของทุกแถว:", my_array[:, 1])
