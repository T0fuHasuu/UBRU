# Panda dataframe works like matrice too

# What is it used for :

    * Data cleaning and organizing

# To use :

    * install : pip install pandas

# Import to usage :

    import pandas as pd
    import numpy as np

# Sorting Tuple :

    a = [15,12.5,'Lisa',22,'Konan']
    print(pd.Series(a))

# Sorting List series :

    a = (15,12.5,'Lisa',22,'Konan')
    print(pd.Series(a))

# Converting using np :

    a = [15,12.5,'Lisa',22,'Konan']
    print(pd.Series(np.array(a)))

# Givin value label to column (na/score) :

    a = np.array([15,12.5,'Lisa',22,'Konan'])
    print(pd.Series(a,name='Score'))                

# Givin Table of value labels to rows and column :

    score = [79,85,81,92,56]
    name = ['Lisa','Jennie','Rose','Jisoo','Minnie']
    print(pd.Series(score, index=name,name='Grade'))

    Ex :
                Grade
        Lisa	79
        Jennie	85
        Rose	81
        Jisoo	92
        Minnie	56

    # Alternative way : pd.Series([79,85,81,92,56],index=['Lisa','Jennie','Rose','Jisoo','Minnie'],name='Grade')

# Using dictionary to map out :

    name = {'Lisa':79,'Jennie':85,'Rose':81,'Jisoo':92,'Minnie':75}
    print(pd.Series(name,name='Grade'))

# Get only specified index :

    name = {'Lisa':79,'Jennie':85,'Rose':81,'Jisoo':92,'Minnie':75}
    print(pd.Series(name, index= ['Lisa','Minnie']))

    Ex : 
                0
        Lisa	79
        Minnie	75

# Slicing :

    name = {'Lisa':79,'Jennie':85,'Rose':81,'Jisoo':92,'Minnie':75}
    print(pd.Series(name)[3:])

    Ex :
                0
        Jisoo	92
        Minnie	75

# Dataframe :

    data = [420,380,390]
    print(pd.DataFrame(data))

# Fitting into column value :

    datas = [420,380,390,250,450]
    cols = ['Calories']
    print(pd.DataFrame(datas, columns=cols))

# Organizing and planning out the row and column label value :

    data = [
        [163,420,50],
        [175,380,40],
        [162,390,45],
        [168,290,48]
    ]
    col = ['height','calories','duration']
    name = ['Lisa','Jennie','Rose','Jisoo']
    print(pd.DataFrame(data, index=name, columns=col))

    Ex :
                height	calories	duration
        Lisa	163	    420	        50
        Jennie	175	    380	        40
        Rose	162	    390	        45
        Jisoo	168	    290	        48

# Iloc to only display index value :

    data = {
        "calories":[420,380,390],
        "duration":[50,40,45]
    }
    df = pd.DataFrame(data)
    print(df)
    df.loc[[0]]   

    Ex :
            calories   duration
    0       420        50
    1       380        40
    2       390        45

    After Iloc :

            calories    duration
    0	    420	        50

# Access with row and column to get specified value :

    data = {
        "calories":[420,380,390],
        "duration":[50,40,45]
    }
    df = pd.DataFrame(data)
    print(df)
    df.iloc[[2],[1]]